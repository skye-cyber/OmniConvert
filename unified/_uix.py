from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Canvas, Color, Rectangle, RoundedRectangle
# from main import Main


class UIXBot:
    '''
    Handles all tasks and initializations needed for ui rendering and animation
    and error display
    '''
    def __init__(self):
        # self.iface = Main()
        # self.log = self.check_log()
        pass

    '''def _force_ui_update(self):
        """ This ensures the UI gets updated immediately """
        if hasattr(self, 'lay'):
            # print("Forcing UI update...")
            self.error_box.canvas.ask_update()
        return True  # Returning True to keep the Clock running

    def create_error_box(self):
        print("Create error box")
        self.error_box = FloatLayout()
        with self.error_box.canvas.before:
            # Set the background color (RGBA format)
            Color(0, 0, 0)  # Teal background
            self.rect = Rectangle(size=self.error_box.size,
                                  pos=self.error_box.pos)

            # Update the rectangle size and position when the layout changes
            self.error_box.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        print(f"Updating rectangle: pos={instance.pos}, size={instance.size}")

    def close_popup(self, instance):
        # self.pop.remove_widget()
        self.pop.dismiss()

    def check_log(self):
        if hasattr(self.iface, 'log_layout'):
            # print("Adding layout to the interface...")
            return True

        else:
            print("Error: 'iface' does not have a 'log_layout' attribute.")
            return False'''
