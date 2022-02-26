from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.vkeyboard import VKeyboard
import keyboard
from Widgets.CustomButton import CustomButton


class ThumbVerificationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'thumb_verification_screen'
        self.kbd = VKeyboard(pos_hint={"center_x": 0.5, "center_y": 0.31}, on_key_up=self.keyup)


        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x": 0.89, "center_y": 0.83})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.83},
                                       on_press=self.onHomeButtonPressed)

        self.thumbVerificationLabel = MDLabel(text="Thumb Verification",
                                        pos_hint={"center_x": 0.5, "center_y": 0.85},
                                        halign="center",
                                        font_style="H5")

        self.thumbVerificationStatusLabel = MDLabel(text="status",
                                         pos_hint={"center_x": 0.5, "center_y": 0.81},
                                         halign="center",
                                         font_style="Subtitle1")

        self.enterUidTextField = MDTextField(mode='rectangle',
                                                hint_text="Enter Your Unique Id",
                                                pos_hint={"center_x": 0.5, "center_y": 0.65},
                                                size_hint=(0.5, None)
                                                )

        self.verifyButton = CustomButton(text="Verify Now",
                                          font_size="17sp",
                                          size_hint=(0.3, 0.06),
                                          md_bg_color=(0.996, 0.447, 0.180, 1),
                                          pos_hint={"center_x": 0.5, "center_y": 0.55}
                                          )


        self.verifyButton.bind(on_release=self.onVerifyButtonPressed)

        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)
        self.add_widget(self.thumbVerificationStatusLabel)
        self.add_widget(self.thumbVerificationLabel)
        self.add_widget(self.enterUidTextField)
        self.add_widget(self.verifyButton)
        self.add_widget(self.kbd)


    def keyup(self, kbd, keycode, *args):
        if isinstance(keycode, tuple):
            keycode = keycode[1]
        keyboard.press_and_release(keycode)

    def onVerifyButtonPressed(self, instance):
        Clock.schedule_once(self.switchToAllOptionScreen, 0.3)



    def onHomeButtonPressed(self, instance):
        print("home button pressed")
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'



    def switchToAllOptionScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'all_option_screen'