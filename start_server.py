#!/usr/bin/env python3
import http.server
import socketserver
import os

PORT = 8080
os.chdir(r'C:\Users\22877\Documents\GitHub\Publicwebpage')

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()
