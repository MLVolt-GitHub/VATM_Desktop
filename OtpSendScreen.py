from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.vkeyboard import VKeyboard
import keyboard

from Widgets.CustomButton import CustomButton


class OtpSendScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'otp_send_screen'
        self.kbd = VKeyboard(pos_hint={"center_x": 0.5, "center_y": 0.21}, on_key_up=self.keyup)


        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x": 0.5, "center_y": 0.9})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.95},
                                       on_press=self.onHomeButtonPressed)

        self.otpSendLabel = MDLabel(text="SEND OTP",
                                        pos_hint={"center_x": 0.5, "center_y": 0.83},
                                        halign="center",
                                        font_style="H5")

        self.otpSendStatusLabel = MDLabel(text="status",
                                         pos_hint={"center_x": 0.5, "center_y": 0.79},
                                         halign="center",
                                         font_style="Subtitle1")

        self.enterMobileNoTextField = MDTextField(mode='rectangle',
                                                hint_text="Enter Your Registered Mobile Number",
                                                pos_hint={"center_x": 0.5, "center_y": 0.6},
                                                size_hint=(0.5, None)
                                                )
        self.sendOtpButton = CustomButton(text="Send",
                                          font_size="17sp",
                                          size_hint=(0.3, 0.06),
                                          md_bg_color=(0.996, 0.447, 0.180, 1),
                                          pos_hint={"center_x": 0.5, "center_y": 0.5}
                                          )

        self.sendOtpButton.bind(on_release=self.onSendOtpButtonPressed)

        self.add_widget(self.kbd)
        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)
        self.add_widget(self.otpSendLabel)
        self.add_widget(self.otpSendStatusLabel)
        self.add_widget(self.enterMobileNoTextField)
        self.add_widget(self.sendOtpButton)

    def keyup(self, kbd, keycode, *args):
        if isinstance(keycode, tuple):
            keycode = keycode[1]
        keyboard.press_and_release(keycode)

    def onSendOtpButtonPressed(self, instance):
        Clock.schedule_once(self.switchToEnterOtpScreen, 0.3)

    def switchToEnterOtpScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'enter_otp_screen'

    def onHomeButtonPressed(self, instance):
        print("home button pressed")
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'