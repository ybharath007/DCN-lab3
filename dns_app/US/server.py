# Bharath Yeddula
from flask import Flask, request
import socket
import json
import requests

app = Flask(__name__)

@app.route('/fibonacci')
def fibonacci():
	hostname = request.args.get("hostname")
	fs_port = request.args.get("fs_port")
	sequence_number = request.args.get("number")
	as_ip = request.args.get("as_ip")
	as_port = request.args.get("as_port")
	if hostname is None or fs_port is None or sequence_number is None or as_ip is None or as_port is None:
		return "Input Parameter Missing", 400

	# get the ip of FS using AS
	dnsQuery = {}
	dnsQuery["NAME"] = hostname
	dnsQuery["TYPE"] = "A"

	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server.sendto(json.dumps(dnsQuery).encode(), (as_ip, int(as_port)))
	resp, addr = server.recvfrom(2048)
	if resp.decode() == "500":
		return "DNS resolution failed", 500
	dns = json.loads(json.loads(resp.decode()))

	# call Fibonacci server
	fib = requests.get("http://"+dns['VALUE']+":"+fs_port+"/fibonacci?"+"number="+sequence_number)
	return fib.text, fib.status_code

app.run(host='0.0.0.0', port=8080)