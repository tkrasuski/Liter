import requests as rq
import json as js
rid = None
headers =  {'Content-type': 'application/json', 'Accept': 'text/plain'}
url = 'http://127.0.0.1:3000/api/welcome'
chunk = {'call':'sq5tk'}
req = rq.post(url, data=js.dumps(chunk), headers=headers,verify=False)
print(req.text)
if req.status_code == 200:
    rid = js.loads(req.text)['call']
else:
    print('connection error!!!')

print(req.status_code)