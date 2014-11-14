# Provides classes to abstract the CouchDB docs/dictionaries into objects


class dictWrapper:
	'''
		dictWrapper (Virtual):
		Provides direct access to the dictionary used to assemble the abstracted object.
	'''
	def __getitem__(self,key):
		'''Provides object[key] syntax method'''
		return(self.dict[key])
	
	def keys(self):
		'''Returns a list of keys in self.dict (Py2)'''
		return(self.dict.keys())


class TXConf(dictWrapper):
	def __init__(self,txConfig):
		self.dict = txConfig
		
		#Everything appears to have these
		for attribute in ["frequency","modulation","mode","description"]:
			setattr(self,attribute,txConfig[attribute])
		
		#Appear with modulation=RTTY
		if(self.modulation == "RTTY"):
			for attribute in ["baud","encoding","shift","stop"]:
				try:
					setattr(self,attribute,txConfig[attribute])
				except KeyError:
					pass
		
		#Appears with modulation=DominoEX
		if(self.modulation == "RTTY"):
			for attribute in ["speed"]:
				try:
					setattr(self,attribute,txConfig[attribute])
				except KeyError:
					pass

	def __str__(self):
		return(str(self.dict))


class SentenceConf(dictWrapper):
	def __init__(self,senConf):
		self.dict = senConf
		
		if(senConf["protocol"]=="UKHAS"):
			self.format = "$${0},".format(senConf["callsign"])
			for field in senConf["fields"]:
				self.format+=("{0}({1}),".format(field["name"],field["sensor"]))
			self.format = self.format[:-1]
			self.format+=("*({})".format(senConf["checksum"]))


class Payload(dictWrapper):
	def __init__(self,payloadConfig):
		self.dict = payloadConfig
		self.name = payloadConfig["name"]
		self.txConfs = []
		for txConfig in payloadConfig["transmissions"]:
			self.txConfs.append(TXConf(txConfig))

		self.sentenceConfs = []
		for senConf in payloadConfig["sentences"]:
			self.sentenceConfs.append(SentenceConf(senConf))


class Flight(dictWrapper):
	def __init__(self,flightDict):
		self.dict = flightDict
		self.name = flightDict["name"]
		self.payloads = []
		for payloadConfig in flightDict["_payload_docs"]:
			self.payloads.append(Payload(payloadConfig))
