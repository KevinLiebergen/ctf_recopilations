# nmap CheatSheet

* Scan specific ips
  * `$ nmap 172.16.1-255.3`

* Scan 100-200 ports
  * `$ nmap -p 100-200 172.16.1.1`

* Scan specific port
  * `$ nmap -p 21 172.16.1.1`

* Scan all ports
  * `$ nmap -p- 172.16.1.1`

* Scan versions
  * `$ nmap -sV 172.16.1.1`

* Script Scanning
  * Analysis with the defaults scripts
  * `$ nmap -sC 172.16.1.1`

* Fast scanning
  * `$ nmap -F 192.168.1.10`

* Input FileName
  * `$ nmap -iL [objetivos.txt]`

* Detect operative system 
  * `$ nmap -O 172.16.1.1` 

* Aggressive scanning (-O -sV -sC --traceroute)
  * `$ nmap -A 172.16.1.1`

* TCP SYN (Stealth) Scan 
  * Never completes TCP connections, default scan by root
  * SYN - SYN/ACK - RST
  * `$ nmap -sS 172.16.1.1`

* TCP connect scan
  * SYN - SYN/ACK - ACK
  * `$ nmap -sT 172.16.1.1`

* Ping scan, disable port scan
  * `$ nmap -sn 172.16.1.1`

* Timing template (-T3 default)
  * paranoid, sneaky, polite, normal, aggresive, insane
  * `$ nmap -T[0-5] 172.16.1.1`

* Save in a file
  * `$ nmap 172.16.1.1 -o scanning.txt`


