
#!/usr/bin/env python

import sys
import struct
import os
import datetime

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr, bind_layers
from scapy.all import Packet, IPOption, Ether
from scapy.all import ShortField, IntField, LongField, BitField, FieldListField, FieldLenField
from scapy.all import IP, UDP, TCP, Raw, ls
from scapy.layers.inet import _IPOption_HDR

 

def receive_pkt(pkt):

    if TCP in pkt:

      print(datetime.datetime.now())  # To observe the delay
      print(pkt.summary())


def main():

    iface = 'h3-eth0'

    print("Sniffing on %s" % iface)

    sys.stdout.flush()
    sniff(iface = iface, prn = lambda x: receive_pkt(x))

if __name__ == '__main__':

    main()
