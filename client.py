from socket import *
import cv2
from pickle import loads
from zlib import decompress

def chunk_image(chunks):
	out = ''
	for chunk in chunks:
		out +=  chunk
	out = decompress(out)
	out = out.encode('string-escape')
	out = loads(out)
	return chunk_image

def Rev():
	addr = ('127.0.0.7',5000)
	s = socket(AF_INET, SOCK_DGRAM)
	s.bind(addr)
	out = []
	
	pre, ADDR = s.recvfrom(12)
	print pre
	(num_chunks, len_last) = (int(pre.split(',')[0]), int(pre.split(',')[1]))
	
	print 'now'
	
	for rond in range(num_chunks):
		if rond != num_chunks - 1:
			chunk, ADDR = s.recvfrom(2**15)
			out.append(chunk)
		else:
			chunk, ADDR = s.recvfrom(len_last)
			out.append(chunk)
		print 'step'
	return out

def show(frame):
	cv2.nameWindow('Chat')
	cv2.imshow('Chat', frame)

if __name__ == '__main__':
	show(chunk_image(Rev()))