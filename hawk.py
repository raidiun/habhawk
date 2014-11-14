import json, habIntf, hawkClasses, hawkSDRIntf

f = open("listenerConfig.conf","r")
config = json.load(f)
f.close()

uploader = habIntf.Uploader(config["callsign"],config["habServer"],config["habDB"])

def getDoc(docID):
	global uploader
	return(uploader._db.get(docID))

#Check if server listener info is up to date, if not update it
if(config["listener_info_doc"] != "undefined"):
	serverDoc = getDoc(config["listener_info_doc"])
	
	fail = False
	for key in config["listener_info"]:
		if(config["listener_info"][key] != serverDoc["data"][key]):
			fail = True
	if(fail):
		print("Updating listener information to match local...")
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
	
	fail = False
	for key in config["listener_telem"]:
		if(config["listener_telem"][key] != serverDoc["data"][key]):
			fail = True
	if(fail):
		print("Updating listener telemetry to match local...")
		config["listener_telem"]["_id"] = config["listener_telem_doc"]
		config["listener_telem_doc"] = uploader.listener_telemetry(config["listener_telem"])
		config["listener_telem"].pop("_id",None)
	else:
		uploader._latest["listener_telemetry"] = config["listener_telem_doc"]
else:
	config["listener_telem_doc"] = uploader.listener_telemetry(config["listener_telem"])

#Write new doc id's (if any) back to configuration file
f = open("listenerConfig.conf","w")
json.dump(config,f,indent=4,separators=(',', ': '),sort_keys=True)# Make the .conf pretty
f.close()

#Get active flights
activeFlights = []

# !!Download from actual, testing DB not up to date!!
for flightInfo in habIntf.Uploader("UBRCVR").flights():
	activeFlights.append(hawkClasses.Flight(flightInfo))

for flight in activeFlights:
	for payload in flight.payloads:
		for txConf in payload.txConfs:
			#Tell SDR to listen for tx's with conf
			hawkSDRIntf.sendTXConf(txConf)

# Make the above run in a loop. How long do we make the loop length?
#
# Need to receive data from the SDR and use uploader.payload_telemetry(sentence)
#
# This data from the SDR should also include a "received frequency"
# which is included in the upload metadata as a rig_info JSO as per fl-digi
# conventions