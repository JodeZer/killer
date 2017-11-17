import soup
import random

def randomPayload(template):
    ret = []
    for t in template:
        one = str(t.index) + "$"
        if t.num == 1:
            one += str(random.randint(1,t.max))
        else:
            part = []
            for i in range (1,t.num + 1):
                part.append(str(i) + "<" + str(random.randint(1,t.max)))
            one += ",".join(part)
        ret.append(one)
    return "}".join(ret)