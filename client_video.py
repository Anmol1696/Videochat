import pickle
from socket import socket
import cv2
import numpy
from bz2 import decompress
import time
from threading import Thread

def chunk_image(chunks):
	out = ''
	for chunk in chunks:
		out +=  chunk
	out = decompress(out)
	sr = pickle.loads(out)
	return sr

frame = [0]

def Rev():
	addr = ('127.0.0.9',5000)
	s = socket()
	s.connect(addr)
	
	while True:
		out = []
		pre = s.recv(12)
		(num_chunks, len_last) = (int(pre.split(',')[0]), int(pre.split(',')[1]))
		for rond in range(num_chunks):
			if rond != num_chunks - 1:
				chunk= s.recv(2**15)
				out.append(chunk)
			else:
				chunk= s.recv(len_last)
				out.append(chunk)
		frame[0] = chunk_image(out) 

def th():
	cv2.namedWindow('Chat')
	while True:
		cv2.imshow('Chat', frame[0])
		cv2.waitKey(20)

if __name__ == '__main__':
	t = Thread(target = th)
	t.start()
	Rev()