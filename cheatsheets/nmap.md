# nmap CheatSheet

* Scan 100-200 ports
  * `$ nmap -p 100-200 172.16.1.1`

* Scan specific port
  * `$ nmap -p 21 172.16.1.1`

* Scan all ports
  * `$ nmap -p- 172.16.1.1`

* Scan versions
  * `$ nmap -sV 172.16.1.1`

* Analysis with the defaults scripts (Script Scanning)
  * `$ nmap -sC 172.16.1.1`

* Aggressive scanning (-O -sV -sC --traceroute)
  * `$ nmap -A 172.16.1.1`

* Detect operative system 
  * `$ nmap -O 172.16.1.1` 

* Timing template (-T3 default)
  * paranoid, sneaky, polite, normal, aggresive, insane
  * `$ nmap -T[0-5] 172.16.1.1`

* Save in a file
  * `$ nmap 172.16.1.1 -o scanning.txt` 
