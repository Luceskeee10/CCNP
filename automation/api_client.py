#!/usr/bin/env python3
import json,urllib.request
with urllib.request.urlopen('http://127.0.0.1:8088/api/v1/interfaces',timeout=5) as r:
 data=json.load(r)
for item in data['interfaces']:
 print(f"{data['device']} {item['name']}: {'UP' if item['admin_up'] and item['oper_up'] else 'DOWN'}")
