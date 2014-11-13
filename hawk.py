import json, habIntf, hawkClasses

config = json.load(open("listenerConfig.conf","rw"))
uploader = habIntf.Uploader(config["callsign"])

if(config["listener_info_doc"] != "undefined"):
	#Check if server edition matches current
	#If not update with new info and set info doc
else:
	#Set info doc

if(config["listener_meta_doc"] != "undefined"):
	#Check if server edition matches current
	#If not update with new meta and set meta doc
else:
	#Set meta doc
