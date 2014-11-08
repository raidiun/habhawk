cache = {}

def addDoc(doc):
	cache[doc["_id"]] = doc

def addViewResult(viewRes):
	for result in viewRes:
		if(result["key"][3]==1):#Linked doc is a payload config
			cache[result["value"]["_id"]] = result["doc"]
		else:
			cache[result["id"]] = result["doc"]

def flush():
	cache = []