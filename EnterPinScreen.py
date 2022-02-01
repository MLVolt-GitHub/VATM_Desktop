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


class EnterPin(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'enter_pin_screen'
        self.kbd = VKeyboard(pos_hint={"center_x": 0.5, "center_y": 0.21}, on_key_up=self.keyup)

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x":0.5, "center_y":0.9})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.95},
                                       on_press=self.onHomeButtonPressed)

        self.enterPinLabel = MDLabel(text="ENTER PIN",
                                        pos_hint={"center_x": 0.5, "center_y": 0.83},
                                        halign="center",
                                        font_style="H5")

        self.pinStatusLabel = MDLabel(text="status",
                                         pos_hint={"center_x": 0.5, "center_y": 0.79},
                                         halign="center",
                                         font_style="Subtitle1")

        self.enterPinTextField = MDTextField(mode='rectangle',
                                                hint_text="Enter PIN Here",
                                                pos_hint={"center_x": 0.5, "center_y": 0.6},
                                                size_hint=(0.5, None))

        self.proceedButton = CustomButton(text="Proceed",
                                           font_size="17sp",
                                           size_hint=(0.3, 0.06),
                                           md_bg_color=(0.996, 0.447, 0.180, 1),
                                           pos_hint={"center_x": 0.5, "center_y": 0.5},
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
        amount=self.manager.get_screen('enter_withdraw_amount_screen').enterAmountTextField.text
        CustomRecept("NuLL", "Null", "NUll", amount, "Null")



    def onHomeButtonPressed(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'