import tkinter as tk
from tkinter import messagebox

def simpan_data():
    nama = entry_nama.get()
    tanggal_lahir = entry_tanggal_lahir.get()
    asal_sekolah = entry_asal_sekolah.get()
    nisn = entry_nisn.get()
    nama_ayah = entry_nama_ayah.get()
    nama_ibu = entry_nama_ibu.get()
    no_hp = entry_no_hp.get()
    alamat = text_alamat.get("1.0", tk.END)

    if not nama or not tanggal_lahir or not asal_sekolah or not nisn:
        messagebox.showwarning("Peringatan", "Harap isi semua kolom yang wajib!")
        return
    
    messagebox.showinfo("Berhasil", "Data berhasil disimpan!")
    print("Data Siswa Baru:")
    print(f"Nama: {nama}")
    print(f"Tanggal Lahir: {tanggal_lahir}")
    print(f"Asal Sekolah: {asal_sekolah}")
    print(f"NISN: {nisn}")
    print(f"Nama Ayah: {nama_ayah}")
    print(f"Nama Ibu: {nama_ibu}")
    print(f"No. HP: {no_hp}")
    print(f"Alamat: {alamat.strip()}")

def hapus_data():
    entry_nama.delete(0, tk.END)
    entry_tanggal_lahir.delete(0, tk.END)
    entry_asal_sekolah.delete(0, tk.END)
    entry_nisn.delete(0, tk.END)
    entry_nama_ayah.delete(0, tk.END)
    entry_nama_ibu.delete(0, tk.END)
    entry_no_hp.delete(0, tk.END)
    text_alamat.delete("1.0", tk.END)

root = tk.Tk()
root.title("Data Siswa Baru")
root.geometry("400x500")
root.configure(bg="#B2EBF2")

label_judul = tk.Label(root, text="DATA SISWA BARU", bg="#B2EBF2", font=("Arial", 16, "bold"))
label_judul.pack(pady=10)

tk.Label(root, text="Nama Lengkap:", bg="#B2EBF2").pack(anchor="w", padx=20)
entry_nama = tk.Entry(root, width=40)
entry_nama.pack(pady=5)

tk.Label(root, text="Tanggal Lahir:", bg="#B2EBF2").pack(anchor="w", padx=20)
entry_tanggal_lahir = tk.Entry(root, width=40)
entry_tanggal_lahir.pack(pady=5)

tk.Label(root, text="Asal Sekolah:", bg="#B2EBF2").pack(anchor="w", padx=20)
entry_asal_sekolah = tk.Entry(root, width=40)
entry_asal_sekolah.pack(pady=5)

tk.Label(root, text="NISN:", bg="#B2EBF2").pack(anchor="w", padx=20)
entry_nisn = tk.Entry(root, width=40)
entry_nisn.pack(pady=5)

tk.Label(root, text="Nama Ayah:", bg="#B2EBF2").pack(anchor="w", padx=20)
entry_nama_ayah = tk.Entry(root, width=40)
entry_nama_ayah.pack(pady=5)

tk.Label(root, text="Nama Ibu:", bg="#B2EBF2").pack(anchor="w", padx=20)
entry_nama_ibu = tk.Entry(root, width=40)
entry_nama_ibu.pack(pady=5)

tk.Label(root, text="Nomor Telepon / HP:", bg="#B2EBF2").pack(anchor="w", padx=20)
entry_no_hp = tk.Entry(root, width=40)
entry_no_hp.pack(pady=5)

tk.Label(root, text="Alamat:", bg="#B2EBF2").pack(anchor="w", padx=20)
text_alamat = tk.Text(root, width=30, height=5)
text_alamat.pack(pady=5)

frame_tombol = tk.Frame(root, bg="#B2EBF2")
frame_tombol.pack(pady=20)

btn_hapus = tk.Button(frame_tombol, text="Hapus", command=hapus_data, bg="#FF5722", fg="white")
btn_hapus.pack(side="left", padx=10)

btn_simpan = tk.Button(frame_tombol, text="Simpan", command=simpan_data, bg="#4CAF50", fg="white")
btn_simpan.pack(side="left", padx=10)

root.mainloop()
