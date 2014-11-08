import couchdbkit, habhawk

class dbConnection:
	def __init__(self,url,dbName):
		self.db = couchdbkit.Server(url)[dbName]

	def getDoc(self,docID):
		if docID in habhawk.dbConnect.cache:
			return(habhawk.dbConnect.cache[docID])
		else:
			doc = self.db.get(docID)
			habhawk.dbConnect.cachier.addDoc(doc)
			return(doc)

	def getView(self,design,view,**kwargs):
		viewStr = design + "/" + view
		vRes = self.db.view(viewStr,**kwargs)
		habhawk.dbConnect.cachier.addViewResult(vRes)
		return(vRes)