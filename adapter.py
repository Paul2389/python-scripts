#! Python3

import subprocess
import re


ADAPTERS = subprocess.run(['netsh', 'interface', 'show', 'interface'], capture_output=True).stdout.decode()
ENABLED_STATE = 'Enabled        Connected      Dedicated        Ethernet'
DISABLED_STATE = 'Disabled       Disconnected   Dedicated        Ethernet'


if re.search(ENABLED_STATE, ADAPTERS):
    print('Adapter is Enabled, Disabling...')
    subprocess.run(['netsh', 'interface', 'set', 'interface', "Ethernet", 'disable'])
elif re.search(DISABLED_STATE, ADAPTERS):
    print('Adapter is Disabled, Enabling...')
    subprocess.run(['netsh', 'interface', 'set', 'interface', "Ethernet", 'enable'])

    
#subprocess.run(['netsh', 'interface', 'set', 'interface', "Ethernet", 'enable'])