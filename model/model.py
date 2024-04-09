#from database.corso_DAO import CorsoDao
#from database.iscrizioni_DAO import Iscrizioni_DAO
#from database.studente_DAO import StudenteDao

import database.studente_DAO
import database.iscrizioni_DAO
import database.corso_DAO


class Model:
    def __init__(self):
        self.corsi = database.corso_DAO.CorsoDao().getCorsiDAO()
        self.studenti = database.studente_DAO.StudenteDao().getStudentiDAO()
        self.iscrizioni=database.iscrizioni_DAO.Iscrizioni_DAO().getIscrizioniDAO()
        pass



    def getStudenti(self):
        return self.studenti


    def getCorsi(self):
        return self.corsi


    def getIscrizioni(self):
        return self.iscrizioni