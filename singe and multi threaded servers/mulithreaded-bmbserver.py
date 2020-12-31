#!/usr/bin/env python

import time, datetime, threading, socket as skt, json, subprocess

#creates and returns a socket
def createSocket():
    #Protocol = UDB, addressFamily = ipv4
    protocol = skt.SOCK_DGRAM
    addressFamily = skt.AF_INET

    #socket creation
    socket = skt.socket(addressFamily, protocol)

    #Bind information
    serverIp = "192.168.99.103"
    serverPrt = 2121

    #Binding port and ip
    socket.bind((serverIp, serverPrt))

    return socket

#logs request
def requestProcessor(request):
    #displays current thread
    print("\nCurrent thread name: {}".format(threading.currentThread().getName()))
    print("Current thread id: {}".format(threading.get_ident()))

    #executing request
    print("\nProcessing thread {}\'s request....".format(threading.currentThread().getName()))
    output = subprocess.getstatusoutput(request[0].decode())
    print("\nFinished processing thread {}\'s request....".format(threading.currentThread().getName()))
    
    
    #gathering log data
    logEntry = {
        "sender": request[1][0],
        "request": request[0].decode(), 
        "datetime": datetime.datetime.now().strftime("%B %d, %Y at %H:%M:%S"),
        "threadId": threading.get_ident(),
        "output": output
    }
    
    #registering log to file
    
    print("Logging user {}\'s request\n\n".format(request[1][0]))
 
    log = open("log.txt", "a")
    log.write("{}\n".format(json.dumps(logEntry)))
    log.close()
    
    print("Finished logging user {}\'s request".format(request[1][0]))
    
    #displays recent log entry
    print("{}\n\n".format(json.dumps(logEntry)))

#create socket
socket = createSocket()

#receiving and processing data
while True:
    #receiving data
    request = socket.recvfrom(2048)
    #print("Data from client: {}".format(data))    
    
    #creates a thread on the fly for the processing of each request
    threading.Thread(name=request[1][0], target=lambda : requestProcessor(request)).start()
    

