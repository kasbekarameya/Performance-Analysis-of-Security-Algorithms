# Security-Algorithm-Performance-Analysis
In order to understand working and performance offered by various Encryption, Signing, and Hashing algorithms, we have implemented various algorithms on a small size file of 1 KB and a large size file of 1 MB. 
All the experiments are conducted on a local machine with the following configuration:
 Processor: Intel® Core™ i5-8250U CPU @ 1.60GHz
 Memory: 8.00 GB DDR4
 Operating System: Windows 10(64-bit)

All the software used in the following code are:
 Python v3.6.5
 Pycryptodome v3.6.6
 Pyca/cryptography v2.3.1
 HashLib v2.5

The performance measures not only include performance based on encryption time & hashing time, but also time per byte required for each operation. Most of the measurements are provided in Micro Seconds (μs) The observations and code used in this experiment are as follows:

	128 bit AES Encryption & Decryption using CBC Mode [1]:

MEASUREMENTS:

Key Generation Time: 9.67 μs
|                 | Time per Byte (μs)|  1 KB  |  1 MB	|
|-----------------|-------------------|--------|--------| 
| For Encryption: |       0.057       |  59.17 |  3144  |
| For Decryption: |       0.770       |  79.7  |  3891  |


	128 bit AES Encryption & Decryption using CTR Mode [1]:

MEASUREMENTS:
Key Generation Time: 10.24 μs
	Time per Byte (μs)	Total Time (μs)
		1 KB	1 MB
For Encryption:	0.055	56.88	2211
For Decryption:	0.701	71.85	2333

	256 bit AES Encryption & Decryption using CBC mode [1]:

MEASUREMENTS:
Key Generation Time: 9.10 μs
	Time per Byte (μs)	Total Time (μs)
		1 KB	1 MB
For Encryption:	0.057	58.59	2307
For Decryption:	0.826	84.6	2380

	SHA Hashing (256-bit SHA, 512-bit SHA & 256-bit SHA-3) [2]:

MEASUREMENTS for 256-bit SHA:
Time per Byte (μs)	Total Time (μs)
	1 KB	1 MB
0.020	20.48	2524.72

MEASUREMENTS for 512-bit SHA:
Time per Byte (μs)	Total Time (μs)
	1 KB	1 MB
0.018	18.77	1627.10

MEASUREMENTS for 256-bit SHA-3:
Time per Byte (μs)	Total Time (μs)
	1 KB	1 MB
0.041	42.09	3327.43

	PKCS #1 v2 Encryption & Decryption using 2048-bit RSA key [1]:

MEASUREMENTS:
Key Generation Time: 155.5 milliseconds
	Time per Byte (μs)	Total Time per Chunk(μs)
		1 KB	1 MB
For Encryption:	17.94	2871	3065
For Decryption:	37.98	9725	10382

	PKCS #1 v2 Encryption & Decryption using 3072-bit RSA key [1]:

MEASUREMENTS:
Key Generation Time: 180.26 milliseconds
	Time per Byte (μs)	Total Time per Chunk (μs)
		1 KB	1 MB
For Encryption:	24.12	3860	3995
For Decryption:	74.05	28437	37345


	Signature & Verification using 2048-bit DSA key [2]:

MEASUREMENTS:
Key Generation Time: 0.73 seconds
	Time per Byte (μs)	Total Time (μs)
		1 KB	1 MB
For Signature Generation:	0.86	888.6	6048.8
For Signature Verification:	1.05	1082.59	6590.01




	Signature & Verification using 3072-bit DSA key [2]:

MEASUREMENTS:
Key Generation Time: 1.56 seconds
	Time per Byte (μs)	Total Time (μs)
		1 KB	1 MB
For Signature Generation:	1.38	1418.8	3979.37
For Signature Verification:	2.32	2377	4010.66

Based on the above measurements & using concepts used in various Encryption, Signing & Hashing Algorithms we have arrived on to following observations:

o	How per byte speed changes for different algorithms between small and large files: 
Time per byte for an operation can be described as the total unit time required to complete one operation on a byte size of data. Here, as per our measurements, we can observe that time per byte for both 1KB & 1MB file when performing AES encryption algorithm is less compared to the that required by RSA encryption algorithm. This is because AES algorithm uses symmetric encryption which can be almost 3 -5 times faster than asymmetric encryption used in the RSA algorithm. 
o	How encryption and decryption times differ for a given encryption algorithm
In the experiments performed using the encryption algorithms such as AES, we have varied various parameters such as modes of operation, etc. From the observations, when we compared the encryption and decryption time for AES encryption using CBC mode & CTR mode, we observed that time required in AES Encryption in CTR mode improves by about 20% compared to AES Encryption in CBC mode.

o	How key generation, encryption, and decryption times differ with the increase in the key size
In the encryption algorithms such as RSA, we have calculated measures for two different key lengths i.e. 2048 bit & 3072 bits. Hence, based on the observations, when we increase the key size from 2048 bits to 3072 bits, the time for encryption & decryption of 1KB & 1MB files for RSA algorithm with a 3072-bit key is 25% slower than that using a 2048-bit key. As for the key generation time, we see a 13% decrease in performance for the 3072-bit key.
o	How hashing time differs between the algorithms and with an increase of the output hash
Hashing algorithms like SHA use various bit keys such as 256 bit & 512 bit in order to generate a hash value or digest of the input data. As per the measurements, when all the three hashing functions i.e. SHA256, SHA512, SHA3-256 are implemented, we observe that SHA-256 requires the same time as SHA-512 when hashing a small file of 1KB, but when trying to hash a large file of 1MB then we see that SHA-512 is about 2% faster than SHA-256. With this, we can infer that SHA-512 is faster with hashing data of larger sizes.  

o	How the performance of symmetric key encryption (AES), hash functions, and public-key encryption (RSA) compare to each other.
When comparing the performance of Symmetric key encryption like AES, hashing functions like SHA256 & Public key encryption like RSA, we have taken into account some of the common parameters between all the three types of algorithms. These parameters are time per byte for various operations and key generation times. 
Hashing Algorithms are used only to generate a digest value for some amount of data. On the other hand, Encryption algorithms are designed to encrypt them as well as decrypt the data. The major difference observed in the measurements obtained above is that hashing algorithms require the least amount of unit time per byte to perform an operation, compared to the Encryption algorithms.
In the encryption algorithms used, we have two variations namely Symmetric- Key Encryption such as AES & Public Key Encryption such as RSA. Here, after calculating the time per byte & key generation time, we can infer that Symmetric Key encryption algorithms require less time than Public Key Encryption algorithms. This is because Public Key Encryption uses more complex mathematical operations such as power & modulus on very large keys (2048 bits). Whereas on the other hand, Symmetric Key encryption uses simpler operations such as XOR and Multiplication using smaller keys (128-bits). 
