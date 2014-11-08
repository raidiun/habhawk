import couchdbkit

class dbConnection:
	def __init__(self,url,dbName):
		self.db = couchdbkit.Server(url)[dbName]

	def getDoc(self,docID):
		return(self.db.get(docID))

	def getView(self,design,view,**kwargs):
		viewStr = design + "/" + view
		return(self.db.view(viewStr,**kwargs))