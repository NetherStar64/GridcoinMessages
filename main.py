
import requests
import json

def nodereq(method, params):
	url = "http://localhost:15715" #Gridcoin instance
	payload = {
		"method": method,
		"params": params,
		"jsonrpc": "2.0",
		"id": 0,
	}
	return requests.post(url, json=payload, auth=requests.auth.HTTPBasicAuth('"YourRPCUsername', 'YourRPCPassword'))

print("Start")

result = nodereq("getblockchaininfo", [])
d = json.loads(result.text)
blockcount = d["result"]["blocks"]

out = open("msg.txt", "a") #Output Filename


#for i in range(blockcount, blockcount-10000, -1): # search from current block to -10000 Blocks ago
for i in range(1,1000):
	if i%200==0:
		print(f"Block {i}")
	result = nodereq("getblockbynumber", [i]).text
	d = json.loads(result)
	print(i, len(d["result"]["tx"]))
	for transaction in d["result"]["tx"]:
		result = nodereq("gettransaction", [transaction])
		d = json.loads(result.text)
		contracts = d["result"]["contracts"]
		for contract in contracts:
			if contract["type"]=="message":
#				print(contract)
				out.write(f"{str(i)}:{d['result']['txid']}\n")
				print(f"'{contract['body']}'")
				out.write(f"'{contract['body']}'")
				out.write("\n")
#		print("*", end="")
#	print("=", end="")

