#!/usr/bin/python3

#Client Program
import socket as skt

#Client Details
clientName = skt.gethostname() 
clientIP = skt.gethostbyname(clientName)

print("Client Name: {}\nClient IP: {}\n\n".format(clientName, clientIP))

#Protocol = UDB, addressFamily = ipv4
protocol = skt.SOCK_DGRAM
addressFamily = skt.AF_INET

#socket creation
socket = skt.socket(addressFamily, protocol)

#server details
serverIp = "192.168.99.103"
serverPort = 2121

print("Server IP: {}\nServer Port: {}\n\n".format(serverIp, serverPort))

#request
request = ""

while True:
    request = input("Enter request: ")

    if(request == "close"):
        break;
    else:
        #send request
        size = socket.sendto(request.encode(), (serverIp, serverPort))
        print("{} byte(s) of data sent.\n".format(size))
