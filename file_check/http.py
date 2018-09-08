import requests
import pprint
import json
import datetime
import os
import sys

## file write
def printlog(logstr):
    path='./test.log'
    with open(path, mode='aw') as f:
        logstr = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')+' '+str(log)+'\n'
        f.write(logstr)

token = "dj00aiZpPUQ4VjY2SDhtUDl0VSZzPWNvbnN1bWVyc2VjcmV0Jng9OGI-"
coordinates="139.427331,35.524357"
output="json"
params = {'coordinates': coordinates, 'output': output, 'appid': token}
url="https://map.yahooapis.jp/alt/V1/getAltitude"

response = requests.get(url, params=params)

# status check
if 200 != response.status_code:
    print "error:" + str(response.status_code)
else:
    print "success:" + str(response.status_code)

res = response.json()

pprint.pprint(res)
altitude = res['Feature'][0]['Property']['Altitude']
log = ''
if altitude > 100:
    log =  "hoge:" + str(altitude)
else:
    log =  "fuga::" + str(altitude)

# file exist check
#checkpath='./transferfile.txt'

conf=sys.argv[1]
with open(conf) as f:
    for line in f:
        line = line.strip()
        print line
        if os.path.exists(line):
            log = line + " is exists. OK"
            printlog(log)
        else:
            log = line + " is not exists. ERROR"
            printlog(log)
