class Flight:
	def __init__(self,flightDict):
		self.dict = flightDict
		self.name = flightDict["name"]
		self.payloads = []
		for payloadConfig in flightDict["_payload_docs"]:
			self.payloads.append(Payload(payloadConfig)) 
