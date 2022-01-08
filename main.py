import threading
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from RtgsScreen import RtgsScreen
from SplashScreen import SplashScreen
from RequiredFunctions import RequiredFunctions
from HomeScreen import HomeScreen
from AllOptionScreen import AllOptionScreen
from BankingScreen import BankingScreen
from StatusScreen import StatusScreen
from BenificeryTransferScreen import BenificeryTransferScreen
from PinChangeScreen import PinChangeScreen
from EnterWithdrawAmountScreen import EnterWithdrawAmountScreen
from EnterPinScreen import EnterPin
from OtpSendScreen import OtpSendScreen
from EnterOtpScreen import EnterOtpScreen


class MyFirstApp(MDApp):
    def build(self):
        try:
            self.sm = ScreenManager()
            self.sm.add_widget(SplashScreen())
            self.sm.add_widget(HomeScreen())
            self.sm.add_widget(OtpSendScreen())
            self.sm.add_widget(EnterOtpScreen())
            self.sm.add_widget(AllOptionScreen())
            self.sm.add_widget(BankingScreen())
            self.sm.add_widget(StatusScreen())
            self.sm.add_widget(RtgsScreen())
            self.sm.add_widget(BenificeryTransferScreen())
            self.sm.add_widget(PinChangeScreen())
            self.sm.add_widget(EnterWithdrawAmountScreen())
            self.sm.add_widget(EnterPin())

            return self.sm
        except Exception as e:
            print(e)
            print("Error in build : MyFirstApp")

    def on_start(self):
        self.sm.current='splash_screen'
        threading.Thread(target=self.verifications).start()


    def verifications(self):
        while(True):
            if(self.sm.get_screen('splash_screen').progress.value==0):
                self.sm.current='splash_screen'
                self.sm.get_screen('splash_screen').checkInternetLbl.text="Checking Internet.."
                if(RequiredFunctions()._checkInternet()):
                    self.sm.get_screen('splash_screen').progress.value=1
                else:
                    self.sm.get_screen('splash_screen').progress.value=0

            elif(self.sm.get_screen('splash_screen').progress.value==1):
                self.sm.get_screen('splash_screen').checkInternetLbl.text = "Internet Available."
                self.sm.current='home_screen'
                break



MyFirstApp().run()
