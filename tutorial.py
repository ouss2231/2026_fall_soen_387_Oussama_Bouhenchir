import json

from http.server import BaseHTTPRequestHandler, HTTPServer


events = [ 
        {"id": "eve_101", "title": "Jazz Ensemlbe: Fall Concert", "seatLeft": 4},
        {"id" : "ev_102", "title" : "Improv Night", "seatLeft" : 0}, 
        
]

class Handler (BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/events":  
            self._send(200, events) 
        else:
            self._send(404, {"error": "Not Found"})

    def _send(self,status,body):
        payload = json.dumps(body).encode()

        self.send_response(status) 
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()

        self.wfile.write(payload)


HTTPServer(("", 3005), Handler).serve_forever()



