from collections import OrderedDict
d=OrderedDict()
d ={'a':5,'b':4 }
d['a'] =d['a']+6
for k,v in d.items():
    print(k,v)