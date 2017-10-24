import os
import mylib
import urllib
import urlparse
import requests

keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
key=mylib.getKey(keyPath)


_d=dict()
_d['dataTerm']='month'

SERVICE='ArpltnInforInqireSvc'
OPERATION_NAME='getMinuDustFrcstDspth'
params1=os.path.join(SERVICE,OPERATION_NAME)
params2 = urllib.urlencode(_d)
params=params1+'?'+'serviceKey='+key['gokr']+'&'+params2
_url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
url=urlparse.urljoin(_url,params)
data=requests.get(url).text
print data