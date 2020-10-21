import re
import requests
import hashlib

h = 'http://134.122.109.72:31906/'

x = r'h3 align=\'center\'>([^\<]+)'
y = r'p align=\'center\'>([^\<]+)'

getval = lambda r: re.findall(x,r)[0]
getflag = lambda r: re.findall(y,r)[0]

def getFlag():
	s = requests.session()
	res = s.get(h)
	r = getval(res.text)
	hash = hashlib.md5(r.encode()).hexdigest()
	res = s.post(h, data=dict(hash=hash))
	return res

print(getflag(getFlag().text))
