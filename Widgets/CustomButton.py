
from kivymd.uix.behaviors import MagicBehavior
from kivymd.uix.button import MDRaisedButton
import threading
from kivy.clock import Clock
import time
class CustomButton(MagicBehavior, MDRaisedButton):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)





    def on_release(self):
        self.grow()








