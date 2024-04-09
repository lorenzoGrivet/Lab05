import flet as ft

from model import model


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def cercaIscritti(self,e):
        corso= self._view.txt_corso.value
        risultato=[]
        b=False

        for a in model.Model().getIscrizioni().keys():
            if a==corso:
                b=True
                risultato=model.Model().getIscrizioni()[a]

                self._view.stampaVideo(risultato)

        if b==False:
            self._view.create_alert("Corso vuoto!!")


    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()
