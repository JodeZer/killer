class SubmitData(object):
    def __init__(self):
        self.type = "submitdata"

class SubmitHeader(object):
    def __init__(self):
        self.type = "header"
        self.referer = kv("Referer",'''https://www.wjx.cn/jq/18227687.aspx''')
        self.origin = kv("Origin",'''https://www.wjx.cn''')
        self.userAgent = kv("User-Agent",'''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36''')
        self.contentType = kv("Content-Type",'''application/x-www-form-urlencoded''')

class SubmitApi(object):
    def __init__(self):
        self.api = '''/handler/processjq.ashx?'''

class SubmitEntity(object):
    def __init__(self, curID,submitType=1,rn=3030350310):
        self.submitType = kv("submittype",submitType)
        self.rn = kv("rn", rn)
        self.curID = kv("curId",curID)

    def genUrl(self,domain, start, end):
        url = domain + SubmitApi().api
        url += ("&" + self.submitType.genParam())
        url += ("&" + self.curID.genParam())
        url += ("&" + self.rn.genParam())
        return url

class kv(object):
    def __init__(self, key ,value):
        self.key = key
        self.value = value
    def genParam(self):
        return self.key + "=" + str(self.value)

# class dataGenerator(obejct):
#     def __init__(self, template):