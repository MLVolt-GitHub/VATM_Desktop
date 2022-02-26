from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.uix.vkeyboard import VKeyboard
import keyboard
from Widgets.CustomButton import CustomButton
from SendOtp import SendOtp
from RequiredFuns import RequiredFuns


class EnterOtpScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'enter_otp_screen'
        self.kbd = VKeyboard(pos_hint={"center_x": 0.5, "center_y": 0.31}, on_key_up=self.keyup)

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x": 0.89, "center_y": 0.83})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.83},
                                       on_press=self.onHomeButtonPressed)

        self.enterOtpLabel = MDLabel(text="ENTER OTP",
                                    pos_hint={"center_x": 0.5, "center_y": 0.85},
                                    halign="center",
                                    font_style="H5")

        self.otpVerificationStatus = MDLabel(text="status",
                                          pos_hint={"center_x": 0.5, "center_y": 0.81},
                                          halign="center",
                                          font_style="Subtitle1")

        self.enterOtpTextField = MDTextField(mode='rectangle',
                                                  hint_text="Enter Your Otp Here",
                                                  pos_hint={"center_x": 0.5, "center_y": 0.65},
                                                  size_hint=(0.5, None)
                                                  )
        self.verifyOtpButton = CustomButton(text="Verify",
                                          font_size="17sp",
                                          size_hint=(0.3, 0.06),
                                          md_bg_color=(0.996, 0.447, 0.180, 1),
                                          pos_hint={"center_x": 0.5, "center_y": 0.55},
                                          )

        self.verifyOtpButton.bind(on_release=self.onVerifyOtpButtonPressed)

        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)
        self.add_widget(self.enterOtpLabel)
        self.add_widget(self.otpVerificationStatus)
        self.add_widget(self.enterOtpTextField)
        self.add_widget(self.verifyOtpButton)
        self.add_widget(self.kbd)

    def keyup(self, kbd, keycode, *args):
        if isinstance(keycode, tuple):
            keycode = keycode[1]
        keyboard.press_and_release(keycode)

    def onVerifyOtpButtonPressed(self, instance):
        enteredOtp = self.enterOtpTextField.text
        if(SendOtp().verifyOtp(enteredOtp)):
            self.otpVerificationStatus.text = "OTP Verified"
            RequiredFuns()._saveToLocalFile(key="verification", value="True")
            Clock.schedule_once(self.switchToAllOptionScreen, 0.3)
        else:
            self.otpVerificationStatus.text = "OTP Not Verified"

            RequiredFuns()._saveToLocalFile(key="verification", value="False")


    def switchToAllOptionScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'all_option_screen'

    def onHomeButtonPressed(self, instance):
        print("Home button pressed")
        self.manager.transition.direction = 'right'
        self.manager.current = 'home_screen'