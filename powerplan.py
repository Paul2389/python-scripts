#! python3
# powerplan.py - changing power plans depending on the cpu load

import psutil
import time
import subprocess
import re
from timeit import default_timer as timer
from win10toast import ToastNotifier

BALANCED = '9897998c-92de-4669-853f-b7cd3ecb2790'
HIGH_PERFORMANCE = '9935e61f-1661-40c5-ae2f-8495027d5d5d'

toast = ToastNotifier()
toast.show_toast("Power Plan", "Power Plan is now running", duration=10)

def cpu_monitor():
    percent = psutil.cpu_percent(interval=10)
    
    return percent

def high_cpu():
    start_time= timer()

    while cpu_monitor() >= 40:
        # Track the time
        stop_time= timer()
        # Check how much time has passed to continue 
        if (stop_time-start_time) <= 60:
            continue
        else:
            # If cpu is higher than the specified amount
            # Check which power plan is currently active
            command_output = subprocess.run(["powercfg","-getactivescheme"], capture_output = True).stdout.decode()
            # If Balanced is active call High Performance
            if re.search(BALANCED, command_output):
                         subprocess.call("powercfg /s" + HIGH_PERFORMANCE)
                        # Show notification
                         toast.show_toast("Power Plan", "Gaming Mode, High Performance.", duration=10)
                         break
            # If High Performance is active stop
            elif re.search(HIGH_PERFORMANCE , command_output):
                break

def low_cpu():
    start_time= timer()

    while cpu_monitor() <= 40:
        # Track the time
        stop_time= timer()
        # Check how much time has passed to continue 
        if (stop_time-start_time) <= 60:
            continue
        else:
            # If cpu is lower than the specified amount
            # Check which power plan is currently active
            command_output = subprocess.run(["powercfg","-getactivescheme"], capture_output = True).stdout.decode()
            # If High Performance is active call Balanced
            if re.search(HIGH_PERFORMANCE , command_output):
                         subprocess.call("powercfg /s" + BALANCED)
                         # Show notification
                         toast.show_toast("Power Plan", "Balanced Mode, BALANCED.", duration=10)
                         break
            # If Balanced is active stop
            elif re.search(BALANCED , command_output):
                break
#LOOP
while True:
    cpu_monitor()
    high_cpu()
    low_cpu()
    time.sleep(120)
