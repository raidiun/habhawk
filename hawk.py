import json, habIntf, hawkClasses

f = open("listenerConfig.conf","r")
config = json.load(f)
close(f)

uploader = habIntf.Uploader(config["callsign"])

def getDoc(docID):
	global uploader
	return(uploader._db.get(docID))

#Check if server listener info is up to date, if not update it
if(config["listener_info_doc"] != "undefined"):
	serverDoc = getDoc(config["listener_info_doc"])
	
	fail = false
	for key in config["listener_info"]:
		if(config["listener_info"][key] != serverDoc[key]):
			fail = true
	if(fail):
		config["listener_info"]["_id"] = config["listener_info_doc"]
		config["listener_info_doc"] = uploader.listener_information(config["listener_info"])
		config["listener_info"].pop("_id",None)
	else:
		uploader._latest["listener_information"] = config["listener_info_doc"]
else:
	config["listener_info_doc"] = uploader.listener_information(config["listener_info"])

#Check if server listener telemetry is up to date, if not update it
if(config["listener_telem_doc"] != "undefined"):
	serverDoc = getDoc(config["listener_telem_doc"])
	
	fail = false
	for key in config["listener_telem"]:
		if(config["listener_telem"][key] != serverDoc[key]):
			fail = true
	if(fail):
		config["listener_telem"]["_id"] = config["listener_telem_doc"]
		config["listener_telem_doc"] = uploader.listener_telemetry(config["listener_telem"])
		config["listener_telem"].pop("_id",None)
	else:
		uploader._latest["listener_telemetry"] = config["listener_telem_doc"]
else:
	config["listener_telem_doc"] = uploader.listener_telemetry(config["listener_telem"])

#Write new doc id's (if any) back to configuration file
f = open("listenerConfig.conf","w")
json.dump(config,f)
close(f)

#Get active flights
activeFlights = []

for flightInfo in uploader.flights():
	activeFlights.append(hawkClasses.Flight(flightInfo))

for flight in activeFlight:
	for payload in flight.payloads:
		for txConf in payload.txConfs:
			#Tell SDR to listen for tx's with conf
			hawkSDRIntf.sendTXConf(txConf)