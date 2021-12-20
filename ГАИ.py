import tkinter as tk
from tkinter import ttk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

        def init_main(self):
            toolbar = tk.Frame(self, bg="#d7d8e0", bd=10)
            toolbar.pack(side=tk.TOP, fill=tk.X)

            btn_open_dialog1 = tk.Button(toolbar, text="Заявка", command=lambda: self.open_dialog1(), bg="#d7d8e0",
                                         bd=0,
                                         compound=tk.LEFT)
            btn_open_dialog1.pack(side=tk.LEFT)

            self.add_img = tk.PhotoImage(file="icons8-администратор-microsoft-50.png")
            btn_open_dialog2 = tk.Button(toolbar, text="ЗаявкаГАИ", command=lambda: self.open_dialog2(), bg="#d7d8e0",
                                         bd=0,
                                         compound=tk.LEFT)
            btn_open_dialog2.pack(side=tk.LEFT)

            self.add_img2 = tk.PhotoImage(file="icons8-администратор-microsoft-50.png")
            btn_open_dialog3 = tk.Button(toolbar, text="Администратор", command=lambda: self.open_dialog3(),
                                         bg="#d7d8e0",
                                         bd=0, compound=tk.LEFT)
            btn_open_dialog3.pack(side=tk.LEFT)

        def open_dialog2(self):
            ZaiavkaGAI()

        def open_dialog1(self):
            Zaiavka()

        def open_dialog3(self):
            Admin()

    class Sotrudniki(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_Sotrudniki()

        def open_dialog8(self):
            Dobavlenie_Sotrudnika()

        def init_Sotrudniki(self):
            self.title("Сотрудники")
            self.geometry("600x420+400+300")
            self.resizable(False, False)

            toolbar2 = tk.Frame(self, bg='#d8d9e9', bd=0)
            toolbar2.pack(side=tk.TOP, fill=tk.X)
            self.add_img6 = tk.PhotoImage(file="siren_emergency_lights_hooter_police_icon_191334.png")
            btn_open_dialog8 = tk.Button(toolbar2, text="Добавить сотрудника", command=lambda: self.open_dialog8(),
                                         bg="#d7d8e0", bd=0,
                                         compound=tk.LEFT)
            btn_open_dialog8.pack(side=tk.LEFT)

            self.grab_set()
            self.focus_set()

        self.tree = ttk.Treeview(self, columns=("ID", "FIO driver", "nomber ud", "nomber pass", "age jods",), height=15,
                                 show="headings")
        self.tree.column("ID", width=20, anchor=tk.CENTER)
        self.tree.column("FIO driver", width=150, anchor=tk.CENTER)
        self.tree.column("nomber ud", width=150, anchor=tk.CENTER)
        self.tree.column("nomber pass", width=120, anchor=tk.CENTER)
        self.tree.column("age jods", width=170, anchor=tk.CENTER)

        self.tree.heading("ID", text="ID")
        self.tree.heading("FIO driver", text="ФИО водителя эвак.")
        self.tree.heading("nomber ud", text="Номер удостоверения")
        self.tree.heading("nomber pass", text="Номер паспорта")
        self.tree.heading("age jods", text="Трудовой стаж")
        self.tree.pack()
        file = open("Sotrudniki.data")
        file.read()

    class ZaiavkiADM(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_ZaiavkiADM()

        def init_ZaiavkiADM(self):
            self.title("Заявления на эвакуацию")
            self.geometry("797x420+400+300")
            self.resizable(False, False)

            self.grab_set()
            self.focus_set()

            self.tree = ttk.Treeview(self,
                                     columns=("ID", "FIO driver", "nomber ud", "nomber pass", "nomber car", "Data",
                                              "Vid"),
                                     height=15, show="headings")
            self.tree.column("ID", width=25, anchor=tk.CENTER)
            self.tree.column("FIO driver", width=120, anchor=tk.CENTER)
            self.tree.column("nomber ud", width=135, anchor=tk.CENTER)
            self.tree.column("nomber pass", width=120, anchor=tk.CENTER)
            self.tree.column("nomber car", width=120, anchor=tk.CENTER)
            self.tree.column("Data", width=150, anchor=tk.CENTER)
            self.tree.column("Vid", width=150, anchor=tk.CENTER)

            self.tree.heading("ID", text="ID")
            self.tree.heading("FIO driver", text="ФИО водителя")
            self.tree.heading("nomber ud", text="Номер удостоверения")
            self.tree.heading("nomber pass", text="Номер паспорта")
            self.tree.heading("nomber car", text="Номер машины")
            self.tree.heading("Data", text="Дата подачи заявления")
            self.tree.heading("Vid", text="Вид заявления")
            self.tree.pack()
            file = open("Zaiavki.data")
            file.read()

    class Protocol(tk.Toplevel):
        def __init__(self):
            super().__init__()
            self.init_Protocol()

        def open_dialog7(self):
            Dobavlenie_Protocol()

        def init_Protocol(self):
            self.title("Протокол")
            self.geometry("900x420+400+300")
            self.resizable(True, True)

            self.grab_set()
            self.focus_set()
            toolbar2 = tk.Frame(self, bg='#d8d9e9', bd=0)
            toolbar2.pack(side=tk.TOP, fill=tk.X)
            self.add_img6 = tk.PhotoImage(file="siren_emergency_lights_hooter_police_icon_191334.png")
            btn_open_dialog7 = tk.Button(toolbar2, text="Заполнить протокол эвакуации",
                                         command=lambda: self.open_dialog7(),
                                         bg="#d7d8e0", bd=0,
                                         compound=tk.LEFT)
            btn_open_dialog7.pack(side=tk.LEFT)
            self.tree = ttk.Treeview(self,
                                     columns=("ID", "nomber car arrest", "FIO driver", "nomber car", "adress arest",
                                              "adres stop", "Data arrest"), height=15,
                                     show="headings")
            self.tree.column("ID", width=20, anchor=tk.CENTER)
            self.tree.column("nomber car arrest", width=150, anchor=tk.CENTER)
            self.tree.column("FIO driver", width=150, anchor=tk.CENTER)
            self.tree.column("nomber car", width=120, anchor=tk.CENTER)
            self.tree.column("adress arest", width=170, anchor=tk.CENTER)
            self.tree.column("adres stop", width=170, anchor=tk.CENTER)
            self.tree.column("Data arrest", width=150, anchor=tk.CENTER)

            self.tree.heading("ID", text="ID")
            self.tree.heading("nomber car arrest", text="Номер эвак. машины")
            self.tree.heading("FIO driver", text="ФИО водителя")
            self.tree.heading("nomber car", text="Номер эвакуатора")
            self.tree.heading("adress arest", text="Место эвакуации")
            self.tree.heading("adres stop", text="Место доставки")
            self.tree.heading("Data arrest", text="Дата эвакуации")
            ysb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
            self.tree.configure(yscroll=ysb.set)
            self.tree.pack()
            file = open("Protokol.data")
            file.read()

    class ZaiavkaGAI(tk.Toplevel):
        def __init__(self):
            super().__init__(root)
            self.init_ZaiavkaGAI()

        def init_ZaiavkaGAI(self):
            self.title("Заполнить заявку ГАИ")
            self.geometry("400x320+400+300")
            self.resizable(False, False)

            label1 = tk.Label(self, text="Сотрудник ГАИ", fg="#eee", bg="#333")
            label1.pack()

            label_FIO_driver = tk.Label(self, text="ФИО водителя")
            label_FIO_driver.place(x=80, y=30)

            label_entry_ud = tk.Label(self, text="Номер удостоверения")
            label_entry_ud.place(x=60, y=60)

            label_entry_pass = tk.Label(self, text="Номер паспорта")
            label_entry_pass.place(x=80, y=90)

            label_entry_nomder_car = tk.Label(self, text="Номер машины")
            label_entry_nomder_car.place(x=80, y=120)

            label_Data = tk.Label(self, text="Дата заполнения")
            label_Data.place(x=80, y=150)

            self.entry_FIO_driver = ttk.Entry(self)
            self.entry_FIO_driver.place(x=190, y=30)

            self.entry_ud = ttk.Entry(self)
            self.entry_ud.place(x=190, y=60)

            self.entry_pass = ttk.Entry(self)
            self.entry_pass.place(x=190, y=90)

            self.entry_nomder_car = ttk.Entry(self)
            self.entry_nomder_car.place(x=190, y=120)

            self.Data = ttk.Entry(self)
            self.Data.place(x=190, y=150)

            btn_cansel = ttk.Button(self, text="Закрыть", command=self.destroy)
            btn_cansel.place(x=240, y=250)

            btn_add = ttk.Button(self, text="Добавить")
            btn_add.place(x=70, y=250)

            self.grab_set()
            self.focus_set()

    class Admin(tk.Toplevel):
        def __init__(self):
            super().__init__()
            self.init_Admin()

        def open_dialog4(self):
            Protocol()

        def open_dialog5(self):
            Sotrudniki()

        @staticmethod
        def open_dialog6():
            ZaiavkiADM()

    def init_Admin(self):
        toolbar1 = tk.Frame(self, bg='#d8d9e9', bd=0)
        toolbar1.pack(side=tk.TOP, fill=tk.X)
        self.add_img3 = tk.PhotoImage(file="siren_emergency_lights_hooter_police_icon_191334.png")
        btn_open_dialog4 = tk.Button(toolbar1, text="Протокол эвакуации", command=lambda: self.open_dialog4(),
                                     bg="#d7d8e0", bd=0, compound=tk.LEFT)
        btn_open_dialog4.pack(side=tk.TOP)
        self.add_img4 = tk.PhotoImage(file="siren_emergency_lights_hooter_police_icon_191334.png")
        btn_open_dialog5 = tk.Button(toolbar1, text="Сотрудники", command=lambda: self.open_dialog5(), bg="#d7d8e0",
                                     bd=0,
                                     compound=tk.LEFT)
        btn_open_dialog5.pack(side=tk.TOP)

        self.add_img5 = tk.PhotoImage(file="siren_emergency_lights_hooter_police_icon_191334.png")
        btn_open_dialog6 = tk.Button(toolbar1, text="Заявления на эвакуацию", command=lambda: self.open_dialog6(),
                                     bg="#d7d8e0", bd=0,
                                     compound=tk.LEFT)
        btn_open_dialog6.pack(side=tk.TOP)


class Zaiavka(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_Zaiavka()

    def init_Zaiavka(self):
        self.title("Заполнить заявку")
        self.geometry("400x320+400+300")
        self.resizable(False, False)
        label1 = tk.Label(self, text="Частное лицо", fg="#eee", bg="#333")
        label1.pack()

        label_FIO_driver = tk.Label(self, text="ФИО водителя")
        label_FIO_driver.place(x=80, y=30)

        label_entry_ud = tk.Label(self, text="Номер удостоверения")
        label_entry_ud.place(x=50, y=60)

        label_entry_pass = tk.Label(self, text="Номер паспорта")
        label_entry_pass.place(x=80, y=90)

        label_entry_nomder_car = tk.Label(self, text="Номер машины")
        label_entry_nomder_car.place(x=80, y=120)

        label_Data = tk.Label(self, text="Дата заполнения")
        label_Data.place(x=80, y=150)

        self.FIO_driver = ttk.Entry(self)
        self.FIO_driver.place(x=180, y=30)

        self.entry_ud = ttk.Entry(self)
        self.entry_ud.place(x=180, y=60)

        self.entry_pass = ttk.Entry(self)
        self.entry_pass.place(x=180, y=90)

        self.entry_nomder_car = ttk.Entry(self)
        self.entry_nomder_car.place(x=180, y=120)

        self.Data = ttk.Entry(self)
        self.Data.place(x=180, y=150)

        self.grab_set()
        self.focus_set()

        btn_cansel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cansel.place(x=240, y=250)

        btn_add = ttk.Button(self, text="Добавить")
        btn_add.place(x=70, y=250)


class Dobavlenie_Protocol(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_Dobavlenie_Protocol()

    def init_Dobavlenie_Protocol(self):
        self.title("Заполнить протокол")
        self.geometry("400x320+400+300")
        self.resizable(False, False)

        label_nomber_car_driver = tk.Label(self, text="Номер машины")
        label_nomber_car_driver.place(x=80, y=30)

        label_entry_FIO = tk.Label(self, text="ФИО водителя")
        label_entry_FIO.place(x=80, y=60)

        label_entry_nomber_car_arrest = tk.Label(self, text="Номер эвак. машины")
        label_entry_nomber_car_arrest.place(x=55, y=90)

        label_entry_adress_arest = tk.Label(self, text="Место эвакуации")
        label_entry_adress_arest.place(x=80, y=120)

        label_entry_jail_adress = tk.Label(self, text="Место доставки")
        label_entry_jail_adress.place(x=80, y=150)

        label_entry_Data = tk.Label(self, text="Дата эвакуации")
        label_entry_Data.place(x=80, y=180)

        self.entry_nomber_car_driver = ttk.Entry(self)
        self.entry_nomber_car_driver.place(x=180, y=30)

        self.entry_FIO = ttk.Entry(self)
        self.entry_FIO.place(x=180, y=60)

        self.entry_nomber_car_arrest = ttk.Entry(self)
        self.entry_nomber_car_arrest.place(x=180, y=90)

        self.entry_adress_arest = ttk.Entry(self)
        self.entry_adress_arest.place(x=180, y=120)

        self.entry_jail_adress = ttk.Entry(self)
        self.entry_jail_adress.place(x=180, y=150)

        self.entry_Data = ttk.Entry(self)
        self.entry_Data.place(x=180, y=180)

        btn_cansel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cansel.place(x=240, y=250)

        btn_add = ttk.Button(self, text="Добавить")
        btn_add.place(x=70, y=250)

        self.grab_set()
        self.focus_set()


class Dobavlenie_Sotrudnika(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_Dobavlenie_Sotrudnika()

    def init_Dobavlenie_Sotrudnika(self):
        self.title("Добавить сотрудника")
        self.geometry("400x320+400+300")
        self.resizable(False, False)

        label_FIO_driver = tk.Label(self, text="ФИО сотрудника")
        label_FIO_driver.place(x=80, y=30)

        label_entry_nomber_ud = tk.Label(self, text="Номер удостоверения")
        label_entry_nomber_ud.place(x=50, y=60)

        label_entry_nomber_pass = tk.Label(self, text="Номер паспорта")
        label_entry_nomber_pass.place(x=80, y=90)

        label_entry_age_jobs = tk.Label(self, text="Трудовой стаж")
        label_entry_age_jobs.place(x=90, y=120)

        self.FIO_driver = ttk.Entry(self)
        self.FIO_driver.place(x=180, y=30)

        self.entry_nomber_ud = ttk.Entry(self)
        self.entry_nomber_ud.place(x=180, y=60)

        self.entry_nomber_pass = ttk.Entry(self)
        self.entry_nomber_pass.place(x=180, y=90)

        self.entry_entry_age_jobs = ttk.Entry(self)
        self.entry_entry_age_jobs.place(x=180, y=120)

        btn_cansel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cansel.place(x=240, y=250)

        btn_add = ttk.Button(self, text="Добавить")
        btn_add.place(x=70, y=250)

    def insert_data(self): self.treeview.insert('', 'end', iid=self.iid, text="Item_" + str(self.id), values=(
        self.name_entry.get(), self.idnumber_entry.get()))

    self.grab_set()
    self.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack(side=tk.TOP, fill=tk.X)
    root.title("Эвакуаторное агенство")
    root.geometry("450x250+100+200")
    root.resizable(False, False)
    root.mainloop()