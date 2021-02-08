# Volatility


* Information about the system and the memory dump
	* `$ volatility -f snap.vmem imageinfo`

* List running processes, in profile insert previous system
	* `$ volatility -f snap.vmem --profile=WinXPSP2x86 pslist`

* pslist with tree structure
	* `$ volatility -f snap.vmem --profile=WinXPSP2x86 pstree`

* List processes that are trying to hide themselves, it will appear "False" in the first two columns
	* `$ volatility -f snap.vmem --profile=WinXPSP2x86 psxview`


* Last commands ran
	* `$ volatility -f snap.vmem --profile=WinXPSP2x86 cmdline`


* Dump a process specified by the 11 PID
	* `$ volatility -f snap.vmem --profile=WinXPSP2x86 procdump -p 11 --dump-dir .`
	* `$ volatility -f snap.vmem --profile=WinXPSP2x86 memdump -p 11 --dump-dir .`


* Information about truecrypt
	* `$ volatility -f snap.vmem --profile WinXPSP2x86 truecryptsummary`
	* `$ volatility -f snap.vmem --profile WinXPSP2x86 truecryptpassphrase`
	* `$ volatility -f snap.vmem --profile WinXPSP2x86 truecryptmaster`
