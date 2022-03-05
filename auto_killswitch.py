#! python3
# auto_killswitch.py - enable auto vpn, killswitch on startup

import subprocess
import time
import re

PASSWORD =''
COMMAND='sudo ufw disable'

CONNECTION_SUCCESS = False
CONNECTION_PATTERN = 'Connection successfully activated'

def killswitch_off():
    subprocess.run('echo {} | sudo -S {}'.format(PASSWORD, COMMAND ), shell=True)
    print('Killswitch is OFF')

def vpn():
    global CONNECTION_SUCCESS
    vpn_connection = subprocess.run(['nmcli', 'con', 'up', 'id', 'Surfshark NL'], capture_output= True).stdout.decode()

    if re.search(CONNECTION_PATTERN, vpn_connection):
        CONNECTION_SUCCESS = True
        return CONNECTION_SUCCESS
    else:
        CONNECTION_SUCCESS = False
        return CONNECTION_SUCCESS

def killswitch_on():
    subprocess.run(['sudo', 'ufw', 'enable'])
    print('killswitch is ON')


# Wait booting sequence
time.sleep(10)
killswitch_off()

while CONNECTION_SUCCESS is False:
    time.sleep(5)
    print('Connecting to VPN...')
    vpn()
    if CONNECTION_SUCCESS is True:
        print('Connection Successful!')
        break

killswitch_on()