import pickle
from socket import socket
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
	s = socket()
	s.connect(addr)
	
	cv2.namedWindow('Chat')
	
	while True:
		out = []
		pre = s.recv(12)
		(num_chunks, len_last) = (int(pre.split(',')[0]), int(pre.split(',')[1]))
		for rond in range(num_chunks):
			if rond != num_chunks - 1:
				chunk= s.recv(2**17)
				out.append(chunk)
			else:
				chunk= s.recv(len_last)
				out.append(chunk)
		cv2.imshow('Chat', chunk_image(out))
		key = cv2.waitKey(20)
		print 'fine'


if __name__ == '__main__':
	Rev()