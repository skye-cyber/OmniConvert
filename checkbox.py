from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView


class RadioButtonApp(App):
    def build(self):
        # Create a vertical BoxLayout for the radio buttons
        layout = BoxLayout(orientation="vertical",
                           size_hint_y=None, spacing=10, padding=20)
        layout.bind(minimum_height=layout.setter('height'))  # Bind height for scrolling

        # Create a ScrollView to contain the layout
        scroll_view = ScrollView(size_hint=(1, 1), pos_hint={"x": 0, "y": 0})

        # Label for the radio button group
        layout.add_widget(Label(text='Choose an option:',
                          size_hint_y=None, height=40))

        # Options (Radio Buttons - CheckBox with group)
        for i, option in enumerate(["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6"]):
            option_layout = BoxLayout(
                orientation='horizontal', size_hint_y=None, height=40, spacing=10)
            option_checkbox = CheckBox(group='options')
            option_layout.add_widget(option_checkbox)
            option_layout.add_widget(Label(text=option))
            layout.add_widget(option_layout)
            # Bind each checkbox to the on_checkbox_active method
            option_checkbox.bind(active=self.on_checkbox_active)

        # Add the layout to the scroll view
        scroll_view.add_widget(layout)

        # Create a Popup with the scroll view
        pop = Popup(content=scroll_view, title="Radio Button Popup")
        return pop

    def on_checkbox_active(self, checkbox, value):
        if value:  # if the checkbox is active (checked)
            print(f'{checkbox} is selected {value}')


if __name__ == '__main__':
    RadioButtonApp().run()
