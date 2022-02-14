import kivy
import os
kivy.require('1.9.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.config import Config
from kivy.uix.label import Label

Config.set('graphics', 'width', 390)
Config.set('graphics', 'height', 460)
min_width = 390
min_height = 460

##MAIN
class WindowManager(ScreenManager):
    pass

class CalculatorWindow(Screen):
    operationtext = ObjectProperty(None)
    operando1 = ""
    operation = ""
    operando2 = ""

    def calc_operation(self, c):
        self.do_operation(c)
        if c != 'C':
            self.operationtext.text = str(self.operando1) + str(self.operation) + str(self.operando2)

    def do_operation(self, c):
        if self.is_number(c):
            if self.operation ==  "":
                self.operando1 = self.operando1 + c
            else:
                self.operando2 = self.operando2 + c
        else:
            if c == 'C':
                self.operando1 = ""
                self.operationtext.text = "0"
                self.resetValues()
            else:
                if c == '.':
                    if self.operation == '':
                        if len(self.operando1) > 0 and '.' not in self.operando1:
                            self.operando1 = self.operando1 + c
                    else:
                        if len(self.operando2) > 0 and '.' not in self.operando2:
                            self.operando2 = self.operando2 + c
                else:
                    if self.operation != '':
                        self.operando_set()
                    if c != '=':
                        self.operation = c

    def operando_set(self):
        op1 = 0
        if self.operando1 == "":
            self.operando1 = 0
        if self.operando2 == "":
            self.operando2 = 0
        
        #Realizar operación
        if self.operation == '*':
            self.operando1 = str(float(self.operando1) * float(self.operando2))
        if self.operation == '/':
            if float(self.operando1) != 0.0 and float(self.operando2) != 0.0:
                self.operando1 = str(float(self.operando1) / float(self.operando2))
        if self.operation == '-':
            self.operando1 = str(float(self.operando1) - float(self.operando2))
        if self.operation == '+':
            self.operando1 = str(float(self.operando1) + float(self.operando2))
        self.resetValues()

    
    def is_number(self, c) -> bool:
        if c == '0' or c == '1' or c == '2' or c == '3' or c == '4' or c == '5' or c == '6' or c == '7' or c == '8' or c == '9':
            return True
        else:
            return False

    def resetValues(self):
        self.operation = ""
        self.operando2 = ""

class MainApp(App):
    title = "MadiCalculator"
    def build(self):
        PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
        kv = Builder.load_file(PROJECT_DIR + '/layout/layout.kv')

        from kivy.core.window import Window
        Window.minimum_width = min_width
        Window.minimum_height = min_height
        return kv

    def init():
        MainApp().run()

if __name__ == "__main__":
    MainApp.init()