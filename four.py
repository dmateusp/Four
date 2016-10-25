from num2words import num2words
import matplotlib.pyplot as plt

def letter_pyramid(number):
	if(number == 4):
		return [4]
	else:
		length_spelled_number = len(num2words(number))
		return [length_spelled_number] + letter_pyramid(length_spelled_number)


for n in range(0, 100, 1):
	l = [n] + letter_pyramid(n)
	plt.plot(l)

plt.xlabel("n iteration")
plt.ylabel("numerical value")

plt.show()