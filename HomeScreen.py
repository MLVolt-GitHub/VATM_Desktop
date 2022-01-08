from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from Widgets.CustomButton import CustomButton
from kivy.clock import Clock
from kivymd.uix.button import MDIconButton

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name='home_screen'

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.6,
            size_hint_y=0.6,
            pos_hint={"center_x":0.5, "center_y":0.5})



        self.fundTransferViaOtpButton = CustomButton(text="Fund Transfer Via Otp",
                                                     font_size="17sp",
                                                     md_bg_color=(0.996, 0.447, 0.180, 1),
                                                     pos_hint={"center_x":0.87, "center_y":0.3},
                                                     )

        self.fundTransferViaOtpButton.bind(on_release=self.onFundTransferViaOtpButtonPressed)

        self.add_widget(self.Vatmlogo)
        self.add_widget(self.fundTransferViaOtpButton)


    def onFundTransferViaOtpButtonPressed(self, instance):
        print("Fund transfer via otp button pressed")
        Clock.schedule_once(self.switchScreen, 0.3)


    def switchScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'otp_send_screen'