from kivy.metrics import dp
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDFillRoundFlatButton, \
    MDFloatingActionButton, MDIconButton, MDRoundFlatButton, MDRoundFlatIconButton, MDRectangleFlatButton

class MyApp(MDApp):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(10))

        # Create buttons
        layout.add_widget(MDRaisedButton(text="Raised Button", size_hint=(0.5, None), height=dp(50), pos_hint={"center_x": 0.5}))
        layout.add_widget(MDFlatButton(text="Flat Button", size_hint=(0.5, None), height=dp(50), pos_hint={"center_x": 0.5}))
        layout.add_widget(MDFillRoundFlatButton(text="Rounded Flat Button", size_hint=(0.5, None), height=dp(50), pos_hint={"center_x": 0.5}))
        layout.add_widget(MDFloatingActionButton(icon="plus", size_hint=(None, None), size=(dp(56), dp(56)), pos_hint={"center_x": 0.5}))
        layout.add_widget(MDIconButton(icon="camera", size_hint=(None, None), size=(dp(48), dp(48)), pos_hint={"center_x": 0.5}))
        layout.add_widget(MDRoundFlatButton(text="Round Flat Button", size_hint=(0.5, None), height=dp(50), pos_hint={"center_x": 0.5}))
        layout.add_widget(MDRoundFlatIconButton(text="Round Icon Button", icon="email", size_hint=(0.7, None), height=dp(50), pos_hint={"center_x": 0.5}))
        layout.add_widget(MDRectangleFlatButton(text="Rectangle Flat Button", size_hint=(0.5, None), height=dp(50), pos_hint={"center_x": 0.5}))

        return layout

if __name__ == '__main__':
    MyApp().run()
