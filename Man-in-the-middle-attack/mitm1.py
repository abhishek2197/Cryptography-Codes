import socket 
import random 
host = socket.gethostname() 
port = 2004
BUFFER_SIZE = 2000 
g=11
p=7
exp= random.randint(1,10)
k= (g**exp)%p
MESSAGE = ""+str(k) 

print "Private Key of Alice = "+str(exp) 
alice = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
alice.connect((host, port))

alice.send(MESSAGE.encode())     
data = alice.recv(BUFFER_SIZE)
print "Alice received data:", data.decode()
    
print "Final key of Alice with Eve "+str((int(data)**exp)%p) 
alice.close() 
