# import importlib
import os
import threading
from colors import (
    Black,
    Blue,
    Cyan,
    # Gray,
    Green,
    # Light_Gray,
    # Magenta,
    # Orange,
    # Purple,
    # Red,
    # Semi_Transparent_White,
    # Transparent,
    # White,
    Yellow,
)
from formats import (
    SUPPORTED_AUDIO_FORMATS_INPUT,
    SUPPORTED_AUDIO_FORMATS_OUTPUT,
    SUPPORTED_IMAGE_FORMATS,
    SUPPORTED_VIDEO_FORMATS,
)
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.app import MDApp
from kivy.metrics import dp
from kivy.clock import Clock
from kivymd.uix.button import (
    MDRaisedButton,
    MDFlatButton,
    MDFillRoundFlatButton,
    MDFloatingActionButton,
    MDIconButton,
    MDRoundFlatButton,
    MDRoundFlatIconButton,
    MDRectangleFlatIconButton,
    MDFloatingActionButtonSpeedDial,
)
from kivymd.uix.button import MDTextButton
from kivy.core.window import Window
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Canvas, Color, Rectangle, RoundedRectangle, texture
from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.spinner import Spinner
from kivy.uix.treeview import TreeView, TreeViewLabel
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.card import MDCard
from kivy.uix.progressbar import ProgressBar
from kivymd.uix.progressbar import MDProgressBar
from kivy.uix.textinput import TextInput
import numpy as np

_filters = [None]


class Main(BoxLayout, MDScreen):  # Using FloatLayout for free positioning
    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.orientation = "vertical"
        # Initialize FBot with the current instance of Main
        from omniConverters import (
            AudioConverter,
            FileConverter,
            TextToSpeechConverter,
            ImageConverter,
            FileScanner,
            VideoConverter,
        )

        self.FileConverter = FileConverter
        self.TextToSpeechConverter = TextToSpeechConverter
        self.FileScanner = FileScanner
        self.AudioConverter = AudioConverter
        self.VideoConverter = VideoConverter
        self.ImageConverter = ImageConverter
        self.popup_active = False  # Initialize a flag for popup state content
        self.bg_buttons = os.listdir("../src/")

        # Define themes
        self.set_theme()

        # Kepp updating font_size
        Clock.schedule_interval(lambda dt: self.adjust_font_size(), 1.0)

        # call top nav
        self.top_nav()
        # call Accordion nav
        self.accordion_nav()

        # Initial button color (e.g., light blue)
        self.bt_default_color = (0.2, 0.6, 0.8, 1)
        # Color when button is clicked (e.g., darker blue)
        self.bt_pressed_color = (0.1, 0.4, 0.6, 1)

        # Label to content area selected file
        self.progress_label = Label(
            text="Progress: 0%",
            size_hint=(1, 0.9),
            pos_hint={"center_x": 0.5, "y": 0.1},
        )

        # Reset cursor when app completes loading
        Window.set_system_cursor("arrow")

    def set_theme(self):
        # Primary Palettes:
        # self.theme_cls.primary_palette = "Red"
        # self.theme_cls.primary_palette = "Pink"
        # self.theme_cls.primary_palette = "Purple"
        # self.theme_cls.primary_palette = "DeepPurple"
        # self.theme_cls.primary_palette = "Indigo"
        # self.theme_cls.primary_palette = "Blue"
        # self.theme_cls.primary_palette = "LightBlue"
        # self.theme_cls.primary_palette = "Cyan"
        # self.theme_cls.primary_palette = "Teal"
        # self.theme_cls.primary_palette = "Green"
        # self.theme_cls.primary_palette = "LightGreen"
        # self.theme_cls.primary_palette = "Lime"
        # self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_palette = "Pink"
        # self.theme_cls.primary_palette = "Amber"
        ''''# self.theme_cls.primary_palette = "Orange"
        # self.theme_cls.primary_palette = "DeepOrange"
        # self.theme_cls.primary_palette = "Gray"
        # self.theme_cls.primary_palette = "BlueGray"'''

        # Accent Palettes:
        # self.theme_cls.accent_palette = "Red"
        # self.theme_cls.accent_palette = "Pink"
        self.theme_cls.accent_palette = "DeepOrange"

        # Available primary_hue Options for primary_hue
        self.theme_cls.primary_hue = "50"  # Very light shade
        self.theme_cls.primary_hue = "100"
        self.theme_cls.primary_hue = "200"
        self.theme_cls.primary_hue = "300"
        self.theme_cls.primary_hue = "400"
        self.theme_cls.primary_hue = "500"  # Default, more balanced color
        self.theme_cls.primary_hue = "600"
        self.theme_cls.primary_hue = "700"
        self.theme_cls.primary_hue = "800"
        self.theme_cls.primary_hue = "900"  # Darkest shade

    def get_pa_color(self, name, _type: bool = True):
        p_colors = {
            "Red": self.theme_cls.primary_palette,
            "Pink": self.theme_cls.primary_palette,
            "Purple": self.theme_cls.primary_palette,
            "DeepPurple": self.theme_cls.primary_palette,
            "Indigo": self.theme_cls.primary_palette,
            "Blue": self.theme_cls.primary_palette,
            "LightBlue": self.theme_cls.primary_palette,
            "Cyan": self.theme_cls.primary_palette,
            "Teal": self.theme_cls.primary_palette,
            "Green": self.theme_cls.primary_palette,
            "LightGreen": self.theme_cls.primary_palette,
            "Lime": self.theme_cls.primary_palette,
            "Yellow": self.theme_cls.primary_palette,
            "Amber": self.theme_cls.primary_palette,
            "Orange": self.theme_cls.primary_palette,
            "DeepOrange": self.theme_cls.primary_palette,
            "Brown": self.theme_cls.primary_palette,
            "Gray": self.theme_cls.primary_palette,
            "BlueGray": self.theme_cls.primary_palette,
        }

        a_color = {
            "Red": self.theme_cls.accent_palette,
            "Pink": self.theme_cls.accent_palette,
            "Purple": self.theme_cls.accent_palette,
            "DeepPurple": self.theme_cls.accent_palette,
            "Indigo": self.theme_cls.accent_palette,
            "Blue": self.theme_cls.accent_palette,
            "LightBlue": self.theme_cls.accent_palette,
            "Cyan": self.theme_cls.accent_palette,
            "Teal": self.theme_cls.accent_palette,
            "Green": self.theme_cls.accent_palette,
            "LightGreen": self.theme_cls.accent_palette,
            "Lime": self.theme_cls.accent_palette,
            "Yellow": self.theme_cls.accent_palette,
            "Amber": self.theme_cls.accent_palette,
            "Orange": self.theme_cls.accent_palette,
            "DeepOrange": self.theme_cls.accent_palette,
        }

        return p_colors.get(name) if _type else a_color.get(name)

    def filter_mapper(self, obj):
        """
        Args:
        obj -> the filter category ie(doc_filter_map, video_filter_map, audio_filter_map, image_filter_map) that the method is expected to return
            It acts like get request, returning only the requested resource.
        Returns:
        dict(obj)
        """
        self.doc_filter_map = {
            "xls": ["*.xlsx", "*.xls"],
            "text": ["*.txt"],
            "csv": ["*.csv"],
            "docx": ["*.doc", "*.docx"],
            "pdf": ["*.pdf"],
            "pptx": ["*.ppt", "*.pptx"],
        }

        self.audio_filter_map = {
            val.lower(): [f"*.{val.lower()}"] for val in SUPPORTED_AUDIO_FORMATS_INPUT
        }
        self.video_filter_map = {
            val.lower(): [f"*.{val.lower()}"] for val in SUPPORTED_VIDEO_FORMATS
        }
        self.image_filter_map = {
            val.lower(): [f"*.{val.lower()}"]
            for val in SUPPORTED_IMAGE_FORMATS.values()
        }

        check = {
            "doc_filter_map": self.doc_filter_map,
            "audio_filter_map": self.audio_filter_map,
            "video_filter_map": self.video_filter_map,
            "image_filter_map": self.image_filter_map,
        }
        print(obj, check.get(obj))
        return check.get(obj)

    def method_mapper(self, res):
        """
        Args:
         res -> the filter category ie(doc_method_map, video_method_map, audio_method_map, image_method_map) that the method is expected to return
            It acts like get request, returning only the requested resource.
        Returns:
        dict(res)
        """
        # create dictionary for maping file conversion to respective method
        self.doc_method_map = {
            "xls": {
                "csv": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).convert_xls_to_csv,
                "audio": self.TextToSpeechConverter(
                    self.IEHandler, self.add_log_label
                ).audiofy,
                "docx": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).convert_xls_to_word,
            },
            "csv": {
                "xls": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).convert_csv_to_xls
            },
            "docx": {
                "text": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).convert_word_to_text,
                "pdf": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).convert_word_to_pdf,
                "audio": self.TextToSpeechConverter(
                    self.IEHandler, self.add_log_label
                ).audiofy,
                "pptx": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).word_to_pptx,
            },
            "pdf": {
                "text": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).convert_pdf_to_text,
                "word": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).convert_pdf_to_word,
                "audio": self.TextToSpeechConverter(
                    self.IEHandler, self.add_log_label
                ).audiofy,
                "image": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).pdf2image,
            },
            "text": {
                "audio": self.TextToSpeechConverter(
                    self.IEHandler, self.add_log_label
                ).audiofy,
                "pdf": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).txt_to_pdf,
                "docx": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).text_to_word,
            },
            "pptx": {
                "text": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).pptx_to_txt,
                "docx": self.FileConverter(
                    self.IEHandler, self.add_log_label
                ).ppt_to_word,
            },
        }

        self.scanner = {
            "pdf": {
                "LongImage": self.FileScanner(
                    self.IEHandler, self.add_log_label
                ).scanAsLongImg,
            }
        }

        # Initialize the nested dictionary
        self.audio_method_map = {}
        for input_format in SUPPORTED_AUDIO_FORMATS_INPUT:
            self.audio_method_map[input_format] = {}  # Inner dict for each input format
            for output_format in SUPPORTED_AUDIO_FORMATS_OUTPUT:
                if input_format != output_format:
                    self.audio_method_map[input_format.lower()][
                        output_format.lower()
                    ] = self.AudioConverter(
                        self.IEHandler, self.add_log_label
                    ).pydub_conv

        # Initialize the nested dictionary
        self.video_method_map = {}
        for key in SUPPORTED_VIDEO_FORMATS:
            # Create a dictionary for each key that contains all other values
            self.video_method_map[key.lower()] = {
                other_key.lower(): self.VideoConverter(
                    self.IEHandler, self.ProgressDisplay
                ).CONVERT_VIDEO
                for other_key in SUPPORTED_VIDEO_FORMATS
                if other_key != key
            }

        # Initialize the nested dictionary
        self.image_method_map = {}
        for key in SUPPORTED_IMAGE_FORMATS:
            # Create a dictionary for each key that contains all other values
            self.image_method_map[key.lower()] = {
                other_key: self.ImageConverter(
                    self.IEHandler, self.add_log_label
                ).convert_image
                for other_key in SUPPORTED_IMAGE_FORMATS
                if other_key != key
            }

        check = {
            "doc_method_map": self.doc_method_map,
            "audio_method_map": self.audio_method_map,
            "video_method_map": self.video_method_map,
            "image_method_map": self.image_method_map,
        }

        return check.get(res)

    def constructor(self, instance, text):
        self.opt_popup = Popup(
            title="Select file type to convert",
            size_hint_y=None,
            size_hint=(None, None),
            size=(400, 400),
        )
        tree_view = TreeView(hide_root=True)
        S_view = ScrollView(
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
            do_scroll_x=False,
            do_scroll_y=True,
        )

        try:
            self.op_type = text

            if text == "Document":
                node = tree_view.add_node(TreeViewLabel(text=text))
                for label in self.method_mapper("doc_method_map").keys():
                    child = tree_view.add_node(TreeViewLabel(text=label), node)
                    child.bind(on_touch_down=self.target_constructor)
                self.terminal_layout.add_widget(
                    Label(
                        text=f"selected {text}",
                        size_hint_y=None,
                        color=Green,
                        height=40,
                    )
                )

            elif text == "Video":
                node = tree_view.add_node(TreeViewLabel(text=text))
                for label in self.method_mapper("video_method_map").keys():
                    child = tree_view.add_node(TreeViewLabel(text=label.lower()), node)
                    child.bind(on_touch_down=self.target_constructor)
                self.terminal_layout.add_widget(
                    Label(
                        text=f"selected {text}",
                        size_hint_y=None,
                        color=Green,
                        height=40,
                    )
                )

            elif text == "Audio":
                node = tree_view.add_node(TreeViewLabel(text=text))
                for label in self.method_mapper("audio_method_map").keys():
                    child = tree_view.add_node(TreeViewLabel(text=label.lower()), node)
                    child.bind(on_touch_down=self.target_constructor)
                self.terminal_layout.add_widget(
                    Label(
                        text=f"selected {text}",
                        size_hint_y=None,
                        color=Green,
                        height=40,
                    )
                )

            elif text == "Image":
                node = tree_view.add_node(TreeViewLabel(text=text))
                for label in self.method_mapper("image_method_map").keys():
                    child = tree_view.add_node(TreeViewLabel(text=label.lower()), node)
                    child.bind(on_touch_down=self.target_constructor)
                self.terminal_layout.add_widget(
                    Label(
                        text=f"selected {text}",
                        size_hint_y=None,
                        color=Green,
                        height=40,
                    )
                )

            elif text == "OCR":
                node = tree_view.add_node(TreeViewLabel(text=text))
                for label in self.method_mapper("doc_method_map").keys():
                    child = tree_view.add_node(TreeViewLabel(text=label.lower()), node)
                    child.bind(on_touch_down=self.target_constructor)
                self.terminal_layout.add_widget(
                    Label(
                        text=f"selected {text}",
                        size_hint_y=None,
                        color=Green,
                        height=40,
                    )
                )

        except AttributeError:
            self.terminal_layout.add_widget(
                Label(
                    text=f"Target format {text}",
                    size_hint_y=None,
                    color=Green,
                    height=40,
                )
            )
        finally:
            S_view.add_widget(tree_view)
            self.opt_popup.content = S_view
            # Bind the size of the tree_view to dynamically update popup size
            tree_view.bind(minimum_height=tree_view.setter("height"))

            # Set popup height to tree_view height dynamically
            def update_popup_size(*args):
                # Set the popup height to the tree_view's height, but limit it to a max of 400
                content_height = tree_view.height + 30  # Extra space for padding
                self.opt_popup.height = min(max(400, content_height), Window.size[1])
                print(
                    f"Content: {content_height - 30} -> popup:{self.opt_popup.height} window_height: {Window.size[1]}"
                )

            self.opt_popup.open()
            # Adjust height as nodes are added
            tree_view.bind(minimum_height=update_popup_size)

    def target_constructor(self, instance, touch):
        self.opt_popup.dismiss()
        self.target_opt_popup = Popup(
            title="Select target format",
            size_hint_y=None,
            size_hint=(None, None),
            size=(400, 400),
        )
        tree_view = TreeView(hide_root=True)
        S_view = ScrollView(
            size_hint=(1, 1),
            pos_hint={"x": 0, "y": 0},
            do_scroll_x=False,
            do_scroll_y=True,
        )

        try:
            self._from = instance.text
            op_method_mapper = {
                "Document": "doc_method_map",
                "Video": "video_method_map",
                "Audio": "audio_method_map",
                "Image": "image_method_map",
            }

            self.target_format = self.method_mapper(
                op_method_mapper.get(self.op_type)
            ).get(instance.text.lower())

            node = tree_view.add_node(
                TreeViewLabel(text=f"Convert: {instance.text} to ??")
            )

            for label in self.target_format.keys():
                child = tree_view.add_node(TreeViewLabel(text=label), node)
                child.bind(on_touch_down=self.on_node_select)
            self.operation = Label(
                text=f"Convert from: {instance.text}",
                size_hint_y=None,
                color=Green,
                height=40,
            )
            self.terminal_layout.add_widget(self.operation)

        except AttributeError:
            self.terminal_layout.add_widget(
                Label(text="Target format ???", size_hint_y=None, color=Blue, height=40)
            )
        finally:
            S_view.add_widget(tree_view)
            self.target_opt_popup.content = S_view
            # Bind the size of the tree_view to dynamically update popup size
            tree_view.bind(minimum_height=tree_view.setter("height"))

            # Set popup height to tree_view height dynamically
            def update_popup_size(*args):
                # Set the popup height to the tree_view's height, but limit it to a max of 400
                content_height = tree_view.height + 30  # Extra space for padding
                self.target_opt_popup.height = min(
                    max(400, content_height), Window.size[1]
                )
                # print(f"Content: {content_height - 30} -> popup:{self.target_opt_popup.height} window_size: {Window.size[1]}")

            self.target_opt_popup.open()
            # Adjust height as nodes are added
            tree_view.bind(minimum_height=update_popup_size)

    def on_node_select(self, instance, touch):
        global _filters
        op_mapper = {
            "Document": "doc_filter_map",
            "Video": "video_filter_map",
            "Audio": "audio_filter_map",
            "Image": "image_filter_map",
        }

        _filters = self.filter_mapper(op_mapper.get(self.op_type)).get(self._from)

        self.target_opt_popup.dismiss()
        self.output_format = instance.text.lower()
        print(f"Target format: {instance.text}")
        print(f"Target method:  {self.target_format.get(instance.text)}")
        # init.get(self.op_type)()  #= init.get(self.op_type)()
        if self.op_type != "Document":
            print("Not a Document")
            self.show_filechooser(
                callback=lambda file, output_format: self.target_format.get(
                    instance.text.lower()
                )(file, output_format)
            )
        else:
            self.show_filechooser(
                callback=lambda file: self.target_format.get(instance.text.lower())(
                    file
                )
            )

        self.operation.text = f"{self.operation.text} to {instance.text.lower()}"
        if instance.collide_point(*touch.pos):
            print(f"Node {instance.text} selected")

    def IEHandler(
        self,
        item,
        error: bool = False,
        log: bool = False,
        progress: bool = True,
        update: bool = False,
        _max: int = None,
        current: int = None,
        progress_type: str = "label",
    ):
        if progress and update and item is not None:
            text = item.text
            self.update_ui(text, update=True)
            # print(self.progress_label.text)
        elif log and item is not None:
            Clock.schedule_once(lambda dt: self.update_ui(item, add=True))
        elif progress:
            if _max is None or current is None:
                print("[WARNING]:\t_max and current must be valid intengers")
            else:
                if progress_type == "label":
                    # Update label with progress
                    from ProgressFactory import LabelProgress

                    LabelProgress(
                        current=current, maximum=_max, callback=self.IEHandler
                    )
                    # progress_text = f"Progress: {(current/_max)*100:.2f}%"
                    # Clock.schedule_once(lambda dt: self.update_ui(progress_text, update=True))
        elif error:
            self.create_error_box()
            self.error_box.add_widget(item)

    def update_ui(self, obj, update: bool = False, add: bool = False):
        if update:
            self.progress_label.text = str(obj)
        elif add:
            self.terminal_layout.add_widget(obj)

    def add_log_label(self):
        self.progress_label = MDLabel(
            text="Progress: [b]0%[/b]",
            markup=True,
            halign="center",
            size_hint=(1, None),
            text_color=Yellow,
            height=40,
        )
        self.terminal_layout.add_widget(self.progress_label)

    def ProgressDisplay(self, update=False, _type="circular", progress=0, _label=False):
        if not update:
            if _label:
                self.add_log_label()
            if _type == "simple":
                self.progress_bar = ProgressBar(
                    max=100,
                    value=0,
                    size_hint=(1, None),
                    height=40,
                )
            if _type == "circular":
                self.progress_bar = MDProgressBar(
                    max=100, size_hint=(1, None), size=(100, 100), value=0
                )
            self.terminal_layout.add_widget(self.progress_bar)  # Add the progress bar
        else:
            self.progress_label.text = f"Progress: [b]{int(progress)}%[/b]"
            self.progress_bar.value = progress

    def create_error_box(self):
        self.error_box = FloatLayout()
        with self.error_box.canvas.before:
            # Set the background color (RGBA format)
            Color(0.5, 0.5, 0.5)  # Teal background
            self.rect = Rectangle(
                size=self.update_error_box.size, pos=self.update_error_box.pos
            )
        self.terminal_layout.add_widget(self.error_box)

    def update_error_box(self, instance):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        print(f"Updating rectangle: pos={instance.pos}, size={instance.size}")

    def top_nav(self):
        # Create top navigation bar (MDTopAppBar)
        top_bar = MDTopAppBar(
            title="FileConverter",  # No title
            elevation=10,  # Shadow for depth
            md_bg_color=self.theme_cls.primary_color,
        )

        # Create a BoxLayout to hold the buttons and spinner inline
        top_layout = BoxLayout(
            orientation="horizontal",
            padding=[dp(4), dp(4), dp(4), dp(7)],
            spacing=dp(10),
        )

        # Home Button (Left side)
        home_button = MDIconButton(
            icon="home",  # Icon for Home
            on_release=self.open_home_accordion,
        )

        # Conversion Spinner (Center)
        self.conversion_spinner = Spinner(
            text="Conversion",  # Default text
            values=(
                "Document",
                "Video",
                "Audio",
                "Image",
                "OCR",
                "Scanning",
            ),  # Spinner options
            size_hint=(None, None),
            size=(dp(150), dp(40)),
            # Optional: Set spinner background color
            background_color=(0.1, 0.5, 0.6, 1),
        )
        self.conversion_spinner.bind(text=self.constructor)

        # Settings Button (Right side)
        settings_button = MDIconButton(
            icon="cog",  # Icon for Settings
            on_release=self.open_settings,
        )

        # Add home button, conversion spinner, and settings button inline
        top_layout.add_widget(home_button)
        top_layout.add_widget(self.conversion_spinner)
        top_layout.add_widget(settings_button)

        # Anchor Layout to center the items in the toolbar
        anchor_layout = AnchorLayout(anchor_x="center")
        anchor_layout.add_widget(top_layout)

        # Add the custom layout to the top bar
        top_bar.add_widget(anchor_layout)

        # Add buttons for the conversion options (assuming show_filechooser is defined)
        # self.options.bind(text=self.control)

        """self.select_file = Button(
            text='Select File', font_size=16, background_color=(0.2, 1, 0.86, 1))
        navbar.add_widget(self.select_file)
        self.select_file.bind(on_press=self.show_filechooser)

        self.display = Button(text='Open File', font_size=16,
                              background_color=(0.2, 3, 0.86, 1))
        navbar.add_widget(self.display)
        self.display.bind(on_press=self.show_filechooser)"""

        self.add_widget(top_bar)

    def accordion_nav(self):
        # Create a FloatLayout for free positioning
        float_layout = FloatLayout()

        # Background image for the overall layout (if needed)
        background = Image(
            source="../src/images/156776-colorfulness-eye-purple-art-gas-1920x1080.jpg",
            allow_stretch=True,
            keep_ratio=False,
        )
        float_layout.add_widget(background)

        # Creating accordion navigation menu
        self.accordion = Accordion(
            size_hint=(1, 1), height=500, pos_hint={"center_x": 0.5, "y": 0}
        )

        # .....................................................................#
        # Create home with unique Background
        self.home = AccordionItem(title="Home", size_hint=(1, 1))
        home_float_layout = FloatLayout()
        home_background = Image(
            source="../src/images/150931-psychedelic-art-green-pattern-purple-fractal-1920x1080.jpg",
            allow_stretch=True,
            keep_ratio=False,
        )
        home_float_layout.add_widget(home_background)

        # Create a ScrollView for the home section
        home_scroll = MDScrollView(size_hint=(1, 1), pos_hint={"x": 0, "y": 0})

        # Create a GridLayout for log items, size_hint_y=None allows it to expand dynamically
        # Add items to home
        self.home_layout = GridLayout(
            cols=1,
            size_hint_y=None,
            pos_hint={"center_x": 0, "y": 0},
            padding=10,
            spacing=2,
        )
        self.home_layout.bind(
            minimum_height=self.home_layout.setter("height")
        )  # Bind height for scrolling

        # Add the home layout to a ScrollView

        # Add log items dynamically (as an example)

        # Add the GridLayout to the ScrollView
        home_scroll.add_widget(self.home_layout)

        # Add ScrollView to the FloatLayout
        home_float_layout.add_widget(home_scroll)

        # Add FloatLayout to the home AccordionItem
        self.home.add_widget(home_float_layout)

        # Add home AccordionItem to the accordion
        self.accordion.add_widget(self.home)

        # .....................................................................#
        # Create conversion with unique background
        self.conversion = AccordionItem(title="Conversion", size_hint=(1, 1))
        conversion_float_layout = FloatLayout()
        conversion_background = Image(
            source="../src/images/156776-colorfulness-eye-purple-art-gas-1920x1080.jpg",
            allow_stretch=True,
            keep_ratio=False,
        )
        conversion_float_layout.add_widget(conversion_background)

        # Create a ScrollView for the conversion section
        conversion_scroll = MDScrollView(size_hint=(1, 1), pos_hint={"x": 0, "y": 0})

        # Create a GridLayout for log items, size_hint_y=None allows it to expand dynamically
        self.conversion_layout = GridLayout(
            cols=3, size_hint_y=None, padding=10, size_hint=(1, 0.5), spacing=10
        )
        self.conversion_layout.bind(
            minimum_height=self.conversion_layout.setter("height")
        )

        conversion_card = MDCard(
            orientation="vertical",
            size_hint=(0.9, 0.4),
            pos_hint={"center_x": 0.5, "y": 0.1},
            elevation=10,
            ripple_behavior=True,
        )

        # Add log items dynamically (as an example)
        card_grid = GridLayout(
            cols=3, size_hint_y=None, padding=10, size_hint=(1, 0.5), spacing=10
        )
        card_grid.bind(minimum_height=card_grid.setter("height"))
        for item in self.filter_mapper("doc_filter_map").keys():
            conv_button = MDRectangleFlatIconButton(
                icon="swap-horizontal",
                text=item,
                # bold=True,
                text_color=Black,
                height=dp(50),
                size_hint=(0.5, None),
                md_bg_color=Cyan,
            )
            card_grid.add_widget(conv_button)
        conversion_card.add_widget(card_grid)
        self.conversion_layout.add_widget(conversion_card)
        # conv_button.bind(on_release=self)

        self.label = Label(
            text="No file Selected",
            size_hint=(1, None),
            pos_hint={"center_x": 0.5, "y": 0.1},
        )

        # Add the GridLayout to the ScrollView
        conversion_scroll.add_widget(self.conversion_layout)

        # Add ScrollView to the FloatLayout
        conversion_float_layout.add_widget(conversion_scroll)

        # Add FloatLayout to the conversion AccordionItem
        self.conversion.add_widget(conversion_float_layout)

        # self.conversion_layout.add_widget(self.label)

        # Add conversion AccordionItem to the accordion
        self.accordion.add_widget(self.conversion)

        # Add terminal to Accordion
        self.add_widget(self.createTerminal())

    def createTerminal(self):
        self.terminal = AccordionItem(title="Terminal", size_hint=(1, 1))
        self.terminal_float_layout = FloatLayout(size_hint=(1, 1))
        self.terminal_scroll_view = MDScrollView(
            size_hint=(1, 1), pos_hint={"x": 0, "y": 0}
        )
        self.terminal_layout = GridLayout(
            cols=1, size_hint_y=None, padding=2, spacing=2
        )
        self.terminal_layout.bind(minimum_height=self.terminal_layout.setter("height"))
        self.gradient_texture = (
            self._create_gradient_texture()
        )  # place holder, remove or implement.

        with self.terminal_float_layout.canvas.before:
            Color(0, 0, 0, 1)  # black background
            self.rect = Rectangle(
                size=self.terminal_float_layout.size, pos=self.terminal_float_layout.pos
            )

        self.terminal_float_layout.bind(
            size=self._update_terminal_rect, pos=self._update_terminal_rect
        )
        self.terminal_float_layout.add_widget(self.terminal_scroll_view)
        self.terminal_scroll_view.add_widget(self.terminal_layout)
        self.terminal.add_widget(self.terminal_float_layout)
        self.accordion.add_widget(self.terminal)

        float_layout = FloatLayout()
        float_layout.add_widget(self.accordion)
        self.add_terminal_text()
        return float_layout

    def add_terminal_text(self):
        self.terminal_input = TerminalInput(
            font_name="FreeMono",
            padding=10,
            multiline=True,
            cursor_color=(1, 1, 1, 1),  # White cursor
            foreground_color=(0, 1, 0, 1),  # Green text
            background_color=(1, 1, 1, 1),  # Black background
            size_hint_y=None,
            height=100,  # Initial height
        )

        self.terminal_layout.add_widget(self.terminal_input)

    def open_home_accordion(self, instance):
        self.home.collapse = False
        self.conversion.collapse = True
        self.terminal.collapse = True

    def open_conversion_accordion(self, instance):
        self.home.collapse = True
        self.conversion.collapse = False
        self.terminal.collapse = True

    def open_log_accordion(self, instance):
        self.home.collapse = True
        self.conversion.collapse = True
        self.terminal.collapse = False

    def open_settings(self, instance):
        pass

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) / 255.0 for i in (0, 2, 4))

    def _update_terminal_rect(self, instance, value):
        num_steps = 300
        # Choose a palette (e.g., Indigo)
        start_hex = "#0c0a19"
        end_hex = "#020204"

        start_color = self.hex_to_rgb(start_hex)
        end_color = self.hex_to_rgb(end_hex)

        def interpolate_color(start, end, fraction):
            return (
                start[0] + (end[0] - start[0]) * fraction,
                start[1] + (end[1] - start[1]) * fraction,
                start[2] + (end[2] - start[2]) * fraction,
                1,  # Alpha (opacity)
            )

        instance.canvas.before.clear()
        with instance.canvas.before:
            for i in range(num_steps):
                fraction = i / (num_steps - 1)  # Calculate fraction
                color = interpolate_color(start_color, end_color, fraction)
                Color(*color)
                Rectangle(
                    pos=(
                        instance.pos[0],
                        instance.pos[1] + (instance.size[1] / num_steps) * i,
                    ),
                    size=(instance.size[0], instance.size[1] / num_steps),
                )

    def _create_gradient_texture(self):
        """Generates a vertical gradient texture."""
        width, height = 1, 64  # Small width, tall height for efficiency
        data = np.zeros((height, width, 3), dtype=np.uint8)

        # Define gradient colors
        start_color = np.array([51, 102, 204])  # RGB (0.2, 0.4, 0.8) in 255 scale
        end_color = np.array([204, 51, 153])  # RGB (0.8, 0.2, 0.6) in 255 scale

        # Fill array with gradient effect
        for y in range(height):
            ratio = y / height  # Gradual transition factor
            data[y, :] = (1 - ratio) * start_color + ratio * end_color

        _texture = texture.texture_create(size=(width, height), colorfmt="rgb")
        _texture.blit_buffer(data.tobytes(), colorfmt="rgb", bufferfmt="ubyte")
        _texture.wrap = "clamp_to_edge"
        _texture.mag_filter = "linear"

        return _texture

    def _update_navbar_rect(self, instance, value):
        # Update the navbar background rectangle size and position
        self.navbar_rect.size = instance.size
        self.navbar_rect.pos = instance.pos

    def control(self, instance, text):
        global _filters, _file
        print("Control")

        if text == "xls to csv":
            _filters = ["*.xls", "*.xlsx"]
            self.show_filechooser(
                callback=lambda file: self.FileConverter.convert_xls_to_csv(file)
            )

        elif text == "csv to xls":
            _filters = ["*.csv"]
            self.show_filechooser(
                callback=lambda file: self.FileConverter.convert_csv_to_xls(file)
            )

        elif text == "word to text":
            _filters = ["*.doc", "*.docx"]
            self.show_filechooser(
                callback=lambda file: self.FileConverter.convert_word_to_text(file)
            )

        elif text == "pdf to text":
            _filters = ["*.pdf"]
            self.show_filechooser(
                callback=lambda file: self.FileConverter.convert_pdf_to_text(file)
            )

        elif text == "pdf to word":
            _filters = ["*.pdf"]
            self.show_filechooser(
                callback=lambda file: self.FileConverter.convert_pdf_to_word(file)
            )

    def show_filechooser(self, callback=None):
        chooserLayout = BoxLayout(orientation="vertical")
        # self.add_widget(chooserLayout)
        # Dynamically add the file chooser to the layout
        print(f"Set filters: {_filters}")
        self.filechooser = FileChooserIconView(
            path="/home/skye/Videos/", filters=_filters
        )
        self.filechooser.bind(
            selection=lambda instance, selection: self.selected(
                instance, selection, callback
            )
        )
        chooserLayout.add_widget(self.filechooser)

        # Add a button to close the popup
        close_button = Button(text="Close", size_hint_y=None, height=50)
        close_button.bind(on_press=self.close_popup)
        chooserLayout.add_widget(close_button)

        # Create and open the popup
        self.popup = Popup(title="Select a File", content=chooserLayout)
        # Automatically adjust the height of the popup based on the content's size
        chooserLayout.bind(
            minimum_height=chooserLayout.setter("height")
        )  # This allows the popup to adjust
        self.popup.open()

    def close_popup(self, instance):
        # Close the popup
        self.popup.dismiss()
        self.reset_options()

    def cancel_selection(self, instance):
        # Close the popup
        self._confirm.remove_widget(self.label)
        self.confirm.dismiss()
        self.selection = []
        self.popup_active = False
        self.reset_options()

    def confirm_selection(self, instance):
        self.confirm.dismiss()
        # Remove the FileChooser from the layout after selection
        self._confirm.remove_widget(self.label)
        self.popup.dismiss()
        self.popup_active = True

    def selected(self, filechooser, selection, callback):
        # Update the label with the selected file
        self.selection = selection
        if self.selection:
            try:
                self.label = Label(
                    text="No file selected",
                    size_hint=(1, 0.9),
                    pos_hint={"center_x": 0.5, "y": 0.1},
                )
                print(f"Selection: {self.selection}")  # For debugging
                self.label.text = f"Selected file: {self.selection[0]}"

                # Create boxlayout for confirmation dialogue
                self._confirm = BoxLayout(orientation="vertical")
                self._confirm.add_widget(self.label)

                _h_confirm = BoxLayout(orientation="horizontal")
                # Add a button to close the popup
                close_button = Button(text="Cancel", size_hint_y=None, height=50)
                close_button.bind(on_press=self.cancel_selection)
                # self.selection = None
                _h_confirm.add_widget(close_button)

                # Add ok button to confirm selection
                ok_button = Button(text="OK", size_hint_y=None, height=50)
                ok_button.bind(on_press=self.confirm_selection)
                _h_confirm.add_widget(ok_button)
                self._confirm.add_widget(_h_confirm)

                # Create and Show confirmation pop up
                self.confirm = Popup(
                    title="Confirm selection",
                    content=self._confirm,
                    size_hint=(None, None),
                    size=(400, 400),
                )

                # Set the height of the popup based on the content's size
                self._confirm.bind(size=self.update_popup_size)

                self.confirm.open()

                file = self.selection[0]

                # Bind the on_dismiss event to continue execution and invoke the callback
                def on_dismiss_callback(instance):
                    if callback:
                        # Call the callback with the selected file
                        print("Calling callback..")
                        # (_) is a common convention in Python to indicate that the parameter is intentionally unused.
                        try:
                            if self.op_type == "Document":
                                Clock.schedule_once(
                                    lambda dt: threading.Thread(
                                        target=callback, args=(file,)
                                    ).start(),
                                    0.3,
                                )
                            else:
                                Clock.schedule_once(
                                    lambda dt: threading.Thread(
                                        target=callback, args=(file, self.output_format)
                                    ).start(),
                                    0.3,
                                )
                        except Exception:
                            raise
                        Clock.schedule_once(lambda dt: self.reset_options(), 1)

            finally:
                ok_button.bind(on_release=on_dismiss_callback)

        else:
            print("No file selected")  # For debugging

    def reset_options(self):
        # Unbind the event temporarily
        self.conversion_spinner.unbind(text=self.constructor)
        # Rest conversion options
        self.conversion_spinner.text = "Conversion"
        # Bind the event temporarily
        self.conversion_spinner.bind(text=self.constructor)

    def update_popup_size(self, instance, value):
        # Update the popup size based on the content size
        self.confirm.size = (
            min(max(400, self._confirm.width + 50), Window.size[0]),
            min(max(400, self._confirm.height), Window.size[1]),
        )

    def adjust_font_size(self, *args):
        new_font_size = Window.size[0] // 40  # Adjust based on width
        # print(f"INFO\tAdjust Font to: {new_font_size}")
        for widget in self.children:
            widget.font_size = new_font_size


class TerminalInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Define the complete initial prompt.
        self.initial_prompt = "┌──(skye㉿kali)-[~]\n└─$"
        self.prompt_marker = "└─$"
        # Initialize with the prompt.
        self.text = self.initial_prompt
        # Compute the allowed edit start as the end of the last prompt line.
        self.current_command_start = self._compute_current_command_start()
        # Ensure the cursor is always in the allowed area.
        self.bind(cursor=self._ensure_cursor)
        # Monitor text changes to restore prompt integrity.
        self.bind(text=self._ensure_prompt_integrity)
        # Ensure our widget has a fixed minimum height (100) and expand as text grows.
        self.height = 100
        # Bind text and width changes to update the height
        self.bind(text=self.update_height, width=self.update_height)
        # Bind text and cursor updates to adjust the scroll position.
        # self.bind(text=self._adjust_scroll, cursor=self._adjust_scroll)

    def update_height(self, *args):
        # Calculate available width for text, subtracting left and right padding.
        if isinstance(self.padding, (list, tuple)):
            left_pad = self.padding[0]
            right_pad = self.padding[2] if len(self.padding) >= 3 else self.padding[0]
        else:
            left_pad = right_pad = self.padding

        available_width = self.width - left_pad - right_pad

        # Use CoreLabel to compute the rendered size of the text.
        lbl = CoreLabel(
            text=self.text,
            font_name=self.font_name,
            font_size=self.font_size,
            text_size=(available_width, None),
        )
        lbl.refresh()  # Force the label to recalc its texture size
        # Get the calculated text height and add vertical padding.
        if isinstance(self.padding, (list, tuple)):
            top_pad = self.padding[1] if len(self.padding) >= 2 else self.padding
            bottom_pad = self.padding[3] if len(self.padding) >= 4 else self.padding
        else:
            top_pad = bottom_pad = self.padding

        new_height = lbl.texture.size[1] + top_pad + bottom_pad

        # Ensure height is never less than 100.
        self.height = max(100, new_height)

    def _compute_current_command_start(self):
        """Return the absolute index immediately after the last prompt marker."""
        idx = self.text.rfind(self.prompt_marker)
        if idx != -1:
            return idx + len(self.prompt_marker)
        return len(self.text)

    def get_cursor_index(self):
        """
        Convert the (col, row) cursor into an absolute index.
        Splitting the text by newline to calculate.
        """
        lines = self.text.split("\n")
        row, col = self.cursor
        abs_index = 0
        try:
            for i in range(row):
                abs_index += len(lines[i]) + 1  # add 1 for the newline
            abs_index += col
            return abs_index
        except Exception:
            return abs_index

    def _get_row_col_from_index(self, index):
        """
        Convert an absolute index back to a (col, row) tuple.
        """
        lines = self.text.split("\n")
        current = 0
        for row, line in enumerate(lines):
            if current + len(line) >= index:
                col = index - current
                return (col, row)
            current += len(line) + 1  # +1 for the newline
        # Fallback: return end-of-text position.
        return (len(lines[-1]), len(lines) - 1)

    def _ensure_cursor(self, instance, value):
        """
        Force the cursor to stay in the allowed region (after current_command_start).
        """
        idx = self.get_cursor_index()
        if idx < self.current_command_start:
            self.cursor = self._get_row_col_from_index(self.current_command_start)

    def insert_text(self, substring, from_undo=False):
        """
        Override insertion: if the cursor is before current_command_start, force it to the allowed spot.
        Wrap the insertion in a try/except to avoid internal index errors.
        """
        # Make sure current_command_start is not beyond the current text.
        if self.current_command_start > len(self.text):
            self.current_command_start = len(self.text)
        idx = self.get_cursor_index()
        if idx < self.current_command_start:
            self.cursor = self._get_row_col_from_index(self.current_command_start)
        try:
            return super().insert_text(substring, from_undo)
        except IndexError:
            # Fallback: force the cursor to the end and try again.
            self.cursor = self._get_row_col_from_index(len(self.text))
            return super().insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode="bkspc"):
        """
        Override backspace: prevent deletion of characters before current_command_start.
        """
        idx = self.get_cursor_index()
        if idx <= self.current_command_start:
            return  # Do nothing if at or before the prompt.
        return super().do_backspace(from_undo, mode)

    def _ensure_prompt_integrity(self, instance, value):
        """
        Ensure that the text always starts with the initial prompt and update the allowed insertion index.
        """
        # Restore initial prompt if missing.
        if not self.text.startswith(self.initial_prompt):
            self.text = self.initial_prompt + self.text[self.current_command_start :]
        # Recompute allowed insertion index.
        new_start = self._compute_current_command_start()
        if new_start != self.current_command_start:
            self.current_command_start = new_start
        # Make sure current_command_start does not exceed text length.
        if self.current_command_start > len(self.text):
            self.current_command_start = len(self.text)
        # Force the cursor into the allowed region.
        if self.get_cursor_index() < self.current_command_start:
            self.cursor = self._get_row_col_from_index(self.current_command_start)

    def _adjust_scroll(self, *args):
        """
        Force the text view to scroll so that new text is visible.
        For TextInput, setting scroll_y to 0 shows the bottom of the text.
        """
        # Scheduling ensures that the update occurs after the layout is recalculated.
        Clock.schedule_once(lambda dt: setattr(self, "scroll_y", 0), 0)


class Fileconverter(MDApp):
    def build(self):
        # Set the window icon (the image should be in the same directory or specify the full path)
        # Use an image in .png format (ideally a square image like 64x64 or 128x128
        Window.set_icon("../src/icons/transaction.png")
        # Change the cursor to "wait" when starting the task
        Window.set_system_cursor("wait")
        # Loader.loading_image = 'Double Ring@1x-1.0s-200px-200px.zip'
        # Change the background color (RGBA format: Red, Green, Blue, Alpha)
        Window.clearcolor = Blue  # Light blue color

        return Main()


if __name__ == "__main__":
    Fileconverter().run()
