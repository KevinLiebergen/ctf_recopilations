## Crackme

1. Hallamos el tipo de fichero que es mediante
* `$ file CrackMeEasy.exe` 

`CrackMeEasy.exe: PE32+ executable (GUI) x86-64 Mono/.Net assembly, for MS Windows`

2. Vemos que es un archivo .NET, utilizamos `dnSpy` para decompilarlo.

3. Buscamos donde hace la comprobación de la password que te pide, hacemos un breakpoint y analizamos la variable con la que comprueba, y esa es la password.

