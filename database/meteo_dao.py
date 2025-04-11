from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        ORDER BY s.Data ASC"""
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getUmiditaTorino(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                FROM situazione s
                WHERE MONTH(s.Data) = %s AND s.Localita = "Torino"
                ORDER BY s.Data ASC
            """

            cursor.execute(query, (mese,))
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getUmiditaMilano(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """
                SELECT s.Localita, s.Data, s.Umidita
                FROM situazione s
                WHERE MONTH(s.Data) = %s AND s.Localita = "Milano"
                ORDER BY s.Data ASC
            """

            cursor.execute(query, (mese,))
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                          row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getUmiditaGenova(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                FROM situazione s
                WHERE MONTH(s.Data) = %s AND s.Localita = "Genova"
                ORDER BY s.Data ASC
            """

            cursor.execute(query, (mese,))
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_Situazioni_By_Month(mese):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s
                        WHERE MONTH(s.Data) = %s
                        ORDER BY s.Data ASC
                    """

            cursor.execute(query, (mese,))
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getUmiditaTorinoDict(mese):
        cnx = DBConnect.get_connection()
        result = {}
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s
                        WHERE MONTH(s.Data) = %s AND s.Localita = "Torino"
                        ORDER BY s.Data DESC
                    """

            cursor.execute(query, (mese,))
            for row in cursor:
                result["Data"] = Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"])
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getUmiditaMilanoDict(mese):
        cnx = DBConnect.get_connection()
        result = {}
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s
                        WHERE MONTH(s.Data) = %s AND s.Localita = "Milano"
                        ORDER BY s.Data DESC
                    """

            cursor.execute(query, (mese,))
            for row in cursor:
                result["Data"] = Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"])
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def getUmiditaGenovaDict(mese):
        cnx = DBConnect.get_connection()
        result = {}
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s
                        WHERE MONTH(s.Data) = %s AND s.Localita = "Genova"
                        ORDER BY s.Data DESC
                    """

            cursor.execute(query, (mese,))
            for row in cursor:
                    result["Data"] = Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"])
            cursor.close()
            cnx.close()
        return result