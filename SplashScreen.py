import requests
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.label import MDLabel
import threading
class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name='splash_screen'
        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.3,
            size_hint_y=0.3,
            pos_hint={"center_x":0.5, "center_y":0.5})

        self.Svnslogo = Image(
            source="Assets/svns_logo.png",
            size_hint_x=0.1,
            size_hint_y=0.1,
            pos_hint={"center_x": 0.5, "center_y": 0.1})

        self.progress = ProgressBar(max=2,
                                    value=0,
                                    pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                    size_hint=(0.4, 0.1))

        self.checkInternetLbl = MDLabel(text="Checking Internet..",
                                        halign="center",
                                        pos_hint={'center_x': 0.5, 'center_y': 0.37})
        self.verifyingVatmLbl = MDLabel(text="Verifying VATM..",
                                        halign="center",
                                        pos_hint={'center_x': 0.5, 'center_y': 0.33})



        self.add_widget(self.checkInternetLbl)
        self.add_widget(self.verifyingVatmLbl)
        self.add_widget(self.progress)
        self.add_widget(self.Vatmlogo)
        self.add_widget(self.Svnslogo)


