import sys
import os

def verify_oka_summary(file_path):
    required_atoms = ["Resilience", "Engagement", "Stress Tolerance", "8-Cluster"]
    errors = []
    
    if not os.path.exists(file_path):
        return f"Error: File {file_path} not found."
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Rule 1: Existence Check
    for atom in required_atoms:
        if atom.lower() not in content.lower():
            errors.append(f"Missing Required Atom: {atom}")
            
    # Rule 2: Basic formatting check
    if "## 2. 핵심 지식 원자" not in content:
        errors.append("Missing Section: 핵심 지식 원자")
        
    return errors

if __name__ == "__main__":
    path = "/Users/dkmac/Desktop/@26/dev/outputs/analyses/PSY_ASSESS_SUMMARY.md"
    results = verify_oka_summary(path)
    if not results:
        print("PASS: OKA Summary follows all basic protocols.")
    else:
        print("FAIL: Validation Errors found:")
        for err in results:
            print(f"- {err}")
