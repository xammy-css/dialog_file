import tkinter as tk
from tkinter import filedialog

def choose_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text="Вибраний файл: " + file_path)
        f = open(file_path)
        textinfile = f.read()
        rechennya = textinfile.split(".")
        label.config(text="Речень: " + str(len(rechennya)))

root = tk.Tk()
root.title("Оберіть файл")
# setting window size
width = 300
height = 100
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

label = tk.Label(root, text="")
label.pack(pady=10)

button = tk.Button(root, text="Обрати файл", command=choose_file)
button.pack(pady=5)


root.mainloop()
