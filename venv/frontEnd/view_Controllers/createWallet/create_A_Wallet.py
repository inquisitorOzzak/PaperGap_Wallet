# from kivy.uix.boxlayout import BoxLayout
# # from kivy.uix.button import Button
# # from kivy.uix.label import Label
from kivy.app import  App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout

# Designate our .kv design file
# Builder.load_file('wallet_build.kv')
class Create_Wallet(FloatLayout):

    def word_Spinner_Clicked(self, value):
        #here we will be implementing some of the
        #backend bitcoin code
        print(value)
        print("/////////")

    def coin_Spinner_Clicked(self, value):
        print(value)
        print("/////////")

    def language_Spinner_Clicked(self, value):
        print(value)
        print("/////////")


class wallet_Build(App):
    def build(self):
        return Create_Wallet()

wallet_Build().run()


