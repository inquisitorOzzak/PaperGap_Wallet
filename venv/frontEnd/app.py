from kivy.app import  App
from kivy.uix.widget import Widget

class testpage(Widget):
    pass

class paperGap_Wallet(App):
    def build(self):
        return testpage()

paperGap_Wallet().run()