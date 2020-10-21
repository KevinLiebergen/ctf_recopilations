# writeup-OverTheWire-24--25

### Level Goal
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.

<br>Un demonio está escuchando en el puerto 30002 y te dará la contraseña para bandit25 si das la contraseña para bandit24 y un PIN secreto de 4 dígitos. No hay forma de averiguar el código PIN excepto si se pasan por las 10000 combinaciones, es decir es necesario aplicar fuerza bruta.

## Solución

-  Una vez te conectes al servidor como bandit24 (ssh bandit25@bandit.labs.overthewire.org -p 2220) es necesario crear un archivo que genere todas posibles combinaciones.

-  Cuando se tenga ese archivo se pasa por parámetro al puerto 30002.

$ chmod 755 generadorNumeros.sh

$ sh generadorNumeros.sh

-  Una vez logueado como bandit24 se crea una carpeta y se copian ambos archivos (generadorNumeros.sh y numeros) a esa carpeta

$ mkdir /tmp/prueba

$ cd /tmp/prueba

-  Se pasa por parametros al puerto 30002 todas las líneas de números que se corresponden con las posibles combinaciones. La salida por la terminal se guarda en el fichero de texto resultados.txt.

$ nc localhost 30002 < numeros > resultados.txt

$ cat resultados.txt | uniq -u

<br>Correct!
<br>The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.
