# Provides interfaces to the SDR
# At the moment just hollow functions pending discussions with SDR team

def sendTXConf(txConf):
	'''Sends the tx/conf to the SDR to allow the SDR to be configured to listen to this payload'''
	#sdr = open("/dev/sdrIn","w+")
	#sdr.write("{0},{1},{2}".format(txConf.frequency,txConf.mode,txConf.baud,txConf.encoding))
	#close(sdr)
	print(txConf)
	#SDR & DP people need to decide on a format for these messages...

def readSDRBuffer():
	'''Reads data from the SDR buffer. (Probably for use in habIntf.Extractor.push())'''
	sdr = open("/dev/sdrBuff","r")
	return(sdr.read(1))
