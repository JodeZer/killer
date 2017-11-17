from urllib import quote

class SubmitData(object):
    def __init__(self):
        self.type = "submitdata"

class SubmitHeader(object):
    def __init__(self,referer):
        self.type = "header"
        self.referer = kv("Referer",referer)
        #self.cookie = kv("Cookie", cookie)
        self.origin = kv("Origin",'''https://www.wjx.cn''')
        self.userAgent = kv("User-Agent",'''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36''')
        self.contentType = kv("Content-Type",'''application/x-www-form-urlencoded''')
    def dict(self):
        dict = {}
        dict[self.referer.key] = self.referer.value
        dict[self.origin.key] = self.origin.value
        dict[self.userAgent.key] = self.userAgent.value
        dict[self.contentType.key] = self.contentType.value
        #dict[self.cookie.key] = self.cookie.value
        return dict
    

class SubmitApi(object):
    def __init__(self):
        self.api = '''/handler/processjq.ashx?'''

class SubmitEntity(object):
    def __init__(self, curID,submitType=1,rn=3030350310):
        self.submitType = kv("submittype",submitType)
        self.rn = kv("rn", rn)
        self.curID = kv("curId",curID)

    def genUrl(self,domain, validate_text,start, end):
        url = domain + SubmitApi().api
        url += ("&" + self.submitType.genParam())
        url += ("&" + self.curID.genParam())
        url += ("&" + self.rn.genParam())
        url += ("&" + kv("starttime", start).genParam())
        url += ("&" + kv("t", end).genParam())
        url += ("&" + kv("validate_text", validate_text).genParam())
        return url

class kv(object):
    def __init__(self, key ,value):
        self.key = key
        self.value = value
    def genParam(self):
        return self.key + "=" + quote(str(self.value))

# class dataGenerator(obejct):
#     def __init__(self, template):