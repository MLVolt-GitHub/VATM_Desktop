from datetime import datetime
from kivy.clock import Clock
from kivymd.uix.label import MDLabel
from kivy.uix.relativelayout import RelativeLayout

class CustomClock(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timeLbl = MDLabel(text="9:45",
                               font_style='H2',
                               pos_hint= {"center_x": 0.5, "center_y": 0.5},
                               halign='center',
                               size_hint_x=None,
                               width=600,
                               text_color=(0, 0.823, 0.968, 1),
                               theme_text_color= "Custom")
        self.dateLbl = MDLabel(text="9:45",
                               font_style='Body2',
                               pos_hint={"center_x": 0.5, "center_y": 0.45},
                               halign='center',
                               size_hint_x=None,
                               width=500,
                               text_color = (0, 0.823, 0.968, 1),
                               theme_text_color = "Custom")

        self.add_widget(self.timeLbl)
        self.add_widget(self.dateLbl)
        Clock.schedule_interval(self.ClockUpdate, 1)

    def ClockUpdate(self, dt):
        now = datetime.now()
        current_time = now.strftime('%H:%M:%S')
        current_date = now.strftime('%A, %B, %d, %Y')

        self.timeLbl.text=current_time
        self.dateLbl.text=current_date

