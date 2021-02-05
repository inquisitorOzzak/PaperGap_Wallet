from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.checkbox import CheckBox
from kivy.app import App


class RecoveryPhrase(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        title = Label(text="Recovery Phrase",
                      size_hint=(1, 0.2),
                      pos_hint={"top": 1},
                      font_size=40
                      )
        info_Label = Label(text="Please write your recovery phrase down on paper and keep it in\n"
                                "a safe,offline place. Never share your recovery phrase with anyone,\n"
                                "and never enter it in any online website or service.",
                           font_size=20,
                           size_hint=(1, 0.3),
                           pos_hint={"top": 0.85})

        warning_Label = Label(text="If you lose your recovery phrase, your wallet cannot be recovered.",
                              font_size=18,
                              size_hint=(1, 0.15),
                              pos_hint={"top": 0.60},
                              color=(1,0,0,1)
                              )
        mnemonic_Label = Label(text="Random Mnemonic Number  Words Will Go \nHere depending on the number of"
                                    "words \nuser chooses and so on User will write \nthis down on paper",
                               font_size=25,
                               size_hint=(1, 0.35),
                               pos_hint={"top": 0.5},
                               color=(0.2745098, 0.59607843, 0.78039216, 1)
                               )

        check_Box = CheckBox(active=True,
                             pos_hint={"top": 0.578, "x": -0.35},
        )

        check_Label =Label(text="I have safely stored my recovery phrase offline",
                           font_size=18,
                           size_hint=(0.5, 0.15),
                           pos_hint= {"x": 0.16}

        )

        self.add_widget(title)
        self.add_widget(info_Label)
        self.add_widget(warning_Label)
        self.add_widget(mnemonic_Label)
        self.add_widget(check_Label)
        self.add_widget(check_Box)

    def checkbox_click(self, instance, value):
        print(value)


class recovery_Phrase_Build(App):
    def build(self):
        return RecoveryPhrase()

recovery_Phrase_Build().run()