import dill
from socket import socket
import cv2
import numpy
from lz4 import decompress, compress
import time
from threading import Thread


def chunk_image(chunks):
	out = ''
	for chunk in chunks:
		out +=  chunk
	out = decompress(out)
	sr = dill.loads(out)
	print type(sr)
	return sr

def chunks(inp):
        sr = dill.dumps(inp)
        inp = compress(sr)
        bs = 2**14
        out = []
        for x in range((len(inp) / bs) + 1):
                out.append(inp[(bs*x):(bs)*(x+1)])
        return out

def Rev():
	addr = ('127.0.0.9',5000)
	s = socket()
	s.connect(addr)
	
	cv2.namedWindow('Chat')
	
	while True:
		try:
			out = []
			pre = s.recv(12)
			(num_chunks, len_last) = (int(pre.split(',')[0]), int(pre.split(',')[1]))
			for rond in range(num_chunks):
				if rond != num_chunks - 1:
					chunk= s.recv(2**14)
					out.append(chunk)
				else:
					chunk= s.recv(len_last)
					out.append(chunk)
			cv2.imshow('Chat', chunk_image(out))
			key = cv2.waitKey(20)
			print 'fine'
		except:
			pass

def Ser():
        addr = ('127.0.0.9', 5001)
        s = socket()
        s.bind(addr)
        
        s.listen(1)
        c, addr = s.accept()
        
        vc = cv2.VideoCapture(0)
        
        while True:
                try:
                        _, frame = vc.read()
                        ch = chunks(frame)
                        pre = str(len(ch)) + ',' + str(len(ch[-1])) + ','
                        pre = pre.ljust(12)
                        c.send(pre)
                        for x in ch:
                                c.send(x)
                        print 'fine'
                except:
                        pass


if __name__ == '__main__':
	t1 = Thread(target = Rev)
	t2 = Thread(target = Ser)
	t1.start()
	t2.start()
