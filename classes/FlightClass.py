import strict_rfc3339, habhawk

class Flight:
	def __init__(self,id):
		
		self.docID = id
		self.doc = habhawk.dbc.getDoc(self.docID)
		
		self.start = strict_rfc3339.rfc3339_to_timestamp(self.doc["start"])
		self.end = strict_rfc3339.rfc3339_to_timestamp(self.doc["end"])
		
		self.name = self.doc["name"]
		
		self.payloads = []
		for payloadID in self.doc["payloads"]:
			self.payloads.append(habhawk.classes.Payload(payloadID))

	def __str__(self):
		return("id:" + str(self.docID)[0:8] + "... start:" + str(self.start) + " end:" + str(self.end) + " isActive:" + str(self.isActive()))
	
	def isActive(self):
		now = int(time.time())
		return(self.start<now and self.end>now)