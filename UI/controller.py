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
        self._mese = 0
        self.costo = 0
        self.res = []
        #self._giorno = 1
        self.situa = 0
        self.temp_cos_to=0
        self.temp_cos_mi=0
        self.temp_cos_ge=0
        miglior_costo = [float("inf")]
        miglior_percorso = []
        self.umidita = {
            "Torino": [68, 70, 65, ..., 72],
            "Milano": [...],
            "Genova": [...],
        }

    def handle_umidita_media(self, e):
        #visualizzare il valore di umidità media in quel mese per tutte le città
        avg_Torino = self._model.get_umidita_torino(self._mese)
        avg_Milano = self._model.get_umidita_milano(self._mese)
        avg_Genova = self._model.get_umidita_genova(self._mese)
        tot = 0
        num = 0
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



    def handle_sequenza(self, giorniCorrenti, giornoTemp):
        #calcola la sequenza ottimale per le analisi


        if self._giorno>15:
            self._view.lst_result.controls.append(ft.Text(f"La sequenza ottima ha costo {self.costo} ed è:"))
            for line in self.res:
                self._view.lst_result.controls.append(ft.Text(str(line)))

        for s in self.situa.get_byGiorno(self.giornoTemp):
            if self.res[self.giorno].localita == "Torino":
                self.temp_cos_to += self.s[self.giorno].umidita
            if self.res[self.giorno].localita == "Milano":
                self.temp_cos_mi= self.s[self.giorno].umidita
            if self.res[self.giorno].localita == "Genova":
                self.temp_cos_ge= self.s[self.giorno].umidita
            if self.temp_cos_to < self.temp_cos_mi and self.temp_cos_to <self.temp_cos_ge and self.res[self.giorno].localita == "Torino":
                if giorniCorrenti<6:
                    self.costo =0





        pass

    def read_mese(self, e):
        self._mese = int(e.control.value)
        self.situa = self._model.getSituazioniByMouth(self._mese)

    def cerca_sequenza(self,
            giorno,  # giorno attuale (0...14)
            citta_corrente,  # città attuale
            giorni_consecutivi,  # quanti giorni consecutivi in questa città
            giorni_per_citta,  # dizionario: città -> giorni totali usati
            costo_parziale,  # costo fino ad ora
            percorso,  # percorso scelto fino a ora
            miglior_costo,  # costo minimo trovato
            miglior_percorso  # percorso minimo trovato
    ):
        if giorno == 15:
            if costo_parziale < miglior_costo[0]:
                miglior_costo[0] = costo_parziale
                miglior_percorso[:] = percorso[:]
            return


        # Tentativo: restare nella stessa città
        if giorni_per_citta[citta_corrente] < 6:
            umid = self.umidita[citta_corrente][giorno]
            giorni_per_citta[citta_corrente] += 1
            percorso.append(citta_corrente)
            self.cerca_sequenza(
                giorno + 1, citta_corrente, giorni_consecutivi + 1,
                giorni_per_citta, costo_parziale + umid,
                percorso, miglior_costo, miglior_percorso
            )
            percorso.pop()
            giorni_per_citta[citta_corrente] -= 1

        # Tentativo: cambiare città (solo se sono passati almeno 3 giorni consecutivi)
        if giorni_consecutivi >= 3:
            for nuova_citta in ["Milano", "Torino", "Genova"]:
                if nuova_citta != citta_corrente and giorni_per_citta[nuova_citta] < 6:
                    umid = self.umidita[nuova_citta][giorno]
                    giorni_per_citta[nuova_citta] += 1
                    percorso.append(nuova_citta)
                    self.cerca_sequenza(
                        giorno + 1, nuova_citta, 1,
                        giorni_per_citta, costo_parziale + umid + 100,
                        percorso, miglior_costo, miglior_percorso
                    )
                    percorso.pop()
                    giorni_per_citta[nuova_citta] -= 1

