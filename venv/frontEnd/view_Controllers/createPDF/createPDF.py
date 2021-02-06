from kivy.app import  App
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout


# setup gui code
KV = '''
<FloatLayout>:
    Label:
        text: 'Create PDF'
        size_hint: (1, 0.2)
        pos_hint: {"top" : 1}
        font_size: 40
        
    Label:
        text: 'Please select the number of public keys/addresses you would like generated'
        font_size: 18
        size_hint: (1, 0.15)
        pos_hint: {"top": 0.85}
         
    Spinner:
        id: entryNumberId
        text: "Entry No"
        values: ["1", "5", "10", "50", "100"]
        on_text: root.entryNumSpinnerClicked(entryNumberId.text)
        size_hint: 0.3, 0.1
        pos_hint: {"top": 0.7, "x":0.1}
        background_color: (0.92156863, 0.88235294, 0.88235294, 1)
        

    CheckBox:
        active: True
        size_hint: 0.1, 0.1
        pos_hint: {"top": 0.7, "x":0.5}
        
    Label:
        text: "Add QR Code"
        font_size: 16
        size_hint: 0.3, 0.1
        pos_hint: {"top": 0.7, "x":0.55}
                

'''

#building Kivy code
root = Builder.load_string(KV)

#Pdf page class
class createPDF(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # root contains all initialzed kivi ui code
        self.root = root


    '''Here is where any setup code for the number
    of pdf entries will be'''
    def entryNumSpinnerClicked(self, value):
        print(value)

    # need to add setup code for QR code checkbox


# build class, will be re-implemented
class BuildPDF(App):
    def build(self):
        return createPDF()

BuildPDF().run()