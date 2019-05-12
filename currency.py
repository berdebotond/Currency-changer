import requests
import json
import sys

class Currency():


	def __init__(self):
		
		self.url = "https://api.exchangeratesapi.io/latest"
		self.name = "Exchange Rate"
		self.__setup()

	def __setup(self):

		try:

			response = requests.get(self.url)
			self.data = response.json()
			self.content = response.content
			pass

		except Exception as e:

			print(e)
			print("__setup")

	def getData(self, startRate, finishRate, value):

		try:

			if(startRate == "EUR" and finishRate == "EUR"):
				
				return float(value);

			elif(startRate == "EUR"):

				secondValue = self.data['rates'][finishRate]
				return (float(value) * float(secondValue))

			elif( finishRate == "EUR" ):

				firstValue = self.data['rates'][startRate]
				return (float(value) / firstValue)

			else:	
				firstValue = self.data['rates'][startRate]
				secondValue = self.data['rates'][finishRate]
				return (float(value) / firstValue) * secondValue

		except Exception as e:

			print(e)
			print("getData")

		pass
		
	def getContent(self):

		string = ""
		dataTypes = json.loads(self.content)
		for x in dataTypes['rates']:
			string += ", " + str(x)
			pass
		return (string + "." )

		pass