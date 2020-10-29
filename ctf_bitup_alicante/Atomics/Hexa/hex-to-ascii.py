frase = "62 69 74 75 70 32 30 7b 6c 30 5f 73 34 62 33 6e 7d"

for letra in frase.split():
	print(bytes.fromhex(letra).decode('utf-8'), end='')

print()
