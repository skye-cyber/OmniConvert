from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, RoundedRectangle

class HoverButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.default_color = (0.2, 0.6, 0.8, 1)
        self.hover_color = (0.1, 0.4, 0.6, 1)

        with self.canvas.before:
            self.color_instruction = Color(*self.default_color)
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[20])

        self.bind(pos=self.update_rect, size=self.update_rect)

        # Bind mouse enter and leave events
        self.bind(on_enter=self.on_hover, on_leave=self.on_leave)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def on_hover(self, *args):
        self.color_instruction.rgba = self.hover_color

    def on_leave(self, *args):
        self.color_instruction.rgba = self.default_color

    def on_mouse_enter(self):
        self.dispatch('on_enter')

    def on_mouse_leave(self):
        self.dispatch('on_leave')

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        btn = HoverButton(text='Hover Me!', background_color=(0, 0, 0, 0))
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    MyApp().run()
