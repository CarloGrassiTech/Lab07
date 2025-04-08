from database import meteo_dao


class Model:
    def __init__(self):
        #self.umiditaTorino = self.get_umidita_torino()
        #self.umiditaMilano = self.get_umidita_milano()
        #self.umiditaGenova = self.get_umidita_genova()
        pass
    def getAllSituazioni(self):
        return meteo_dao.MeteoDao.get_all_situazioni()
    def get_umidita_torino(self, mese):
        return meteo_dao.MeteoDao.getUmiditaTorino(mese)

    def get_umidita_milano(self, mese):
        return meteo_dao.MeteoDao.getUmiditaMilano(mese)

    def get_umidita_genova(self, mese):
        return meteo_dao.MeteoDao.getUmiditaGenova(mese)
    def getSituazioniByMouth(self, mese):
        return meteo_dao.MeteoDao.get_Situazioni_By_Mouth(mese)