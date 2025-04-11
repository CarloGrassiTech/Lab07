from datetime import datetime

import flet as ft


from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 1
        self.costo = 0
        self.res = []
        self._cambiCity= 0


    def handle_umidita_media(self, e):
        #visualizzare il valore di umidità media in quel mese per tutte le città
        avg_Torino = self._model.get_umidita_torino(self._mese)
        avg_Milano = self._model.get_umidita_milano(self._mese)
        avg_Genova = self._model.get_umidita_genova(self._mese)
        tot = 0
        num = 0
        self._view.lst_result.clean()
        for i in avg_Torino:
            tot += i.umidita
            num +=1
        self._view.lst_result.controls.append(ft.Text(f"La media di umidità per il mese di {self._mese}, nella città di Torino è: {tot/num}"))
        tot = 0
        num = 0
        for i in avg_Milano:
            tot += i.umidita
            num += 1
        self._view.lst_result.controls.append(ft.Text(
            f"La media di umidità per il mese di {self._mese}, nella città di Milano è: {tot / num}"))

        tot = 0
        num = 0
        for i in avg_Genova:
            tot += i.umidita
            num += 1
        self._view.lst_result.controls.append(ft.Text(
            f"La media di umidità per il mese di {self._mese}, nella città di Genova è: {tot / num}"))
        self._view.update_page()



    def handle_sequenza(self, giorniCorrenti, cittaCorrente, giorniFila):
        #calcola la sequenza ottimale per le analisi
        dictRimTorino = self._model._dict_riman_torino
        dictRimMilano = self._model._dict_riman_milano
        dictRimGenova = self._model._dict_riman_genova
        if self._view.lst_result != None:
            self._view.lst_result.clean()
        if giorniCorrenti>15:
            self.costo = 100*self._cambiCity
            for i in self.res:
                self.costo+=float(i.umidita)
            self._view.lst_result.controls.append(ft.Text(f"La sequenza ottima ha costo {self.costo} ed è:"))
            for line in self.res:
                self._view.lst_result.controls.append(ft.Text(str(line)))
            self._view.update_page()

        else:
            print(f" mese: { int(self._mese)}, giorno: {len(self.res)+1}")
            data = datetime.date(2013, int(self._mese) , len(self.res)+1)
            if len(self.res) ==0:
                if data in dictRimTorino and data in dictRimMilano and data in dictRimGenova:
                    self.res.append(min(dictRimTorino[data], dictRimMilano[data], dictRimGenova[data]))
                else:
                    print(f"Data {data} non presente in tutti i dizionari.")
                self.res.append(min(dictRimTorino[data],dictRimMilano[data],dictRimGenova[data]))
                giorniCorrenti = 1
                giorniFila = 1
                cittaCorrente = self.res[0].citta
            else:
                if giorniFila <3:
                    if cittaCorrente == "Torino":
                        self.res.append(dictRimTorino[data])
                    elif cittaCorrente == "Milano":
                        self.res.append(dictRimMilano[data])
                    elif cittaCorrente == "Genova":
                        self.res.append(dictRimGenova[data])
                    giorniCorrenti+=1
                    giorniFila+=1
                    self.handle_sequenza(giorniCorrenti, cittaCorrente, giorniFila)

                elif giorniFila == 6:
                    self._cambiCity +=1
                    if cittaCorrente == "Torino":
                        self.res.append(min(dictRimMilano[data],dictRimGenova[data]))
                        cittaCorrente= self.res[len(self.res)-1].citta
                        giorniCorrenti += 1
                        giorniFila = 1
                    elif cittaCorrente == "Milano":
                        self.res.append(min(dictRimGenova[data],dictRimTorino[data]))
                        cittaCorrente = self.res[len(self.res) - 1].citta
                        giorniCorrenti += 1
                        giorniFila = 1
                    elif cittaCorrente == "Genova":
                        self.res.append(min(dictRimTorino[data],dictRimMilano[data]))
                        cittaCorrente = self.res[len(self.res) - 1].citta
                        giorniCorrenti += 1
                        giorniFila = 1
                    self.handle_sequenza(giorniCorrenti, cittaCorrente, giorniFila)
                else:
                    #tutti i casi intermedi tra 3 e 6
                    self.res.append(min(dictRimTorino[data], dictRimMilano[data], dictRimGenova[data]))
                    giorniCorrenti += 1
                    if cittaCorrente == self.res[len(self.res) - 1].citta:
                        giorniFila += 1
                    else:
                        self._cambiCity += 1
                        cittaCorrente = self.res[len(self.res) - 1].citta
                        giorniFila = 1
                    self.handle_sequenza(giorniCorrenti, cittaCorrente, giorniFila)


    def read_mese(self, e):
        self._mese = int(e.control.value)
        self._model.set_dict(self._mese)

