from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalcApp(App):
    # build: Initializes the application, it will be called once
    def build(self):
        # Create App Layout
        body_layout = BoxLayout()
        body_layout.orientation = "vertical"

        self.calc_screen = TextInput()
        self.calc_screen.background_color = "green"
        self.calc_screen.foreground_color = "white"
        self.calc_screen.multiline = False
        self.calc_screen.halign = "right"
        self.calc_screen.font_size = 55
        self.calc_screen.readonly = True
        body_layout.add_widget(self.calc_screen)

        self.operators = ["+", "-", "*", "/"]
        self.last_input_text = ""

        calc_btns = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
            ["="]
        ]
        for row in calc_btns:
            row_layout = BoxLayout()
            for ch in row:
                new_btn = Button()
                new_btn.text = ch
                new_btn.font_size = 30
                new_btn.background_color = "yellow"
                new_btn.pos_hint = {"center_x": 0.5, "center_y": 0.5}
                row_layout.add_widget(new_btn)

                if new_btn.text in self.operators:
                    new_btn.background_color = "cyan"
                elif new_btn.text == "C":
                    new_btn.background_color = "red"

                # Add Events to Buttons
                if new_btn.text == "=":
                    new_btn.bind(on_press=self.handle_equal_pressed)
                    new_btn.background_color = "cyan"
                    new_btn.font_size = 55
                else:
                    new_btn.bind(on_press=self.handle_btn_pressed)

            body_layout.add_widget(row_layout)

        # return the main layout
        return body_layout

    # Handle Events Functions
    def handle_btn_pressed(self, btn_pressed):
        if (btn_pressed.text == "C"):
            self.calc_screen.text = ""
        elif (self.calc_screen.text == "") and (btn_pressed.text in self.operators):
            return
        elif (btn_pressed.text in self.operators) and (self.last_input_text in self.operators):
            return
        else:
            self.calc_screen.text = self.calc_screen.text + btn_pressed.text

        self.last_input_text = btn_pressed.text

    def handle_equal_pressed(self, btn_pressed):
        if (self.calc_screen.text != "") and (self.last_input_text not in self.operators):
            self.calc_screen.text = str(eval(self.calc_screen.text))


if __name__ == "__main__":
    calc_app = CalcApp()
    calc_app.run()
