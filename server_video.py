from socket import socket
import cv2
from pickle import dumps
from bz2 import compress


def chunks(inp):
	sr = dumps(inp)
	inp = compress(sr)
	bs = 2**17
	out = []
	for x in range((len(inp) / bs) + 1):
		out.append(inp[(bs*x):(bs)*(x+1)])
	return out

def Ser():
	addr = ('127.0.0.8', 5000)
	s = socket()
	s.bind(addr)
	
	s.listen(1)
	c, addr = s.accept()
	
	vc = cv2.VideoCapture(0)
	
	while True:
		_, frame = vc.read()
		ch = chunks(frame)
		pre = str(len(ch)) + ',' + str(len(ch[-1])) + ','
		pre = pre.ljust(12)
		c.send(pre)
		for x in ch:
			c.send(x)
		print 'fine'


if __name__ == '__main__':
	Ser()
