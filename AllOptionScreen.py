from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton

from Widgets.CustomButton import CustomButton
class AllOptionScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'all_option_screen'

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x":0.5, "center_y":0.83})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.83},
                                       on_press=self.onHomeButtonPressed)

        self.bankingButton = CustomButton(text="BANKING",
                                          font_size="17sp",
                                          size_hint=(0.3, 0.06),
                                          md_bg_color=(0.996, 0.447, 0.180, 1),
                                          pos_hint={"center_x":0.16, "center_y":0.7},
                                          )


        self.rtgsButton = CustomButton(text="RTGS",
                                          font_size="17sp",
                                          size_hint=(0.3, 0.06),
                                          md_bg_color=(0.996, 0.447, 0.180, 1),
                                          pos_hint={"center_x":0.16, "center_y":0.6},
                                          )

        self.pinChangeButton = CustomButton(text="PIN CHANGE",
                                       font_size="17sp",
                                       size_hint=(0.3, 0.06),
                                       md_bg_color=(0.996, 0.447, 0.180, 1),
                                       pos_hint={"center_x": 0.16, "center_y": 0.5},
                                      )

        self.withdrawButton = CustomButton(text="WITHDRAW",
                                       font_size="17sp",
                                       size_hint=(0.3, 0.06),
                                       md_bg_color=(0.996, 0.447, 0.180, 1),
                                       pos_hint={"center_x": 0.84, "center_y": 0.7},
                                       )

        self.benificeryTransferButton = CustomButton(text="BENIFICERY TRANSFER",
                                           font_size="17sp",
                                           size_hint=(0.3, 0.06),
                                           md_bg_color=(0.996, 0.447, 0.180, 1),
                                           pos_hint={"center_x": 0.84, "center_y": 0.6},
                                           )

        self.balanceButton = CustomButton(text="BALANCE",
                                           font_size="17sp",
                                           size_hint=(0.3, 0.06),
                                           md_bg_color=(0.996, 0.447, 0.180, 1),
                                           pos_hint={"center_x": 0.84, "center_y": 0.5},
                                          )

        self.bankingButton.bind(on_release=self.onBankingButtonPressed)
        self.rtgsButton.bind(on_release=self.onRtgsButtonPressed)
        self.pinChangeButton.bind(on_release=self.onPinChangeButtonPressed)
        self.withdrawButton.bind(on_release=self.onWithdrawButtonPressed)
        self.benificeryTransferButton.bind(on_release=self.onBenificeryTransferButtonPressed)
        self.balanceButton.bind(on_release=self.onBalanceButtonPressed)


        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)

        self.add_widget(self.bankingButton)
        self.add_widget(self.rtgsButton)
        self.add_widget(self.pinChangeButton)
        self.add_widget(self.withdrawButton)
        self.add_widget(self.benificeryTransferButton)
        self.add_widget(self.balanceButton)





    def onBankingButtonPressed(self, instance):
        Clock.schedule_once(self.switchToBankingScreen, 0.3)

    def onRtgsButtonPressed(self, instance):
        Clock.schedule_once(self.switchToRtgsScreen, 0.3)

    def onPinChangeButtonPressed(self, instance):
        Clock.schedule_once(self.switchToPinChangeScreen, 0.3)

    def onWithdrawButtonPressed(self, instance):
        Clock.schedule_once(self.switchToWithdrawScreen, 0.3)

    def onBenificeryTransferButtonPressed(self, instance):
        Clock.schedule_once(self.switchToBenificeryTransferScreen, 0.3)

    def onBalanceButtonPressed(self, instance):
        print("Balance Pressed")



    def switchToBankingScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'banking_screen'

    def switchToRtgsScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'rtgs_via_account_no_screen'

    def switchToPinChangeScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'pin_change_screen'

    def switchToWithdrawScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'bank_selection_screen'

    def switchToBenificeryTransferScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'benificery_transfer_screen'



    def onHomeButtonPressed(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'
