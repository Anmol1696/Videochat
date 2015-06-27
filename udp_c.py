import pickle
from socket import *
import cv2
import numpy
from bz2 import decompress
import time

def chunk_image(chunks):
	out = ''
	for chunk in chunks:
		out +=  chunk
	out = decompress(out)
	sr = pickle.loads(out)
	print type(sr)
	return sr

def Rev():
	addr = ('127.0.0.8',5000)
	s = socket(AF_INET, SOCK_DGRAM)
	cv2.namedWindow('Chat')
	
	s.sendto('nice', addr)
	print 'nice sent' 
	
	while True:
		out = []
		chunk,ADDR = s.recvfrom()
		out.append(chunk)
		while len(chunk) == 2**15:
			chunk,ADDR = s.recvfrom()
			out.append(chunk)
		cv2.imshow('Chat', chunk_image(out))
		key = cv2.waitKey(2)
		print 'fine'


if __name__ == '__main__':
	Rev()