# Provides interfaces to the SDR

def sendTXConf(txConf):
	'''Sends the tx/conf to the SDR to allow the SDR to be configured to listen to this payload'''
	sdr = open("/dev/sdrIn","w+")
	sdr.write("{0},{1},{2}".format(txConf.frequency,txConf.mode,txConf.baud,txConf.encoding))
	close(sdr)

def readSDRBuffer():
	'''Reads data from the SDR buffer. (Probably for use in habIntf.Extractor.push())'''
	sdr = open("/dev/sdrBuff","r")
	return(sdr.read(1))
