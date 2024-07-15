from tkinter import *
import tkinter.font

root = Tk()
root.geometry("300x550")

changefont = tkinter.font.Font(size=20)
jud1 = Label(root, text="DAFTAR", font=changefont)
jud1.place(x=80, y=10)

labelfr = LabelFrame(root, text="result", padx=20, pady=20)
labelfr.place(x=15, y=330)

nama = Label(root, text="NAMA DEPAN")
nama2 = Label(root, text="NAMA BELAKANG")
nomor = Label(root, text="NOMOR SELULER ATAU EMAIL")
kata = Label(root, text="KATA SANDI")
tanggal_label = Label(root, text="TANGGAL LAHIR")
jenis = Label(root, text="JENIS KELAMIN")

e1 = Entry(root, width=40)
e2 = Entry(root, width=40)
e3 = Entry(root, width=40)
e4 = Entry(root, width=40)
e5 = Entry(root, width=40)

nama.place(x=20, y=50)
nama2.place(x=20, y=90)
nomor.place(x=20, y=130)
kata.place(x=20, y=170)
tanggal_label.place(x=20, y=210)  # Menambah label untuk tanggal lahir
jenis.place(x=20, y=250)

e1.place(x=20, y=70)
e2.place(x=20, y=110)
e3.place(x=20, y=150)
e4.place(x=20, y=190)

list1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
         "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
c1 = StringVar()
droplist = OptionMenu(root, c1, *list1)
droplist.config(width=5)
c1.set("Tanggal")
droplist.place(x=15, y=225)

list2 = ["JANUARI", "FEBRUARI", "MARET", "APRIL", "MEI", "JUNI", "JULI", "AGUSTUS", "SEBTEMBER", "OKTOBER", "NOVEMBER",
         "DESEMBER"]
c2 = StringVar()
droplist = OptionMenu(root, c2, *list2)
droplist.config(width=10)
c2.set("Bulan")
droplist.place(x=90, y=225)

list3 = ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019",
         "2020", "2021", "2022", "2023", "2024"]
c3 = StringVar()
droplist = OptionMenu(root, c3, *list3)
droplist.config(width=5)
c3.set("Tahun")
droplist.place(x=195, y=225)

r = StringVar()
r.set("perempuan")

rb = Radiobutton(root, text="perempuan", variable=r, value="perempuan").place(x=20, y=270)
rb2 = Radiobutton(root, text="laki-laki", variable=r, value="laki-laki").place(x=110, y=270)
rb2 = Radiobutton(root, text="khusus", variable=r, value="khusus").place(x=180, y=270)


def cetak():
    class orang:
        def __init__(self, nama, nama2, nomor, kata, tanggal, jenis):
            self.nama = nama
            self.nama2 = nama2
            self.nomor = nomor
            self.kata = kata
            self.tanggal = tanggal
            self.jenis = jenis

        def hasil(self):
            # Mendapatkan nilai dari opsi tanggal, bulan, dan tahun yang dipilih
            tanggal_lahir = c1.get() + " " + c2.get() + " " + c3.get()
            lbl = Label(labelfr,
                        text="NAMA DEPAN =" + self.nama + "\nNAMA BELAKANG =" + self.nama2 + "\nNOMOR SELULER ATAU EMAIL =" +
                             self.nomor + "\nKATA SANDI =" + self.kata + "\nTANGGAL LAHIR =" + tanggal_lahir +
                             "\nJENIS KELAMIN =" + self.jenis).grid()

    ditamilkan = orang(e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), r.get())
    ditamilkan.hasil()


btn = Button(root, text="DAFTAR", command=cetak).place(x=100, y=305)

root.mainloop()
