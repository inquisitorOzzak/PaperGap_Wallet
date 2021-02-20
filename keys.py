#import bitcoin library
import bitcoin as b

#generate and print private key
private_key = b.random_key()
print("Private Key: ", private_key)

#generate and print public key
public_key = b.privtopub(private_key)
print("Public Key: ", public_key)

#generate and print address
address = b.pubtoaddr(public_key)
print("Address: ", address)
