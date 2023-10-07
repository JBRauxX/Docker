import socket
import numpy as np
import math

HOST = "127.0.0.1"
PORT = 8000
den = 20
rad = 100
theta = math.tau / den

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
msg = s.recv(1024)
print(msg.decode("utf-8"))

for step in range(10):
    i = step%den
    x = np.array([math.cos(i*theta) * rad])
    y = np.array([math.sin(i*theta) * rad])
    data = np.array([np.array([y]), np.array([x])])
    s.sendall(data)