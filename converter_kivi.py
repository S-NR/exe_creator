import jieba
from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from kivy.uix.scrollview import ScrollView


def convert_text_to_unicode(text):
    return ''.join([f'\\u{ord(c):04X}' for c in text])

def convert_text_to_hex(text):
    return ', '.join([f'0x{ord(c):04X}' for c in text])

def convert_unicode_to_text(text):
    try:
        return text.encode('utf-8').decode('unicode_escape')
    except Exception as e:
        return f"[Unicode Decode Error]: {e}"

def convert_hex_to_text(text):
    try:
        hex_parts = [x.strip() for x in text.strip(',').split(',')]
        chars = [chr(int(part, 16)) for part in hex_parts if part.lower().startswith("0x")]
        return ''.join(chars)
    except Exception as e:
        return f"[Hex Decode Error]: {e}"

def manual_spacing(sentence):
    replacements = {
        "距离可能有错": "距离 可能有错",
        "请检查": "请检查 ",
        "被测介质的设定": "被测介质的设定 ",
        "示波器上的波形": "示波器上的波形 ",
    }
    for key, value in replacements.items():
        sentence = sentence.replace(key, value)
    return sentence

def jieba_spacing(text):
    return ' '.join(jieba.cut(text))


class TextToolApp(TabbedPanel):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.tab_height = 40
        self.padding = 10

        self.build_unicode_tab()
        self.build_spacing_tab()

    def build_unicode_tab(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_unicode = TextInput(hint_text="Enter text or encoded string", size_hint_y=None, height=100)
        layout.add_widget(self.input_unicode)

        buttons = BoxLayout(size_hint_y=None, height=40, spacing=10)
        for text, func in [
            ("Text → Unicode", lambda: self.convert_unicode("unicode")),
            ("Text → Hex", lambda: self.convert_unicode("hex")),
            ("Unicode → Text", lambda: self.convert_unicode("u2t")),
            ("Hex → Text", lambda: self.convert_unicode("h2t"))
        ]:
            buttons.add_widget(Button(text=text, on_press=lambda _, f=func: f()))
        layout.add_widget(buttons)

        self.output_unicode = Label(text="", size_hint_y=None, height=150)
        scroll = ScrollView()
        scroll.add_widget(self.output_unicode)
        layout.add_widget(scroll)

        layout.add_widget(Button(text="Copy Result", size_hint_y=None, height=40, on_press=self.copy_unicode))

        self.add_widget(layout)
        self.default_tab_text = "Unicode/Hex"

    def build_spacing_tab(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_spacing = TextInput(hint_text="Enter Chinese sentence", size_hint_y=None, height=100)
        layout.add_widget(self.input_spacing)

        buttons = BoxLayout(size_hint_y=None, height=40, spacing=10)
        for text, func in [
            ("Manual Spacing", lambda: self.spacing_convert("manual")),
            ("Jieba Spacing", lambda: self.spacing_convert("jieba"))
        ]:
            buttons.add_widget(Button(text=text, on_press=lambda _, f=func: f()))
        layout.add_widget(buttons)

        self.output_spacing = Label(text="", size_hint_y=None, height=150)
        scroll = ScrollView()
        scroll.add_widget(self.output_spacing)
        layout.add_widget(scroll)

        layout.add_widget(Button(text="Copy Result", size_hint_y=None, height=40, on_press=self.copy_spacing))

        self.add_widget(layout)
        self.tab_list[-1].text = "Chinese Spacing"

    def convert_unicode(self, mode):
        text = self.input_unicode.text.strip()
        if mode == "unicode":
            result = convert_text_to_unicode(text)
        elif mode == "hex":
            result = convert_text_to_hex(text)
        elif mode == "u2t":
            result = convert_unicode_to_text(text)
        elif mode == "h2t":
            result = convert_hex_to_text(text)
        else:
            result = "[Invalid mode]"
        self.output_unicode.text = result

    def spacing_convert(self, mode):
        text = self.input_spacing.text.strip()
        if not text:
            self.output_spacing.text = "[Input missing]"
            return
        if mode == "manual":
            result = manual_spacing(text)
        else:
            result = jieba_spacing(text)
        self.output_spacing.text = result

    def copy_unicode(self, *_):
        Clipboard.copy(self.output_unicode.text or "")

    def copy_spacing(self, *_):
        Clipboard.copy(self.output_spacing.text or "")


class MyApp(App):
    def build(self):
        return TextToolApp()


if __name__ == "__main__":
    MyApp().run()
