# necessary imports
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.app import App

class confirmPhrase(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        title = Label(text="Confirm Phrase",
                      size_hint=(1, 0.2),
                      pos_hint={"top": 1},
                      font_size=40
                      )

        confirm_Label = Label(text="To confirm your phrase please retype the recovery phrase you have just obtained",
                           font_size=20,
                           size_hint=(1, 0.3),
                           pos_hint={"top": 0.85})

        '''declared text input as attribute so that changing state can be traced
        can probably be better re-implemented later'''

        self.mnemonic = TextInput(text='Type your recovery phrase here',
                                    font_size=15,
                                    size_hint=(0.4, 0.1),
                                    pos_hint={"top": 0.5, "x":0.3},
                                    foreground_color=(0,0,1,1))

        submit_Button = Button(
                               text="Submit Phrase",
                               pos_hint = {"y": 0.1, "x": 0.25,},
                               size_hint = (0.5, 0.12),
                               background_color = (0,0,1,1),
                               font_size =25,
                               on_press=self.submit_Text)


        self.add_widget(title)
        self.add_widget(confirm_Label)
        self.add_widget(self.mnemonic)
        self.add_widget(submit_Button)

# function call for checking correct mnemonic
    def submit_Text(self, object):

        print(self.mnemonic.text)

'''need to add input validations and '''

class confirm_Phrase_Build(App):
    def build(self):
        return confirmPhrase()

confirm_Phrase_Build().run()