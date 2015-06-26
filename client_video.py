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
	return sr

def Rev():
	addr = ('127.0.0.9',5000)
	s = socket()
	s.connect(addr)
	out = []
	
	pre = s.recv(12)
	print pre
	(num_chunks, len_last) = (int(pre.split(',')[0]), int(pre.split(',')[1]))
	
	print 'now'
	
	for rond in range(num_chunks):
		if rond != num_chunks - 1:
			chunk= s.recv(2**15)
			out.append(chunk)
		else:
			chunk= s.recv(len_last)
			out.append(chunk)
		print 'step'
	return out

def show(frame):
	cv2.namedWindow('Chat')
	cv2.imshow('Chat', frame)
	print frame

if __name__ == '__main__':
	show(chunk_image(Rev()))