import socket 
 
host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
MESSAGE = "Private Key is 5" 
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))
 

tcpClientA.send(MESSAGE)     
data = tcpClientA.recv(BUFFER_SIZE)
print " Client2 received data:", data
    
 
tcpClientA.close() 
