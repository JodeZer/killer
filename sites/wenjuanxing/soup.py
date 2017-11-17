
def parseTemplate(url):
    #TODO
    ret=[]
    ret.append(template(1,1,2))
    ret.append(template(2,1,5))
    ret.append(template(3,5,5))
    return ret


class template(object):
    def __init__(self, index, num, max):
        self.index=index
        self.num=num
        self.max=max