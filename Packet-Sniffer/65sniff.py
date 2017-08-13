
#abhishek_2197
import os
import socket
from struct import *


s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP) #Creates a socket instance (That can track raw data and tcp protocols used)



while 1:#Assuming the program keeps running and sniffs packets until stopped execution forcefully 
   
    recv = s.recvfrom(65565) #Receive the raw packet
    recv = recv[0]
    ip_header = recv[0:20] #First 20 bytes form the ip header

    ip_unpacked = unpack('!BBHHHBBH4s4s' , ip_header) #unpack is used to unpack the various IP header fields. It returns a python list with each field as an element of the list.
     
    #From here on different parts of the ip-header are extracted based on the architecture
    version_val = ip_unpacked[0] 
    version = version_val>>4
    ipheader_val = version_val&0xF
    ipheader_length = ipheader_val*4
    ttl = ip_unpacked[5]
    protocol = ip_unpacked[6]
    source_addr = socket.inet_ntoa(ip_unpacked[8]);
    destination_addr = socket.inet_ntoa(ip_unpacked[9]);
         
    print '----- IP  HEADER --------'
    print 'Version : '+str(version)

    print 'IP Header Length : '+str(ipheader_length)
 
    print 'Time To Live : ' +str(ttl)
 
    print 'Protocol : '+str(protocol)

    print 'Source Address : '+str(source_addr)
 
    print 'Destination Address : '+str(destination_addr)
     
    #Now comes the TCP Header which is calculated using the length of IP Header

    tcp_header = recv[ipheader_length:ipheader_length+20] #Extracting the TCP Header content from the packet 
    tcp_unpacked = unpack('!HHLLBBHHH' , tcp_header) #Similar unpacking as for the IP Header
     
    #From here on different parts of the tcp-header are extracted based on the architecture
    source_port = tcp_unpacked[0]
    dest_port = tcp_unpacked[1]
    sequence = tcp_unpacked[2]
    acknowledgement = tcp_unpacked[3]
    data_offset = tcp_unpacked[4]
    tcpheader_length = data_offset >> 4
    window_size = tcp_unpacked[5]
    checksum = tcp_unpacked[6]
    urgent = tcp_unpacked[7]

   
    print '-----TCP Header------'  
    print 'Source Port : '+str(source_port)

    print 'Destination Port : '+str(dest_port)

    print 'Sequence Number : '+str(sequence)

    print 'Acknowledgement : '+str(acknowledgement)

    print 'TCP header length : '+str(tcpheader_length)
 
    print 'Window Size: '+str(window_size)

    print 'Checksum: '+str(checksum)
 
    print 'Urgent: '+str(urgent)
     
    	

