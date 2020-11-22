from nsetools import Nse
from pprint import pprint

class Machine():
	def __init__(self):
		self.nse = Nse()

	def getQuote(self, stockName):
		"""
		Fetches Quote for Given Stock
		"""
		return self.nse.get_quote(stockName)

	def showQuote(self, quote):
		"""
		Pretty Print a received Quote
		"""
		pprint(quote)

	def getIndexList(self):
		"""
		Fetches the available Index list
		"""
		return self.nse.get_index_list()

	def showIndexList(self):
		"""
		Pretty Print available Index List
		"""
		pprint(self.getIndexList())

	def getIndexQuote(self, indexName):
		"""
		Fetch Index Quote
		"""
		return self.nse.get_index_quote(indexName)

	def showIndexQuote(self, indexName):
		"""
		Pretty Print Available Index Quote
		"""
		pprint(self.getIndexQuote(indexName))

def main():
	machine = Machine()
	# quote = machine.getQuote('INFY')
	# machine.showQuote(quote)
	machine.showIndexQuote('NIFTY BANK')

if __name__ == '__main__':
	main()