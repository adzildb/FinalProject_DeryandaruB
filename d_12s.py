#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink


def Network():
    net = Mininet(topo=None, build=False, ipBase='192.168.0.0/24', link=TCLink)
  
    info("*** Creating Network")
    print("")
    print("")

    info("*** Adding Controller 1 and Controller 2")
    print("")
    print("")

    # add Controller
    c1 = net.addController(name='Controller1', controller=RemoteController, ip='10.0.2.4', port=6633)

    c2 = net.addController(name='Controller2', controller=RemoteController, ip='10.0.2.5', port=6634)


    info("*** Adding hosts")
    print("")

    # Add hosts
    Host1 = net.addHost( 'h1', ip='192.168.0.1/24' )
    Host2 = net.addHost( 'h2', ip='192.168.0.2/24' )
    Host3 = net.addHost( 'h3', ip='192.168.0.3/24' )
    Host4 = net.addHost( 'h4', ip='192.168.0.4/24' )
    Host5 = net.addHost( 'h5', ip='192.168.0.5/24' )
    Host6 = net.addHost( 'h6', ip='192.168.0.6/24' )
    Host7 = net.addHost( 'h7', ip='192.168.0.7/24' )
    Host8 = net.addHost( 'h8', ip='192.168.0.8/24' )
    Host9 = net.addHost( 'h9', ip='192.168.0.9/24' )
    Host10 = net.addHost( 'h10', ip='192.168.0.10/24' )
    Host11 = net.addHost( 'h11', ip='192.168.0.11/24' )
    Host12 = net.addHost( 'h12', ip='192.168.0.12/24' )
    Host13 = net.addHost( 'h13', ip='192.168.0.13/24' )
    Host14 = net.addHost( 'h14', ip='192.168.0.14/24' )
    Host15 = net.addHost( 'h15', ip='192.168.0.15/24' )
    Host16 = net.addHost( 'h16', ip='192.168.0.16/24' )
    Host17 = net.addHost( 'h17', ip='192.168.0.17/24' )
    Host18 = net.addHost( 'h18', ip='192.168.0.18/24' )
    Host19 = net.addHost( 'h19', ip='192.168.0.19/24' )
    Host20 = net.addHost( 'h20', ip='192.168.0.20/24' )
    Host21 = net.addHost( 'h21', ip='192.168.0.21/24' )
    Host22 = net.addHost( 'h22', ip='192.168.0.22/24' )
    Host23 = net.addHost( 'h23', ip='192.168.0.23/24' )
    Host24 = net.addHost( 'h24', ip='192.168.0.24/24' )
    Host25 = net.addHost( 'h25', ip='192.168.0.25/24' )
    Host26 = net.addHost( 'h26', ip='192.168.0.26/24' )
    Host27 = net.addHost( 'h27', ip='192.168.0.27/24' )
    Host28 = net.addHost( 'h28', ip='192.168.0.28/24' )
    Host29 = net.addHost( 'h29', ip='192.168.0.29/24' )
    Host30 = net.addHost( 'h30', ip='192.168.0.30/24' )
    Host31 = net.addHost( 'h31', ip='192.168.0.31/24' )
    Host32 = net.addHost( 'h32', ip='192.168.0.32/24' )
    Host33 = net.addHost( 'h33', ip='192.168.0.33/24' )
    Host34 = net.addHost( 'h34', ip='192.168.0.34/24' )
    Host35 = net.addHost( 'h35', ip='192.168.0.35/24' )
    Host36 = net.addHost( 'h36', ip='192.168.0.36/24' )

  
    #switches
    Switch1 = net.addSwitch( 's1' )
    Switch2 = net.addSwitch( 's2' )
    Switch3 = net.addSwitch( 's3' )
    Switch4 = net.addSwitch( 's4' )
    Switch5 = net.addSwitch( 's5' )
    Switch6 = net.addSwitch( 's6' )
    Switch7 = net.addSwitch( 's7' )
    Switch8 = net.addSwitch( 's8' )
    Switch9 = net.addSwitch( 's9' )
    Switch10 = net.addSwitch( 's10' )
    Switch11 = net.addSwitch( 's11' )
    Switch12 = net.addSwitch( 's12' )

    # Add links
    net.addLink( Host1, Switch1 )
    net.addLink( Host2, Switch1 )
    net.addLink( Host3, Switch1 )
    net.addLink( Host4, Switch2 )
    net.addLink( Host5, Switch2 )
    net.addLink( Host6, Switch2 )
    net.addLink( Host7, Switch3 )
    net.addLink( Host8, Switch3 )
    net.addLink( Host9, Switch3 )
    net.addLink( Host10, Switch4 )
    net.addLink( Host11, Switch4 )
    net.addLink( Host12, Switch4 )
    net.addLink( Host13, Switch5 )
    net.addLink( Host14, Switch5 )
    net.addLink( Host15, Switch5 )
    net.addLink( Host16, Switch6 )
    net.addLink( Host17, Switch6 )
    net.addLink( Host18, Switch6 )
    net.addLink( Host19, Switch7 )
    net.addLink( Host20, Switch7 )
    net.addLink( Host21, Switch7 )
    net.addLink( Host22, Switch8 )
    net.addLink( Host23, Switch8 )
    net.addLink( Host24, Switch8 )
    net.addLink( Host25, Switch9 )    
    net.addLink( Host26, Switch9 )
    net.addLink( Host27, Switch9 )
    net.addLink( Host28, Switch10 )
    net.addLink( Host29, Switch10 )
    net.addLink( Host30, Switch10 )
    net.addLink( Host31, Switch11 )
    net.addLink( Host32, Switch11 )
    net.addLink( Host33, Switch11 )
    net.addLink( Host34, Switch12 )
    net.addLink( Host35, Switch12 )
    net.addLink( Host36, Switch12 )


    net.addLink( Switch1, Switch2 )
    net.addLink( Switch2, Switch3 )
    net.addLink( Switch3, Switch4 )
    net.addLink( Switch4, Switch5 )
    net.addLink( Switch5, Switch6 )
    net.addLink( Switch6, Switch7 )
    net.addLink( Switch7, Switch8 )
    net.addLink( Switch8, Switch9 )
    net.addLink( Switch9, Switch10 )
    net.addLink( Switch10, Switch11 )
    net.addLink( Switch11, Switch12 )


    net.build()

    for controller in net.controllers:
        controller.start()

    net.get('s1').start([c1,c2])
    net.get('s2').start([c1,c2])
    net.get('s3').start([c1,c2])
    net.get('s4').start([c1,c2])
    net.get('s5').start([c1,c2])
    net.get('s6').start([c1,c2])
    net.get('s7').start([c2,c1])
    net.get('s8').start([c2,c1])
    net.get('s9').start([c2,c1])
    net.get('s10').start([c2,c1])
    net.get('s11').start([c2,c1])
    net.get('s12').start([c2,c1])
    
    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    Network()
