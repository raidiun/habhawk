def sendTXConf(txConf):
	sdr = open("/dev/sdrIn","w+")
	sdr.write("{0},{1},{2}".format(txConf.frequency,txConf.mode,txConf.baud,txConf.encoding))
	close(sdr)

def readSDRBuffer():
	sdr = open("/dev/sdrBuff","r")
	return(sdr.read(1))
