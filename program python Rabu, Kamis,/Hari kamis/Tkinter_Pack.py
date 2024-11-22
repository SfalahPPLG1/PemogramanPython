import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="Label 1")
label.pack()

button = tk.Button(root, text="Tombol 1")
button.pack()

Checkbox = tk.Checkbutton (root, text="Centang 1")
Checkbox.pack()
root.mainloop()