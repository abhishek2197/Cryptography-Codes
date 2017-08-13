import socket 
 
host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = "Private key is 7"
 
tcpClientB = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientB.connect((host, port))

tcpClientB.send(MESSAGE.encode())     
data = tcpClientB.recv(BUFFER_SIZE)
print " Client received data:", data.decode()
    
 
tcpClientB.close() 
