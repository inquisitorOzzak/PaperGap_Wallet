# can't sleep so checking out the library :)
import bitcoin
b = bitcoin


# testing the key generation functions

myPrvKey = b.random_key()
myPubKey = b.privtopub(myPrvKey)
myPubAdd = b.pubtoaddr(myPubKey)

print("Private Key: " + myPrvKey + "\n\nPublic Key: " + myPubKey + "\n\nPublicAddress: " + myPubAdd)




# testing seed generation functions

mySeed = b.random_electrum_seed()       # why you no work?