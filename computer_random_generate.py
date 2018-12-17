# Import the Qiskit SDK
import random
for x in range(5096):
	randomnv=random.randint(0,1)
	newstr = "".join((str(randomnv), '\n'))
	f = open('computer_random_list', 'a')
	f.write(newstr)
	f.close()
