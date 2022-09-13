import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(('',8000), handler) as httpd:
    print('Server run in port 8000...')
    httpd.serve_forever()

