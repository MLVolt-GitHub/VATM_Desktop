from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.vkeyboard import VKeyboard
import keyboard

from CustomRecept import CustomRecept
from Widgets.CustomButton import CustomButton
from RequiredFuns import RequiredFuns


class EnterPin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'enter_pin_screen'
        self.kbd = VKeyboard(pos_hint={"center_x": 0.5, "center_y": 0.31}, on_key_up=self.keyup)

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x":0.89, "center_y":0.83})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.83},
                                       on_press=self.onHomeButtonPressed)

        self.enterPinLabel = MDLabel(text="ENTER PIN",
                                        pos_hint={"center_x": 0.5, "center_y": 0.85},
                                        halign="center",
                                        font_style="H5")

        self.pinStatusLabel = MDLabel(text="status",
                                         pos_hint={"center_x": 0.5, "center_y": 0.81},
                                         halign="center",
                                         font_style="Subtitle1")

        self.enterPinTextField = MDTextField(mode='rectangle',
                                                hint_text="Enter PIN Here",
                                                pos_hint={"center_x": 0.5, "center_y": 0.65},
                                                size_hint=(0.5, None))

        self.proceedButton = CustomButton(text="Proceed",
                                           font_size="17sp",
                                           size_hint=(0.3, 0.06),
                                           md_bg_color=(0.996, 0.447, 0.180, 1),
                                           pos_hint={"center_x": 0.5, "center_y": 0.55},
                                           )

        self.proceedButton.bind(on_release=self.onProceedButtonPressed)

        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)
        self.add_widget(self.enterPinLabel)
        self.add_widget(self.pinStatusLabel)
        self.add_widget(self.enterPinTextField)
        self.add_widget(self.proceedButton)
        self.add_widget(self.kbd)

    def keyup(self, kbd, keycode, *args):
        if isinstance(keycode, tuple):
            keycode = keycode[1]
        keyboard.press_and_release(keycode)

    def onProceedButtonPressed(self, instance):
        bankName=RequiredFuns()._fetchLocalSavedCredentials("bank")
        contactNum = RequiredFuns()._fetchLocalSavedCredentials("mob")
        amount = RequiredFuns()._fetchLocalSavedCredentials("amount")
        cardNum = RequiredFuns().selectedBankToCardNumber(contactNumber=contactNum, bankName=bankName)
        enteredPin = self.enterPinTextField.text
        try:
            RequiredFuns().downloadQrCode(cardNumber=cardNum[0], pin=enteredPin, amount=amount)
            RequiredFuns()._saveToLocalFile(key="qr", value="True")
        except Exception as e:
            print(e)
            RequiredFuns()._saveToLocalFile(key="qr", value="False")
        amount=self.manager.get_screen('enter_withdraw_amount_screen').enterAmountTextField.text
        CustomRecept("NuLL", "Null", "NUll", amount, "Null")

        self.manager.get_screen("status_screen").statusLabel.text="The Recept is printing of amount "+str(amount)
        self.manager.transition.direction = 'left'
        self.manager.current = 'status_screen'
        Clock.schedule_once(self.moveToHome, 4)




    def onHomeButtonPressed(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'

    def moveToHome(self, dt):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'
