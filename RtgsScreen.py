from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from Widgets.CustomButton import CustomButton
from kivy.clock import Clock


class RtgsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name='rtgs_screen'

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x":0.5, "center_y":0.9})

        self.homeButton = MDIconButton(icon="Assets/home_icon.png",
                                       pos_hint={"center_x": 0.03, "center_y": 0.95},
                                       on_press=self.onHomeButtonPressed)

        self.rtgsLabel = MDLabel(text="RTGS Transfer",
                                 pos_hint={"center_x": 0.5, "center_y": 0.83},
                                 halign="center",
                                 font_style="H5")

        self.chooseYourMethodLabel = MDLabel(text="Choose Your Transfer Method",
                                            pos_hint={"center_x": 0.5, "center_y": 0.79},
                                            halign="center",
                                            font_style="Subtitle1")

        self.accountNoButton = CustomButton(text="ACCOUNT NO.",
                                            font_size="17sp",
                                            size_hint=(0.3, 0.06),
                                            md_bg_color=(0.996, 0.447, 0.180, 1),
                                            pos_hint={"center_x": 0.16, "center_y": 0.7},
                                            )

        self.upiButton = CustomButton(text="UPI",
                                      font_size="17sp",
                                      size_hint=(0.3, 0.06),
                                      md_bg_color=(0.996, 0.447, 0.180, 1),
                                      pos_hint={"center_x": 0.5, "center_y": 0.7},
                                      )

        self.regMobileNoButton = CustomButton(text="REG. MOBILE NO.",
                                      font_size="17sp",
                                      size_hint=(0.3, 0.06),
                                      md_bg_color=(0.996, 0.447, 0.180, 1),
                                      pos_hint={"center_x": 0.84, "center_y": 0.7},
                                      )

        self.accountNoButton.bind(on_release=self.onAccountNoButtonPressed)
        self.upiButton.bind(on_release=self.onUpiButtonPressed)
        self.regMobileNoButton.bind(on_release=self.onRegMobileNoButtonPressed)



        self.add_widget(self.Vatmlogo)
        self.add_widget(self.homeButton)
        self.add_widget(self.rtgsLabel)
        self.add_widget(self.chooseYourMethodLabel)

        self.add_widget(self.accountNoButton)
        self.add_widget(self.upiButton)
        self.add_widget(self.regMobileNoButton)



    def onAccountNoButtonPressed(self, instance):
        self.upiButton.md_bg_color = (0.996, 0.447, 0.180, 1)
        self.accountNoButton.md_bg_color = (0, 0, 1, 1)
        self.regMobileNoButton.md_bg_color = (0.996, 0.447, 0.180, 1)

    def onUpiButtonPressed(self, instance):
        self.upiButton.md_bg_color=(0, 0, 1, 1)
        self.accountNoButton.md_bg_color=(0.996, 0.447, 0.180, 1)
        self.regMobileNoButton.md_bg_color=(0.996, 0.447, 0.180, 1)

    def onRegMobileNoButtonPressed(self, instance):
        self.upiButton.md_bg_color=(0.996, 0.447, 0.180, 1)
        self.accountNoButton.md_bg_color=(0.996, 0.447, 0.180, 1)
        self.regMobileNoButton.md_bg_color=(0, 0, 1, 1)


    def onHomeButtonPressed(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current='home_screen'

