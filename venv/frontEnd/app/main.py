from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.graphics import Rectangle
from kivy.uix.image import Image


class Homepage(BoxLayout):
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
        create_Wallet_Button.bind(on_press=self.switchCreateWallet)




        exit_Button = Button(text='Restore Previous Wallet',
                                size_hint=(None, None),
                                height=70,
                                width=380,
                                pos_hint={'center_x':0.5},
                                font_size=25,
                                )
        exit_Button.bind(on_press=self.switchRecoveryPhrase)

        #adding UI elements to root
        self.add_widget(welcome_Label)
        self.add_widget(create_Wallet_Button)
        self.add_widget(exit_Button)

    def switchCreateWallet(self, obj):
        sm.transition.direction = 'left'
        sm.current = "Create_Wallet"

    def switchRecoveryPhrase(self, obj):
        sm.transition.direction = 'left'
        sm.current = "Confirm_Phrase"


class Create_Wallet(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.coin_Type = None
        self.language = None
        self.word_Num = None
        self._mnemonic = None


        back_Button = Button(
            background_normal ='C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/button.png',
            background_down = 'C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/back-button-pressed.png',
            size_hint = (0.08, 0.12),
            pos_hint= {"top": 0.98},
            on_press=self.backHomepage

        )


        info_Label = Label(
            text="In order to access your bitcoin wallet we will generate a random mnemonic",
            font_size=23,
            size_hint =(1, 0.2),
            pos_hint ={"top": 0.94}

        )

        coin_Spinner = Spinner(
            text="Coin Type",
            values=("Bitcoin", "Bitcoin Cash", "Dogecoin"),
            size_hint=(0.3, 0.1),
            pos_hint={"top": 0.65, "x": 0.02},
            background_color=(0.92156863, 0.88235294, 0.88235294, 1)

        )

        word_Num_Spinner = Spinner(
            text="Word Number",
            values = ("12", "16", "20", "24"),
            size_hint=(0.3, 0.1),
            pos_hint= {"top": 0.65, "x":0.35},
            background_color=(0.92156863, 0.88235294, 0.88235294, 1)

        )

        language_Spinner = Spinner(
            text="Mnemonic Language",
            values=("English", "Español", "Français"),
            size_hint=(0.3, 0.1),
            pos_hint={"top": 0.65, "x":0.68},
            background_color=(0.92156863, 0.88235294, 0.88235294, 1)

        )

        generate_Button = Button(
            size = (180, 330),
            text="Generate Wallet",
            pos_hint={"y": 0.05, "x": 0.25},
            size_hint=(0.5, 0.15),
            background_color= (0,0,1,1),
            font_size=25
        )

        self.add_widget(back_Button)
        self.add_widget(info_Label)
        self.add_widget(coin_Spinner)
        self.add_widget(word_Num_Spinner)
        self.add_widget(language_Spinner)
        self.add_widget(generate_Button)

        coin_Spinner.bind(text=self.coin_Spinner_Clicked)
        word_Num_Spinner.bind(text=self.word_Spinner_Clicked)
        language_Spinner.bind(text=self.language_Spinner_Clicked)
        generate_Button.bind(on_press=self.generate_Wallet)

    def coin_Spinner_Clicked(self, obj,  value):
        '''setup code for currency choice'''
        print(value)

        #setting as default for timebeing
        self.coin_Type = "Bitcoin"
        print("/////////")

    def word_Spinner_Clicked(self, obj, value):
        '''setup code for number of mnemonic letters'''
        print(value)

        #setting given sword number
        self.word_Num = int(value)

    def language_Spinner_Clicked(self, obj, value):
        '''setup code for lanuage choice
        note may be re-implented or scrapped'''
        print(value)

        #set as default until language feature implemented
        self.language = "English"


    def generate_Wallet(self, obj):

        # will add language and coin type later
        # created_Mnemonic = Mnemonic_gen(self.word_Num)
        # self.setMnemonic(created_Mnemonic.words)
        sm.current = "Recovery_Phrase"

    def getMnemonic(self):
        return self._mnemonic

    def setMnemonic(self, words):
        self._mnemonic = words

    def backHomepage(self, obj):
        sm.transition.direction = 'right'
        sm.current = 'Homepage'



class confirmPhrase(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        home_Button = Button(
            background_normal='C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/backToHomeButton-blue.png',
            background_down = 'C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/backToHomeButton-cyan.png',
            pos_hint={"top": 0.98, 'x':0.85},
            size_hint= (None, None),
            height = 80,
            width = 100,
            background_color=(0, 0, 1, 1),
            on_press = self.returnToHome

        )

        back_Button = Button(
            background_normal ='C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/button.png',
            background_down = 'C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/back-button-pressed.png',
            size_hint = (0.08, 0.12),
            pos_hint= {"top": 0.98},
            on_press=self.backRecoverypage

        )

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
        self.add_widget(back_Button)
        self.add_widget(home_Button)

# function call for checking correct mnemonic
    def submit_Text(self, object):
        sm.transition.direction = "left"
        sm.current = "CreatePDF"
        print(self.mnemonic.text)

    def backRecoverypage(self, obj):
        sm.transition.direction = "right"
        sm.current = 'Recovery_Phrase'

    def returnToHome(self, obj):
        sm.transition.direction = "right"
        sm.current = 'Homepage'

'''need to add input validations and '''


#class uses float layout for co-ordinating UI elements
class RecoveryPhrase(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        back_Button = Button(
            background_normal ='C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/button.png',
            background_down = 'C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/back-button-pressed.png',
            size_hint = (0.08, 0.12),
            pos_hint= {"top": 0.98},
            on_press=self.backCreateWallet

        )
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
        mnemonic_Label = Label(text="mnemonic label",
                               font_size=25,
                               size_hint=(1, 0.35),
                               pos_hint={"top": 0.5},
                               color=(0.2745098, 0.59607843, 0.78039216, 1)
                               )

        check_Box = CheckBox(active=False,
                             pos_hint={"top": 0.578, "x": -0.35},
        )

        check_Box.bind(active=self.checkbox_click)

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
        self.add_widget(back_Button)

    '''method for checkbox state change
    should dynamically create a button to transition to 
    next screen'''
    def checkbox_click(self, instance, value):
        if value:
            #here we generate the next navigation button
            self.temp_Button = Button(
                text="Continue to Wallet",
                size_hint=(0.2, 0.1),
                pos_hint={"x": 0.78, "top":0.13},
                background_color=(0, 0, 1, 1),
                on_press=self.confirmPhraseScreen
            )


            self.add_widget(self.temp_Button)
        else:
            self.remove_widget(self.temp_Button)

    def confirmPhraseScreen(self, obj):
        sm.transition.direction = "left"
        sm.current = "Confirm_Phrase"

    def backCreateWallet(self, obj):
        sm.transition.direction = "right"
        sm.current = "Create_Wallet"


# Pdf page class
class CreatePDF(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        back_Button = Button(
            background_normal ='C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/button.png',
            background_down = 'C:/Users/rober/github_Projs/teamSoftwareProject/venv/frontEnd/assets/back-button-pressed.png',
            size_hint = (0.08, 0.12),
            pos_hint= {"top": 0.98},
            on_press=self.backConfirmPhrase

        )

        pdf_Label = Label(
            text="Create PDF",
            size_hint= (1, 0.2),
            pos_hint= {"top": 1},
            font_size=40
        )

        info_Label = Label(
            text= "Please select the number of public keys/addresses you would like generated",
            font_size=18,
            size_hint = (1, 0.15),
            pos_hint = {"top": 0.85}
        )

        entryNumSpinner = Spinner(
            text="Entry No",
            values=("1", "5", "10", "50", "100"),
            size_hint= (0.3,0.1),
            pos_hint={"top": 0.7, "x":0.1},
            background_color= (0.92156863, 0.88235294, 0.88235294, 1)

        )

        qr_Checkbox = CheckBox(
            active=False,
            size_hint = (0.1, 0.1),
            pos_hint = {"top": 0.7, "x":0.5}
        )

        qr_Label = Label(
            text= "Add QR Code",
            font_size= 16,
            size_hint= (0.3, 0.1),
            pos_hint={"top": 0.7, "x":0.55}
        )
        self.previewPDFButton = Button(text='Preview PDF',
                                size_hint=(None, None),
                                height=70,
                                width=380,
                                pos_hint={'center_x':0.5, "top": 0.4},
                                font_size=25,
                                background_color = (0,0,1,1),
                                on_press=self.createPDFPreview
                                )

        self.add_widget(pdf_Label)
        self.add_widget(info_Label)
        self.add_widget(entryNumSpinner)
        self.add_widget(qr_Checkbox)
        self.add_widget(qr_Label)
        self.add_widget(self.previewPDFButton)
        self.add_widget(back_Button)

        entryNumSpinner.bind(text=self.entryNumSpinnerClicked)
        qr_Checkbox.bind(active=self.checkbox_click)
    '''Here is where any setup code for the number
of pdf entries will be'''

    def entryNumSpinnerClicked(self,obj, value):
        print(value)

    def checkbox_click(self, obj, value):
        if value:
            #user has chosen to take a QR code
            print("OR code will be added for each entry in your pdf")

    def createPDFPreview(self, obj):
        #here is where all PDF generation code will be
        #within the size/scope of this rectangle
        #will be reviewed later in production
        self.remove_widget(self.previewPDFButton)

    def backConfirmPhrase(self, obj):
        sm.transition.direction = "right"
        sm.current = 'Confirm_Phrase'



class PaperGapWallet(App):
    def build(self):
        global sm
        sm = ScreenManager()
        homepage_Screen =Screen(name="Homepage")
        homepage_Screen.add_widget(Homepage())
        sm.add_widget(homepage_Screen)

        create_Wallet_Screen = Screen(name="Create_Wallet")
        create_Wallet_Screen.add_widget(Create_Wallet())
        sm.add_widget(create_Wallet_Screen)

        confirmPhrase_Screen = Screen(name="Confirm_Phrase")
        confirmPhrase_Screen.add_widget(confirmPhrase())
        sm.add_widget(confirmPhrase_Screen)

        recoveryPhrase_Screen = Screen(name="Recovery_Phrase")
        recoveryPhrase_Screen.add_widget(RecoveryPhrase())
        sm.add_widget(recoveryPhrase_Screen)

        createPDF_Screen = Screen(name="CreatePDF")
        createPDF_Screen.add_widget(CreatePDF())
        sm.add_widget(createPDF_Screen)

        return sm

if __name__ == "__main__":
    PaperGapWallet().run()