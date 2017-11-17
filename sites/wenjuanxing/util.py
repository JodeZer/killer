
import re
import time
import datetime
import random

def getId(url):
    return re.search('''https://www.wjx.cn/.+/([0-9]+).aspx?''', url).group(1)

def getDomain(url):
    return "https://www.wjx.cn"

def sitimulateTime(n):
    delta = 30
    now = time.time()
    ret = []
    for i in range (0, n):
        endTs = int(round((now-30*i)*1000))
        startTs = int((endTs - 1000 * 60)/1000)
        startFmt = datetime.datetime.fromtimestamp(startTs).strftime("%Y-%m-%d %H:%M:%S")
        ret.append([startFmt, endTs])
    return ret

def randomFileName():
    now = int(round(time.time()))
    rand = random.randint(0, 1000)
    return str(now) + "-" + str(rand) 
    
