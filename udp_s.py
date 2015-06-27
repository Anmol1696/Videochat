from socket import *
import cv2
from pickle import dumps
from bz2 import compress


def chunks(inp):
	sr = dumps(inp)
	inp = compress(sr)
	bs = 2**15
	out = []
	for x in range((len(inp) / bs) + 1):
		out.append(inp[(bs*x):(bs)*(x+1)])
	return out

def Ser():
	addr = ('127.0.0.8', 5000)
	c = socket(AF_INET, SOCK_DGRAM)
	c.bind(addr)
	
	_, address = c.recvfrom()
	print 'Recived nice from -> ', address
	
	vc = cv2.VideoCapture(0)
	
	while True:
		_, frame = vc.read()
		ch = chunks(frame)
		for x in ch:
			c.sendto(x, address)
		print 'fine'


if __name__ == '__main__':
	Ser()
