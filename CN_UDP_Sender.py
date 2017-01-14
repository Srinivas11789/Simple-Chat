# Sender Program
from socket import *
ip = '192.168.43.223'  # Ip address of the connected machine
port = 33333                    
sock1 = socket(AF_INET, SOCK_DGRAM) # UDP Socket Intialization
msg = "Hi, This is the packet you sent !!!"
sock1.sendto(msg, (ip, port))



