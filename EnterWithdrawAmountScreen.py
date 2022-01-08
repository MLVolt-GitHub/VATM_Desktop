from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from Widgets.CustomButton import CustomButton


class EnterWithdrawAmountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'enter_withdraw_amount_screen'

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x":0.5, "center_y":0.9})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.95},
                                       on_press=self.onHomeButtonPressed)

        self.enterAmountLabel = MDLabel(text="ENTER AMOUNT",
                                        pos_hint={"center_x": 0.5, "center_y": 0.83},
                                        halign="center",
                                        font_style="H5")

        self.amountStatusLabel = MDLabel(text="status",
                                         pos_hint={"center_x": 0.5, "center_y": 0.79},
                                         halign="center",
                                         font_style="Subtitle1")

        self.enterAmountTextField = MDTextField(mode='rectangle',
                                                hint_text="Enter Amount Here",
                                                pos_hint={"center_x": 0.5, "center_y": 0.6},
                                                size_hint=(0.5, None)
                                                )
        self.proceedButton = CustomButton(text="Proceed",
                                           font_size="17sp",
                                           size_hint=(0.3, 0.06),
                                           md_bg_color=(0.996, 0.447, 0.180, 1),
                                           pos_hint={"center_x": 0.5, "center_y": 0.5},
                                           )

        self.proceedButton.bind(on_release=self.onProceedButtonPressed)

        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)
        self.add_widget(self.enterAmountLabel)
        self.add_widget(self.amountStatusLabel)
        self.add_widget(self.enterAmountTextField)
        self.add_widget(self.proceedButton)

    def onProceedButtonPressed(self, instance):
        Clock.schedule_once(self.switchToEnterPinScreen, 0.3)


    def switchToEnterPinScreen(self, dt):
        self.manager.transition.direction = 'left'
        self.manager.current = 'enter_pin_screen'

    def onHomeButtonPressed(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'