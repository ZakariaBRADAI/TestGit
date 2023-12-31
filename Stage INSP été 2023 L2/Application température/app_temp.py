# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_temp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(819, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(29, 299, 761, 301))
        self.widget.setObjectName("widget")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 0, 762, 291))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.title = QtWidgets.QLabel(self.widget1)
        self.title.setObjectName("title")
        self.horizontalLayout_7.addWidget(self.title)
        self.pushButton_edit_Commands = QtWidgets.QPushButton(self.widget1)
        self.pushButton_edit_Commands.setObjectName("pushButton_edit_Commands")
        self.horizontalLayout_7.addWidget(self.pushButton_edit_Commands)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.widget1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_select_serial_port = QtWidgets.QLabel(self.widget1)
        self.label_select_serial_port.setObjectName("label_select_serial_port")
        self.horizontalLayout.addWidget(self.label_select_serial_port)
        self.comboBox_select_serial_port = QtWidgets.QComboBox(self.widget1)
        self.comboBox_select_serial_port.setObjectName("comboBox_select_serial_port")
        self.comboBox_select_serial_port.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_select_serial_port)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_baudrate = QtWidgets.QLabel(self.widget1)
        self.label_baudrate.setObjectName("label_baudrate")
        self.horizontalLayout_2.addWidget(self.label_baudrate)
        self.lineEdit_baudrate = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_baudrate.setObjectName("lineEdit_baudrate")
        self.horizontalLayout_2.addWidget(self.lineEdit_baudrate)
        self.label_timeout = QtWidgets.QLabel(self.widget1)
        self.label_timeout.setObjectName("label_timeout")
        self.horizontalLayout_2.addWidget(self.label_timeout)
        self.lineEdit_timeout = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_timeout.setObjectName("lineEdit_timeout")
        self.horizontalLayout_2.addWidget(self.lineEdit_timeout)
        self.pushButton_validate_device = QtWidgets.QPushButton(self.widget1)
        self.pushButton_validate_device.setObjectName("pushButton_validate_device")
        self.horizontalLayout_2.addWidget(self.pushButton_validate_device)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_2 = QtWidgets.QFrame(self.widget1)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_new_acquiring = QtWidgets.QPushButton(self.widget1)
        self.button_new_acquiring.setObjectName("button_new_acquiring")
        self.horizontalLayout_3.addWidget(self.button_new_acquiring)
        self.checkBox_plot = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_plot.setObjectName("checkBox_plot")
        self.horizontalLayout_3.addWidget(self.checkBox_plot)
        self.button_stop_acquiring = QtWidgets.QPushButton(self.widget1)
        self.button_stop_acquiring.setObjectName("button_stop_acquiring")
        self.horizontalLayout_3.addWidget(self.button_stop_acquiring)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.line_3 = QtWidgets.QFrame(self.widget1)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_duree = QtWidgets.QLabel(self.widget1)
        self.label_duree.setObjectName("label_duree")
        self.horizontalLayout_4.addWidget(self.label_duree)
        self.SpinBox_duree = QtWidgets.QDoubleSpinBox(self.widget1)
        self.SpinBox_duree.setObjectName("SpinBox_duree")
        self.horizontalLayout_4.addWidget(self.SpinBox_duree)
        self.comboBox_duree = QtWidgets.QComboBox(self.widget1)
        self.comboBox_duree.setObjectName("comboBox_duree")
        self.comboBox_duree.addItem("")
        self.comboBox_duree.addItem("")
        self.comboBox_duree.addItem("")
        self.comboBox_duree.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_duree)
        self.pushButton_change_duree = QtWidgets.QPushButton(self.widget1)
        self.pushButton_change_duree.setObjectName("pushButton_change_duree")
        self.horizontalLayout_4.addWidget(self.pushButton_change_duree)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line_4 = QtWidgets.QFrame(self.widget1)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.line_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_temp_mesuree = QtWidgets.QLabel(self.widget1)
        self.label_temp_mesuree.setObjectName("label_temp_mesuree")
        self.horizontalLayout_5.addWidget(self.label_temp_mesuree)
        self.affiche_temp_mesuree = QtWidgets.QLineEdit(self.widget1)
        self.affiche_temp_mesuree.setReadOnly(True)
        self.affiche_temp_mesuree.setObjectName("affiche_temp_mesuree")
        self.horizontalLayout_5.addWidget(self.affiche_temp_mesuree)
        self.label_date_mesure = QtWidgets.QLabel(self.widget1)
        self.label_date_mesure.setObjectName("label_date_mesure")
        self.horizontalLayout_5.addWidget(self.label_date_mesure)
        self.affiche_date_mesure = QtWidgets.QLineEdit(self.widget1)
        self.affiche_date_mesure.setText("")
        self.affiche_date_mesure.setReadOnly(True)
        self.affiche_date_mesure.setObjectName("affiche_date_mesure")
        self.horizontalLayout_5.addWidget(self.affiche_date_mesure)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.line_5 = QtWidgets.QFrame(self.widget1)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_seuil = QtWidgets.QLabel(self.widget1)
        self.label_seuil.setObjectName("label_seuil")
        self.horizontalLayout_6.addWidget(self.label_seuil)
        self.lineEdit_seuil = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_seuil.setObjectName("lineEdit_seuil")
        self.horizontalLayout_6.addWidget(self.lineEdit_seuil)
        self.label_mail = QtWidgets.QLabel(self.widget1)
        self.label_mail.setObjectName("label_mail")
        self.horizontalLayout_6.addWidget(self.label_mail)
        self.lineEdit_mail = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_mail.setObjectName("lineEdit_mail")
        self.horizontalLayout_6.addWidget(self.lineEdit_mail)
        self.label_password = QtWidgets.QLabel(self.widget1)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_6.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_6.addWidget(self.lineEdit_password)
        self.checkBox_seuil = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_seuil.setObjectName("checkBox_seuil")
        self.horizontalLayout_6.addWidget(self.checkBox_seuil)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.line_6 = QtWidgets.QFrame(self.widget1)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout.addWidget(self.line_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 819, 21))
        self.menubar.setObjectName("menubar")
        self.menuEnregistrer_l_acquisition = QtWidgets.QMenu(self.menubar)
        self.menuEnregistrer_l_acquisition.setObjectName("menuEnregistrer_l_acquisition")
        self.menuEnregistrer_la_figure = QtWidgets.QMenu(self.menubar)
        self.menuEnregistrer_la_figure.setObjectName("menuEnregistrer_la_figure")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionen_txt = QtWidgets.QAction(MainWindow)
        self.actionen_txt.setObjectName("actionen_txt")
        self.actionen_csv = QtWidgets.QAction(MainWindow)
        self.actionen_csv.setObjectName("actionen_csv")
        self.actionen_png = QtWidgets.QAction(MainWindow)
        self.actionen_png.setObjectName("actionen_png")
        self.actionen_jpg = QtWidgets.QAction(MainWindow)
        self.actionen_jpg.setObjectName("actionen_jpg")
        self.actionGuide_d_utilisation = QtWidgets.QAction(MainWindow)
        self.actionGuide_d_utilisation.setObjectName("actionGuide_d_utilisation")
        self.menuEnregistrer_l_acquisition.addAction(self.actionen_txt)
        self.menuEnregistrer_l_acquisition.addAction(self.actionen_csv)
        self.menuEnregistrer_la_figure.addAction(self.actionen_png)
        self.menuEnregistrer_la_figure.addAction(self.actionen_jpg)
        self.menuHelp.addAction(self.actionGuide_d_utilisation)
        self.menubar.addAction(self.menuEnregistrer_l_acquisition.menuAction())
        self.menubar.addAction(self.menuEnregistrer_la_figure.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Suivi en temps réel de la température :</span></p></body></html>"))
        self.pushButton_edit_Commands.setText(_translate("MainWindow", "Edit Commands"))
        self.label_select_serial_port.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Veuillez sélectionner le port série relié au capteur :</span></p></body></html>"))
        self.comboBox_select_serial_port.setItemText(0, _translate("MainWindow", "choisir un port série"))
        self.label_baudrate.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Veuillez entrer la valeur du baudrate :</span></p></body></html>"))
        self.label_timeout.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Veuillez entrer du timeout (en s) :</span></p></body></html>"))
        self.pushButton_validate_device.setText(_translate("MainWindow", "Valider"))
        self.button_new_acquiring.setText(_translate("MainWindow", "Lancer une nouvelle acquisition"))
        self.checkBox_plot.setText(_translate("MainWindow", "Plot"))
        self.button_stop_acquiring.setText(_translate("MainWindow", "Arrêter l\'acquisition en cours"))
        self.label_duree.setText(_translate("MainWindow", "Durée entre 2 mesures :"))
        self.comboBox_duree.setItemText(0, _translate("MainWindow", "unité"))
        self.comboBox_duree.setItemText(1, _translate("MainWindow", "secondes"))
        self.comboBox_duree.setItemText(2, _translate("MainWindow", "minutes"))
        self.comboBox_duree.setItemText(3, _translate("MainWindow", "heures"))
        self.pushButton_change_duree.setText(_translate("MainWindow", "Changer la durée"))
        self.label_temp_mesuree.setText(_translate("MainWindow", "Température mesurée :"))
        self.label_date_mesure.setText(_translate("MainWindow", "Date de la mesure :"))
        self.label_seuil.setText(_translate("MainWindow", "Température seuil (en °C) :"))
        self.label_mail.setText(_translate("MainWindow", "e-mail :"))
        self.label_password.setText(_translate("MainWindow", "password :"))
        self.checkBox_seuil.setText(_translate("MainWindow", "Prévenir par mail"))
        self.menuEnregistrer_l_acquisition.setTitle(_translate("MainWindow", "Enregistrer l\'acquisition"))
        self.menuEnregistrer_la_figure.setTitle(_translate("MainWindow", "Enregistrer la figure"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionen_txt.setText(_translate("MainWindow", "en .txt"))
        self.actionen_csv.setText(_translate("MainWindow", "en .csv"))
        self.actionen_png.setText(_translate("MainWindow", "en .png"))
        self.actionen_jpg.setText(_translate("MainWindow", "en .jpg"))
        self.actionGuide_d_utilisation.setText(_translate("MainWindow", "Guide d\'utilisation"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
