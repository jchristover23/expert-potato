import random,Scan
from datetime import datetime
from tkinter import *
from tkinter import messagebox
TIPE = ' '
jam_masuk = ' '
E1 = ' '
E3 = ' '
biaya = ' '
menit_masuk = ' '


def cek():
    try:
        if len(E1.get()) != 8:
            messagebox.showerror("Alert", "Format Waktu Salah !")
        else:
            biaya_hitung()
    except ValueError:
        messagebox.showerror("Alert", "Format Waktu Salah !")

def cek_bayar():
    if int(E3.get()) > int(biaya):
        kembali = int(E3.get()) - int(biaya)
        hitung.destroy()
        messagebox.showinfo("Terima Kasih", "Kembalian Anda %d\nHati - Hati di jalan!" % kembali)
        karcis.destroy()
        Scan.scan()
    elif int(E3.get()) == int(biaya):
        hitung.destroy()
        messagebox.showinfo("Terima Kasih", "Hati - Hati di jalan!")
        karcis.destroy()
        Scan.scan()
    else:
        hitung.destroy()
        messagebox.showerror("Alert","Maaf Uang Anda Kurang")
        biaya_hitung()

def karcis():
    global E1
    global TIPE
    global jam_masuk
    global menit_masuk
    global karcis
    karcis = Tk()
    karcis.title("Rincian Parkir Anda")
    L1 = Label(karcis, text="Nama :")
    L1.grid(row = 1, column = 1, pady = 1, padx = 5, sticky = W)
    L1.config(font=("Helvetica", 15))
    nama = open('nama.txt')
    z = nama.readlines()
    NAMA = random.choice(z)
    NAMABARU = NAMA[:-1]
    L2 = Label(karcis, text= NAMABARU)
    L2.grid(row = 1, column = 2, pady = 1, padx = 10, sticky = W)
    L2.config(font=("Helvetica", 15))

    L3 = Label(karcis, text="NIM :")
    L3.config(font=("Helvetica", 15))
    L3.grid(row = 2, column = 1, pady = 1, padx = 5, sticky = W)
    NIM = str(random.randint(1, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
    L4= Label(karcis, text=NIM)
    L4.grid(row = 2, column = 2, pady = 1, padx = 10, sticky = W)
    L4.config(font=("Helvetica", 15))

    L5 = Label(karcis, text="Plat :")
    L5.config(font=("Helvetica", 15))
    L5.grid(row = 3, column=1,pady=1,padx=5,sticky = W)
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    PLAT = random.choice(alphabet)+random.choice(alphabet)+' '+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+' '+random.choice(alphabet)+random.choice(alphabet)
    L6 = Label(karcis, text= PLAT)
    L6.config(font=("Helvetica", 15))
    L6.grid(row = 3, column=2,pady=1,padx=10,sticky = W)

    L7 = Label(karcis, text="Tipe :")
    L7.config(font=("Helvetica", 15))
    L7.grid(row = 4, column=1,pady=1,padx=5,sticky = W)
    TIPE = random.choice(['Motor','Mobil'])
    L8 = Label(karcis, text=TIPE)
    L8.config(font=("Helvetica", 15))
    L8.grid(row = 4, column=2,pady=1,padx=5,sticky = W)

    L9 = Label(karcis, text="Masuk :")
    L9.config(font=("Helvetica", 15))
    L9.grid(row = 5, column=1,pady=1,padx=5,sticky = W)
    masuk = datetime.now()
    masuk_karcis = str("{:%H:%M:%S}".format(masuk))
    masuk = str(masuk)
    jam_masuk = masuk[11:13]
    menit_masuk = masuk[14:16]
    L10 = Label(karcis, text=masuk_karcis)
    L10.config(font=("Helvetica", 15))
    L10.grid(row = 5, column=2,pady=1,padx=5,sticky = W)

    L11 = Label(karcis, text="Keluar :")
    L11.config(font=("Helvetica", 15))
    L11.grid(row = 6, column=1,pady=1,padx=5,sticky = W)
    E1 = Entry(karcis, bd=1,width = 10)
    E1.config(font=("Helvetica", 15))
    E1.grid(row = 6, column=2,pady=1,padx=5,sticky = W)
    hitung = Button(karcis, text="Hitung", command=cek)
    karcis.bind('<Return>', lambda press_key: cek())
    hitung.grid(row=7, column=3, pady=5, padx=10, sticky=W)
    karcis.mainloop()

def biaya_hitung():
    global E3
    global biaya
    global hitung
    hitung = Tk()
    hitung.title("Biaya")
    L1 = Label(hitung, text="Biaya :")
    L1.config(font=("Helvetica", 15))
    L1.grid(row = 1, column=1,pady=1,padx=5,sticky = W)
    keluar = E1.get()
    jam_keluar = keluar[0:2]
    menit_keluar = keluar[3:5]
    durasi = (int(jam_keluar) - int(jam_masuk))
    if menit_keluar > menit_masuk:
        durasi += 1
    if TIPE == 'Motor':
        biaya = durasi * 2000
    else:
        biaya = durasi * 3000
    L2 = Label(hitung, text= biaya)
    L2.config(font=("Helvetica", 15))
    L2.grid(row=1, column=2, pady=1, padx=5, sticky=W)

    L3 = Label(hitung, text="Bayar :")
    L3.config(font=("Helvetica", 15))
    L3.grid(row=2, column=1, pady=1, padx=5, sticky=W)
    E3 = Entry(hitung, bd=1, width=5)
    E3.config(font=("Helvetica", 15))
    E3.grid(row=2, column=2, pady=1, padx=5, sticky=W)

    bayar = Button(hitung, text="Bayar", command=cek_bayar)
    bayar.grid(row=3, column=2, pady=5, padx=10, sticky=W)

    hitung.bind('<Return>', lambda press_key: cek_bayar())
    hitung.mainloop()
