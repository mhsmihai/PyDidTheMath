from kivy.app import App
from kivy.app import runTouchApp
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FallOutTransition, WipeTransition
from kivy.uix.textinput import TextInput
import re #cotey
import math


Builder.load_file('./pydidthemath.kv')
Window.size = (550, 350)
Window.minimum_width, Window.minimum_height = Window.size

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.FirstWindow = FirstWindow()
        self.SecondWindow = SecondWindow()
        #self.transition = WipeTransition()
        pass


class FirstWindow(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        # self._keyboard = Window.request_keyboard(self.press, self)
        # self._keyboard.bind(on_key_down=self.press)
    # Sterge ceea ce e pe ecran
    def clear(self):
        self.ids.input_box.text = "0"

    # Sterge ultimul caracter
    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.ids.input_box.text = prev_number

    # Preia valoarea butonului apasat
    def button_value(self, number):
        prev_number = self.ids.input_box.text
        if len(prev_number) > 22:
            return
        if "wrong equation" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"
        
        else:
            self.ids.input_box.text = f"{prev_number}{number}"
        

    # Preia semnele
    def sings(self, sing):
        prev_number = self.ids.input_box.text
        if len(prev_number) > 22:
            return
        self.ids.input_box.text = f"{prev_number}{sing}"

    # Preia valoarea zecimala
    def dot(self):
        prev_number = self.ids.input_box.text
        if len(prev_number) > 22:
            return
        num_list = re.split("\+|\*|-|/|%", prev_number)

        if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/" in prev_number or "%" in prev_number) and "." not in num_list[-1]:
            prev_number = f"{prev_number}."
            self.ids.input_box.text = prev_number

        elif '.' in prev_number:
            pass

        else:
            prev_number = f'{prev_number}.'
            self.ids.input_box.text = prev_number

    # Calculeaza rezultatul
    def results(self):
        prev_number = self.ids.input_box.text
        try:
            result = eval(prev_number)
            result = int(result*1000000)/1000000
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "wrong equation"

    # De la pozitiv la negativ
    def positive_negative(self):
        prev_number = self.ids.input_box.text
        if len(prev_number) > 22:
            return
        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"


class SecondWindow(Screen):
    eval_str = ""
	    # Sterge ceea ce e pe ecran
    def clear(self):
        self.ids.input_box.text = "0"
        self.eval_str = ""

    # Sterge ultimul caracter
    def remove_last(self):
        prev_number = self.ids.input_box.text
        prev_number = prev_number[:-1]
        self.eval_str = self.eval_str[:-1]
        self.ids.input_box.text = prev_number

    # Preia valoarea butonului apasat
    def button_value(self, number):
        prev_number = self.ids.input_box.text
        if len(prev_number) > 22:
            return
        self.eval_str = f"{self.eval_str}{number}"
        # try:
        #     if "math." in number:
        #         number.replace("math.", '')
        # except TypeError:
        #     pass
        if isinstance(number, str):
            if "math." in number:
                number = number.replace("math.", '')
        if "wrong equation" in prev_number:
            prev_number = ''

        if prev_number == '0':
            self.ids.input_box.text = ''
            self.ids.input_box.text = f"{number}"

        else:
            self.ids.input_box.text = f"{prev_number}{number}"

    # Preia semnele
    def sings(self, sing):
        prev_number = self.ids.input_box.text
        if len(prev_number) > 22:
            return
        self.ids.input_box.text = f"{prev_number}{sing}"
        self.eval_str = f"{self.eval_str}{sing}"

    # Preia valoarea zecimala
    def dot(self):
        prev_number = self.ids.input_box.text
        if len(prev_number) > 22:
            return
        num_list = re.split("\+|\*|-|/|%|(|)", prev_number)

        if ("+" in prev_number or "-" in prev_number or "*" in prev_number or "/" in prev_number or "%" in prev_number) and "." not in num_list[-1]:
            prev_number = f"{prev_number}."
            self.eval_str = f"{self.eval_str}."
            self.ids.input_box.text = prev_number

        elif '.' in prev_number:
            pass

        else:
            prev_number = f'{prev_number}.'
            self.eval_str = f"{self.eval_str}."
            self.ids.input_box.text = prev_number

    # Calculeaza rezultatul
    def results(self):
        prev_number = self.ids.input_box.text
        print(self.eval_str)
        try:
            result = eval(self.eval_str)
            result = int(result*1000000)/1000000
            self.ids.input_box.text = str(result)
        except:
            self.ids.input_box.text = "wrong equation"

    # De la pozitiv la negativ
    def positive_negative(self):
        prev_number = self.ids.input_box.text
        if len(prev_number) > 22:
            return
        if "-" in prev_number:
            self.ids.input_box.text = f"{prev_number.replace('-', '')}"
            self.eval_str = f"{self.eval_str.replace('-', '')}"
        else:
            self.ids.input_box.text = f"-{prev_number}"
            self.eval_str = f"-{self.eval_str}"

class PyDidTheMath(App):
    def build(self):
        self.WindowManager = WindowManager()
        return self.WindowManager

if __name__ == "__main__":
    PyDidTheMath().run()