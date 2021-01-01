#!/usr/bin/env python

import time, datetime, threading, socket as skt, json, subprocess

print("B.M.B. TALKKET\n\n")

#creates a socket
def createSocket():
   #Protocol = UDB, addressFamily = ipv4
    protocol = skt.SOCK_DGRAM
    addressFamily = skt.AF_INET

    #socket creation
    socket = skt.socket(addressFamily, protocol)
    return socket

#binds socket to ip and port
def serverSocket():
    #creates socket
    socket = createSocket()
    
    #Bind information
    serverIp = "192.168.99.1"
    serverPrt = 2121

    #Binding port and ip
    socket.bind((serverIp, serverPrt))

    return socket

#logs request
def requestProcessor(request):
    #displays current thread
    #print("\nCurrent thread name: {}".format(threading.currentThread().getName()))
    #print("Current thread id: {}".format(threading.get_ident()))

    #gathering log data
    logEntry = {
        "sender": request[1][0],
        "message": request[0].decode(), 
        "datetime": datetime.datetime.now().strftime("%B %d, %Y at %H:%M:%S"),
    }
    
    #registering log to file
    #print("Logging user {}\'s request\n\n".format(request[1][0]))
 
    log = open("messages.txt", "a")
    log.write("{}\n".format(json.dumps(logEntry)))
    log.close()
    
    #print("Finished logging user {}\'s request".format(request[1][0]))
    
    #displays recent log entry
    #print("{}\n\n".format(json.dumps(logEntry)))
    
    #printing text
    print("{}: {}\n".format(logEntry["sender"], logEntry["message"]))

def client(socket):
    #server details
    recipients = ["192.168.99.103","192.168.99.108"]
    serverPort = 2121

    print("Type message and press enter to sent at anytime\n\n")

    #request
    request = ""

    while True:
        request = input()

        if(request == "close"):
            break;
        elif(request.strip() != ""):
            size = 0
            #send request
            for recipient in recipients:
                #send request
                size = socket.sendto(request.encode(), (recipient, serverPort))
                
            print("{} byte(s) of data sent.\n\n".format(size * 3))

#receiving and processing data
def listener(socket):
    while True:
        #receiving data
        request = socket.recvfrom(2048)
        #print("Data from client: {}".format(data))    
    
        #processes message
        requestProcessor(request)
    
# listens for messages and prints them
listenerThread = threading.Thread(target=lambda : listener(serverSocket()))
clientThread = threading.Thread(target=lambda : client(createSocket()))
listenerThread.start()
clientThread.start()
