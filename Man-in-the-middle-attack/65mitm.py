import socket 
from threading import Thread 
import random
from SocketServer import ThreadingMixIn 
 

class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "New server socket thread started for " +ip + ":" +str(port) 
 
    def run(self): 
           data = conn.recv(2048)  
           z= (g**exp3)%p
           MESSAGE = ""+str(z)
           
           print "Eve received data:", data.decode()
           x =set()
           x.add((int(data)**exp3)%p)
           print "This thread communicates with key "+str((int(data)**exp3)%p)
           
           print "Data sent to the thread : "+MESSAGE
           conn.send(MESSAGE.encode())  
 

TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20  

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
exp3= random.randint(1,10)
g=11
p=7 
while True: 
    tcpServer.listen(4) 
    
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 
