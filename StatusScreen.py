from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivy.clock import Clock

class StatusScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name='status_screen'

        self.Vatmlogo = Image(
            source="Assets/vatm_logo.png",
            size_hint_x=0.2,
            size_hint_y=0.2,
            pos_hint={"center_x": 0.5, "center_y": 0.9})

        self.statusLabel = MDLabel(text="Thanks for your request",
                                   pos_hint={"center_x": 0.5, "center_y": 0.5},
                                   halign="center",
                                   font_style="H4")

        self.add_widget(self.Vatmlogo)
        self.add_widget(self.statusLabel)


    def nextScreen(self, f):
        Clock.schedule_once(f, 3)

