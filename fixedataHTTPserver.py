#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer

INTERFACE = '127.0.0.1' #loopback address
PORT_NUMBER = 8080      #http port number

class Error(Exception):
	pass

class DataRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self): #Handler for HTTP GET requests
		try:
			param = self.path.lstrip("/") #exmpl://8080/56 then path=/56,param=56
			size = int(param) #Raising exception if it is not int.

        # If the provided path is not a number, return a HTTP 400 error
   #limiting the size of path to avoid server overload and raising manual exception
			if (not param.isnumeric() or size >500):
				raise Error
        # Generate the date to return
			data = '.' * size

        # Write back HTTP response
			self.send_response_only(200) 
	#it was including server and date headers so used _omly
			self.send_header('Content-type','text/plain')
			self.send_header('Content-Length', size)
			self.end_headers()
			self.wfile.write(data.encode())
			return

		except (ValueError , Error): #Handling both value and manual exception
			self.send_response(400) #client error bad request
			self.end_headers()
			return

		

try:
    # Start HTTP server on configured interface / port
    server = HTTPServer((INTERFACE, PORT_NUMBER), DataRequestHandler)
    print('HTTP server started on %s:%d' % (INTERFACE, PORT_NUMBER))
    server.serve_forever()

# Catch Ctrl-C to gracefully shut down the server
except KeyboardInterrupt:
    print('Shutting down the web server')
    server.socket.close()
