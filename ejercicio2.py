#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI

class LinearTopo(Topo):
    def build(self):
        switches = []  # Lista para guardar los switches
        lastSwitch = None
        for i in range(4):
            switch = self.addSwitch('s%s' % (i+1))
            switches.append(switch)  # Guardar switch
            if lastSwitch:
                self.addLink(lastSwitch, switch)
            lastSwitch = switch

        for i in range(5):
            host = self.addHost('h%s' % (i+1))
            self.addLink(host, switches[i % 4])  # Usar la lista switches

if __name__ == '__main__':
    topo = LinearTopo()
    net = Mininet(topo=topo, controller=None)  # Aquí le dices que no use controlador
    net.start()
    CLI(net)
    net.stop()
