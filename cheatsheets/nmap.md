# nmap CheatSheet

* Escanear puertos del 100 al 200
  * `$ nmap -p 100-200 172.16.1.1`

* Escanear puerto específico
  * `$ nmap -p 21 172.16.1.1`

* Escanear todos los puertos
  * `$ nmap -p- 172.16.1.1`

* Escanear versiones
  * `$ nmap -sV 172.16.1.1`

* Análisis con los scripts por defecto (Script Scanning)
  * `$ nmap -sC 172.16.1.1`

* Escaneo agresivo (-O -sV -sC --traceroute)
  * `$ nmap -A 172.16.1.1`

* Detección sistema operativo
  * `$ nmap -O 172.16.1.1` 


* Timing template (-T3 default)
  * paranoid, sneaky, polite, normal, aggresive, insane
  * `$ nmap -T[0-5] 172.16.1.1`

* Guardado en un fichero
  * `$ nmap 172.16.1.1 -o scanning.txt` 
