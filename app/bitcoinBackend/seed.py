import binascii as b0
import os
import hashlib

class MnemonicGenerator():
    # generates random seed
    def __init__(self):
        self.entropy = os.urandom(32)

    def generateBinary(self):

        # convert it to hex
        entropy_hex = b0.hexlify(self.entropy)
        bytes = len(entropy_hex)

        # add first 8 bits of sha256 because entropy is 32 bytes
        hashed256 = hashlib.sha256(self.entropy).hexdigest()

        # entropy to binary
        result_binary = (
                    bin(int(entropy_hex, 16))[2:].zfill(bytes + 8) + bin(int(hashed256, 16))[2:].zfill(256)[: bytes + 8 // 32])

        return result_binary

# create list of all suitable mnemonic words by reading in from a file
    def createWordList(self, language):
        words = []
        abso_Path = os.path.abspath("app")
        filename = abso_Path + "/bitcoinBackend/locales/{mnemonicLanguage}.txt".format(mnemonicLanguage=str(language))
        filename = filename.replace("\\", "/")
        with open(filename,"r", encoding="utf8") as file:
            for word in file.readlines():
                words.append(word.strip())
        return words


    # for i in range(len(result_binary) // 13):
    def generateMnemonic(self, menmonic_Range, words, result_binary):
        # create the mnemonic of 24 words

        mnemonic_list = []
        for i in range(menmonic_Range):
            index = int(result_binary[i * 11: (i + 1) * 11], 2)
            mnemonic_list.append(words[index])
        output_Mnemonic_List = mnemonic_list
        mnemonic = " ".join(mnemonic_list)

        #this will need to be encrypted
        return (mnemonic, output_Mnemonic_List)

code = MnemonicGenerator()
binary = code.generateBinary()