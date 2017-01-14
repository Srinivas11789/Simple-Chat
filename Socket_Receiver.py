import socket
### Receiver program

# Setting the Interface to Wireless

Interface = 'wlan0'
print Interface
ETH_P_ALL=0x0003

### RAW Socket Creation

s=socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL))

### Interface binding to listen to the socket                             
                                                  
s.bind((Interface, 0))

### Socket Receive 

try:                                                                                                           
  while 1: 
   data, addr = s.recvfrom(65535)
   #print data
   #print addr
   payload = []
   for i in list(data):
     i= i.encode("hex")
     payload.append(i)
   if str(int(payload[23],16)) == '17': 
    if data[42:44] == 'Hi':
     if Interface == 'wlan0':
       print "PHYSICAL LAYER: --------------------------------> Wireless\n"
     print "ETHERNET LAYER: --------------------------------> \n"
     print "*The Data Link Component of the packet is as follow -  the FRAME is as follows\n"
     print "*The Destination MAC is %s:%s:%s:%s:%s:%s\n" % (payload[0],payload[1],payload[2],payload[3],payload[4],payload[5]) 
     print "*The Source MAC is %s:%s:%s:%s:%s:%s\n" % (payload[6],payload[7],payload[8],payload[9],payload[10],payload[11])
     if payload[12]+payload[13] == '0800':
        print "*Type is as follows:%s IPV4 \n" % (payload[12]+payload[13])
     print "NETWORK LAYER: ---------------------------------> \n"
     print "*The Source IP is %s.%s.%s.%s\n" % (str(int(payload[26],16)),str(int(payload[27],16)),str(int(payload[28],16)),str(int(payload[29],16)))
     print "*The Destination IP is %s.%s.%s.%s\n" % (str(int(payload[30],16)),str(int(payload[31],16)),str(int(payload[32],16)),str(int(payload[33],16)))
     print "*The IP Version is %s\n" % (str(int(payload[14][:1],16)))
     print "TRANSPORT LAYER: --------------------------------> \n"
     print "*The Protocol Type is %s UDP \n" % (str(int(payload[23],16)))
     print "*The Source Port and the Destination Port is %s,%s \n" % (str(int(payload[34]+payload[35],16)),str(int(payload[36]+payload[37],16)))
     print "APPLICATION LAYER: ------------------------------> \n"
     print "*The Payload is as follows --> \"%s\" \n" % (data[42:])
     break     
except:
   print "Error"
