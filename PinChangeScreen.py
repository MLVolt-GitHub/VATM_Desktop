from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.vkeyboard import VKeyboard
import keyboard
from Widgets.CustomButton import CustomButton


class PinChangeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'pin_change_screen'
        self.kbd = VKeyboard(pos_hint={"center_x": 0.5, "center_y": 0.21}, on_key_up=self.keyup)

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x": 0.5, "center_y": 0.9})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.95},
                                       on_press=self.onHomeButtonPressed)

        self.pinChangeLabel = MDLabel(text="PIN CHANGE",
                                     pos_hint={"center_x": 0.5, "center_y": 0.83},
                                     halign="center",
                                     font_style="H5")

        self.pinChangeStatusLabel = MDLabel(text="status",
                                             pos_hint={"center_x": 0.5, "center_y": 0.79},
                                             halign="center",
                                             font_style="Subtitle1")

        self.enterOldPinTextField = MDTextField(mode='rectangle',
                                                  hint_text="Enter Old Pin",
                                                  pos_hint={"center_x": 0.28, "center_y": 0.6},
                                                  size_hint=(0.5, None))

        self.enterNewPinTextField = MDTextField(mode='rectangle',
                                                  hint_text="Enter New Pin",
                                                  pos_hint={"center_x": 0.28, "center_y": 0.5},
                                                  size_hint=(0.5, None))


        self.confirmNewPinTextField = MDTextField(mode='rectangle',
                                                  hint_text="Confirm New Pin",
                                                  pos_hint={"center_x": 0.28, "center_y": 0.4},
                                                  size_hint=(0.5, None))

        self.submitButton = CustomButton(text="SUBMIT",
                                          font_size="17sp",
                                          size_hint=(0.3, 0.08),
                                          md_bg_color=(0.996, 0.447, 0.180, 1),
                                          pos_hint={"center_x": 0.835, "center_y": 0.5}
                                          )

        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)
        self.add_widget(self.pinChangeLabel)
        self.add_widget(self.pinChangeStatusLabel)
        self.add_widget(self.enterOldPinTextField)
        self.add_widget(self.enterNewPinTextField)
        self.add_widget(self.confirmNewPinTextField)
        self.add_widget(self.submitButton)
        self.add_widget(self.kbd)


    def keyup(self, kbd, keycode, *args):
        if isinstance(keycode, tuple):
            keycode = keycode[1]
        keyboard.press_and_release(keycode)

    def onHomeButtonPressed(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'