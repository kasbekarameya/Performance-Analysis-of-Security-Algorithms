	from Crypto.PublicKey import RSA
	from Crypto.Cipher import PKCS1_OAEP, AES
	import time

	s = time.clock()
	enckey = RSA.generate(2048)
	print((time.clock()-s)*10**6)
	prikey = enckey.export_key()
	with open("private.pem","wb") as priv:
		priv.write(prikey)

	pubkey = enckey.publickey().export_key()	 
	with open("public.pem","wb") as pub:
		pub.write(pubkey)



	def onekb():
		encryptdata = b''

		CHUNK_SIZE = 16
		with open("onekb.txt","rb") as infile:
			#plaintxt = infile.read()
			chunk = infile.read(CHUNK_SIZE)
			while chunk:

				publickey = RSA.importKey(open("public.pem").read())
				paddedpub = PKCS1_OAEP.new(publickey)
				k = time.clock()
				encryptdata += paddedpub.encrypt(chunk)
				print((time.clock()-k)*10**6)
				chunk = infile.read(CHUNK_SIZE) #read the next chunk
			infile.close()

		with open("enckb.enc",'wb') as outfile:
			outfile.write(encryptdata)

		message = b''
		CHUNK_SIZE = 256

		with open("enckb.enc","rb") as infile:
			#plaintxt = infile.read()
			chunk = infile.read(CHUNK_SIZE)
			while chunk:
				#print(len(chunk))
				privatekey = RSA.importKey(open('private.pem').read())
				paddedpriv = PKCS1_OAEP.new(privatekey)
				m = time.clock()
				message += paddedpriv.decrypt(chunk)
				print((time.clock()-m)*10**6)
				chunk = infile.read(CHUNK_SIZE) #read the next chunk
			infile.close()


		with open("deckb.txt",'wb') as outfile:
			outfile.write(message)

	def onemb():
		encryptdata = b''

		CHUNK_SIZE = 16
		with open("onemb.txt","rb") as infile:
			#plaintxt = infile.read()
			chunk = infile.read(CHUNK_SIZE)
			while chunk:

				publickey = RSA.importKey(open("public.pem").read())
				paddedpub = PKCS1_OAEP.new(publickey)
				k = time.clock()
				encryptdata += paddedpub.encrypt(chunk)
				print((time.clock()-k)*10**6)
				chunk = infile.read(CHUNK_SIZE) #read the next chunk
			infile.close()

		with open("encmb.enc",'wb') as outfile:
			outfile.write(encryptdata)

		message = b''
		CHUNK_SIZE = 256

		with open("encmb.enc","rb") as infile:
			#plaintxt = infile.read()
			chunk = infile.read(CHUNK_SIZE)
			while chunk:
				#print(len(chunk))
				privatekey = RSA.importKey(open('private.pem').read())
				paddedpriv = PKCS1_OAEP.new(privatekey)
				m = time.clock()
				message += paddedpriv.decrypt(chunk)
				print((time.clock()-m)*10**6)
				chunk = infile.read(CHUNK_SIZE) #read the next chunk
			infile.close()


		with open("decmb.txt",'wb') as outfile:
			outfile.write(message)


	onekb()
	onemb()