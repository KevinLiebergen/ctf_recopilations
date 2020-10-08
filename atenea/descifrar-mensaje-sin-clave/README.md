# ¿Podrás descifrar el mensaje sin clave?

Esta prueba consiste en un texto cifrado, no se sabe que tipo de criptografía ni que clave se usa.

Cada carácter se sustituye por un determinado carácter del alfabeto del texto cifrado, por lo que averiguamos que carácter se sustituye por cada letra a partir de palabras pequeñas.

Ni las letras mayúsculas ni las vocales con tildes se sustituyen por lo que las letras cifradas las transformamos en mayúsculas.

## Ejecución

-  `git clone https://github.com/KevinLiebergen/Podras-descifrar-el-mensaje-sin-clave.git`

-  `cd Podras-descifrar-el-mensaje-sin-clave`

-  `python3 descifrarMensajeSinClave.py`

El flag se encuentra escondido en el archivo creado, las letras mayúsculas dentro del flag hay que transformarlas a minúsculas.
