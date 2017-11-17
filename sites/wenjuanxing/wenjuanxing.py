import requests
import soup
import payload
import model
import util
from urllib import quote


def main():
    #url= '''https://www.wjx.cn/m/18154018.aspx?from=groupmessage'''
    url = '''https://www.wjx.cn/jq/18227687.aspx'''
    n=1

    
    # phase1 : parse url to submit template
    templates = soup.parseTemplate(url)

    # get session cookie through verify api
    # cookieStr, cookieDict= getCookie(url)
    # print cookieStr

    session = getSession()
    print session.cookies.get_dict()
    #downloadVery(url, cookieDict)
    # phase2: payload generator

    # phase3: if need, download verification and ocr code

    # phase4: use payload, vercode, url and url headers to hack the fucking website
    #print util.getId(url)
    #cookie = ".ASPXANONYMOUS=P4k54UeV0wEkAAAAYmE0N2U4OTAtOTJkYy00NDgzLWE4YTMtMjBlMTc1MDRmMDdiKPBn5ySjrpuJ-DZzoN5o8vHPXcM1;ASP.NET_SessionId=0q3gkpay5gycmgvkucrifk2k"#".ASPXANONYMOUS=heZIRDyV0wEkAAAAZTA0YjIzN2EtMGMwZS00MDg0LWE4Y2YtMDM5OGYwN2JlYTdkxdTmAc1BJNWwJfjdJVSSNpkTxbU1;ASP.NET_SessionId=av0b5wveac0h12ll1ltzh4lu"
    entity=model.SubmitEntity(util.getId(url))
    commonHead=model.SubmitHeader(url).dict()
    print commonHead
    i=0
    tss = util.sitimulateTime(n)
    for payload in yieldNPayload(templates, n):
        ts=tss[i]
        print downloadVeryPic(session, util.getId(url),ts[1])
        str= raw_input("very code:")
        url = entity.genUrl(util.getDomain(url), str,ts[0],ts[1])
        print url
        print payload
        submit(session, url, commonHead, "submitdata=" + quote(payload))
        i+=1
    return 0

def yieldNPayload(template, n):
    for i in range (0,n):
        yield payload.randomPayload(template)

def submit(session, url, headers, payload):
    response = session.request("POST", url, data=payload, headers=headers)
    print session.cookies.get_dict()
    print response.content

def getCookie(url):
    session = requests.Session()
    session.request("Get", '''https://www.wjx.cn/AntiSpamImageGen.aspx?q=18227687&t=1510906863464''')
    dict= session.cookies.get_dict()
    t = []
    for k in dict:
        t.append(str(k) + "=" + str(dict[k]))
    return ";".join(t), dict

def getCookie2(url):
    session = requests.Session()
    session.request("Get", '''https://www.wjx.cn/AntiSpamImageGen.aspx?q=18227687&t=1510906863464''')
    dict= session.cookies.get_dict()
    t = []
    for k in dict:
        t.append(str(k) + "=" + str(dict[k]))
    print ";".join(t)

    session.request("Get", '''https://www.wjx.cn/AntiSpamImageGen.aspx?q=18227687&t=1510906863464''')
    dict= session.cookies.get_dict()
    t = []
    for k in dict:
        t.append(str(k) + "=" + str(dict[k]))
    print ";".join(t)

def getSession():
    session = requests.Session()
    session.request("Get", '''https://www.wjx.cn/AntiSpamImageGen.aspx?q=18227687&t=1510906863464''')
    return session

def downloadVery(url, cookieDict):
    session = requests.Session()
    session.request("Get", '''https://www.wjx.cn/AntiSpamImageGen.aspx?q=18227687&t=1510906863464''',cookies = cookieDict)
    dict= session.cookies.get_dict()
    t = []
    for k in dict:
         t.append(str(k) + "=" + str(dict[k]))
    print ";".join(t)

def downloadVeryPic(session, id, time):
    url = '''https://www.wjx.cn/AntiSpamImageGen.aspx?q=''' + str(id) + "&t=" + str(time)
    response = requests.request("Get", url)
    fn = util.randomFileName()
    fn += ".png"
    with open(fn, "wb") as f:
        f.write(response.content)
    return fn

if __name__ == "__main__":
    main()
    #print getCookie2("")
    #print downloadVeryPic("18227687",[], "1510906863464")