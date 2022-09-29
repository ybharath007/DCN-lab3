# Bharath Yeddula
from flask import Flask, request
import requests
import json
import socket

app = Flask(__name__)

@app.route('/register', methods=["PUT"])
def register():
	input_data = request.json

	dns_record = {}
	dns_record["NAME"] = input_data["hostname"]
	dns_record["VALUE"] = input_data["ip"]
	dns_record["TYPE"] = "A"
	dns_record["TTL"] = 10

	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server.sendto(json.dumps(dns_record).encode(),(input_data["as_ip"], int(input_data["as_port"])))
	resp, clientAddr = server.recvfrom(2048)

	if resp.decode() == "201":
		return "DNS registration success", 201
	else:
		return "DNS registration falied", 500


def fib(num):
	if num == 0:
		return 0
	elif num == 1 or num == 2:
		return 1
	else:
		return fib(num-1) + fib(num-2)

@app.route('/fibonacci')
def fibonacci():
	sequence_number = request.args.get("number")
	if not sequence_number.isnumeric():
		return "Not a number", 400
	else:
		return str(fib(int(sequence_number))), 200

app.run(host='0.0.0.0', port=9090)