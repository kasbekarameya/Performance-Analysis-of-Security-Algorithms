from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa

def onekb():
	prikey = dsa.generate_private_key( key_size=3072, backend=default_backend())
	
	with open("onekb.txt","rb") as infile:
		indata = infile.read()

	kbsig = prikey.sign( indata,hashes.SHA256())
	print("DSA Signature for 1 KB file:\n ",kbsig,"\n")

	pubkey = prikey.public_key()
	pubkey.verify( kbsig, indata, hashes.SHA256())


def onemb():
	prikey = dsa.generate_private_key( key_size=2048, backend=default_backend())
	
	with open("onemb.txt","rb") as infile:
		chunk = infile.read()

	mbsig = prikey.sign( chunk,hashes.SHA256())
	print("DSA Signature for 1 MB file:\n ",mbsig)

	public_key = prikey.public_key()
	public_key.verify( mbsig, chunk, hashes.SHA256())

onekb()

onemb()