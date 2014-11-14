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
			self.__setattr__(attribute,txConfig[attribute])
		#self.frequency = txConfig["frequency"]
		#self.modulation = txConfig["modulation"]
		#self.mode = txConfig["mode"]
		#self.description = txConfig["description"]
		
		#Appear with modulation=RTTY
		if(self.modulation == "RTTY"):
			for attribute in ["baud","encoding","shift","stop"]:
				self.__setattr__(attribute,txConfig[attribute])
		#self.baud = txConfig["baud"]
		#self.encoding = txConfig["encoding"]
		#self.shift = txConfig["shift"]
		#self.stop = txConfig["stop"]
		
		#Appears with modulation=DominoEX
		if(self.modulation == "RTTY"):
			for attribute in ["speed"]:
				self.__setattr__(attribute,txConfig[attribute])
		#self.speed = txConfig["speed"]


class Payload(dictWrapper):
	def __init__(self,payloadConfig):
		self.dict = payloadConfig
		self.name = payloadConfig["name"]
		self.txConfs = []
		for txConfig in payloadConfig["transmissions"]:
			self.txConfs.append(TXConf(txConfig))


class Flight(dictWrapper):
	def __init__(self,flightDict):
		self.dict = flightDict
		self.name = flightDict["name"]
		self.payloads = []
		for payloadConfig in flightDict["_payload_docs"]:
			self.payloads.append(Payload(payloadConfig))

#Sample transmission configs
'''>>> flgs[0]["_payload_docs"][0]["transmissions"]
	[{u'modulation': u'DominoEX', u'frequency': 434075000, u'speed': 16, u'mode': u'USB', u'description': u'primary RTTY telemetry stream'}]
	>>> flgs[1]["_payload_docs"][0]["transmissions"]
	[{u'baud': 300, u'parity': u'none', u'description': u'SP5NVX_7N2_800_200', u'encoding': u'ASCII-7', u'modulation': u'RTTY', u'shift': 800, u'stop': 2, u'frequency': 27900000, u'mode': u'USB'}]
	>>> flgs[2]["_payload_docs"][0]["transmissions"]
	[{u'baud': 50, u'parity': u'none', u'description': u'PicoHorus payload #1', u'encoding': u'ASCII-7', u'modulation': u'RTTY', u'shift': 450, u'stop': 2, u'frequency': 434650000, u'mode': u'USB'}]
	>>> flgs[3]["_payload_docs"][0]["transmissions"]
	[{u'modulation': u'DominoEX', u'frequency': 434500000, u'speed': 16, u'mode': u'USB', u'description': u'Primary'}]
'''