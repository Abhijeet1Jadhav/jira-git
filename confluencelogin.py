import json
import httplib2
import urllib

get_url = "https://demo-sw.atlassian.net/wiki/rest/api/content/393217expand=body.storage"
login_url = "https://<your confluence url>/dologin.action"
username = "jadhavabhijeet6411@gmail.com"
password = "Sunnyaj@3024"

h = httplib2.Http(".cache")

headers = {'Content-type': 'application/x-www-form-urlencoded'}
body={'os_username': username, 'os_password': password}
resp, content = h.request(
 uri=login_url, 
 method='POST',
 headers = headers,
 body=urllib.urlencode(body)
)
cookies = resp.get("set-cookie")
headers = {'Cookie': cookies}

response, content = h.request(get_url, 'GET', headers=headers)

obj = json.loads(content)
print (obj['body']['storage']['value'])
