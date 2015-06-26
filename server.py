from socket import *
import cv2
from pickle import dumps
from zlib import compress


def chunks(inp):
	bs = 2**15
	out = []
	for x in range((len(inp) / bs) + 1):
		out.append(inp[(bs*x):(bs)*(x+1)])
	return out

def Ser(inp):
	addr = ('127.0.0.7', 5000)
	s = socket(AF_INET, SOCK_DGRAM)
	serlize = dumps(inp)
	sr = serlize.decode('string-escape')
	data = compress(sr)
	ch = chunks(data)
	pre = str(len(ch)) + ',' + str(len(ch[-1])) + ','
	pre = pre.ljust(12)
	s.sendto(pre, addr)
	for x in ch:
		s.sendto(x, addr)

def Frame():
	vc = cv2.VideoCapture(0)
	_, frame = vc.read()
	vc.release()
	return frame

if __name__ == '__main__':
	Ser(Frame())
