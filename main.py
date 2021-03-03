
from app.bitcoinBackend.seed import *
from app.bitcoinBackend.wallet_generation import *


from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import StringProperty
from app.pdf.pdfGen import *

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')




class Homepage(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Ui element instantiations
        welcome_Label = Label(text="Welcome to Paper Gap Wallet",
                              size_hint=(0.6, 0.3),
                              height=180,
                              width=330,
                              pos_hint={'center_x': 0.5, "top": 0.85},
                              font_size=42,
                              )

        create_Wallet_Button = Button(text='Create a New Wallet',
                                      size_hint=(0.5, 0.12),
                                      # height=70,
                                      # width=380,
                                      pos_hint={'center_x': 0.5, "top": 0.45},
                                      font_size=25,
                                      background_color=(0, 0, 1, 1)
                                      )
        create_Wallet_Button.bind(on_press=self.switchCreateWallet)

        exit_Button = Button(text='Restore Previous Wallet',
                             size_hint=(0.5, 0.12),
                             height=70,
                             width=380,
                             pos_hint={'center_x': 0.5, "top": 0.26},
                             font_size=25,
                             )
        exit_Button.bind(on_press=self.switchRecoveryPhrase)

        # adding UI elements to root
        self.add_widget(welcome_Label)
        self.add_widget(create_Wallet_Button)
        self.add_widget(exit_Button)

    def switchCreateWallet(self, _):
        sm.transition.direction = 'left'
        sm.current = "Create_Wallet"

    def switchRecoveryPhrase(self, _):
        sm.transition.direction = 'left'
        sm.current = "Confirm_Phrase"


class Create_Wallet(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.coin_Type = None
        self.language = None
        self.word_Num = None
        self.mnemonic = 'Waiting to be generated...'

        # Ui elements generated on view instantiation
        self.back_Button = Button(
            text="Back",
            pos_hint={"top": 0.97, "x": 0.022},
            size_hint=(0.15, 0.1),
            background_color=(0, 0, 1, 1),
            on_press=self.backHomepage

        )

        info_Label = Label(
            text="In order to access your bitcoin wallet we will generate a random mnemonic",
            font_size=23,
            size_hint=(1, 0.2),
            pos_hint={"top": 0.94}

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
            values=("12", "16", "20", "24"),
            size_hint=(0.3, 0.1),
            pos_hint={"top": 0.65, "x": 0.35},
            background_color=(0.92156863, 0.88235294, 0.88235294, 1)

        )

        language_Spinner = Spinner(
            text="Mnemonic Language",
            values=("English", "Español", "Français"),
            size_hint=(0.3, 0.1),
            pos_hint={"top": 0.65, "x": 0.68},
            background_color=(0.92156863, 0.88235294, 0.88235294, 1)

        )

        generate_Button = Button(
            size=(180, 330),
            text="Generate Wallet",
            pos_hint={"y": 0.05, "x": 0.25},
            size_hint=(0.5, 0.15),
            background_color=(0, 0, 1, 1),
            font_size=25
        )

        self.add_widget(self.back_Button)
        self.add_widget(info_Label)
        self.add_widget(coin_Spinner)
        self.add_widget(word_Num_Spinner)
        self.add_widget(language_Spinner)
        self.add_widget(generate_Button)

        coin_Spinner.bind(text=self.coin_Spinner_Clicked)
        word_Num_Spinner.bind(text=self.word_Spinner_Clicked)
        language_Spinner.bind(text=self.language_Spinner_Clicked)
        generate_Button.bind(on_press=self.generate_Wallet)

    def coin_Spinner_Clicked(self, _, value):
        """setup code for currency choice"""
        print(value)

        # setting as default for timebeing
        self.coin_Type = "Bitcoin"

    def word_Spinner_Clicked(self, _, value):
        """setup code for number of mnemonic letters"""
        print(value)

        # setting given word number
        self.word_Num = int(value)

    def language_Spinner_Clicked(self, _, value):
        """setup code for language choice
        note may be re-implented or scrapped"""
        print(value)

        # set as default until language feature implemented
        self.language = value

    def generate_Wallet(self, _):
        # will add language and coin type later

        # sm.transition.direction = "left"
        # sm.current = "Confirm_Phrase"
        self.clear_widgets()

        # elements generated when "Generate Wallet" Ui button selected
        title = Label(text="Recovery Phrase",
                      size_hint=(1, 0.2),
                      pos_hint={"top": 1},
                      font_size=40
                      )
        info_Label_Warning = Label(text="Please write your recovery phrase down on paper and keep it in\n"
                                        "a safe,offline place. Never share your recovery phrase with anyone,\n"
                                        "and never enter it in any online website or service.",
                                   font_size=20,
                                   size_hint=(1, 0.3),
                                   pos_hint={"top": 0.85})

        warning_Label = Label(text="If you lose your recovery phrase, your wallet cannot be recovered.",
                              font_size=18,
                              size_hint=(1, 0.15),
                              pos_hint={"top": 0.60},
                              color=(1, 0, 0, 1)
                              )

        check_Box = CheckBox(active=False,
                             size_hint=(0.05, 0.05),
                             pos_hint={"top": 0.1, "x": 0.2},
                             )

        check_Box.bind(active=self.checkbox_click)

        check_Label = Label(text="I have safely stored my recovery phrase offline",
                            font_size=18,
                            size_hint=(0.5, 0.15),
                            pos_hint={"x": 0.25}

                            )

        # creating mnemonic properties
        mnemonic_Obj = MnemonicGenerator()
        binary = mnemonic_Obj.generateBinary()
        availText = mnemonic_Obj.createWordList(self.language)
        mnemonic = mnemonic_Obj.generateMnemonic(self.word_Num, availText, binary)
        print("This is the created Mnemonic for user: " + mnemonic[0])

        mnemonic_Label = Label(text=str(mnemonic[0]),
                               font_size=25,
                               size_hint=(1, 0.35),
                               text_size=(self.width, None),
                               pos_hint={"top": 0.5},
                               color=(0.2745098, 0.59607843, 0.78039216, 1)
                               )

        self.add_widget(title)
        self.add_widget(info_Label_Warning)
        self.add_widget(warning_Label)
        self.add_widget(mnemonic_Label)
        self.add_widget(check_Label)
        self.add_widget(check_Box)
        self.add_widget(self.back_Button)

    def checkbox_click(self, _, value):
        if value:
            # here we generate the next navigation button
            self.temp_Button = Button(
                text="Continue to Wallet",
                size_hint=(0.2, 0.1),
                pos_hint={"x": 0.78, "top": 0.13},
                background_color=(0, 0, 1, 1),
                on_press=self.confirmPhraseScreen
            )

            self.add_widget(self.temp_Button)
        else:
            self.remove_widget(self.temp_Button)

    def confirmPhraseScreen(self, _):
        sm.transition.direction = "left"
        sm.current = "Confirm_Phrase"

    def backHomepage(self, _):
        sm.transition.direction = 'right'
        sm.current = 'Homepage'


class confirmPhrase(FloatLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        home_Button = Button(
            text="Return Home",
            pos_hint={"top": 0.95, 'x': 0.82},
            size_hint=(0.15, 0.1),
            background_color=(0, 0, 1, 1),
            on_press=self.returnToHome

        )

        back_Button = Button(
            text="Back",
            pos_hint={"top": 0.95, "x": 0.022},
            size_hint=(0.15, 0.1),
            background_color=(0, 0, 1, 1),
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

        self.mnemonic = TextInput(hint_text='Type your recovery phrase here',
                                  font_size=15,
                                  size_hint=(0.4, 0.1),
                                  pos_hint={"top": 0.5, "x": 0.3},
                                  foreground_color=(0, 0, 1, 1))

        submit_Button = Button(
            text="Submit Phrase",
            pos_hint={"y": 0.1, "x": 0.25, },
            size_hint=(0.5, 0.12),
            background_color=(0, 0, 1, 1),
            font_size=25,
            on_press=self.submit_Text)

        self.add_widget(title)
        self.add_widget(confirm_Label)
        self.add_widget(self.mnemonic)
        self.add_widget(submit_Button)
        self.add_widget(back_Button)
        self.add_widget(home_Button)

    # function call for checking correct mnemonic
    def submit_Text(self, _):

        user_Wallet = User_Wallet(self.mnemonic.text)
        if user_Wallet.verifyMnemonic() == 1:
            print("Mnemonic is valid!")
            print(self.mnemonic.text)

            # removing any previously created addresses
            # os.remove('derived_addresses.txt')

            # generates a thousand initally, trims down entrys based on
            # user preference
            user_Wallet.generateWalletContent(100)

            sm.transition.direction = "left"
            sm.current = "CreatePDF"

        else:
            print("Mnemonic not valid")
            print(self.mnemonic.text)

    def backRecoverypage(self, _):
        sm.transition.direction = "right"
        sm.current = 'Create_Wallet'

    def returnToHome(self, _):
        sm.transition.direction = "right"
        sm.current = 'Homepage'


'''need to add input validations and '''


# class uses float layout for co-ordinating UI elements


# Pdf page class
class CreatePDF(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.added = False # check variable for removing UI elements
        self.adQR = False
        self.spinner_Num = 10 # default spinner value


        self.back_Button = Button(
            text="Back",
            pos_hint={"top": 0.95, "x": 0.022},
            size_hint=(0.15, 0.1),
            background_color=(0, 0, 1, 1),
            on_press=self.backConfirmPhrase

        )

        self.pdf_Label = Label(
            text="Create PDF",
            size_hint=(1, 0.2),
            pos_hint={"top": 1},
            font_size=40
        )

        self.info_Label = Label(
            text="Please select the number of public keys/addresses you would like generated",
            font_size=18,
            size_hint=(1, 0.15),
            pos_hint={"top": 0.85}
        )

        self.entryNumSpinner = Spinner(
            text="Entry No",
            values=("1", "5", "10", "50", "100"),
            size_hint=(0.3, 0.1),
            pos_hint={"top": 0.7, "x": 0.1},
            background_color=(0.92156863, 0.88235294, 0.88235294, 1)

        )

        self.previewPDFButton = Button(text='Preview PDF',
                                       size_hint=(None, None),
                                       height=70,
                                       width=380,
                                       pos_hint={'center_x': 0.5, "top": 0.25},
                                       font_size=25,
                                       background_color=(0, 0, 1, 1),
                                       on_press=self.createPDFPreview
                                       )

        self.PDF_Name = TextInput(hint_text='Give A Name To Your Wallet',
                font_size=25,
                size_hint=(0.45, 0.12),
                pos_hint={"top": 0.45, 'center_x': 0.5},
                foreground_color=(1, 1, 1, 1),
                background_color=(0,0,0,1),
                halign= 'center'

                    )

        self.qr_Checkbox = CheckBox(
            active=False,
            size_hint=(0.1, 0.1),
            pos_hint={"top": 0.7, "x": 0.5}
        )

        self.qr_Label = Label(
            text="Add QR Code",
            font_size=16,
            size_hint=(0.3, 0.1),
            pos_hint={"top": 0.7, "x": 0.55}
        )

        self.add_widget(self.pdf_Label)
        self.add_widget(self.info_Label)
        self.add_widget(self.entryNumSpinner)


        self.add_widget(self.back_Button)

        self.qr_Checkbox.bind(active=self.checkbox_click)
        self.entryNumSpinner.bind(text=self.entryNumSpinnerClicked)



    '''Here is where any setup code for the number
of pdf entries will be'''

    def entryNumSpinnerClicked(self, _, value):

        if self.added == True:
            self.remove_widget(self.qr_Checkbox)
            self.remove_widget(self.qr_Label)
            self.remove_widget(self.previewPDFButton)
            self.remove_widget(self.PDF_Name)

        if int(value) > 10:
            print("wont be allowed to generate QR codes")
            self.add_widget(self.previewPDFButton)
            self.add_widget(self.PDF_Name)
            self.added = True
        else:

            self.add_widget(self.qr_Checkbox)
            self.add_widget(self.qr_Label)
            self.add_widget(self.previewPDFButton)
            self.add_widget(self.PDF_Name)
            self.added = True

        self.spinner_Num = value


    def checkbox_click(self, _, value):
        if value:
            self.adQR = True
            print("OR code will be added for each entry in your pdf")

    def createPDFPreview(self, _):
        self.remove_widget(self.previewPDFButton)
        self.remove_widget(self.entryNumSpinner)
        self.remove_widget(self.qr_Label)
        self.remove_widget(self.qr_Checkbox)
        self.remove_widget(self.PDF_Name)
        self.remove_widget(self.back_Button)

        self.pdf_Label.text = "Content Sample"
        self.info_Label.text = "Here is a sample of what will be on your PDF"
        address_Data = parseTextFile(int(self.spinner_Num))
        abs_Path = os.path.abspath('app') + '/pdf/QR/'
        abs_Path = abs_Path.replace('\\', '/')
        generatePDF(self.PDF_Name.text, self.adQR, abs_Path, address_Data)

        # display_Text = ' '
        # for data in address_Data:
        #     display_Text += "%s     %s \n" % (str(data[0]), str(data[1]))

        # print(display_Text)
        #
        # self.addressData = ScrollView(size_hint = (0.8, 0.55))
        # self.addressData.add_widget(TextInput(text = display_Text, size_hint= (1, None), height = self.addressData.height))
        self.walletContent = ScrollView(
            size_hint=(1, 0.8),
            bar_width=10,
            bar_color=(1, 0, 0, 1),  # red
            bar_inactive_color=(0, 0, 1, 1),  # blue
            size=(Window.width, (Window.height // 2)),

        )

        self.add_widget(self.walletContent)
        data_Label = Label(text='', size_hint=(None, None), size= (15, 15), font_size=15)
        for address_Info in address_Data:
            data_Label.text += "%s      %s \n" % (str(address_Info[0]), str(address_Info[1]))

        self.walletContent.add_widget(data_Label)


    def backConfirmPhrase(self, _):
        sm.transition.direction = "right"
        sm.current = 'Confirm_Phrase'


class PaperGapWallet(App):
    def build(self):
        global sm
        sm = ScreenManager()
        homepage_Screen = Screen(name="Homepage")
        homepage_Screen.add_widget(Homepage())
        sm.add_widget(homepage_Screen)

        create_Wallet_Screen = Screen(name="Create_Wallet")
        create_Wallet_Screen.add_widget(Create_Wallet())
        sm.add_widget(create_Wallet_Screen)

        confirmPhrase_Screen = Screen(name="Confirm_Phrase")
        confirmPhrase_Screen.add_widget(confirmPhrase())
        sm.add_widget(confirmPhrase_Screen)


        createPDF_Screen = Screen(name="CreatePDF")
        createPDF_Screen.add_widget(CreatePDF())
        sm.add_widget(createPDF_Screen)

        return sm


if __name__ == "__main__":
    PaperGapWallet().run()

# validMneFrench = 'veston chéquier frégate inexact viseur genou ruiner académie scinder rayonner cendrier accepter novembre pliage acteur casque houleux corniche girafe plaisir silicium frivole verdure sommeil'
# validMneEspan = 'pecho aula ameno reino tres mesón bondad bufón vivir primo quieto enemigo juerga altar onda jaula pupila subir tuerto balde fiar obispo nota alto'
# validMnsEng = 'pen claim celery asda elite fashion crucial faculty merry pen idle wealth bundle office basic much other direct cross snack provide move cage cousin'

