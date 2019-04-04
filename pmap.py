#!/usr/bin/env python2.7

from scapy.all import *
import argparse
from prettytable import PrettyTable
import itertools
import time as Ti
<<<<<<< HEAD
<<<<<<< HEAD

=======
#This a new code of mine
>>>>>>> beta_version
=======


>>>>>>> beta_version
start = Ti.time()
#set arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p","--pcap",  help="the pcap file loction that you want to read from")
args = parser.parse_args()
pcap = args.pcap

print """

                    __                             __
                   | _|		    /^-^\         |_ |
                   | |     	   / o o \         | |
                   | |            /   Y   \        | |
                   | |            V \ v / V        | |
                   | |              / - \          | |
                   | |             /    |          | |
                   | |       (    /     |          | |
                   | |        ===/___) ||          | |
                   | |                             | |
                   |__|         		  |__|



                        ____                                      
                       |  _ \ _ __ ___   __ _ _ __                
                       | |_) | '_ ` _ \ / _` | '_ \               
                       |  __/| | | | | | (_| | |_) |              
                       |_|   |_| |_| |_|\__,_| .__/               
                                             |_|                  


"""


#Create a dictionary to hold IPs Source and Open Ports :
d1 = {}
#Iterarte over packets and append IP source and Open Ports source to the dictionary:
print "[+] Iterate over packets and store them into a dict ....."
a = d1.setdefault
with PcapReader(pcap) as packets:
	for pkt in packets:
		if IP or TCP or UDP in pkt:
			try:
				a(pkt[IP].src, []).append(pkt[TCP].dport)
			except:
				pass
#create the table of Host IP and Open Ports
print "[+] Done!"
print "[+] Creating a Table of Host IP and Open Ports....."
t = PrettyTable(["Host IP", "Open Ports"])
print "[+] Done!"
#Remove repeated Open Ports from the dictionary
print "[+] Remove repeated Open Ports from Dict...."
b = d1.iteritems()
result = {key:list(set(value)) for key, value in b}
print "[+] Done!"

# Sorted based on the number of Open Ports :
print "[+] Sorte based on the number of Open Ports......"
c = result.iteritems()
d = t.add_row
for key, value in sorted(c, key=lambda (k,v):len(v), reverse=True):
		d([key, value])
print "[+] Done!"
# print the Result
print "[+] Print the Result"
print(t)
print "[+] Done! Great Job!"

end = Ti.time()

print "Time for execution is {} secs .".format(end-start)
