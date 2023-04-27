import tkinter as tk
import re

def encode_yandex_travel_suffix(text):
    return (text.replace('?', '%3F')
                .replace('=', '%3D')
                .replace(':', '%3A')
                .replace('/', '%2F')
                .replace('&', '%26'))

regex_patterns = [
    (re.compile(r'https://www.aviasales.ru/(.*)'), "https://tp.media/r?marker=219224.articles&trs=30770&p=4114&u=https%3A%2F%2Faviasales.ru%2F", "Aviasales"),
    (re.compile(r'https://level.travel/search(.*)'), "https://tp.media/r?marker=219224.articles&trs=30770&p=660&campaign_id=26&u=https%3A%2F%2Flevel.travel%2Fsearch", "Level.Travel"),
    (re.compile(r'(https://fstravel.com/.*)'), "https://tp.media/r?marker=219224.articles&trs=30770&p=4997&campaign_id=174&u=", "FUN&SUN"),
    (re.compile(r'https://travel.yandex.ru(/.*)'), "https://tp.media/r?marker=219224.articles&trs=30770&p=5916&campaign_id=193&u=https%3A%2F%2Ftravel.yandex.ru", "Yandex Travel"),
    (re.compile(r'https://www.onlinetours.ru(/tours/.*)'), "https://tp.media/r?marker=219224.articles&trs=30770&p=1094&campaign_id=43&u=https%3A%2F%2Fwww.onlinetours.ru", "Onlinetours"),
]

def convert_link(event=None):
    input_link = input_box.get()
    output_link = None
    link_type = None

    for pattern, prefix, pattern_type in regex_patterns:
        match = pattern.search(input_link)
        if match:
            suffix = match.group(1)
            if pattern_type == "Yandex Travel" or pattern_type == "Onlinetours":
                suffix = encode_yandex_travel_suffix(suffix)
            output_link = f"{prefix}{suffix}"
            link_type = pattern_type
            break

    if not output_link:
        output_box.delete(0, tk.END)
        output_box.insert(0, "Invalid link")
    else:
        output_box.delete(0, tk.END)
        output_box.insert(0, output_link)
        input_box.delete(0, tk.END)
        link_type_text.set(link_type)
def copy_to_clipboard(event):
    output_text = output_box.get()
    window.clipboard_clear()
    window.clipboard_append(output_text)
    window.update()
    output_box.config(bg='yellow')
    window.after(100, lambda: output_box.config(bg='white'))

window = tk.Tk()
window.title("Link Converter")
icon = tk.PhotoImage(file="icon.png")
window.iconphoto(True, icon)

input_label = tk.Label(window, text="Input Link:")
input_label.grid(column=0, row=0)
input_box = tk.Entry(window, width=50)
input_box.grid(column=1, row=0, padx=5, pady=5, sticky="EW")
input_box.bind("<Return>", convert_link)

output_label = tk.Label(window, text="Output Link:")
output_label.grid(column=0, row=1)
output_box = tk.Entry(window, width=50)
output_box.grid(column=1, row=1, padx=5, pady=5, sticky="EW")
output_box.bind("<Button-1>", copy_to_clipboard)

convert_button = tk.Button(window, text="Convert", command=convert_link)
convert_button.grid(column=0, row=2, columnspan=2, padx=5, pady=5, sticky="EW")

link_type_text = tk.StringVar()
link_type_label = tk.Label(window, textvariable=link_type_text)
link_type_label.grid(column=0, row=3, columnspan=2, padx=5, pady=5)

window.columnconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

window.mainloop()