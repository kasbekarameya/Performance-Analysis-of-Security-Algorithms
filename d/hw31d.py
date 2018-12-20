import hashlib
import time

def sha256():
	print("sha256")
	with open("onekb.txt","rb") as kbfile:
		kb = kbfile.read()
		s = time.clock()
		kbhash = hashlib.sha256(kb).hexdigest();
		print((time.clock()-s)*10**6)

		print(kbhash)

	with open("onemb.txt","rb") as mbfile:
		mb = mbfile.read()
		m = time.clock()
		mbhash = hashlib.sha256(mb).hexdigest();
		print((time.clock()-m)*10**6)
		print(mbhash)    

def sha512():
	print("sha512")
	with open("onekb.txt","rb") as kbfile:
		kb = kbfile.read()
		s = time.clock()
		kbhash = hashlib.sha512(kb).hexdigest();
		print((time.clock()-s)*10**6)
		print(kbhash)

	with open("onemb.txt","rb") as mbfile:
		mb = mbfile.read()
		m = time.clock()
		mbhash = hashlib.sha512(mb).hexdigest();
		print((time.clock()-m)*10**6)
		print(mbhash)  

def sha3_256():
	print("sha3-256")
	with open("onekb.txt","rb") as kbfile:
		kb = kbfile.read()
		s = time.clock()
		kbhash = hashlib.sha3_256(kb).hexdigest();
		print((time.clock()-s)*10**6)
		print(kbhash)

	with open("onemb.txt","rb") as mbfile:
		mb = mbfile.read()
		m = time.clock()
		mbhash = hashlib.sha3_256(mb).hexdigest();
		print((time.clock()-m)*10**6)
		print(mbhash)  

sha256() 
sha512()   	
sha3_256()