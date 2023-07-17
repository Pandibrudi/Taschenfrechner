import re
import random
from kivy.core.text import LabelBase
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from frechheiten import frechheiten


class CalculatorGridLayout(GridLayout):
    def calculate_result(self, expression):
        try:
            result = str(eval(expression))
            print(result)
            self.check_if_too_easy(expression)
            
        except:
            result = 'Error'

        self.ids.input_field.text = ""
        self.ids.input_field.text = str(result)

    def button_pressed(self, button):
        button_text = button.text
        current_text = self.ids.input_field.text

        if button_text == '=':
            self.calculate_result(current_text)
        elif button_text == 'C':
            self.ids.input_field.text = ''
        elif button_text == 'DEL':
            self.ids.input_field.text = current_text[:-1]
        else:
            current_text += button_text
            self.ids.input_field.text = current_text
    
    def check_if_too_easy(self, expression):
        regex = r'^(\d+)\s*([+\-*/])\s*(\d+)$'
        match = re.match(regex, expression)

        if match:
            first_number = int(match.group(1))
            operator = match.group(2)
            second_number = int(match.group(3))

            if operator == '+':
                result = first_number + second_number
                self.display_popup(random.choice(frechheiten))
            elif operator == '-':
                result = first_number - second_number
                self.display_popup(random.choice(frechheiten))
            elif operator == '*' and first_number <= 10 and second_number <= 10:
                result = first_number * second_number
                self.display_popup(random.choice(frechheiten))

    def display_popup(self, text):
        LabelBase.register(name='Comic', fn_regular='comic.ttf')

        popup_content = Label(text=text, font_name='Comic', font_size=20, color=(1, 1, 0, 1))

        popup = Popup(title='LOL', content=popup_content, size_hint=(None, None), size=(800, 400),
                    background_color=(0, 1, 1, 1))

        popup.open()

class CalculatorApp(App):
    def build(self):
        self.title = "Taschenfrechner"
        return CalculatorGridLayout()

if __name__ == '__main__':
    CalculatorApp().run()