import requests
url='http://freegeoip.net/json/'
geostr=requests.get(url).text
print geostr