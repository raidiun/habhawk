class TXParams:
	def __init__(self,sentenceJSON):
		self.raw = sentenceJSON
	
	def __getitem__(self,key):
		return(self.raw[key])
