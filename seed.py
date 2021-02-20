#import binascii, os and hashlib libraries
import binascii as b0
import os
import hashlib

#change input of number of bits into number of bytes
def bitsToBytes(n):
    bytes = n//8
    return bytes

#generate random string of size 32 bytes for entropy
entropy = os.urandom(bitsToBytes(256))

#convert it to hex
entropy_hex = b0.hexlify(entropy)
bytes=len(entropy_hex)

#add first 8 bits of sha256 because entropy is 32 bytes
hashed256 = hashlib.sha256(entropy).hexdigest()

#entropy to binary
result_binary = (bin(int(entropy_hex, 16))[2:].zfill(bytes+8) + bin(int(hashed256,16))[2:].zfill(256)[: bytes + 8 // 32])

#create list of all suitable mnemonic words by reading in from a file
words=[]
with open("words.txt", "r") as file:
    for word in file.readlines():
        words.append(word.strip())

#create the mnemonic of 24 words
mnemonic_list=[]
for i in range(len(result_binary)//13):
    index = int(result_binary[i*11 : (i+1)*11],2)
    mnemonic_list.append(words[index])
mnemonic = " ".join(mnemonic_list)
print(mnemonic)
