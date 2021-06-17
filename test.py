
#!/usr/bin/env python

from mininet.cli import CLI
from mininet.net import Mininet
from mininet.link import Link,TCLink,Intf


if '__main__' == __name__:

  net = Mininet(link=TCLink)

  h1 = net.addHost('h1')    # Sender
  h2 = net.addHost('h2')    # Router
  h3 = net.addHost('h3')    # Receiver

  net.addLink(h1, h2)   # Sender - Router
  net.addLink(h2, h3)   # Receiver - Router

  net.build()


  # Seperate the network
  
  h1.cmd('ifconfig h1-eth0 172.16.0.1 netmask 255.255.0.0')
  h2.cmd('ifconfig h2-eth0 172.16.0.2 netmask 255.255.0.0')

  h3.cmd('ifconfig h3-eth0 172.17.0.1 netmask 255.255.0.0')
  h2.cmd('ifconfig h2-eth1 172.17.0.2 netmask 255.255.0.0')

  h2.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward') # Routing => enable

  h1.cmd('route add default gw 172.16.0.2')  # h2-eth0
  h3.cmd('route add default gw 172.17.0.2')  # h2-eth1


  CLI(net)

  net.stop()
