from database import meteo_dao


class Model:
    def __init__(self):
        #self.umiditaTorino = self.get_umidita_torino()
        #self.umiditaMilano = self.get_umidita_milano()
        #self.umiditaGenova = self.get_umidita_genova()
        self._dict_riman_torino = {}
        self._dict_riman_milano = {}
        self._dict_riman_genova = {}

    def set_dict(self, mese):
        self._dict_riman_torino = meteo_dao.MeteoDao.getUmiditaTorinoDict(mese)
        self._dict_riman_milano = meteo_dao.MeteoDao.getUmiditaMilanoDict(mese)
        self._dict_riman_genova = meteo_dao.MeteoDao.getUmiditaGenovaDict(mese)


    def getAllSituazioni(self):
        return meteo_dao.MeteoDao.get_all_situazioni()

    def get_umidita_torino(self, mese):
        return meteo_dao.MeteoDao.getUmiditaTorino(mese)

    def get_umidita_milano(self, mese):
        return meteo_dao.MeteoDao.getUmiditaMilano(mese)

    def get_umidita_genova(self, mese):
        return meteo_dao.MeteoDao.getUmiditaGenova(mese)

    def getSituazioniByMonth(self, mese):
        return meteo_dao.MeteoDao.get_Situazioni_By_Mouth(mese)