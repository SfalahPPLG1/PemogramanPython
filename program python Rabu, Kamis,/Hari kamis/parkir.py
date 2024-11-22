import PySimpleGUI as sg
from datetime import datetime

TARIF_PER_JAM = 2000

layout = [
    [sg.Text("Aplikasi Parkir Elektronik", font=("Helvetica", 16), justification="center", size=(40, 1))],
    [sg.Text("Cari NoPol"), sg.Input(key="-CARI_NOPOL-", size=(15, 1)), sg.Button("Cari")],
    [sg.Text("No Plat Polisi"), sg.Input(key="-NOPOL-", size=(20, 1))],
    [sg.Text("Waktu Masuk"), sg.Input(key="-MASUK-", size=(20, 1))],
    [sg.Text("Waktu Keluar"), sg.Input(key="-KELUAR-", size=(20, 1))],
    [sg.Text("Biaya"), sg.Input("0", key="-BIAYA-", size=(20, 1), readonly=True), sg.Button("Hitung")],
    [sg.Text("Biaya Per Jam", font=("Helvetica", 12)), sg.Text(f"Rp. {TARIF_PER_JAM:,}", font=("Helvetica", 20), text_color="red")],
    [sg.Text("List Pelanggan Urut Terakhir Keluar", font=("Helvetica", 10), text_color="blue")],
    [sg.Table(values=[], headings=["No Plat Polisi", "Masuk", "Keluar", "Biaya"], key="-TABLE1-", auto_size_columns=True, justification="center")],
    [sg.Text("List Pelanggan Banyak Bayar", font=("Helvetica", 10), text_color="blue")],
    [sg.Table(values=[], headings=["No Plat Polisi", "Masuk", "Keluar", "Biaya"], key="-TABLE2-", auto_size_columns=True, justification="center")],
]

window = sg.Window("Aplikasi Parkir", layout)

data_pelanggan = []

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break

    if event == "Hitung":
        try:
            nopol = values["-NOPOL-"]
            waktu_masuk = values["-MASUK-"]
            waktu_keluar = values["-KELUAR-"]
            
            format_waktu = "%H:%M"  
            masuk = datetime.strptime(waktu_masuk, format_waktu)
            keluar = datetime.strptime(waktu_keluar, format_waktu)
            
            durasi = (keluar - masuk).seconds / 3600
            biaya = int(durasi) * TARIF_PER_JAM
            
            window["-BIAYA-"].update(f"{biaya}")
            
            data_pelanggan.append([nopol, waktu_masuk, waktu_keluar, f"Rp. {biaya:,}"])
            
            window["-TABLE1-"].update(values=data_pelanggan)
        except Exception as e:
            sg.popup_error("Terjadi kesalahan: Pastikan waktu dalam format HH:MM!")
    
    if event == "Cari":
        nopol_cari = values["-CARI_NOPOL-"]
        hasil_cari = [item for item in data_pelanggan if item[0] == nopol_cari]
        if hasil_cari:
            sg.popup(f"Data ditemukan:\n{hasil_cari[0]}")
        else:
            sg.popup("Data tidak ditemukan!")

window.close()