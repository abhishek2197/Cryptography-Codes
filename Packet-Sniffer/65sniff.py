
#abhishek_2197
import os
import socket
from struct import *


s= socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
#s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))


while 1:
   
    recv = s.recvfrom(65565) #Receive the raw packet
    recv = recv[0]
    ip_header = recv[0:20]

    ip_unpacked = unpack('!BBHHHBBH4s4s' , ip_header)
     
    version_val = ip_unpacked[0]
    version = version_val>>4
    ipheader_val = version_val&0xF
    ipheader_length = ipheader_val*4
    ttl = ip_unpacked[5]
    protocol = ip_unpacked[6]
    source_addr = socket.inet_ntoa(ip_unpacked[8]);
    destination_addr = socket.inet_ntoa(ip_unpacked[9]);
     
    print 'Version : '+str(version)

    print 'IP Header Length : '+str(ipheader_length)
 
    print 'TTL : ' +str(ttl)
 
    print 'Protocol : '+str(protocol)

    print 'Source Address : '+str(source_addr)
 
    print 'Destination Address : '+str(destination_addr)
     
    tcp_header = recv[ipheader_length:ipheader_length+20]
    tcp_unpacked = unpack('!HHLLBBHHH' , tcp_header)
     
    source_port = tcp_unpacked[0]
    dest_port = tcp_unpacked[1]
    sequence = tcp_unpacked[2]
    acknowledgement = tcp_unpacked[3]
    data_offset = tcp_unpacked[4]
    tcpheader_length = data_offset >> 4
     
    print 'Source Port : '+str(source_port)

    print 'Destination Port : '+str(dest_port)

    print 'Sequence Number : '+str(sequence)

    print 'Acknowledgement : '+str(acknowledgement)

    print 'TCP header length : '+str(tcpheader_length)
     
    tot_header = ipheader_length+tcpheader_length*4
    packet_len=len(recv)
    data_size = packet_len-tot_header
    data=recv[tot_header:]     

   
   
    print 'Data : '+data
    	

