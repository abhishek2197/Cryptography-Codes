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

print "Private Key of Bob = "+str(exp) 
Bob = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
Bob.connect((host, port))

Bob.send(MESSAGE.encode())     
data = Bob.recv(BUFFER_SIZE)
print "Bob received data:", data.decode()
    
print "Final key of Bob with Eve "+str((int(data)**exp)%p) 
Bob.close() 
