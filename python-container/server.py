import socket  
import numpy as np

host = '127.0.0.1'
port = 8000  

def setup():
    size(800, 800)
    
    global s    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))

    print(host , port)
    s.listen(1)
    print('Server listening....')

    
def draw():
    background(255)
    translate(width>>1, height>>1)
    clientsocket, address  = s.accept()
    print('Connected by', addr)
    while True:
        try:
            data = conn.recv(1024)
            if not data: break
            #print (data)
            print("Client Says: " + bytearray(data, 'utf-8').decode())
            #conn.sendall("Server Says:hi")

        except socket.error:
            print( "Error Occured.")
            #conn.close()
            break