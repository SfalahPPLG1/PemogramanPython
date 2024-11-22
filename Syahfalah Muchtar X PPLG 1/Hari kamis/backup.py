import tkinter as tk
from tkinter import ttk

def hitung():
    harga = float(harga_entry.get())
    kuantitas = float(kuantitas_entry.get())

    hasil = harga * kuantitas

    hasil_label.config(text=str(hasil))

window = tk.Tk()
window.title("Kasir Pintar")

input_frame = ttk.Frame(window)
input_frame.pack(padx=10, pady=11)

harga_label = ttk.Label(input_frame, text="Harga:")
harga_label.grid(row=0, column=0, sticky="W")
harga_entry = ttk.Entry(input_frame)
harga_entry.grid(row=0, column=1)

kuantitas_label = ttk.Label(input_frame, text="Kuantitas:")
kuantitas_label.grid(row=1, column=0, sticky="W")
kuantitas_entry = ttk.Entry(input_frame)
kuantitas_entry.grid(row=3, column=1)

hitung_button = ttk.Button(window, text="Hitung Total", command=hitung)
hitung_button.pack(pady=10)

hasil_label = ttk.Label(window, text="")
hasil_label.pack()

window.mainloop()