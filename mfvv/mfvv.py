# Ja, das MVC Pattern fehlt noch. ;-)
# Kommt dann im nächsten Schritt

import platform
import sys
from PyQt5 import QtWidgets, QtCore, uic
import functions.textspeech as ts
import functions.mfvvfunc as mf


def load_config(cfg_file: str) -> dict:
    res_dict = {}
    with open(cfg_file, "r") as fobj:
        for line in fobj:
            tmp = line.replace("\n", "").split(':')
            key = tmp[0]
            value = tmp[1]
            res_dict.update({key:value})
    return res_dict


def check_os():
    return platform.system().lower()


def db_system(db: str):
    db_systems = {
        'sqlite3':'db_modul_sqlite',
        'PostgreSQL':'db_modul_postgresql',
        'mysql': 'db_modul_mysql',
        'mariadb': 'db_modul_mariadb'
    }
    return db_systems.get(db.lower())


class MainDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("Main.ui", self)
        # Slots einrichten
        self.ui.btn_stammdaten.clicked.connect(self.onStammdaten)
        self.ui.pb_info.clicked.connect(self.ShowInfo)
        self.ui.actionProgramm_beenden.triggered.connect(self.onBeenden)
        self.ui.actionInfo_ueber.triggered.connect(self.ShowInfo)
        self.ui.actionNeuMitglied.triggered.connect(self.NewMitglied)

    def onStammdaten(self):
        pass

    def ShowInfo(self):
        infodialog = InfoDialog()
        infodialog.show()

    def NewMitglied(self):
        nm_dialog = MitgliedForm()
        nm_dialog.show()

    def onBeenden(self):
        self.close()


class InfoDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("info.ui", self)
        self.ui.btn_OK.clicked.connect(self.clickedOK)

    def clickedOK(self):
        self.ui.close()


class MitgliedForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("Mitglied.ui", self)
        self.ui.pB_OK.clicked.connect(self.clickedOK)
        self.ui.pB_Abbrechen.clicked.connect(self.clickedAbbrechen)
        #self.ui.lcd_Alter.display(mf.calculate_age(self.ui.dE_geburtstag.date))

    def clickedOK(self):
        # Eingaben in Datenbank schreiben
        data = {
            "anrede": self.ui.cB_Anrede.currentText(),
            "vorname": self.ui.lE_Vorname.text(),
            "name": self.ui.lE_Nachname.text(),
            "strasse": self.ui.lE_Strasse.text(),
            "plz": self.ui.lE_PLZ.text(),
            "ort": self.ui.lE_Ort.text(),
            "telefon": self.ui.lE_Telefon.text(),
            "mobiltel": self.ui.lE_Mobil.text(),
            "whatsapp_erlaubt": mf.bool2int(self.ui.cB_whatsapp.isChecked()),
            "telegram_erlaubt":  mf.bool2int(self.ui.cB_telegram.isChecked()),
            "email": self.ui.lE_Email.text(),
            "geburtstag": self.ui.dE_geburtstag.date(),
            "geb_anzeigen": mf.bool2int(self.ui.cB_GebKalender.isChecked()),
            "eintritt": self.ui.dE_Eintritt.date(),
            "austritt": self.ui.dE_Austritt.date(),
            "gestorben": self.ui.dE_gestorben.date(),
            "beitrag": float(self.ui.lE_Beitrag.text()),
            "IBAN": self.ui.lE_iban.text(),
            "bank": self.ui.lE_Bank.text(),
            "funktion": self.ui.cBox_Funktion.currentText(),

        }
        self.Write_Mitglied_db(data)
        self.ui.close()

    def clickedAbbrechen(self):
        self.ui.close()

    def Write_Mitglied_db(self, data):
        print(data)



def main():

    operating_system = check_os()
    mfvv_cfg = load_config("mfvv.cfg")
    db_sys = db_system(mfvv_cfg.get("db_system"))
    if mfvv_cfg.get("sound") == "on":
        ts.txt2speech("Willkommen zur Modellflugvereinsverwaltung", 'de', slow=False)
    app = QtWidgets.QApplication(sys.argv)
    dialog = MainDialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()