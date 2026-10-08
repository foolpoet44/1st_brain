#!/usr/bin/env python3
"""
Raw Session Archiver for csp-brain Vault
Scans Hermes sessions and converts them to markdown with YAML frontmatter.
"""

import os
import json
from datetime import datetime
from pathlib import Path

# Configuration
HERMES_SESSIONS_DIR = "/opt/data/home/.hermes/sessions"
OUTPUT_DIR = "/opt/data/csp-brain/raw/sessions"
STATE_FILE = "/opt/data/home/.hermes/raw_archive_state.json"

def load_state():
    """Load the archive state from disk."""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    return {"archived_sessions": [], "last_run": None}

def save_state(state):
    """Save the archive state to disk."""
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def session_to_markdown(session_data, session_id):
    """Convert a session JSONL to markdown with YAML frontmatter."""
    # Parse session data
    messages = []
    if isinstance(session_data, list):
        messages = session_data
    elif isinstance(session_data, dict):
        messages = session_data.get("messages", [])
    
    # Extract metadata
    created_at = None
    model = None
    tool_calls_count = 0
    
    for msg in messages:
        if msg.get("role") == "system" and not created_at:
            # Try to extract timestamp from content or metadata
            pass
        if msg.get("role") == "assistant":
            model = msg.get("model", model)
            tool_calls = msg.get("tool_calls", [])
            tool_calls_count += len(tool_calls) if tool_calls else 0
    
    # Generate filename-safe ID
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"session_{session_id}_{timestamp}.md"
    
    # Build markdown content
    frontmatter = f"""---
session_id: {session_id}
archived_at: {datetime.now().isoformat()}
model: {model or "unknown"}
message_count: {len(messages)}
tool_calls_count: {tool_calls_count}
---

# Session: {session_id}

"""
    
    # Add messages
    md_content = frontmatter
    for i, msg in enumerate(messages):
        role = msg.get("role", "unknown")
        content = msg.get("content", "")
        
        # Handle tool calls
        tool_calls = msg.get("tool_calls", [])
        tool_call_ids = [tc.get("id", "") for tc in tool_calls] if tool_calls else []
        
        # Handle tool results
        tool_call_id = msg.get("tool_call_id", "")
        
        if role == "system":
            md_content += f"\n## System\n\n{content}\n"
        elif role == "user":
            md_content += f"\n## User\n\n{content}\n"
        elif role == "assistant":
            md_content += f"\n## Assistant\n\n{content}\n"
            if tool_calls:
                md_content += f"\n### Tool Calls\n\n```json\n{json.dumps(tool_calls, indent=2)}\n```\n"
        elif role == "tool":
            md_content += f"\n## Tool Result ({tool_call_id})\n\n{content}\n"
    
    return filename, md_content

def main():
    """Main archiving function."""
    print("=" * 60)
    print("csp-brain Raw Session Archiver")
    print("=" * 60)
    
    # Load state
    state = load_state()
    archived_ids = set(state.get("archived_sessions", []))
    print(f"Previously archived sessions: {len(archived_ids)}")
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Scan for session files
    new_archived = 0
    errors = []
    
    if not os.path.exists(HERMES_SESSIONS_DIR):
        print(f"ERROR: Hermes sessions directory not found: {HERMES_SESSIONS_DIR}")
        return
    
    session_files = list(Path(HERMES_SESSIONS_DIR).glob("*.jsonl"))
    # Also check for .json files
    session_files.extend(Path(HERMES_SESSIONS_DIR).glob("*.json"))
    
    print(f"Found {len(session_files)} session files")
    
    for session_path in session_files:
        session_id = session_path.stem  # filename without extension
        
        # Skip if already archived
        if session_id in archived_ids:
            continue
        
        try:
            # Read session data
            with open(session_path, 'r', encoding='utf-8') as f:
                if session_path.suffix == '.jsonl':
                    # JSONL format - one JSON object per line
                    messages = []
                    for line in f:
                        line = line.strip()
                        if line:
                            messages.append(json.loads(line))
                    session_data = messages
                else:
                    # JSON format
                    session_data = json.load(f)
            
            # Convert to markdown
            filename, md_content = session_to_markdown(session_data, session_id)
            
            # Write output file
            output_path = os.path.join(OUTPUT_DIR, filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
            # Update state
            archived_ids.add(session_id)
            new_archived += 1
            print(f"  Archived: {session_id} -> {filename}")
            
        except Exception as e:
            error_msg = f"Error processing {session_id}: {str(e)}"
            errors.append(error_msg)
            print(f"  ERROR: {error_msg}")
    
    # Save updated state
    state["archived_sessions"] = sorted(list(archived_ids))
    state["last_run"] = datetime.now().isoformat()
    state["total_archived"] = len(archived_ids)
    save_state(state)
    
    # Summary
    print("\n" + "=" * 60)
    print("ARCHIVE SUMMARY")
    print("=" * 60)
    print(f"New sessions archived: {new_archived}")
    print(f"Total archived sessions: {len(archived_ids)}")
    print(f"Errors encountered: {len(errors)}")
    
    if errors:
        print("\nErrors:")
        for err in errors[:10]:  # Show first 10 errors
            print(f"  - {err}")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more")

if __name__ == "__main__":
    main()
