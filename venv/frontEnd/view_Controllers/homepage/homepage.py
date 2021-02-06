from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class homepage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #setup for box layout
        self.orientation = 'vertical'
        self.spacing = 30
        self.padding = 80

        #Ui element instantiations
        welcome_Label = Label(text="Welcome to Paper Gap Wallet",
                              size_hint=(None, None),
                              height = 180,
                              width = 330,
                              pos_hint={'center_x': 0.5},
                              font_size=42,
                              )



        create_Wallet_Button = Button(text='Create a New Wallet',
                                size_hint=(None, None),
                                height=70,
                                width=380,
                                pos_hint={'center_x':0.5},
                                font_size=25,
                                background_color = (0,0,1,1)
                                )

        exit_Button = Button(text='Exit',
                                size_hint=(None, None),
                                height=70,
                                width=380,
                                pos_hint={'center_x':0.5},
                                font_size=25,
                                # background_color = (0,0,1,1)
                                )
        #adding UI elements to root
        self.add_widget(welcome_Label)
        self.add_widget(create_Wallet_Button)
        self.add_widget(exit_Button)
