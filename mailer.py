import os
import sys
import time
from os import system
from time import sleep

## ORIGINAL SCRIPT BY THELINUXCHOICE

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
	request = requests.get("https://www.google.com/search?q=tahmid+rayat", timeout=3)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("[!] No internet connection [!]")
    sys.exit()

import requests

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'

def hprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8.0 / 100)

logo = """
\033[1;32m  ______    _         \033[1;33m  __  __       _ _           
\033[1;32m |  ____|  | |        \033[1;33m |  \/  |     (_) |          
\033[1;32m | |__ __ _| | _____  \033[1;33m | \  / | __ _ _| | ___ _ __ 
\033[1;32m |  __/ _  | |/ / _ \ \033[1;33m | |\/| |/ _  | | |/ _ \  __|
\033[1;32m | | | (_| |   <  __/ \033[1;33m | |  | | (_| | | |  __/ |   
\033[1;32m |_|  \__,_|_|\_\___| \033[1;33m |_|  |_|\__,_|_|_|\___|_|   

\033[1;36m [\033[1;37m+\033[1;36m]\033[1;32m CREATED BY HTR-TECH \033[1;31m(\033[1;33mTAHMID RAYAT\033[1;31m)
"""

system("clear")
print (logo)
print ('')
hprint(G + ' Launching Fake Mailer ...')
sleep(2)
print ('')
to = raw_input(G + " Send Mail To" + C + " : " + Y)
print ('')
subject = raw_input(G + " Input Mail Subject" + C + " : " + Y)
print ("")
msg = raw_input(G + " Input Mail Content" + C + " : " + Y)
print ("")
usagnt = 'Mozilla/5.0 (Linux; Android 6.0.1; HTC6545LVW Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/283.0.0.16.120;]'
sess = requests.Session()
rth = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': usagnt,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': msg
})

if '200' in rth.text:
    hprint(G + " Sending Email >>>>>>>>>>")
else:
    hprint(G + " Sending Email >>>>>>>>>>")
    print ('')
    time.sleep(2)
    hprint(C + " Mail Successfully Sent !!")
    print ('')
    sleep(3)
    hprint(W + " Process can take some time !!")
    print ('')
    print (Y + " Visit www.github.com/htr-tech for More Tools" + W)
    print ('')


