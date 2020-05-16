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

    info("*** Creating Network")
    print("")
    print("")

    info("*** Adding Controller")
    print("")
    print("")

    # add Controller
    c1 = net.addController(name='Controller1', controller=RemoteController, ip='10.0.2.4', port=6633)


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
    Host37 = net.addHost( 'h37', ip='192.168.0.37/24' )
    Host38 = net.addHost( 'h38', ip='192.168.0.38/24' )
    Host39 = net.addHost( 'h39', ip='192.168.0.39/24' )
    Host40 = net.addHost( 'h40', ip='192.168.0.40/24' )
    Host41 = net.addHost( 'h41', ip='192.168.0.41/24' )
    Host42 = net.addHost( 'h42', ip='192.168.0.42/24' )
    Host43 = net.addHost( 'h43', ip='192.168.0.43/24' )
    Host44 = net.addHost( 'h44', ip='192.168.0.44/24' )
    Host45 = net.addHost( 'h45', ip='192.168.0.45/24' )
    Host46 = net.addHost( 'h46', ip='192.168.0.46/24' )
    Host47 = net.addHost( 'h47', ip='192.168.0.47/24' )
    Host48 = net.addHost( 'h48', ip='192.168.0.48/24' )
    Host49 = net.addHost( 'h49', ip='192.168.0.49/24' )
    Host50 = net.addHost( 'h50', ip='192.168.0.50/24' )
    Host51 = net.addHost( 'h51', ip='192.168.0.51/24' )
    Host52 = net.addHost( 'h52', ip='192.168.0.52/24' )
    Host53 = net.addHost( 'h53', ip='192.168.0.53/24' )
    Host54 = net.addHost( 'h54', ip='192.168.0.54/24' )
    Host55 = net.addHost( 'h55', ip='192.168.0.55/24' )
    Host56 = net.addHost( 'h56', ip='192.168.0.56/24' )
    Host57 = net.addHost( 'h57', ip='192.168.0.57/24' )
    Host58 = net.addHost( 'h58', ip='192.168.0.58/24' )
    Host59 = net.addHost( 'h59', ip='192.168.0.59/24' )
    Host60 = net.addHost( 'h60', ip='192.168.0.60/24' )
    Host61 = net.addHost( 'h61', ip='192.168.0.61/24' )
    Host62 = net.addHost( 'h62', ip='192.168.0.62/24' )
    Host63 = net.addHost( 'h63', ip='192.168.0.63/24' )
    Host64 = net.addHost( 'h64', ip='192.168.0.64/24' )
    Host65 = net.addHost( 'h65', ip='192.168.0.65/24' )
    Host66 = net.addHost( 'h66', ip='192.168.0.66/24' )
    Host67 = net.addHost( 'h67', ip='192.168.0.67/24' )
    Host68 = net.addHost( 'h68', ip='192.168.0.68/24' )
    Host69 = net.addHost( 'h69', ip='192.168.0.69/24' )
    Host70 = net.addHost( 'h70', ip='192.168.0.70/24' )
    Host71 = net.addHost( 'h71', ip='192.168.0.71/24' )
    Host72 = net.addHost( 'h72', ip='192.168.0.72/24' )
    Host73 = net.addHost( 'h73', ip='192.168.0.73/24' )
    Host74 = net.addHost( 'h74', ip='192.168.0.74/24' )
    Host75 = net.addHost( 'h75', ip='192.168.0.75/24' )
    Host76 = net.addHost( 'h76', ip='192.168.0.76/24' )
    Host77 = net.addHost( 'h77', ip='192.168.0.77/24' )
    Host78 = net.addHost( 'h78', ip='192.168.0.78/24' )
    Host79 = net.addHost( 'h79', ip='192.168.0.79/24' )
    Host80 = net.addHost( 'h80', ip='192.168.0.80/24' )
    Host81 = net.addHost( 'h81', ip='192.168.0.81/24' )
    Host82 = net.addHost( 'h82', ip='192.168.0.82/24' )
    Host83 = net.addHost( 'h83', ip='192.168.0.83/24' )
    Host84 = net.addHost( 'h84', ip='192.168.0.84/24' )
    Host85 = net.addHost( 'h85', ip='192.168.0.85/24' )
    Host86 = net.addHost( 'h86', ip='192.168.0.86/24' )
    Host87 = net.addHost( 'h87', ip='192.168.0.87/24' )
    Host88 = net.addHost( 'h88', ip='192.168.0.88/24' )
    Host89 = net.addHost( 'h89', ip='192.168.0.89/24' )
    Host90 = net.addHost( 'h90', ip='192.168.0.90/24' )
    Host91 = net.addHost( 'h91', ip='192.168.0.91/24' )
    Host92 = net.addHost( 'h92', ip='192.168.0.92/24' )
    Host93 = net.addHost( 'h93', ip='192.168.0.93/24' )
    Host94 = net.addHost( 'h94', ip='192.168.0.94/24' )
    Host95 = net.addHost( 'h95', ip='192.168.0.95/24' )
    Host96 = net.addHost( 'h96', ip='192.168.0.96/24' )
    Host97 = net.addHost( 'h97', ip='192.168.0.97/24' )
    Host98 = net.addHost( 'h98', ip='192.168.0.98/24' )
    Host99 = net.addHost( 'h99', ip='192.168.0.99/24' )
    Host100 = net.addHost( 'h100', ip='192.168.0.100/24' )
    Host101 = net.addHost( 'h101', ip='192.168.0.101/24' )
    Host102 = net.addHost( 'h102', ip='192.168.0.102/24' )
    Host103 = net.addHost( 'h103', ip='192.168.0.103/24' )
    Host104 = net.addHost( 'h104', ip='192.168.0.104/24' )
    Host105 = net.addHost( 'h105', ip='192.168.0.105/24' )
    Host106 = net.addHost( 'h106', ip='192.168.0.106/24' )
    Host107 = net.addHost( 'h107', ip='192.168.0.107/24' )
    Host108 = net.addHost( 'h108', ip='192.168.0.108/24' )

  
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
    Switch13 = net.addSwitch( 's13' )
    Switch14 = net.addSwitch( 's14' )
    Switch15 = net.addSwitch( 's15' )
    Switch16 = net.addSwitch( 's16' )
    Switch17 = net.addSwitch( 's17' )
    Switch18 = net.addSwitch( 's18' )
    Switch19 = net.addSwitch( 's19' )
    Switch20 = net.addSwitch( 's20' )
    Switch21 = net.addSwitch( 's21' )
    Switch22 = net.addSwitch( 's22' )
    Switch23 = net.addSwitch( 's23' )
    Switch24 = net.addSwitch( 's24' )
    Switch25 = net.addSwitch( 's25' )
    Switch26 = net.addSwitch( 's26' )
    Switch27 = net.addSwitch( 's27' )
    Switch28 = net.addSwitch( 's28' )
    Switch29 = net.addSwitch( 's29' )
    Switch30 = net.addSwitch( 's30' )
    Switch31 = net.addSwitch( 's31' )
    Switch32 = net.addSwitch( 's32' )
    Switch33 = net.addSwitch( 's33' )
    Switch34 = net.addSwitch( 's34' )
    Switch35 = net.addSwitch( 's35' )
    Switch36 = net.addSwitch( 's36' )


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
    net.addLink( Host37, Switch13 )
    net.addLink( Host38, Switch13 )
    net.addLink( Host39, Switch13 )
    net.addLink( Host40, Switch14 )
    net.addLink( Host41, Switch14 )
    net.addLink( Host42, Switch14 )
    net.addLink( Host43, Switch15 )    
    net.addLink( Host44, Switch15 )
    net.addLink( Host45, Switch15 )
    net.addLink( Host46, Switch16 )
    net.addLink( Host47, Switch16 )
    net.addLink( Host48, Switch16 )
    net.addLink( Host49, Switch17 )
    net.addLink( Host50, Switch17 )
    net.addLink( Host51, Switch17 )
    net.addLink( Host52, Switch18 )
    net.addLink( Host53, Switch18 )
    net.addLink( Host54, Switch18 )
    net.addLink( Host55, Switch19 )
    net.addLink( Host56, Switch19 )
    net.addLink( Host57, Switch19 )
    net.addLink( Host58, Switch20 )
    net.addLink( Host59, Switch20 )
    net.addLink( Host60, Switch20 )
    net.addLink( Host61, Switch21 )    
    net.addLink( Host62, Switch21 )
    net.addLink( Host63, Switch21 )
    net.addLink( Host64, Switch22 )
    net.addLink( Host65, Switch22 )
    net.addLink( Host66, Switch22 )
    net.addLink( Host67, Switch23 )
    net.addLink( Host68, Switch23 )
    net.addLink( Host69, Switch23 )
    net.addLink( Host70, Switch24 )
    net.addLink( Host71, Switch24 )
    net.addLink( Host72, Switch24 )
    net.addLink( Host73, Switch25 )
    net.addLink( Host74, Switch25 )
    net.addLink( Host75, Switch25 )
    net.addLink( Host76, Switch26 )
    net.addLink( Host77, Switch26 )
    net.addLink( Host78, Switch26 )
    net.addLink( Host79, Switch27 )    
    net.addLink( Host80, Switch27 )
    net.addLink( Host81, Switch27 )
    net.addLink( Host82, Switch28 )
    net.addLink( Host83, Switch28 )
    net.addLink( Host84, Switch28 )
    net.addLink( Host85, Switch29 )
    net.addLink( Host86, Switch29 )
    net.addLink( Host87, Switch29 )
    net.addLink( Host88, Switch30 )
    net.addLink( Host89, Switch30 )
    net.addLink( Host90, Switch30 )
    net.addLink( Host91, Switch31 )
    net.addLink( Host92, Switch31 )
    net.addLink( Host93, Switch31 )
    net.addLink( Host94, Switch32 )
    net.addLink( Host95, Switch32 )
    net.addLink( Host96, Switch32 )
    net.addLink( Host97, Switch33 )    
    net.addLink( Host98, Switch33 )
    net.addLink( Host99, Switch33 )
    net.addLink( Host100, Switch34 )
    net.addLink( Host101, Switch34 )
    net.addLink( Host102, Switch34 )
    net.addLink( Host103, Switch35 )
    net.addLink( Host104, Switch35 )
    net.addLink( Host105, Switch35 )
    net.addLink( Host106, Switch36 )
    net.addLink( Host107, Switch36 )
    net.addLink( Host108, Switch36 )

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
    net.addLink( Switch12, Switch13 )
    net.addLink( Switch13, Switch14 )
    net.addLink( Switch14, Switch15 )
    net.addLink( Switch15, Switch16 )
    net.addLink( Switch16, Switch17 )
    net.addLink( Switch17, Switch18 )
    net.addLink( Switch18, Switch19 )
    net.addLink( Switch19, Switch20 )
    net.addLink( Switch20, Switch21 )
    net.addLink( Switch21, Switch22 )
    net.addLink( Switch22, Switch23 )
    net.addLink( Switch23, Switch24 )
    net.addLink( Switch24, Switch25 )
    net.addLink( Switch25, Switch26 )
    net.addLink( Switch26, Switch27 )
    net.addLink( Switch27, Switch28 )
    net.addLink( Switch28, Switch29 )
    net.addLink( Switch29, Switch30 )
    net.addLink( Switch30, Switch31 )
    net.addLink( Switch31, Switch32 )
    net.addLink( Switch32, Switch33 )
    net.addLink( Switch33, Switch34 )
    net.addLink( Switch34, Switch35 )
    net.addLink( Switch35, Switch36 )


    net.build()

    for controller in net.controllers:
        controller.start()

    net.get('s1').start([c1])
    net.get('s2').start([c1])
    net.get('s3').start([c1])
    net.get('s4').start([c1])
    net.get('s5').start([c1])
    net.get('s6').start([c1])
    net.get('s7').start([c1])
    net.get('s8').start([c1])
    net.get('s9').start([c1])
    net.get('s10').start([c1])
    net.get('s11').start([c1])
    net.get('s12').start([c1])
    net.get('s13').start([c1])
    net.get('s14').start([c1])
    net.get('s15').start([c1])
    net.get('s16').start([c1])
    net.get('s17').start([c1])
    net.get('s18').start([c1])
    net.get('s19').start([c1])
    net.get('s20').start([c1])
    net.get('s21').start([c1])
    net.get('s22').start([c1])
    net.get('s23').start([c1])
    net.get('s24').start([c1])
    net.get('s25').start([c1])
    net.get('s26').start([c1])
    net.get('s27').start([c1])
    net.get('s28').start([c1])
    net.get('s29').start([c1])
    net.get('s30').start([c1])
    net.get('s31').start([c1])
    net.get('s32').start([c1])
    net.get('s33').start([c1])
    net.get('s34').start([c1])
    net.get('s35').start([c1])
    net.get('s36').start([c1])
    
    print("")

    CLI(net)
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    Network()
