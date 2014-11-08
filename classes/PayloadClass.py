import habhawk

class Payload:
	def __init__(self,id):
		global db
		
		self.docID = id
		self.doc = habhawk.dbc.getDoc(self.docID)
		
		self.name = self.doc["name"]
		
		self.txParams = []
		for config in self.doc["transmissions"]:
			self.txParams.append(habhawk.classes.TXParams(config))
		
		self.sentenceFormats = []
		for config in self.doc["sentences"]:
				self.sentenceFormats.append(habhawk.classes.SentenceFormat(config))
	
	def __str__(self):
		return(str(self.doc))