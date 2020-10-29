## gdb Debugger

* Some theory
    * `ESP register` Register to the top of the stack (Stack Pointer)
    * `EBP register` Register to the bottom of the stack (Bottom Pointer)
    * `EIP register` Point address of the next instruction (Instruction Pointer)

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