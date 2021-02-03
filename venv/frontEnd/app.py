from kivy.app import  App
from kivy.uix.widget import Widget
from view_Controllers.homepage import homepage
from view_Controllers.create_A_Wallet import Create_Wallet



class paperGap_Wallet(App):
    def build(self):
        # return homepage()
        return Create_Wallet()

paperGap_Wallet().run()