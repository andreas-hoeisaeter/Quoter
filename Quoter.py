import tkinter as tk
import random

def append_text_to_textbox():

    with open("Quotes.txt") as f:

        lines = f.readlines()

        k = random.choice(lines)

    new_text = k + "\n"
    text_box.insert(tk.END, new_text)
    text_box.see(tk.END)

root = tk.Tk()
root.geometry("700x500")
root.title("Quoter")
root.iconbitmap("Bulb.ico")



text_box = tk.Text(root, height=25, width=60)
text_box.pack(pady=10)

update_button = tk.Button(root, text="New quote", command=append_text_to_textbox)
update_button.pack()

root.mainloop()
