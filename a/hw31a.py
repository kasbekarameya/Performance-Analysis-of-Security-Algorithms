from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import time

def onekb():
	s = time.clock()
	key = os.urandom(16)
	print((time.clock()-s)*10**6)

	def enckb(ip, key ):
		ip = pad(ip, AES.block_size)
		iv = os.urandom(16)
		encryptor = AES.new(key, AES.MODE_CBC, iv)
		k = time.clock()
		e = encryptor.encrypt(ip)
		print((time.clock()-k)*10**6)
		return iv + e	

	def deckb(ep, key ):
		iv = ep[:AES.block_size]
		decryptor = AES.new(key, AES.MODE_CBC, iv)
		m = time.clock()
		d = decryptor.decrypt(ep[AES.block_size:])
		print((time.clock()-m)*10**6)
		return unpad(d, AES.block_size)

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

	def enckb(ip1, key):
		ip1 = pad(ip1, AES.block_size)
		iv1 = os.urandom(16)
		encryptor = AES.new(key1, AES.MODE_CBC, iv1)
		k = time.clock()
		e = encryptor.encrypt(ip1)
		print((time.clock()-k)*10**6)
		return iv1 + e	

	def deckb(ep, key):
		iv1 = ep[:AES.block_size]
		decryptor = AES.new(key1, AES.MODE_CBC, iv1)
		m = time.clock()
		d = decryptor.decrypt(ep[AES.block_size:])
		print((time.clock()-m)*10**6)
		return unpad(d, AES.block_size)

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