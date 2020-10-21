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

* Continue to the next breakpoint
    * `(gdb) continue`
    * `(gdb) c`

* Next instruction (doesn't input into functions)
    * `(gdb) next`
    * `(gdb) n`

* Input into functions
    * `(gdb) step`
    * `(gdb) s`

* Call/print some function/variable
    * `(gdb) print func("a")`
    * `(gdb) p variable_a`

* set
    * `(gdb) set`
    * `(gdb) s`

* Exit program
    * `(gdb) quit`
    * `(gdb) q`