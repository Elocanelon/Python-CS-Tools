from scapy.all import *

#SNIFFING 
result=sniff(count=5) #Muestra los primeros 5 paquetes en el proceso de sniffing
#result=sniff(filter="tcp", count=2) #solo arroja los primeros dos paquetes TCP 

result.nsummary()
result[0].show