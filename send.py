#!/usr/bin/env python

import argparse
import sys
import socket
import random
import struct
import datetime

from scapy.all import *

def main():

    dest = '172.17.0.1'  # destination = h3
    iface = 'h1-eth0'

    print ("Sending on interface %s to %s" % (iface, str(dest)))
    msg = input("Message : ")

    while(msg.casefold() != 'end') :

        pkt = Ether(src=get_if_hwaddr(iface)) / IP(dst=dest) / TCP(dport=1234, sport=49153) / msg  # Make a packet
        pkt.show2()

        print(datetime.datetime.now())  # To observe the delay

        sendp(pkt, iface=iface, verbose=False)

        msg = input("Message : ")

if __name__ == '__main__':

    main()
