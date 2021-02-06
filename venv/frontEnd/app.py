
#various page testing imports
from kivy.app import  App
from kivy.uix.widget import Widget
from view_Controllers.homepage import homepage
from view_Controllers.create_A_Wallet import Create_Wallet


''' will need to decide on how to transition views here'''
class paperGap_Wallet(App):
    def build(self):

        return Create_Wallet()

paperGap_Wallet().run()