from http.server import BaseHTTPRequestHandler, HTTPServer

class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        if self.path == "/api":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello from Backend Server!")

        elif self.path == "/api/users":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"users": ["John", "Alice", "Bob"]}')

        elif self.path == "/api/orders":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"orders": [101, 102, 103]}')

        elif self.path == "/api/products":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"products": ["Phone", "Laptop", "Tablet"]}')

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

server = HTTPServer(("0.0.0.0", 5000), handler)
print("Server running on port 5000...")
server.serve_forever()
