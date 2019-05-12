from currency import Currency

def main():

	currencyObj = Currency()

	print("Description: \nThis is a currency changer\nCurrency types which it's \
working:" + currencyObj.getContent() + "\n\nFirst currency type:")
	firstRate = input()

	print("Second currency type:")
	secondRate = input()

	print("The value in the first currency type:")
	value = input()

	result = currencyObj.getData(str(firstRate).upper(), str(secondRate).upper() , value)
	
	print(str(result) + " " + str(secondRate).upper())
	pass


if __name__ == '__main__':
	main()