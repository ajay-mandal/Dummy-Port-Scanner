#!/bin/python3
import sys
import socket
from datetime import datetime 

#Define our target

if len(sys.argv) == 2:
	#Translate hostname to IPV4
	target = socket.gethostbyname(sys.argv[1])

	#Add pretty banner
	print("-" * 50)
	print("Scanning target: "+target)
	print("Time started: "+str(datetime.now()))
	print("-" * 50)

	try:

		for port in range(20,100):
			#For TCP Connection Only
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target, port)) 
			#returns an error indicator - if port is open it throws a 0, otherwise 1
			if result == 0:
				print(f"Port {port} is open")
			s.close()


	except KeyboardInterrupt:
		print("\nExisting program.")
		sys.exit()

	except socket.gaierror:
		print("Hostname could not be ressolved.")
		sys.exit()

	except socket.error:
		print("Could not connect to server.")
		sys.exit()




else:
	print("\nInvalid amount of arguments.")
	print("Syntax: python3 port-scanner.py <ip>")


