#! python3
# auto_killswitch.py - enable auto vpn, killswitch on startup

import subprocess
import time

PASSWORD =''
COMMAND='sudo ufw disable'


def killswitch_off():
    subprocess.run('echo {} | sudo -S {}'.format(PASSWORD, COMMAND), shell=True)

def vpn():
    subprocess.run(['nmcli', 'con', 'up', 'id', 'Surfshark NL'])
    time.sleep(5)

def killswitch_on():
    subprocess.run(['sudo', 'ufw', 'enable'])


time.sleep(10)
killswitch_off()
vpn()
killswitch_on()