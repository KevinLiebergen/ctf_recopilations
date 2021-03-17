## gdb Debugger

* Some theory
    * `ESP register` Register to the top of the stack (Stack Pointer)
    * `EBP register` Register to the bottom of the stack (Bottom Pointer)
    * `EIP register` Point address of the next instruction (Instruction Pointer)

* Extra
    * `PEDA` Python Exploit Development Assistance for GDB, [recommended](https://github.com/longld/peda).
    * Inspect the functions and their address of the executable program
        * `$ objdump -M intel -D ./executable ` 
    * Maintain session
        * `$ (python exploit.py; cat) | ./executable`
        * `$ cat exploit - | ./executable`

  * Interactive shell (python 2)
    * `$ (python -c 'print("A"*5 + "\xde\xad\xbe\xef")'; cat;) | ./executable`

  * __There are differences between Python 2 and 3 por exploitation!__
    * [Python 2 vs 3 for Binary Exploitation Scripts](https://www.youtube.com/watch?v=FxNS-zSS7MQ)


* Install
    * `$ sudo apt install gdb`

* Compile
    * `$ gcc -o ej1 ej1.c --debug`

* Debugg
    * `$ gdb ej1`

* List source file
    * `(gdb) list`
    * `(gdb) l`

* Breakpoint
    * `(gdb) break main`
    * `(gdb) b main`

* Break by line
    * `(gdb) break 24`
    * `(gdb) b 24`

* Break by address
	* `(gdb) break *0x804855b`
	* `(gdb) b *0x804855b`

* Info breakpoints
	* `(gdb) info breakpoints`
	* `(gdb) i b`

* Delete breakpoints
	* `(gdb) delete 2`
	* `(gdb) d 2`

* Run the program
    * `(gdb) r`
    * `(gdb) run`
    * `(gdb) run $(python3 -c "print('A'*200)")`

* Continue to the next breakpoint
    * `(gdb) continue`
    * `(gdb) c`

* Next instruction (doesn't input into functions)
    * `(gdb) next`
    * `(gdb) n`

* Input into functions
    * `(gdb) step`
    * `(gdb) s`

* View registers
    * `(gdb) info registers esp`
    * `(gdb) info registers ebp`
    * `(gdb) i r ebp`
    * `...`

* Examine
    * `(gdb) x/`

* Disasssembly
    * `(gdb) disas main`

* Print some hexadecimal characters as argument
    * `(gdb) r $(printf "aaaaaabbbb\xa5\x51\x55\x55\x55\x55")`

* Exit program
    * `(gdb) quit`
    * `(gdb) q`


