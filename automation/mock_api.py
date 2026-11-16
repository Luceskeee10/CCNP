#!/usr/bin/env python3
"""Offline REST lab: no auth by design; bind loopback only."""
from http.server import BaseHTTPRequestHandler,HTTPServer
import json
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path!='/api/v1/interfaces':self.send_error(404);return
  payload=json.dumps({'device':'LAB-R1','interfaces':[{'name':'GigabitEthernet0/0','admin_up':True,'oper_up':True},{'name':'GigabitEthernet0/1','admin_up':True,'oper_up':False}]}).encode()
  self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(payload)));self.end_headers();self.wfile.write(payload)
HTTPServer(('127.0.0.1',8088),Handler).serve_forever()
