import platform
import sys
from PyQt5 import QtWidgets, QtCore, uic
import functions.textspeech as ts


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
        'mysql': 'db_modul_mysql',
        'mariadb': 'db_modul_mariadb'
    }
    return db_systems.get(db.lower())



class MainDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi("Main.ui", self)
        # Slots einrichten
        #self.ui.buttonOK.clicked.connect(self.onOK)
        #self.ui.buttonAbbrechen.clicked.connect(self.onAbbrechen)
        self.ui.btn_stammdaten.clicked.connect(self.onStammdaten)
        self.ui.pb_info.clicked.connect(self.ShowInfo)

    def onStammdaten(self):
        pass

    def ShowInfo(self):
        def clickedOK():
            infodialog.close()

        infodialog = uic.loadUi("info.ui")
        infodialog.btn_OK.clicked.connect(clickedOK)
        infodialog.show()


    def onOK(self):
        # Daten auslesen
        print("Vorname: {}".format(self.ui.vorname.text()))
        print("Nachname: {}".format(self.ui.nachname.text()))
        print("Adresse: {}".format(self.ui.adresse.toPlainText()))
        datum = self.ui.geburtsdatum.date().toString("dd.MM.yyyy")
        print("Geburtsdatum: {}".format(datum))
        if self.ui.agb.checkState():
            print("AGBs akzeptiert")
        if self.ui.katalog.checkState():
            print("Katalog bestellt")
        self.close()

    def onAbbrechen(self):
        self.close()


def main():

    operating_system = check_os()
    mfvv_config = load_config("mfvv.cfg")
    db_sys = db_system(mfvv_config.get("db_system"))
    if mfvv_config.get("sound") == "on":
        ts.txt2speech("Willkomen zur Modellflugvereinsverwaltung", 'de', slow=False)
    app = QtWidgets.QApplication(sys.argv)
    dialog = MainDialog()
    dialog.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()