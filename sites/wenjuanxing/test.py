import model
import util
import soup
import payload

testUrl = '''https://www.wjx.cn/m/18154018.aspx?from=groupmessage'''
testUrl2 = '''https://www.wjx.cn/jq/18227687.aspx'''
print util.getId(testUrl)
print util.getId(testUrl2)
# e=model.SubmitEntity(util.getId(testUrl),"123")
# print e.genUrl(util.getDomain(testUrl),123,123)


# url = "https://www.wjx.cn/handler/processjq.ashx"

# querystring = {"submittype":"1","curID":"18227687","t":"1510824446834","starttime":"2017/11/16 17:27:08","rn":"3030350310"}

# payload = "submitdata=1%25242%257D2%25242%257D3%25241%253C2%252C2%253C2%252C3%253C2%252C4%253C2%252C5%253C2%252C6%253C2%252C7%253C2"
# headers = {
#     'referer': "https://www.wjx.cn/jq/18227687.aspx",
#     'origin': "https://www.wjx.cn",
#     'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
#     'content-type': "application/x-www-form-urlencoded",
#     'cache-control': "no-cache",
#     'postman-token': "ec220369-cea2-6f21-8430-b9dab7d26ad0"
#     }

# response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

# print(response.text)

# curl -X POST \
#   'https://www.wjx.cn/handler/processjq.ashx?submittype=1&curID=18227687&t=1510824446834&starttime=2017%2F11%2F16%2017%3A27%3A08&rn=3030350310' \
#   -H 'cache-control: no-cache' \
#   -H 'content-type: application/x-www-form-urlencoded' \
#   -H 'origin: https://www.wjx.cn' \
#   -H 'postman-token: e158e3f5-2d1a-52c2-03dc-3ff9d535a3cc' \
#   -H 'referer: https://www.wjx.cn/jq/18227687.aspx' \
#   -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' \
#   -d submitdata=1%25242%257D2%25242%257D3%25241%253C2%252C2%253C2%252C3%253C2%252C4%253C2%252C5%253C2%252C6%253C2%252C7%253C2
# print payload.randomPayload(soup.parseTemplate(""))


#curl 'https://www.wjx.cn/AntiSpamImageGen.aspx?q=18227687&t=1510906863464' -H 'Pragma: no-cache' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' -H 'Accept: image/webp,image/apng,image/*,*/*;q=0.8' -H 'Referer: https://www.wjx.cn/jq/18227687.aspx' 
#-H 'Cookie: .ASPXANONYMOUS=heZIRDyV0wEkAAAAZTA0YjIzN2EtMGMwZS00MDg0LWE4Y2YtMDM5OGYwN2JlYTdkxdTmAc1BJNWwJfjdJVSSNpkTxbU1;
# UM_distinctid=15fc3ad1c126d-0cd94002cb869c-31657c00-13c680-15fc3ad1c15ee; SojumpABX_512=1; award_18154018=1; ASP.NET_SessionId=pngnpury1amqxoergnr3w1be; lllogcook=1; spiderregkey=www.wjx.cn%c2%a7%c2%a72; ConnectQQ=1; SojumpSurvey=0102517383EF8E2DD508FE51139576B02DD50800237100710024003300370034003000310064006300390061003300310034003900360032003500370064006600640061003800620066006100380066003800300034003600300000012F00FF12B9FF5112E08365F93541DE3AAF813C157E2B66; LastCheckUpdateDate=1; LastCheckDesign=1; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1510904632703; CNZZDATA4478442=cnzz_eid%3D348010643-1510813131-%26ntime%3D1510903811; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1510816423,1510824126,1510824135,1510904627; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1510906774' -H 'Connection: keep-alive' -H 'Cache-Control: no-cache' --compressed



 #curl 'https://www.wjx.cn/handler/processjq.ashx?submittype=1&curID=18227687&t=1510907047988&validate_text=3333&starttime=2017%2F11%2F17%2016%3A19%3A32&rn=3030350311' -H 'Pragma: no-cache' -H 'Origin: https://www.wjx.cn' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: zh-CN,zh;q=0.8,en;q=0.6' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Accept: */*' -H 'Cache-Control: no-cache' -H 'Referer: https://www.wjx.cn/jq/18227687.aspx' 
#-H 'Cookie: .ASPXANONYMOUS=heZIRDyV0wEkAAAAZTA0YjIzN2EtMGMwZS00MDg0LWE4Y2YtMDM5OGYwN2JlYTdkxdTmAc1BJNWwJfjdJVSSNpkTxbU1; UM_distinctid=15fc3ad1c126d-0cd94002cb869c-31657c00-13c680-15fc3ad1c15ee; SojumpABX_512=1; award_18154018=1; ASP.NET_SessionId=pngnpury1amqxoergnr3w1be; lllogcook=1; spiderregkey=www.wjx.cn%c2%a7%c2%a72; ConnectQQ=1; SojumpSurvey=0102517383EF8E2DD508FE51139576B02DD50800237100710024003300370034003000310064006300390061003300310034003900360032003500370064006600640061003800620066006100380066003800300034003600300000012F00FF12B9FF5112E08365F93541DE3AAF813C157E2B66; LastCheckUpdateDate=1; LastCheckDesign=1; _cnzz_CV4478442=%E7%94%A8%E6%88%B7%E7%89%88%E6%9C%AC%7C%E5%85%8D%E8%B4%B9%E7%89%88%7C1510904632703; CNZZDATA4478442=cnzz_eid%3D348010643-1510813131-%26ntime%3D1510903811; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1510816423,1510824126,1510824135,1510904627; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1510906774' -H 'Connection: keep-alive' --data 'submitdata=1%241%7D2%241%7D3%241%3C1%2C2%3C1%2C3%3C1%2C4%3C1%2C5%3C1%2C6%3C1%2C7%3C1' --compressed