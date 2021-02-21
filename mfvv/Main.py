# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(504, 346)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/Airplane_Silhouette_L_64x64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_stammdaten = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stammdaten.setGeometry(QtCore.QRect(130, 70, 51, 61))
        self.btn_stammdaten.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/shiny/64x64/icon-17.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_stammdaten.setIcon(icon1)
        self.btn_stammdaten.setIconSize(QtCore.QSize(64, 64))
        self.btn_stammdaten.setObjectName("btn_stammdaten")
        self.pb_Mitglieder = QtWidgets.QPushButton(self.centralwidget)
        self.pb_Mitglieder.setGeometry(QtCore.QRect(30, 70, 61, 61))
        self.pb_Mitglieder.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/sketch/PNG - color/64px/handy-icon_08.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_Mitglieder.setIcon(icon2)
        self.pb_Mitglieder.setIconSize(QtCore.QSize(64, 64))
        self.pb_Mitglieder.setObjectName("pb_Mitglieder")
        self.pb_dokumente = QtWidgets.QPushButton(self.centralwidget)
        self.pb_dokumente.setGeometry(QtCore.QRect(220, 70, 51, 61))
        self.pb_dokumente.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/shiny/64x64/icon-18.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_dokumente.setIcon(icon3)
        self.pb_dokumente.setIconSize(QtCore.QSize(64, 64))
        self.pb_dokumente.setObjectName("pb_dokumente")
        self.pb_termine = QtWidgets.QPushButton(self.centralwidget)
        self.pb_termine.setGeometry(QtCore.QRect(310, 70, 61, 61))
        self.pb_termine.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/sketch/PNG - color/64px/handy-icon_04.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_termine.setIcon(icon4)
        self.pb_termine.setIconSize(QtCore.QSize(64, 64))
        self.pb_termine.setObjectName("pb_termine")
        self.pb_einstellungen = QtWidgets.QPushButton(self.centralwidget)
        self.pb_einstellungen.setGeometry(QtCore.QRect(400, 70, 61, 61))
        self.pb_einstellungen.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/sketch/PNG - color/64px/handy-icon_13.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_einstellungen.setIcon(icon5)
        self.pb_einstellungen.setIconSize(QtCore.QSize(64, 64))
        self.pb_einstellungen.setObjectName("pb_einstellungen")
        self.pb_info = QtWidgets.QPushButton(self.centralwidget)
        self.pb_info.setGeometry(QtCore.QRect(30, 180, 61, 61))
        self.pb_info.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/sketch/PNG - color/64px/handy-icon_01.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_info.setIcon(icon6)
        self.pb_info.setIconSize(QtCore.QSize(64, 64))
        self.pb_info.setObjectName("pb_info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 504, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pb_Mitglieder, self.btn_stammdaten)
        MainWindow.setTabOrder(self.btn_stammdaten, self.pb_dokumente)
        MainWindow.setTabOrder(self.pb_dokumente, self.pb_termine)
        MainWindow.setTabOrder(self.pb_termine, self.pb_info)
        MainWindow.setTabOrder(self.pb_info, self.pb_einstellungen)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modellflugvereinsverwaltung Mfvv"))
        self.btn_stammdaten.setToolTip(_translate("MainWindow", "Stammdaten"))
        self.pb_Mitglieder.setToolTip(_translate("MainWindow", "Mitglieder"))
        self.pb_dokumente.setToolTip(_translate("MainWindow", "Dokumente"))
        self.pb_termine.setToolTip(_translate("MainWindow", "Kalender"))
        self.pb_einstellungen.setToolTip(_translate("MainWindow", "Einstellungen"))
        self.pb_info.setToolTip(_translate("MainWindow", "Info"))