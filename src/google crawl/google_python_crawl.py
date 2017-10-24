# coding: utf-8

import re
import urllib2
import os

url = 'http://www.google.com/search?q=python'
headers = {'User-Agent' : 'Mozilla 5.0'}
request = urllib2.Request(url, None, headers)
response = urllib2.urlopen(request)
html = response.read()
p=re.compile('href="(https://.*?)"')
res=p.findall(html)
f=open(os.path.join('src','google_python.html'),'w')
f.write(html)
f.close()