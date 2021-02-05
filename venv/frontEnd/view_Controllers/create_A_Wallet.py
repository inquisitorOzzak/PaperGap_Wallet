# from kivy.uix.boxlayout import BoxLayout
# # from kivy.uix.button import Button
# # from kivy.uix.label import Label
from kivy.app import  App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget

# Designate our .kv design file
Builder.load_file('wallet_build.kv')
class Create_Wallet(Widget):
        # info_Label = Label(
        #     text = "In order to access your bitcoin wallet we will generate a random mnemonic",
        #     font_size = 20,
        #     width = self.width,
        #     height = 60
        #
        # )
        #
        # word_Num_Dropdown = Spinner(
        #     id = spinner_id,
        #     text = "Word Number",
        #     values = ["16", "20", "24"],
        #
        # )
    def word_Spinner_Clicked(self, value):
        #here we will be implementing some of the
        #backend bitcoin code
        print(value)
        print("/////////")
        print(self.ids.click_label.text)


class wallet_Build(App):
    def build(self):
        return Create_Wallet()

wallet_Build().run()


