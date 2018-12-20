from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
import time

def onekb():
	s = time.clock()
	prikey = dsa.generate_private_key( key_size=2048, backend=default_backend())
	print((time.clock()-s)*10**6)
	
	with open("onekb.txt","rb") as infile:
		indata = infile.read()

	k = time.clock()
	kbsig = prikey.sign( indata,hashes.SHA256())
	print((time.clock()-k)*10**6)
	print("DSA Signature for 1 KB file:\n ",kbsig,"\n")

	m = time.clock()
	pubkey = prikey.public_key()
	pubkey.verify( kbsig, indata, hashes.SHA256())
	print((time.clock()-m)*10**6)


def onemb():
	s = time.clock()
	prikey = dsa.generate_private_key( key_size=2048, backend=default_backend())
	print((time.clock()-s)*10**6)
	
	with open("onemb.txt","rb") as infile:
		chunk = infile.read()

	k = time.clock()
	mbsig = prikey.sign( chunk,hashes.SHA256())
	print((time.clock()-k)*10**6)
	print("DSA Signature for 1 MB file:\n ",mbsig)

	public_key = prikey.public_key()
	m = time.clock()
	public_key.verify( mbsig, chunk, hashes.SHA256())
	print((time.clock()-m)*10**6)

onekb()

onemb()