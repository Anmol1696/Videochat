from socket import socket
import cv2
from pickle import dumps
from bz2 import compress


def chunks(inp):
	bs = 2**15
	out = []
	for x in range((len(inp) / bs) + 1):
		out.append(inp[(bs*x):(bs)*(x+1)])
	return out

def Ser(inp):
	addr = ('127.0.0.9', 5000)
	s = socket()
	s.bind(addr)
	
	s.listen(1)
	c, addr = s.accept()
	
	sr = dumps(inp)
	data = compress(sr)
	ch = chunks(data)
	pre = str(len(ch)) + ',' + str(len(ch[-1])) + ','
	pre = pre.ljust(12)
	c.send(pre)
	for x in ch:
		c.send(x)

def Frame():
	vc = cv2.VideoCapture(0)
	_, frame = vc.read()
	vc.release()
	print frame
	return frame

if __name__ == '__main__':
	Ser(Frame())
