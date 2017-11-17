import model
import util
import soup
import payload

# testUrl = '''https://www.wjx.cn/m/18154018.aspx?from=groupmessage'''
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

print payload.randomPayload(soup.parseTemplate(""))