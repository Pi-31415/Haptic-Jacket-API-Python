'''
Author : Pi 
Date: Mar 27, 2021
Description:  This is the Haptic Jacket controller middleware API in Python
Dependencies : socket, time
'''

import socket
from time import sleep

# Scan the IPs into the dictionary, it's more convenient. Keys as strings
# Read from the text file/ or scan from network.

# Instead of activate, put control motor function which allows different 
# parameters

# separate for GUI

# Value in dictionary should be the IP number

# Allow hard code the message

# Have low level control

# Build a very simple demo application
# for single, multiple or moving
# as comprehensive and control as possible

# Put on one stable environment

# George will also have feedback

# UDP Configuration
UDP_IP = "127.0.0.1"
UDP_PORT = 33333

def send_UDP_message(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Internet  # UDP
    sock.sendto(message, (UDP_IP, UDP_PORT))

def activate_motor(motor_id):
    COMMAND = bytes(str(motor_id),'utf-8')
    send_UDP_message(COMMAND)
    print("Motor %s Activated" % motor_id)

def stop_all_motors():
    COMMAND = bytes('0','utf-8')
    send_UDP_message(COMMAND)
    print("All Motors Stopped")

def continuous_motion(delay_time,maximum_motor_id):
    x = 1
    while True:
        stop_all_motors()
        activate_motor(x)
        #Delay the time between motors in seconds
        sleep(delay_time)
        x += 1
        if(x>=maximum_motor_id):
            x=1

def delay(delay_time):
    sleep(delay_time)