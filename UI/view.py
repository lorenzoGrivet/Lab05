import flet as ft

import database
from database.corso_DAO import CorsoDao


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff

        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("Gestione studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.txt_corso = ft.Dropdown(label="Corso",width=500,hint_text="Inserisci corso")
        self.fillCorso()

        # button for the "hello" reply
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca Iscritti",on_click=self._controller.cercaIscritti)


        row1 = ft.Row([self.txt_corso, self.btn_cerca_iscritti],alignment=ft.MainAxisAlignment.CENTER)

        #Row2
        self.txt_matricola = ft.TextField(label="Matricola")
        self.txt_nome=ft.TextField(label="Nome",read_only=True)
        self.txt_cognome = ft.TextField(label="Cognome", read_only=True)

        row2=ft.Row([self.txt_matricola,self.txt_cognome,self.txt_nome],alignment=ft.MainAxisAlignment.CENTER)

        #Row3
        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca studente")
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca corsi")
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca iscritti")

        row3=ft.Row([self.btn_cerca_studente,self.btn_cerca_corsi,self.btn_cerca_iscritti],alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1,row2,row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def fillCorso(self):
        for a in database.corso_DAO.CorsoDao().getCorsiDAO():
            self.txt_corso.options.append(ft.dropdown.Option(key=a.codins,text=a.nome))
        self.update_page()

    def stampaVideo(self,lista):
        self.lv=ft.ListView(auto_scroll=True,spacing=4,padding=20,expand=100)

        for a in lista:
            self.lv.controls.append(ft.Text(str(a)))

        self._page.add(ft.Text(f"Ci sono {len(lista)} studenti iscritti:", text_align=ft.TextAlign.LEFT))

        self._page.add(self.lv)
        self._page.update()


