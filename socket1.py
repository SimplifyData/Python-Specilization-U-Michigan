
"""
This a script for using lower level sockets
"""
import socket

HOST = 'www.pythonlearn.com'

PORT = 80

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect((HOST,PORT))

mysock.send(b'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print(data.decode("utf-8"))

mysock.close()