from database.corso_DAO import CorsoDao
from database.iscrizioni_DAO import Iscrizioni_DAO
from database.studente_DAO import StudenteDao


class Model:
    def __init__(self):
        self.corsi = CorsoDao().getCorsiDAO()
        self.studenti = StudenteDao().getStudentiDAO()
        self.iscrizioni=Iscrizioni_DAO().getIscrizioniDAO()
        pass



    def getStudenti(self):
        return self.studenti


    def getCorsi(self):
        return self.corsi


    def getIscrizioni(self):
        return self.iscrizioni