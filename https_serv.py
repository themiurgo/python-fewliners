#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A simple HTTPS server"""

import http.server
import ssl

SERVER_ADDRESS = ""
SERVER_PORT = 4443
CERT_FILE = "etc/nginx/conf/db.themiurgo.net.cert"
KEY_FILE = "/etc/nginx/conf/db.themiurgo.net.key"

httpd = http.server.HTTPServer((SERVER_ADDRESS, PORT),
        http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile=CERT_FILE,
        keyfile=KEY_FILE, server_side=True)
httpd.serve_forever()
