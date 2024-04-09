import database.DB_connect
import database.studente_DAO

class Iscrizioni_DAO:

    def getIscrizioniDAO(self):

        cnx = database.DB_connect.get_connection()
        cursor = cnx.cursor()
        query ="""SELECT *
                FROM iscrizione"""
        cursor.execute(query)
        result={}
        studente=None

        for row in cursor:
            for alunno in database.studente_DAO.StudenteDao().getStudentiDAO():
                if alunno.matricola==row[0]:
                    studente=alunno


            if result.__contains__(row[1]):
                lista=result[row[1]]
            else:
                lista=[]

            lista.append(studente)
            result[row[1]]=lista

        cursor.close()


        return result