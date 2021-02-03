from kivy.app import  App
from kivy.uix.widget import Widget
from view_Controllers.homepage import homepage



class paperGap_Wallet(App):
    def build(self):
        return homepage()

paperGap_Wallet().run()