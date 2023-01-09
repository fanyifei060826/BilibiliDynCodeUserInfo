import requests
import json
dyn=int(input('动态码'))
infos={'dynamic_id':dyn}
response=requests.get('http://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail',params=infos)
#'https://api.vc.bilibili.com/svr_sync/v1/svr_sync/fetch_session_msgs?sender_device_id=1&talker_id=123&session_type=1&size=20&build=0&mobi_app=web'
#http://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail
if response.status_code==200:
    print('Server Connected，200')
else:
    print('Server redirected or resource missing, status code：%d'%requests.status_codes)
def jprint(obj):
    text=json.dumps(obj,sort_keys=True,indent=4)
    print(text)
jprint(response.json())
