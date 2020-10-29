1. Se extrae el zip
2. Con steghide se extrae, nos pide contraseña, insertamos como contenido el contenido del fichero oculto al descomprimir .secreto.txt 
3. Nos saca un fichero denominado notsecret.txt, con una imagen codificada en base64
4. La abrimos con un convertidor y nos renderiza en un código qr
5. escaneamos el codigo qr y nos aparece la flag
