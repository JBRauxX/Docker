import socket  
import numpy as np

#host = '127.0.0.1'
port = 8000  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), port))
s.listen(1)


while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    
    #clientsocket = s.recv(1024).decode("utf-8")
    #print(clientsocket)