# Bharath Yeddula
import socket
import json
import os.path

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('', 53533))

while True:
	msg, clientAddr = server.recvfrom(2048)
	msgJson = json.loads(msg.decode())

	# dns register request
	if len(msgJson) == 4:
		dnsJson = {}
		with open("dns.txt", 'r') as dns:
			storedDns = dns.read()
			if storedDns != "":
				dnsJson = json.loads(storedDns)
		with open('dns.txt', 'w') as dns:
			dnsJson[msgJson["NAME"]] = json.dumps(msgJson)
			dns.write(json.dumps(dnsJson))
		server.sendto(str(201).encode(), clientAddr)
	elif len(msgJson) == 2:
		with open("dns.txt", "r") as dns:
			storedDns = dns.read()
			if storedDns == "":
				server.sendto(str(500).encode(), clientAddr) 
			else:
				storedDns = json.loads(storedDns)
				if msgJson["NAME"] not in storedDns:
					server.sendto(str(500).encode(), clientAddr)
				else:
					server.sendto(json.dumps(dnsJson[msgJson["NAME"]]).encode(), clientAddr)