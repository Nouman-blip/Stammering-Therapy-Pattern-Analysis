# hyperlink_label.py
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty
import webbrowser

class HyperlinkLabel(ButtonBehavior, Label):
    url = StringProperty('')

    def on_release(self):
        webbrowser.open(self.url)
