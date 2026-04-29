# Extracted Knowledge from Conv: 18e98d97-8a3b-40c5-b345-9f12ff9def57

**Date**: 2026-01-09T23:11:01.835588Z

### Extracted Code (bash)

```bash
mkdir ms-google-bridge
cd ms-google-bridge

# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 프로젝트 구조
mkdir -p {src,config,logs,data,tests}
touch src/{__init__.py,ms_connector.py,google_connector.py,notion_hub.py,workflows.py}
touch config/{settings.py,credentials.json}
touch requirements.txt
touch main.py
```

### Extracted Code (txt)

```txt
# Microsoft 생태계
msal==1.26.0
msgraph-sdk==1.1.0
O365==2.0.31

# Google 생태계
google-api-python-client==2.108.0
google-auth-httplib2==0.2.0
google-auth-oauthlib==1.2.0

# Notion
notion-client==2.2.1

# 유틸리티
python-dotenv==1.0.0
requests==2.31.0
schedule==1.2.0
pandas==2.1.4
pyyaml==6.0.1

# 로깅 및 모니터링
loguru==0.7.2
```

### Extracted Code (python)

```python
import os
from dotenv import load_dotenv

load_dotenv()

# Microsoft
MS_CLIENT_ID = os.getenv('MS_CLIENT_ID')
MS_CLIENT_SECRET = os.getenv('MS_CLIENT_SECRET')
MS_TENANT_ID = os.getenv('MS_TENANT_ID')
MS_SCOPES = [
    'Calendars.ReadWrite',
    'Files.ReadWrite.All',
    'Mail.ReadWrite',
    'Tasks.ReadWrite'
]

# Google
GOOGLE_CREDENTIALS_FILE = 'config/google_credentials.json'
GOOGLE_TOKEN_FILE = 'config/google_token.json'
GOOGLE_SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/tasks'
]

# Notion
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_DATABASE_ID = os.getenv('NOTION_DATABASE_ID')
```

### Extracted Code (env)

```env
MS_CLIENT_ID=your_client_id
MS_CLIENT_SECRET=your_client_secret
MS_TENANT_ID=your_tenant_id

NOTION_TOKEN=your_notion_token
NOTION_DATABASE_ID=your_database_id
```

### Extracted Code (python)

```python
from O365 import Account
from config.settings import MS_CLIENT_ID, MS_CLIENT_SECRET, MS_SCOPES
from loguru import logger

class MSConnector:
    def __init__(self):
        self.credentials = (MS_CLIENT_ID, MS_CLIENT_SECRET)
        self.account = None
        
    def authenticate(self):
        """Microsoft 인증"""
        try:
            self.account = Account(self.credentials)
            
            if not self.account.is_authenticated:
                # 브라우저 인증
                self.account.authenticate(scopes=MS_SCOPES)
                logger.info("MS 인증 성공")
            
            return True
        except Exception as e:
            logger.error(f"MS 인증 실패: {e}")
            return False
    
    def get_calendar_events(self, days=7):
        """Outlook 캘린더 이벤트 조회"""
        if not self.account:
            self.authenticate()
        
        schedule = self.account.schedule()
        calendar = schedule.get_default_calendar()
        
        from datetime import datetime, timedelta
        start = datetime.now()
        end = start + timedelta(days=days)
        
        events = calendar.get_events(
            start=start,
            end=end,
            include_recurring=True
        )
        
        return [{
            'id': event.object_id,
            'subject': event.subject,
            'start': event.start.isoformat(),
            'end': event.end.isoformat(),
            'location': event.location,
            'body': event.body,
            'attendees': [a.address for a in event.attendees],
            'source': 'microsoft'
        } for event in events]
    
    def create_calendar_event(self, event_data):
        """Outlook 캘린더 이벤트 생성"""
        schedule = self.account.schedule()
        calendar = schedule.get_default_calendar()
        
        event = calendar.new_event()
        event.subject = event_data['subject']
        event.start = event_data['start']
        event.end = event_data['end']
        event.location = event_data.get('location', '')
        event.body = event_data.get('body', '')
        
        event.save()
        logger.info(f"MS 이벤트 생성: {event.subject}")
        return event.object_id
    
    def get_onedrive_files(self, folder_path='root'):
        """OneDrive 파일 목록 조회"""
        storage = self.account.storage()
        drive = storage.get_default_drive()
        
        if folder_path == 'root':
            folder = drive.get_root_folder()
        else:
            folder = drive.get_item_by_path(folder_path)
        
        files = []
        for item in folder.get_items():
            files.append({
                'id': item.object_id,
                'name': item.name,
                'path': item.full_path,
                'size': item.size,
                'modified': item.modified.isoformat(),
                'web_url': item.web_url,
                'source': 'onedrive'
            })
        
        return files
    
    def get_tasks(self, list_name='Tasks'):
        """MS To Do 작업 조회"""
        todo = self.account.tasks()
        task_list = todo.get_folder(folder_name=list_name)
        
        tasks = []
        for task in task_list.get_tasks():
            tasks.append({
                'id': task.object_id,
                'title': task.subject,
                'status': task.status,
                'due_date': task.due.isoformat() if task.due else None,
                'created': task.created.isoformat(),
                'source': 'ms_todo'
            })
        
        return tasks
```

### Extracted Code (python)

```python
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from config.settings import GOOGLE_CREDENTIALS_FILE, GOOGLE_TOKEN_FILE, GOOGLE_SCOPES
from loguru import logger
import os.path

class GoogleConnector:
    def __init__(self):
        self.creds = None
        self.calendar_service = None
        self.drive_service = None
        self.tasks_service = None
        
    def authenticate(self):
        """Google 인증"""
        try:
            if os.path.exists(GOOGLE_TOKEN_FILE):
                self.creds = Credentials.from_authorized_user_file(
                    GOOGLE_TOKEN_FILE, GOOGLE_SCOPES
                )
            
            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    self.creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        GOOGLE_CREDENTIALS_FILE, GOOGLE_SCOPES
                    )
                    self.creds = flow.run_local_server(port=0)
                
                with open(GOOGLE_TOKEN_FILE, 'w') as token:
                    token.write(self.creds.to_json())
            
            self.calendar_service = build('calendar', 'v3', credentials=self.creds)
            self.drive_service = build('drive', 'v3', credentials=self.creds)
            self.tasks_service = build('tasks', 'v1', credentials=self.creds)
            
            logger.info("Google 인증 성공")
            return True
            
        except Exception as e:
            logger.error(f"Google 인증 실패: {e}")
            return False
    
    def get_calendar_events(self, days=7):
        """Google 캘린더 이벤트 조회"""
        from datetime import datetime, timedelta
        
        start_time = datetime.utcnow().isoformat() + 'Z'
        end_time = (datetime.utcnow() + timedelta(days=days)).isoformat() + 'Z'
        
        events_result = self.calendar_service.events().list(
            calendarId='primary',
            timeMin=start_time,
            timeMax=end_time,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])
        
        return [{
            'id': event['id'],
            'subject': event.get('summary', ''),
            'start': event['start'].get('dateTime', event['start'].get('date')),
            'end': event['end'].get('dateTime', event['end'].get('date')),
            'location': event.get('location', ''),
            'description': event.get('description', ''),
            'attendees': [a['email'] for a in event.get('attendees', [])],
            'source': 'google'
        } for event in events]
    
    def create_calendar_event(self, event_data):
        """Google 캘린더 이벤트 생성"""
        event = {
            'summary': event_data['subject'],
            'location': event_data.get('location', ''),
            'description': event_data.get('body', ''),
            'start': {
                'dateTime': event_data['start'],
                'timeZone': 'Asia/Seoul',
            },
            'end': {
                'dateTime': event_data['end'],
                'timeZone': 'Asia/Seoul',
            }
        }
        
        created_event = self.calendar_service.events().insert(
            calendarId='primary',
            body=event
        ).execute()
        
        logger.info(f"Google 이벤트 생성: {event['summary']}")
        return created_event['id']
    
    def get_drive_files(self, folder_id='root'):
        """Google Drive 파일 목록 조회"""
        query = f"'{folder_id}' in parents and trashed=false"
        
        results = self.drive_service.files().list(
            q=query,
            fields="files(id, name, mimeType, size, modifiedTime, webViewLink)",
            pageSize=100
        ).execute()
        
        files = results.get('files', [])
        
        return [{
            'id': f['id'],
            'name': f['name'],
            'type': f['mimeType'],
            'size': f.get('size', 0),
            'modified': f['modifiedTime'],
            'web_url': f['webViewLink'],
            'source': 'google_drive'
        } for f in files]
    
    def get_tasks(self, tasklist='@default'):
        """Google Tasks 조회"""
        results = self.tasks_service.tasks().list(
            tasklist=tasklist
        ).execute()
        
        tasks = results.get('items', [])
        
        return [{
            'id': task['id'],
            'title': task.get('title', ''),
            'status': task.get('status', ''),
            'due_date': task.get('due', None),
            'notes': task.get('notes', ''),
            'source': 'google_tasks'
        } for task in tasks]
```

### Extracted Code (python)

```python
from notion_client import Client
from config.settings import NOTION_TOKEN, NOTION_DATABASE_ID
from loguru import logger
from datetime import datetime

class NotionHub:
    """Notion을 중앙 허브로 활용"""
    
    def __init__(self):
        self.client = Client(auth=NOTION_TOKEN)
        self.database_id = NOTION_DATABASE_ID
    
    def create_unified_record(self, data, record_type):
        """통합 레코드 생성"""
        try:
            properties = self._build_properties(data, record_type)
            
            response = self.client.pages.create(
                parent={"database_id": self.database_id},
                properties=properties
            )
            
            logger.info(f"Notion 레코드 생성: {data.get('name', data.get('subject', 'Unknown'))}")
            return response['id']
            
        except Exception as e:
            logger.error(f"Notion 레코드 생성 실패: {e}")
            return None
    
    def _build_properties(self, data, record_type):
        """Notion 속성 구성"""
        base_properties = {
            "이름": {
                "title": [{
                    "text": {
                        "content": data.get('name', data.get('subject', data.get('title', 'Untitled')))
                    }
                }]
            },
            "타입": {
                "select": {
                    "name": record_type
                }
            },
            "출처": {
                "select": {
                    "name": data.get('source', 'unknown')
                }
            },
            "생성일": {
                "date": {
                    "start": datetime.now().isoformat()
                }
            }
        }
        
        # 타입별 추가 속성
        if record_type == '캘린더':
            base_properties["시작"] = {"date": {"start": data['start']}}
            base_properties["종료"] = {"date": {"start": data['end']}}
            if data.get('location'):
                base_properties["위치"] = {"rich_text": [{"text": {"content": data['location']}}]}
        
        elif record_type == '파일':
            base_properties["URL"] = {"url": data.get('web_url', '')}
            base_properties["크기"] = {"number": int(data.get('size', 0))}
        
        elif record_type == '작업':
            base_properties["상태"] = {"select": {"name": data.get('status', '진행중')}}
            if data.get('due_date'):
                base_properties["마감일"] = {"date": {"start": data['due_date']}}
        
        return base_properties
    
    def search_records(self, query, record_type=None):
        """Notion 검색"""
        filter_conditions = {
            "and": [
                {
                    "property": "이름",
                    "title": {
                        "contains": query
                    }
                }
            ]
        }
        
        if record_type:
            filter_conditions["and"].append({
                "property": "타입",
                "select": {
                    "equals": record_type
                }
            })
        
        results = self.client.databases.query(
            database_id=self.database_id,
            filter=filter_conditions
        )
        
        return results['results']
```

### Extracted Code (python)

```python
from src.ms_connector import MSConnector
from src.google_connector import GoogleConnector
from src.notion_hub import NotionHub
from loguru import logger
from datetime import datetime
import json

class SyncWorkflows:
    def __init__(self):
        self.ms = MSConnector()
        self.google = GoogleConnector()
        self.notion = NotionHub()
        
        # 인증
        self.ms.authenticate()
        self.google.authenticate()
    
    def sync_calendars_to_notion(self):
        """양쪽 캘린더를 Notion에 통합"""
        logger.info("=== 캘린더 동기화 시작 ===")
        
        # MS 캘린더
        ms_events = self.ms.get_calendar_events(days=7)
        for event in ms_events:
            self.notion.create_unified_record(event, '캘린더')
        
        # Google 캘린더
        google_events = self.google.get_calendar_events(days=7)
        for event in google_events:
            self.notion.create_unified_record(event, '캘린더')
        
        logger.info(f"동기화 완료: MS {len(ms_events)}개, Google {len(google_events)}개")
        
        return {
            'ms_count': len(ms_events),
            'google_count': len(google_events),
            'timestamp': datetime.now().isoformat()
        }
    
    def sync_files_to_notion(self):
        """양쪽 파일을 Notion에 통합"""
        logger.info("=== 파일 동기화 시작 ===")
        
        # OneDrive
        onedrive_files = self.ms.get_onedrive_files()
        for file in onedrive_files[:50]:  # 최근 50개
            self.notion.create_unified_record(file, '파일')
        
        # Google Drive
        drive_files = self.google.get_drive_files()
        for file in drive_files[:50]:  # 최근 50개
            self.notion.create_unified_record(file, '파일')
        
        logger.info(f"파일 동기화 완료: OneDrive {len(onedrive_files)}개, Drive {len(drive_files)}개")
        
        return {
            'onedrive_count': len(onedrive_files),
            'drive_count': len(drive_files),
            'timestamp': datetime.now().isoformat()
        }
    
    def sync_tasks_to_notion(self):
        """양쪽 작업을 Notion에 통합"""
        logger.info("=== 작업 동기화 시작 ===")
        
        # MS To Do
        ms_tasks = self.ms.get_tasks()
        for task in ms_tasks:
            self.notion.create_unified_record(task, '작업')
        
        # Google Tasks
        google_tasks = self.google.get_tasks()
        for task in google_tasks:
            self.notion.create_unified_record(task, '작업')
        
        logger.info(f"작업 동기화 완료: MS {len(ms_tasks)}개, Google {len(google_tasks)}개")
        
        return {
            'ms_count': len(ms_tasks),
            'google_count': len(google_tasks),
            'timestamp': datetime.now().isoformat()
        }
    
    def cross_platform_event_create(self, event_data, target='both'):
        """양쪽 캘린더에 동시 생성"""
        results = {}
        
        if target in ['both', 'microsoft']:
            ms_id = self.ms.create_calendar_event(event_data)
            results['microsoft'] = ms_id
        
        if target in ['both', 'google']:
            google_id = self.google.create_calendar_event(event_data)
            results['google'] = google_id
        
        # Notion에도 기록
        self.notion.create_unified_record(event_data, '캘린더')
        
        return results
    
    def generate_daily_report(self):
        """일일 통합 리포트 생성"""
        report = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'calendars': self.sync_calendars_to_notion(),
            'files': self.sync_files_to_notion(),
            'tasks': self.sync_tasks_to_notion()
        }
        
        # JSON으로 저장
        with open(f"data/report_{report['date']}.json", 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        
        logger.info(f"일일 리포트 생성 완료: {report['date']}")
        return report
```

### Extracted Code (python)

```python
from src.workflows import SyncWorkflows
from loguru import logger
import schedule
import time

# 로깅 설정
logger.add(
    "logs/bridge_{time}.log",
    rotation="1 day",
    retention="30 days",
    level="INFO"
)

def main():
    """메인 실행"""
    logger.info("=== MS-Google Bridge 시작 ===")
    
    workflows = SyncWorkflows()
    
    # 즉시 실행
    print("\n1. 캘린더 동기화 중...")
    workflows.sync_calendars_to_notion()
    
    print("\n2. 파일 동기화 중...")
    workflows.sync_files_to_notion()
    
    print("\n3. 작업 동기화 중...")
    workflows.sync_tasks_to_notion()
    
    print("\n✅ 초기 동기화 완료!")
    print("\n자동화 스케줄 시작...")
    
    # 스케줄 설정
    schedule.every().day.at("09:00").do(workflows.generate_daily_report)
    schedule.every(30).minutes.do(workflows.sync_calendars_to_notion)
    schedule.every(2).hours.do(workflows.sync_files_to_notion)
    schedule.every(1).hours.do(workflows.sync_tasks_to_notion)
    
    # 무한 루프 실행
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()
```

### Extracted Code (python)

```python
from src.workflows import SyncWorkflows
from datetime import datetime, timedelta

workflows = SyncWorkflows()

# 양쪽 캘린더에 동시 생성
event = {
    'subject': '프로젝트 킥오프 미팅',
    'start': (datetime.now() + timedelta(days=1)).isoformat(),
    'end': (datetime.now() + timedelta(days=1, hours=1)).isoformat(),
    'location': '3층 회의실',
    'body': 'Q1 프로젝트 킥오프'
}

results = workflows.cross_platform_event_create(event, target='both')
print(f"생성 완료: {results}")
```

### Extracted Code (python)

```python
# cli.py
import click
from src.workflows import SyncWorkflows

@click.group()
def cli():
    """MS-Google Bridge CLI"""
    pass

@cli.command()
def sync_all():
    """전체 동기화"""
    workflows = SyncWorkflows()
    workflows.sync_calendars_to_notion()
    workflows.sync_files_to_notion()
    workflows.sync_tasks_to_notion()
    click.echo("✅ 전체 동기화 완료")

@cli.command()
@click.option('--title', prompt='이벤트 제목')
@click.option('--date', prompt='날짜 (YYYY-MM-DD)')
def create_event(title, date):
    """크로스 플랫폼 이벤트 생성"""
    from datetime import datetime
    
    workflows = SyncWorkflows()
    event = {
        'subject': title,
        'start': f"{date}T09:00:00",
        'end': f"{date}T10:00:00",
    }
    workflows.cross_platform_event_create(event)
    click.echo(f"✅ '{title}' 이벤트 생성 완료")

if __name__ == '__main__':
    cli()
```

### Extracted Code (dockerfile)

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### Extracted Code (yaml)

```yaml
# docker-compose.yml
version: '3.8'

services:
  bridge:
    build: .
    volumes:
      - ./config:/app/config
      - ./logs:/app/logs
      - ./data:/app/data
    environment:
      - TZ=Asia/Seoul
    restart: unless-stopped
```

### Extracted Code (python)

```python
# daily_schedule.py
from O365 import Account
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

def show_today_schedule():
    print("\n📅 오늘의 통합 일정\n")
    print("=" * 50)
    
    # MS 캘린더 (인증은 최초 1회만)
    ms_account = Account(('YOUR_CLIENT_ID', 'YOUR_SECRET'))
    if not ms_account.is_authenticated:
        ms_account.authenticate()
    
    schedule = ms_account.schedule()
    calendar = schedule.get_default_calendar()
    
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    
    print("\n[MS Outlook 일정]")
    for event in calendar.get_events(start=today, end=tomorrow):
        print(f"  {event.start.strftime('%H:%M')} - {event.subject}")
    
    # Google 캘린더
    creds = Credentials.from_authorized_user_file('token.json')
    service = build('calendar', 'v3', credentials=creds)
    
    print("\n[Google 캘린더 일정]")
    events = service.events().list(
        calendarId='primary',
        timeMin=today.isoformat() + 'Z',
        timeMax=tomorrow.isoformat() + 'Z',
        singleEvents=True,
        orderBy='startTime'
    ).execute().get('items', [])
    
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"  {start[11:16]} - {event['summary']}")

if __name__ == '__main__':
    show_today_schedule()
```
