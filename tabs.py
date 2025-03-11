from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem

class ConverterTabs(TabbedPanel):
    def __init__(self, **kwargs):
        super(ConverterTabs, self).__init__(**kwargs)

        self.default_tab_text = 'Home'
        self.default_tab_content = Button(text="Hi")
        # Document Tab
        doc_tab = TabbedPanelItem(text='Documents')
        doc_tab.add_widget(Button(text="PDF to DOCX", size_hint_y=None, height=50))
        doc_tab.add_widget(Button(text="DOCX to TXT", size_hint_y=None, height=50))
        self.add_widget(doc_tab)

        # Audio Tab
        audio_tab = TabbedPanelItem(text='Audio')
        audio_tab.add_widget(Button(text="MP3 to WAV", size_hint_y=None, height=50))
        audio_tab.add_widget(Button(text="WAV to MP3", size_hint_y=None, height=50))
        self.add_widget(audio_tab)

class ConverterApp(App):
    def build(self):
        return ConverterTabs()

if __name__ == '__main__':
    ConverterApp().run()
