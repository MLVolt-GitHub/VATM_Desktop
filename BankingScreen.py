from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from RequiredFuns import RequiredFuns
from Widgets.CustomButton import CustomButton

class BankingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'banking_screen'

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x":0.89, "center_y":0.83})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.83},
                                       on_press=self.onHomeButtonPressed)

        self.bankingLabel = MDLabel(text="BANKING",
                                   pos_hint={"center_x": 0.5, "center_y": 0.85},
                                   halign="center",
                                   font_style="H5")

        self.requestPassbookButton = CustomButton(text="REQUEST PASSBOOK",
                                          font_size="17sp",
                                          size_hint=(0.3, 0.06),
                                          md_bg_color=(0.996, 0.447, 0.180, 1),
                                          pos_hint={"center_x":0.16, "center_y":0.7},
                                          )

        self.requestCheckbookButton = CustomButton(text="REQUEST CHECKBOOK",
                                          font_size="17sp",
                                          size_hint=(0.3, 0.06),
                                          md_bg_color=(0.996, 0.447, 0.180, 1),
                                          pos_hint={"center_x":0.16, "center_y":0.6},
                                          )

        self.requestNewAtmCardButton = CustomButton(text="REQUEST NEW ATM CARD",
                                       font_size="17sp",
                                       size_hint=(0.3, 0.06),
                                       md_bg_color=(0.996, 0.447, 0.180, 1),
                                       pos_hint={"center_x": 0.16, "center_y": 0.5},
                                       )

        self.updateAdhaarButton = CustomButton(text="UPDATE ADHAAR",
                                       font_size="17sp",
                                       size_hint=(0.3, 0.06),
                                       md_bg_color=(0.996, 0.447, 0.180, 1),
                                       pos_hint={"center_x": 0.84, "center_y": 0.7},
                                       )

        self.requestCreditCardButton = CustomButton(text="REQUEST CREDIT CARD",
                                           font_size="17sp",
                                           size_hint=(0.3, 0.06),
                                           md_bg_color=(0.996, 0.447, 0.180, 1),
                                           pos_hint={"center_x": 0.84, "center_y": 0.6},
                                           )



        self.requestPassbookButton.bind(on_release=self.onRequestPassbookButtonPressed)
        self.requestCheckbookButton.bind(on_release=self.onRequestCheckbookButtonPressed)
        self.requestNewAtmCardButton.bind(on_release=self.onRequestNewAtmCardButtonPressed)
        self.updateAdhaarButton.bind(on_release=self.onUpdateAdhaarButtonPressed)
        self.requestCreditCardButton.bind(on_release=self.onRequestCreditCardButtonPressed)

        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)
        self.add_widget(self.bankingLabel)

        self.add_widget(self.requestPassbookButton)
        self.add_widget(self.requestCheckbookButton)
        self.add_widget(self.requestNewAtmCardButton)
        self.add_widget(self.updateAdhaarButton)
        self.add_widget(self.requestCreditCardButton)

    def onRequestPassbookButtonPressed(self, instance):
        Clock.schedule_once(self.switchToStatusScreen, 0.3)

    def onRequestCheckbookButtonPressed(self, instance):
        Clock.schedule_once(self.switchToStatusScreen, 0.3)

    def onRequestNewAtmCardButtonPressed(self, instance):
        Clock.schedule_once(self.switchToStatusScreen, 0.3)

    def onUpdateAdhaarButtonPressed(self, instance):
        Clock.schedule_once(self.switchToStatusScreen, 0.3)

    def onRequestCreditCardButtonPressed(self, instance):
        Clock.schedule_once(self.switchToStatusScreen, 0.3)


    def switchToStatusScreen(self, dt):
        self.manager.get_screen("status_screen").statusLabel.text="Thanks for your request."
        self.manager.transition.direction = 'left'
        self.manager.current = 'status_screen'
        Clock.schedule_once(self.moveToHome, 3)
        #self.manager.get_screen('status_screen').nextScreen(self.onHomeButtonPressed)

    def onHomeButtonPressed(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'

    def moveToHome(self, dt):
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'