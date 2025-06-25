########################################################################################
########################################################################################
# unicode and hex to text conersion
########################################################################################
########################################################################################
# # import tkinter as tk
# from tkinter import messagebox

# # ---------- Constants ----------
# FONT_NORMAL = ("Arial", 10)
# FONT_HEADER = ("Arial", 18)

# # ---------- GUI setup ----------
# root = tk.Tk()
# root.title("Hex & Unicode Converter")
# root.geometry("700x500")

# # ---------- Widgets ----------
# label = tk.Label(root, text="Converter list", font=FONT_HEADER)
# label.pack(pady=20)

# entry = tk.Entry(root, width=90)
# output_label = tk.Label(root, text="", font=("Arial", 12), wraplength=650, bg="#f0f0f0", anchor="w", justify="left", height=10)

# # Buttons
# btn_convert_mode = tk.Button(root, text="CONVERT Hex to \\uXXXX")
# btn_decode_mode = tk.Button(root, text="DECODE \\uXXXX to Text")
# btn_back = tk.Button(root, text="Back to Home")
# btn_do_convert = tk.Button(root, text="Convert")
# btn_copy = tk.Button(root, text="Copy")

# # ---------- Helper Functions ----------
# def reset_ui():
#     for widget in (entry, output_label, btn_back, btn_do_convert, btn_copy):
#         widget.pack_forget()
#     btn_convert_mode.pack_forget()
#     btn_decode_mode.pack_forget()

# def back_to_main():
#     reset_ui()
#     label.config(text="Converter list")
#     btn_convert_mode.pack(pady=10)
#     btn_decode_mode.pack(pady=10)

# # ---------- Converter Functions ----------
# def convert_hex_to_unicode():
#     input_data = entry.get().strip()
#     try:
#         hex_values = [x.strip() for x in input_data.strip(',').split(',')]
#         unicode_string = ''.join([f'\\u{val[2:].zfill(4)}' for val in hex_values if val.lower().startswith("0x")])
#         output_label.config(text=unicode_string)
#         output_label.unicode_result = unicode_string
#     except Exception as e:
#         messagebox.showerror("Error", f"Conversion failed: {e}")

# def decode_unicode_string():
#     input_data = entry.get().strip()
#     try:
#         decoded = input_data.encode('utf-8').decode('unicode_escape')
#         output_label.config(text=decoded)
#         output_label.unicode_result = decoded
#     except Exception as e:
#         messagebox.showerror("Error", f"Decoding failed: {e}")

# def copy_to_clipboard():
#     result = getattr(output_label, 'unicode_result', '')
#     if result:
#         root.clipboard_clear()
#         root.clipboard_append(result)
#         root.update()
#         messagebox.showinfo("Copied", "Text copied to clipboard!")
#     else:
#         messagebox.showwarning("Nothing to Copy", "Please convert or decode first.")

# # ---------- Mode Screens ----------
# def show_convert_mode():
#     reset_ui()
#     label.config(text="Enter Hex values (e.g., 0x0412,0x043E,...):")
#     entry.delete(0, tk.END)
#     output_label.config(text="")

#     entry.pack(pady=5)
#     btn_do_convert.config(text="Convert", command=convert_hex_to_unicode)
#     btn_do_convert.pack(pady=5)
#     btn_copy.pack(pady=5)
#     output_label.pack(pady=10, fill="x", padx=10)
#     btn_back.pack(pady=10)

# def show_decode_mode():
#     reset_ui()
#     label.config(text="Enter Unicode string (e.g., \\u0412\\u043E...):")
#     entry.delete(0, tk.END)
#     output_label.config(text="")

#     entry.pack(pady=5)
#     btn_do_convert.config(text="Decode", command=decode_unicode_string)
#     btn_do_convert.pack(pady=5)
#     btn_copy.pack(pady=5)
#     output_label.pack(pady=10, fill="x", padx=10)
#     btn_back.pack(pady=10)

# # ---------- Initial Setup ----------
# btn_convert_mode.config(command=show_convert_mode)
# btn_decode_mode.config(command=show_decode_mode)
# btn_back.config(command=back_to_main)
# btn_copy.config(command=copy_to_clipboard)

# # ---------- Start ----------
# back_to_main()
# root.mainloop()





########################################################################################
########################################################################################
# text to unicode and hex conersion
########################################################################################
########################################################################################
# import tkinter as tk
# from tkinter import messagebox

# # ---------- Constants ----------
# FONT_HEADER = ("Arial", 18)
# FONT_OUTPUT = ("Arial", 14, "bold")

# # ---------- GUI setup ----------
# root = tk.Tk()
# root.title("Text to Unicode / Hex Converter")
# root.geometry("700x400")

# # ---------- Widgets ----------
# label = tk.Label(root, text="Converter Menu", font=FONT_HEADER)
# label.pack(pady=20)

# entry = tk.Entry(root, width=90)
# output_label = tk.Label(root, text="", wraplength=650, bg="#f0f0f0", anchor="w", justify="left", height=4, font=FONT_OUTPUT)

# # Buttons
# btn_unicode = tk.Button(root, text="Convert Text to \\uXXXX")
# btn_hex = tk.Button(root, text="Convert Text to Hex")
# btn_back = tk.Button(root, text="Back to Home")
# btn_convert = tk.Button(root, text="Convert")
# btn_copy = tk.Button(root, text="Copy")

# # ---------- Helper Functions ----------
# def reset_ui():
#     for widget in (entry, output_label, btn_back, btn_convert, btn_copy):
#         widget.pack_forget()
#     btn_unicode.pack_forget()
#     btn_hex.pack_forget()

# def back_to_main():
#     reset_ui()
#     label.config(text="Converter Menu")
#     btn_unicode.pack(pady=10)
#     btn_hex.pack(pady=10)

# def copy_to_clipboard():
#     result = getattr(output_label, 'unicode_result', '')
#     if result:
#         root.clipboard_clear()
#         root.clipboard_append(result)
#         root.update()
#         messagebox.showinfo("Copied", "Result copied to clipboard!")
#     else:
#         messagebox.showwarning("Nothing to Copy", "Please convert first.")

# # ---------- Converters ----------
# def text_to_unicode_string():
#     text = entry.get()
#     result = ''.join([f'\\u{ord(char):04X}' for char in text])
#     output_label.config(text=result)
#     output_label.unicode_result = result

# def text_to_hex_string():
#     text = entry.get()
#     result = ', '.join([f'0x{ord(char):04X}' for char in text])
#     output_label.config(text=result)
#     output_label.unicode_result = result

# # ---------- Mode Screens ----------
# def show_unicode_mode():
#     reset_ui()
#     label.config(text="Enter text to convert to \\uXXXX format:")
#     entry.delete(0, tk.END)
#     output_label.config(text="")
#     entry.pack(pady=5)
#     btn_convert.config(text="Convert", command=text_to_unicode_string)
#     btn_convert.pack(pady=5)
#     btn_copy.pack(pady=5)
#     output_label.pack(pady=10, fill="x", padx=10)
#     btn_back.pack(pady=10)

# def show_hex_mode():
#     reset_ui()
#     label.config(text="Enter text to convert to Hex (0xXXXX):")
#     entry.delete(0, tk.END)
#     output_label.config(text="")
#     entry.pack(pady=5)
#     btn_convert.config(text="Convert", command=text_to_hex_string)
#     btn_convert.pack(pady=5)
#     btn_copy.pack(pady=5)
#     output_label.pack(pady=10, fill="x", padx=10)
#     btn_back.pack(pady=10)

# # ---------- Button Commands ----------
# btn_unicode.config(command=show_unicode_mode)
# btn_hex.config(command=show_hex_mode)
# btn_back.config(command=back_to_main)
# btn_copy.config(command=copy_to_clipboard)

# # ---------- Start ----------
# back_to_main()
# root.mainloop()


########################################################################################
########################################################################################
# unicode and hex to text conersion
# text to unicode and hex conversion
########################################################################################
########################################################################################

# # pip install jieba --> for chinese new window spacing
# import tkinter as tk
# from tkinter import ttk, messagebox

# # ---------- Constants ----------
# FONT_HEADER = ("Arial", 16, "bold")
# FONT_NORMAL = ("Arial", 12)
# FONT_OUTPUT = ("Arial", 14, "bold")

# # ---------- GUI Setup ----------
# root = tk.Tk()
# root.title("Universal Text Converter")
# root.geometry("720x420")

# # ---------- Widgets ----------
# label = tk.Label(root, text="Universal Text Converter", font=FONT_HEADER)
# label.pack(pady=20)

# # Dropdown menu for conversion type
# conversion_types = [
#     "Text → Unicode (\\uXXXX)",
#     "Text → Hex (0xXXXX)",
#     "Unicode (\\uXXXX) → Text",
#     "Hex (0xXXXX) → Text"
# ]
# selected_conversion = tk.StringVar(value=conversion_types[0])
# dropdown = ttk.Combobox(root, textvariable=selected_conversion, values=conversion_types, state="readonly", font=FONT_NORMAL)
# dropdown.pack(pady=10)

# # Input field
# entry = tk.Entry(root, width=90, font=FONT_NORMAL)
# entry.pack(pady=10)

# # Output label
# output_label = tk.Label(root, text="", wraplength=680, bg="#f0f0f0", anchor="w", justify="left", height=5, font=FONT_OUTPUT)
# output_label.pack(pady=10, fill="x", padx=10)

# # Buttons
# btn_frame = tk.Frame(root)
# btn_frame.pack(pady=10)

# convert_btn = tk.Button(btn_frame, text="Convert", font=FONT_NORMAL)
# copy_btn = tk.Button(btn_frame, text="Copy", font=FONT_NORMAL)

# convert_btn.grid(row=0, column=0, padx=10)
# copy_btn.grid(row=0, column=1, padx=10)

# # ---------- Logic Functions ----------
# def convert_text_to_unicode(text):
#     return ''.join([f'\\u{ord(c):04X}' for c in text])

# def convert_text_to_hex(text):
#     return ', '.join([f'0x{ord(c):04X}' for c in text])

# def convert_unicode_to_text(text):
#     try:
#         return text.encode('utf-8').decode('unicode_escape')
#     except Exception as e:
#         return f"[Error decoding Unicode]: {e}"

# def convert_hex_to_text(text):
#     try:
#         hex_parts = [x.strip() for x in text.strip(',').split(',')]
#         chars = [chr(int(part, 16)) for part in hex_parts if part.lower().startswith("0x")]
#         return ''.join(chars)
#     except Exception as e:
#         return f"[Error decoding Hex]: {e}"

# def perform_conversion():
#     input_data = entry.get().strip()
#     option = selected_conversion.get()
#     result = ""

#     if option == "Text → Unicode (\\uXXXX)":
#         result = convert_text_to_unicode(input_data)
#     elif option == "Text → Hex (0xXXXX)":
#         result = convert_text_to_hex(input_data)
#     elif option == "Unicode (\\uXXXX) → Text":
#         result = convert_unicode_to_text(input_data)
#     elif option == "Hex (0xXXXX) → Text":
#         result = convert_hex_to_text(input_data)

#     output_label.config(text=result)
#     output_label.unicode_result = result

# def copy_to_clipboard():
#     result = getattr(output_label, 'unicode_result', '')
#     if result:
#         root.clipboard_clear()
#         root.clipboard_append(result)
#         root.update()
#         messagebox.showinfo("Copied", "Result copied to clipboard!")
#     else:
#         messagebox.showwarning("Nothing to Copy", "Please perform a conversion first.")

# # ---------- Button Bindings ----------
# convert_btn.config(command=perform_conversion)
# copy_btn.config(command=copy_to_clipboard)

# # ---------- Run App ----------
# root.mainloop()


########################################################################################
########################################################################################
# unicode and hex to text conersion
# text to unicode and hex conversion
# chinese string spacing
########################################################################################
########################################################################################
# import tkinter as tk
# from tkinter import ttk, messagebox
# import jieba

# # ---------- Fonts ----------
# FONT_HEADER = ("Arial", 16, "bold")
# FONT_NORMAL = ("Arial", 12)
# FONT_OUTPUT = ("Arial", 14, "bold")

# # ---------- Conversion Functions ----------

# def convert_text_to_unicode(text):
#     return ''.join([f'\\u{ord(c):04X}' for c in text])

# def convert_text_to_hex(text):
#     return ', '.join([f'0x{ord(c):04X}' for c in text])

# def convert_unicode_to_text(text):
#     try:
#         return text.encode('utf-8').decode('unicode_escape')
#     except Exception as e:
#         return f"[Error decoding Unicode]: {e}"

# def convert_hex_to_text(text):
#     try:
#         hex_parts = [x.strip() for x in text.strip(',').split(',')]
#         chars = [chr(int(part, 16)) for part in hex_parts if part.lower().startswith("0x")]
#         return ''.join(chars)
#     except Exception as e:
#         return f"[Error decoding Hex]: {e}"

# # Chinese spacing helpers
# def manual_spacing(text):
#     replacements = {
#         "距离可能有错": "距离 可能有错",
#         "请检查": "请检查",
#         "被测介质的设定": "被测 介质的设定",
#         "示波器上的波形": "示波器上的 波形",
#     }
#     for key, value in replacements.items():
#         text = text.replace(key, value)
#     return text

# def jieba_spacing(text):
#     return ' '.join(jieba.cut(text))

# # ---------- Main App ----------

# root = tk.Tk()
# root.title("Universal Text Converter & Chinese Spacing Tool")
# root.geometry("750x500")

# # Create Tabs
# notebook = ttk.Notebook(root)
# notebook.pack(expand=True, fill="both")

# # -------- Tab 1: Text <-> Unicode/Hex Conversion --------

# tab1 = ttk.Frame(notebook)
# notebook.add(tab1, text="Unicode/Hex Converter")

# ttk.Label(tab1, text="Select Conversion Type:", font=FONT_NORMAL).pack(pady=8)
# conversion_types = [
#     "Text → Unicode (\\uXXXX)",
#     "Text → Hex (0xXXXX)",
#     "Unicode (\\uXXXX) → Text",
#     "Hex (0xXXXX) → Text"
# ]
# selected_conversion = tk.StringVar(value=conversion_types[0])
# dropdown = ttk.Combobox(tab1, textvariable=selected_conversion, values=conversion_types, state="readonly", font=FONT_NORMAL)
# dropdown.pack(pady=5)

# entry1 = tk.Entry(tab1, width=90, font=FONT_NORMAL)
# entry1.pack(pady=10)

# output_label1 = tk.Label(tab1, text="", wraplength=700, bg="#f0f0f0", anchor="w", justify="left", height=6, font=FONT_OUTPUT)
# output_label1.pack(padx=10, pady=10, fill="x")

# btn_frame1 = tk.Frame(tab1)
# btn_frame1.pack(pady=10)

# def perform_conversion():
#     input_data = entry1.get().strip()
#     option = selected_conversion.get()
#     result = ""

#     if option == "Text → Unicode (\\uXXXX)":
#         result = convert_text_to_unicode(input_data)
#     elif option == "Text → Hex (0xXXXX)":
#         result = convert_text_to_hex(input_data)
#     elif option == "Unicode (\\uXXXX) → Text":
#         result = convert_unicode_to_text(input_data)
#     elif option == "Hex (0xXXXX) → Text":
#         result = convert_hex_to_text(input_data)

#     output_label1.config(text=result)
#     output_label1.result_text = result

# def copy_to_clipboard_1():
#     result = getattr(output_label1, 'result_text', '')
#     if result:
#         root.clipboard_clear()
#         root.clipboard_append(result)
#         root.update()
#         messagebox.showinfo("Copied", "Result copied to clipboard!")
#     else:
#         messagebox.showwarning("Nothing to Copy", "Please perform a conversion first.")

# btn_convert = tk.Button(btn_frame1, text="Convert", font=FONT_NORMAL, command=perform_conversion)
# btn_copy = tk.Button(btn_frame1, text="Copy Result", font=FONT_NORMAL, command=copy_to_clipboard_1)

# btn_convert.grid(row=0, column=0, padx=15)
# btn_copy.grid(row=0, column=1, padx=15)

# # -------- Tab 2: Chinese Sentence Spacing --------

# tab2 = ttk.Frame(notebook)
# notebook.add(tab2, text="Chinese Sentence Spacing")

# ttk.Label(tab2, text="Enter Chinese Sentence:", font=FONT_NORMAL).pack(pady=8)
# entry2 = tk.Entry(tab2, width=90, font=FONT_NORMAL)
# entry2.pack(pady=10)

# output_label2 = tk.Label(tab2, text="", wraplength=700, bg="#f0f0f0", anchor="w", justify="left", height=6, font=FONT_OUTPUT)
# output_label2.pack(padx=10, pady=10, fill="x")

# btn_frame2 = tk.Frame(tab2)
# btn_frame2.pack(pady=10)

# def convert_spacing(mode):
#     sentence = entry2.get().strip()
#     if not sentence:
#         messagebox.showwarning("Input Missing", "Please enter a sentence.")
#         return
#     if mode == "manual":
#         result = manual_spacing(sentence)
#     else:
#         result = jieba_spacing(sentence)
#     output_label2.config(text=result)
#     output_label2.result_text = result

# def copy_to_clipboard_2():
#     text = getattr(output_label2, 'result_text', '')
#     if text:
#         root.clipboard_clear()
#         root.clipboard_append(text)
#         root.update()
#         messagebox.showinfo("Copied", "Spaced sentence copied to clipboard.")
#     else:
#         messagebox.showwarning("Nothing to Copy", "Please perform a conversion first.")

# btn_manual = tk.Button(btn_frame2, text="Manual Spacing", font=FONT_NORMAL, command=lambda: convert_spacing("manual"))
# btn_jieba = tk.Button(btn_frame2, text="jieba Spacing", font=FONT_NORMAL, command=lambda: convert_spacing("jieba"))
# btn_copy_spacing = tk.Button(btn_frame2, text="Copy Result", font=FONT_NORMAL, command=copy_to_clipboard_2)

# btn_manual.grid(row=0, column=0, padx=15)
# btn_jieba.grid(row=0, column=1, padx=15)
# btn_copy_spacing.grid(row=0, column=2, padx=15)

# # ---------- Run App ----------
# root.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox
import jieba

# ---------- Fonts ----------
FONT_HEADER = ("Arial", 16, "bold")
FONT_NORMAL = ("Arial", 12)
FONT_OUTPUT = ("Arial", 14, "bold")

# ---------- Conversion Functions ----------

def convert_text_to_unicode(text):
    return ''.join([f'\\u{ord(c):04X}' for c in text])

def convert_text_to_hex(text):
    return ', '.join([f'0x{ord(c):04X}' for c in text])

def convert_unicode_to_text(text):
    try:
        return text.encode('utf-8').decode('unicode_escape')
    except Exception as e:
        return f"[Error decoding Unicode]: {e}"

def convert_hex_to_text(text):
    try:
        hex_parts = [x.strip() for x in text.strip(',').split(',')]
        chars = [chr(int(part, 16)) for part in hex_parts if part.lower().startswith("0x")]
        return ''.join(chars)
    except Exception as e:
        return f"[Error decoding Hex]: {e}"

# Chinese spacing helpers

def manual_spacing(sentence):
    # Add custom rules based on known phrases
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

# ---------- Main App ----------

root = tk.Tk()
root.title("Universal Text Converter & Chinese Spacing Tool")
root.geometry("750x500")

# Create Tabs
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# -------- Tab 1: Text <-> Unicode/Hex Conversion --------

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Unicode/Hex Converter")

ttk.Label(tab1, text="Select Conversion Type:", font=FONT_NORMAL).pack(pady=8)
conversion_types = [
    "Text → Unicode (\\uXXXX)",
    "Text → Hex (0xXXXX)",
    "Unicode (\\uXXXX) → Text",
    "Hex (0xXXXX) → Text"
]
selected_conversion = tk.StringVar(value=conversion_types[0])
dropdown = ttk.Combobox(tab1, textvariable=selected_conversion, values=conversion_types, state="readonly", font=FONT_NORMAL)
dropdown.pack(pady=5)

entry1 = tk.Entry(tab1, width=90, font=FONT_NORMAL)
entry1.pack(pady=10)

output_label1 = tk.Label(tab1, text="", wraplength=700, bg="#f0f0f0", anchor="w", justify="left", height=6, font=FONT_OUTPUT)
output_label1.pack(padx=10, pady=10, fill="x")

btn_frame1 = tk.Frame(tab1)
btn_frame1.pack(pady=10)

def perform_conversion():
    input_data = entry1.get().strip()
    option = selected_conversion.get()
    result = ""

    if option == "Text → Unicode (\\uXXXX)":
        result = convert_text_to_unicode(input_data)
    elif option == "Text → Hex (0xXXXX)":
        result = convert_text_to_hex(input_data)
    elif option == "Unicode (\\uXXXX) → Text":
        result = convert_unicode_to_text(input_data)
    elif option == "Hex (0xXXXX) → Text":
        result = convert_hex_to_text(input_data)

    output_label1.config(text=result)
    output_label1.result_text = result

def copy_to_clipboard_1():
    result = getattr(output_label1, 'result_text', '')
    if result:
        root.clipboard_clear()
        root.clipboard_append(result)
        root.update()
        messagebox.showinfo("Copied", "Result copied to clipboard!")
    else:
        messagebox.showwarning("Nothing to Copy", "Please perform a conversion first.")

btn_convert = tk.Button(btn_frame1, text="Convert", font=FONT_NORMAL, command=perform_conversion)
btn_copy = tk.Button(btn_frame1, text="Copy Result", font=FONT_NORMAL, command=copy_to_clipboard_1)

btn_convert.grid(row=0, column=0, padx=15)
btn_copy.grid(row=0, column=1, padx=15)

# -------- Tab 2: Chinese Sentence Spacing --------

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Chinese Sentence Spacing")

ttk.Label(tab2, text="Enter Chinese Sentence:", font=FONT_NORMAL).pack(pady=8)
entry2 = tk.Entry(tab2, width=90, font=FONT_NORMAL)
entry2.pack(pady=10)

output_label2 = tk.Label(tab2, text="", wraplength=700, bg="#f0f0f0", anchor="w", justify="left", height=6, font=FONT_OUTPUT)
output_label2.pack(padx=10, pady=10, fill="x")

btn_frame2 = tk.Frame(tab2)
btn_frame2.pack(pady=10)

def convert_spacing(mode):
    sentence = entry2.get().strip()
    if not sentence:
        messagebox.showwarning("Input Missing", "Please enter a sentence.")
        return
    if mode == "manual":
        result = manual_spacing(sentence)
    else:
        result = jieba_spacing(sentence)
    output_label2.config(text=result)
    output_label2.result_text = result

def copy_to_clipboard_2():
    text = getattr(output_label2, 'result_text', '')
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        messagebox.showinfo("Copied", "Spaced sentence copied to clipboard.")
    else:
        messagebox.showwarning("Nothing to Copy", "Please perform a conversion first.")

btn_manual = tk.Button(btn_frame2, text="Manual Spacing", font=FONT_NORMAL, command=lambda: convert_spacing("manual"))
btn_jieba = tk.Button(btn_frame2, text="jieba Spacing", font=FONT_NORMAL, command=lambda: convert_spacing("jieba"))
btn_copy_spacing = tk.Button(btn_frame2, text="Copy Result", font=FONT_NORMAL, command=copy_to_clipboard_2)

btn_manual.grid(row=0, column=0, padx=15)
btn_jieba.grid(row=0, column=1, padx=15)
btn_copy_spacing.grid(row=0, column=2, padx=15)

# ---------- Run App ----------
root.mainloop()
