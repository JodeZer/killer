
import re

def getId(url):
    return re.search('''www.wjx.cn/m/(.+).aspx?''', url).group(1)

def getDomain(url):
    return "https://www.wjx.cn"