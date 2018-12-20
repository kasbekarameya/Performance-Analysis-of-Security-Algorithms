from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Util.Padding import pad, unpad
import os
import time

def onekb():
	s = time.clock()
	key = os.urandom(16)
	print((time.clock()-s)*10**6)

	def enckb(ip, key ,key_size=128):
		ip = ip + b"\0" * (AES.block_size - len(ip) % AES.block_size)
		count = Counter.new(128)
		encryptor = AES.new(key, AES.MODE_CTR, counter = count)
		k = time.clock()
		e = encryptor.encrypt(ip)
		print((time.clock()-k)*10**6)	
		return e

	def deckb(ep, key ,key_size=128):
		count = Counter.new(128)
		decryptor = AES.new(key, AES.MODE_CTR, counter = count)
		m = time.clock()
		d =decryptor.decrypt(ep)
		print((time.clock()-m)*10**6)
		return d.rstrip(b"\0")

	with open("onekb.txt","rb") as ifile:
		inputtxt = ifile.read()
		enctxt = enckb(inputtxt, key)

	with open("enckb" + ".enc", 'wb') as ofile:
		ofile.write(enctxt)

	with open("enckb.enc","rb") as ifile:
		outputtxt = ifile.read()
		dectxt = deckb(outputtxt, key)
	
	with open("deckb" + ".txt", 'wb') as ofile:
		ofile.write(dectxt)

def onemb():
	key1 = os.urandom(16)

	def enckb(ip1, key ,key_size=128):
		ip1 = ip1 + b"\0" * (AES.block_size - len(ip1) % AES.block_size)
		count1 = Counter.new(128)
		encryptor = AES.new(key1, AES.MODE_CTR, counter = count1)
		k = time.clock()
		e = encryptor.encrypt(ip1)
		print((time.clock()-k)*10**6)	
		return e	

	def deckb(ep, key ,key_size=128):
		count1 = Counter.new(128)
		decryptor = AES.new(key1, AES.MODE_CTR, counter = count1)
		m = time.clock()
		d =decryptor.decrypt(ep)
		print((time.clock()-m)*10**6)
		return d.rstrip(b"\0")

	with open("onemb.txt","rb") as ifile:
		inputtxt1 = ifile.read()
		enctxt1 = enckb(inputtxt1, key1)

	with open("encmb" + ".enc", 'wb') as ofile:
		ofile.write(enctxt1)

	with open("encmb.enc","rb") as ifile:
		outputtxt1 = ifile.read()
		dectxt1 = deckb(outputtxt1, key1)
	
	with open("decmb" + ".txt", 'wb') as ofile:
		ofile.write(dectxt1)

onekb()		
onemb()