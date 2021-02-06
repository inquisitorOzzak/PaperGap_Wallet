
#imports

#kivy file with setup code is loaded based on class name
from kivy.app import  App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


class Create_Wallet(FloatLayout):

    def word_Spinner_Clicked(self, value):
        '''setup code for number of mnemonic letters'''
        print(value)
        print("/////////")

    def coin_Spinner_Clicked(self, value):
        '''setup code for currency choice'''
        print(value)
        print("/////////")

    def language_Spinner_Clicked(self, value):
        '''setup code for lanuage choice
        note may be re-implented or scrapped'''
        print(value)
        print("/////////")


# builder
class wallet_Build(App):
    def build(self):
        return Create_Wallet()

wallet_Build().run()


