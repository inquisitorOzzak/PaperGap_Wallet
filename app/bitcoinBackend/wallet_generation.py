from bitmerchant.wallet import *
from cryptos import *

class User_Wallet():

    def __init__(self, mnemonic):
        self.__words = mnemonic
        self.__wordsList = mnemonic.split()
        self.__valid_seed = True
        self.__wallet = Wallet.from_master_secret(self.__words)  # generates wallet based on the words
        self.__priv_key = self.__wallet.serialize_b58(private=True)  # generates extended private key
        self.__pub_key = self.__wallet.serialize_b58(private=False)  # generates extended public key

    # compares inputted seed with list of 2048 words
    def __verify_seed(self):
        language_List = ["English", "Français", "Español"]
        check_Eng = 1
        check_Fr = 1
        check_Es = 1

        abso_Path = os.path.abspath("app")
        for lang in language_List:

            filename = abso_Path + "/bitcoinBackend/locales/{mnemonicLanguage}.txt".format(mnemonicLanguage=str(lang))
            print(filename)
            filename = filename.replace("\\", "/")
            file = open(filename, "r", encoding="utf8")
            file_contents = file.read()
            for word in self.__wordsList:
                if word not in file_contents:

                    if lang == language_List[0]:
                        check_Eng = 0
                    elif lang == language_List[1]:
                        check_Fr = 0
                    else:
                        check_Es = 0

                    file.close()
                    break
            file.close()
            
        return check_Eng + check_Fr + check_Es
    def verifyMnemonic(self):
        return self.__verify_seed()

    # outputs wallet attributes to user.
    # will need authentication from user like password to access
    # will be used strictly for debugging purposes...
    def get_wallet(self):
        if self.__valid_seed:
            print("\nThese words are the mnemonic seed from which "
                  "the public and private extended keys "
                  "are generated \n mnemonic seed: ", self.__words)

            print("\nThis extended private key is used to generate "
                  "derived addresses and public keys which can "
                  "only be accessed by inputting the extended "
                  "private key \n Extended private key: ", self.__priv_key)

            print("\nThe extended public key is visible by all users and "
                  "is derived from the mnemonic seed \nExtended Public Key: ", self.__pub_key)

    # derives a variable amount of address/ public key pairs from extended private
    # key. If a user wants to access their wallet they should input the private key to
    # generate these addresses, after entering their password.
    # using .txt file as simple implementation
    def __gen_derived_address(self, var):
        if self.__valid_seed:
            file = open("derived_addresses.txt", "w")
            for x in range(var):
                my_wallet_children = self.__wallet.deserialize(self.__priv_key)
                pub_child = my_wallet_children.get_child(x, is_prime=True, as_private=False)
                file.write("address " + str(x + 1) + ":\t" + str(pub_child.to_address()) + "\n")
            file.close()

    def generateWalletContent(self, entry_number):
        self.__gen_derived_address(entry_number)

