# Extracted Knowledge from Conv: 4981bac2-f924-4530-b166-6bba9dfdccb0

**Date**: 2025-12-10T06:04:28.321422Z

### Extracted Code (python)

```python
import base64

client_id = "your_client_id"
client_secret = "your_client_secret"

# Base64 인코딩
credentials = f"{client_id}:{client_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()
bearer_token = f"Basic {encoded_credentials}"
```

### Extracted Code (python)

```python
import requests
import base64

# 인증 정보
client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
organization_id = "YOUR_ORG_ID"  # Business API용

# Bearer Token 생성
credentials = f"{client_id}:{client_secret}"
encoded = base64.b64encode(credentials.encode()).decode()

# API 호출
url = f"https://YOUR_PORTAL.udemy.com/api-2.0/organizations/{organization_id}/courses/list/"

headers = {
    "Authorization": f"Basic {encoded}",
    "Content-Type": "application/json"
}

params = {
    "fields[courses]": "@all",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
courses = response.json()

print(courses)
```

### Extracted Code (javascript)

```javascript
const axios = require('axios');

const clientId = 'YOUR_CLIENT_ID';
const clientSecret = 'YOUR_CLIENT_SECRET';
const organizationId = 'YOUR_ORG_ID';
const portalName = 'YOUR_PORTAL_NAME';

// Bearer Token 생성
const token = Buffer.from(`${clientId}:${clientSecret}`).toString('base64');

// API 호출
const url = `https://${portalName}.udemy.com/api-2.0/organizations/${organizationId}/courses/list/`;

axios.get(url, {
  headers: {
    'Authorization': `Basic ${token}`,
    'Content-Type': 'application/json'
  },
  params: {
    'fields[courses]': '@all',
    'page': 1,
    'page_size': 10
  }
})
.then(response => {
  console.log(response.data);
})
.catch(error => {
  console.error(error);
});
```
