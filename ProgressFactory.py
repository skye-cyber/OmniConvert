from kivy.animation import Animation
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from colors import (Black, Blue, Cyan, Gray, Green, Light_Gray, Magenta,
                    Orange, Purple, Red, Semi_Transparent_White, Transparent,
                    White, Yellow)


class ProgressBundle:
    def __init__(self):
        pass

    def SimpleProgressBar(self, maximum: int = 100):
        self.progress_bar = ProgressBar(maximum)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.progress_bar)

        # Start the progress update every second
        # Update every 0.1 seconds
        Clock.schedule_interval(self.update_progress, 0.01)
        return layout

    def update_progress(self, dt):
        if self.progress_bar.value < self.progress_bar.max:
            self.progress_bar.value += 1  # Increment the progress


class CircularProgress(FloatLayout):
    def __init__(self, **kwargs):
        super(CircularProgress, self).__init__(**kwargs)
        self.progress = 0

        # Create a button to start the animation
        btn = Button(text="Start Progress", size_hint=(
            None, None), size=(200, 50), pos=(100, 100))
        btn.bind(on_press=self.start_progress)
        self.add_widget(btn)

    def start_progress(self, instance):
        self.progress = 0
        # Update every 0.1 seconds
        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        self.progress += 5  # Increase progress
        if self.progress >= 361:
            self.progress = 0  # Reset after full circle
            return False  # Stop the update

        self.canvas.clear()
        with self.canvas:
            Color(0, 1, 0, 1)  # Green color
            # Draw the circular progress
            Ellipse(pos=self.center, size=(100, 100),
                    angle_start=0, angle_end=self.progress)


class LabelProgress:
    def __init__(self, current, maximum, popup: bool = False, callback=None):
        # self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Progress: 0%', markup=True, size_hint=(1, None), color=Yellow, height=40)
        # self.layout.add_widget(self.label)

        if callback and popup:
            pass
        else:
            self.progress = (current/maximum)*100
            self.label.text = f'Progress: [b][color=#FFFF00]{self.progress:.2f}[/color][/b]%'
            callback(item=self.label, log=True, update=True)
        # Clock.schedule_interval(self.update_progress, 0.1)
        self.progress = 0
        # return self.layout


