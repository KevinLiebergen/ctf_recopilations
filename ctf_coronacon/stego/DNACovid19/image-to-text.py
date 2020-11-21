import pytesseract as tess
from PIL import Image

img = Image.open('seqfragment.jpg')

text = tess.image_to_string(img)

print(text.rstrip())

a = []
result, gs, aes, cs, ts = 0, 0, 0, 0, 0

for i in text:
	if i in ['G', 'A', 'C', 'T']:
		if i == 'G':
			gs += 1
		elif i == 'A':
			aes += 1
		elif i == 'C':
			cs += 1
		else:
			ts += 1
        
		a.append(i)

	else:
		print(len(a))
		result = result + len(a)
		a = []


print(result)

print("Gs: {}".format(gs))
print("As: {}".format(aes))
print("Cs: {}".format(cs))
print("Ts: {}".format(ts))


