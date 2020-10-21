from functools import reduce

textoOriginal = open('texto_cifrado.txt', 'r')
textoDescifrado = open('textoDescifrado.txt', 'w')


diccionario = [("z", "F"),
                ("s", "L"),
                ("q", "A"),
                ("*", "G"),
                ("k", "R"),
                ("t", "E"),
                ("n", "Y"),
                ("h", "P"),
                ("l", "S"),
                ("r", "D"),
                ("%", "O"),
                ("x", "U"),
                ("&", "I"),
                ("$", "N"),
                ("e", "C"),
                ("y", "T"),
                ("w", "B"),
                ("p", "J"),
                ("c", "V"),
                ("b", "X"),
                ("j", "Q"),
                ("m", "Z")]

dato = textoOriginal.read()

textoOriginal.close()

# La funcion reduce(fun, seq) suele aplicarse a una funcion particular pasada en su
#argumento a todos los elementos de la lista mencionados en la secuencia transmitida

salida = reduce(lambda a, kv: a.replace(*kv), diccionario, dato)

textoDescifrado.write(salida)
textoDescifrado. close()
