import tkinter as tk

def show_text():
  input_text = text.get()
  label.config(text=input_text)

root = tk.Tk()
root.title("サンプルアプリ（Tkinter）")
root.geometry('500x300')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

text = tk.Entry(root)
text.grid(row=0, column=0, padx=20, pady=10, ipady=3, sticky="ew")

label = tk.Label(root, text="ここにテキストが表示されます")
label.grid(row=1, column=0, padx=20, pady=10, ipady=3, sticky="ew")

button = tk.Button(root, text="表示", command=show_text, width=10)
button.grid(row=2, column=0, padx=20, ipady=3, pady=10)

root.mainloop()
