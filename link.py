import tkinter as tk
import re

aviasales_regex = re.compile(r'https://www.aviasales.ru/(.*)')

def convert_link(event=None):
    input_link = input_box.get()
    if "https://fstravel.com/" in input_link:
        output_link = "https://tp.media/r?marker=219224.articles&trs=30770&p=4997&campaign_id=174&u=" + input_link
        link_type_text.set("FUN&SUN")
    else:
        match = aviasales_regex.search(input_link)
        if not match:
            output_box.delete(0, tk.END)
            output_box.insert(0, "Invalid link")
            return
        search_path = match.group(1)
        output_link = "https://tp.media/r?marker=219224.articles&trs=30770&p=4114&u=https%3A%2F%2Faviasales.ru%2F" + search_path
        link_type_text.set("Aviasales")
    output_box.delete(0, tk.END)
    output_box.insert(0, output_link)
    input_box.delete(0, tk.END)

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