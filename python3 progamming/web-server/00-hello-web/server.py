# -*- coding:utf-8 -*-

import django

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    page ="<html><body><p>Hello,web!</p></body></html>"
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(self.page)))
        self.end_headers()
        self.wfile.write(self.page)

if __name__ == "__main__":
    serverAddress = (' ', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.server_forever()
