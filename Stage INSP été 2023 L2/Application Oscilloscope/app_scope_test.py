# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_scope_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 230, 621, 351))
        self.widget.setObjectName("widget")
        self.splitter_7 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_7.setGeometry(QtCore.QRect(10, 8, 621, 211))
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.splitter = QtWidgets.QSplitter(self.splitter_7)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_connexion_type = QtWidgets.QLabel(self.splitter)
        self.label_connexion_type.setObjectName("label_connexion_type")
        self.label_bdrate = QtWidgets.QLabel(self.splitter)
        self.label_bdrate.setObjectName("label_bdrate")
        self.lineEdit_bdrate = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_bdrate.setObjectName("lineEdit_bdrate")
        self.label_timeout = QtWidgets.QLabel(self.splitter)
        self.label_timeout.setObjectName("label_timeout")
        self.lineEdit_timeout = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_timeout.setObjectName("lineEdit_timeout")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_select_oscillo = QtWidgets.QLabel(self.splitter_2)
        self.label_select_oscillo.setObjectName("label_select_oscillo")
        self.comboBox_select_oscillo = QtWidgets.QComboBox(self.splitter_2)
        self.comboBox_select_oscillo.setObjectName("comboBox_select_oscillo")
        self.button_params_oscillo = QtWidgets.QPushButton(self.splitter_7)
        self.button_params_oscillo.setObjectName("button_params_oscillo")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_lambda_c = QtWidgets.QLabel(self.splitter_3)
        self.label_lambda_c.setObjectName("label_lambda_c")
        self.spinBox_lambda_c = QtWidgets.QSpinBox(self.splitter_3)
        self.spinBox_lambda_c.setMinimum(350)
        self.spinBox_lambda_c.setMaximum(1100)
        self.spinBox_lambda_c.setObjectName("spinBox_lambda_c")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_vcursor = QtWidgets.QLabel(self.splitter_4)
        self.label_vcursor.setObjectName("label_vcursor")
        self.button_appear_vcursor = QtWidgets.QPushButton(self.splitter_4)
        self.button_appear_vcursor.setObjectName("button_appear_vcursor")
        self.checkBox_cursor = QtWidgets.QPushButton(self.splitter_4)
        self.checkBox_cursor.setObjectName("checkBox_cursor")
        self.button_acquire = QtWidgets.QPushButton(self.splitter_7)
        self.button_acquire.setObjectName("button_acquire")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_lambda_pic = QtWidgets.QLabel(self.splitter_5)
        self.label_lambda_pic.setObjectName("label_lambda_pic")
        self.value_lambda_pic = QtWidgets.QLineEdit(self.splitter_5)
        self.value_lambda_pic.setReadOnly(True)
        self.value_lambda_pic.setObjectName("value_lambda_pic")
        self.label_largeur = QtWidgets.QLabel(self.splitter_5)
        self.label_largeur.setObjectName("label_largeur")
        self.label_largeur_mi_hauteur = QtWidgets.QLineEdit(self.splitter_5)
        self.label_largeur_mi_hauteur.setReadOnly(True)
        self.label_largeur_mi_hauteur.setObjectName("label_largeur_mi_hauteur")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_date_acquisition = QtWidgets.QLabel(self.splitter_6)
        self.label_date_acquisition.setObjectName("label_date_acquisition")
        self.label_date = QtWidgets.QLineEdit(self.splitter_6)
        self.label_date.setText("")
        self.label_date.setReadOnly(True)
        self.label_date.setObjectName("label_date")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 646, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuEnregister_l_acquisition_en = QtWidgets.QMenu(self.menuBar)
        self.menuEnregister_l_acquisition_en.setObjectName("menuEnregister_l_acquisition_en")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuEnregistrer_l_acquisition_en = QtWidgets.QMenu(self.menuBar)
        self.menuEnregistrer_l_acquisition_en.setObjectName("menuEnregistrer_l_acquisition_en")
        MainWindow.setMenuBar(self.menuBar)
        self.action_png = QtWidgets.QAction(MainWindow)
        self.action_png.setObjectName("action_png")
        self.action_jpg = QtWidgets.QAction(MainWindow)
        self.action_jpg.setObjectName("action_jpg")
        self.action_csv = QtWidgets.QAction(MainWindow)
        self.action_csv.setObjectName("action_csv")
        self.action_txt = QtWidgets.QAction(MainWindow)
        self.action_txt.setObjectName("action_txt")
        self.action_png_2 = QtWidgets.QAction(MainWindow)
        self.action_png_2.setObjectName("action_png_2")
        self.action_jpg_2 = QtWidgets.QAction(MainWindow)
        self.action_jpg_2.setObjectName("action_jpg_2")
        self.action_csv_2 = QtWidgets.QAction(MainWindow)
        self.action_csv_2.setObjectName("action_csv_2")
        self.action_txt_2 = QtWidgets.QAction(MainWindow)
        self.action_txt_2.setObjectName("action_txt_2")
        self.action_png_3 = QtWidgets.QAction(MainWindow)
        self.action_png_3.setObjectName("action_png_3")
        self.action_jpg_3 = QtWidgets.QAction(MainWindow)
        self.action_jpg_3.setObjectName("action_jpg_3")
        self.action_csv_3 = QtWidgets.QAction(MainWindow)
        self.action_csv_3.setObjectName("action_csv_3")
        self.action_txt_3 = QtWidgets.QAction(MainWindow)
        self.action_txt_3.setObjectName("action_txt_3")
        self.actionGuide_d_utilisation = QtWidgets.QAction(MainWindow)
        self.actionGuide_d_utilisation.setObjectName("actionGuide_d_utilisation")
        self.action_csv_4 = QtWidgets.QAction(MainWindow)
        self.action_csv_4.setObjectName("action_csv_4")
        self.action_txt_4 = QtWidgets.QAction(MainWindow)
        self.action_txt_4.setObjectName("action_txt_4")
        self.menuEnregister_l_acquisition_en.addAction(self.action_png_3)
        self.menuEnregister_l_acquisition_en.addAction(self.action_jpg_3)
        self.menuHelp.addAction(self.actionGuide_d_utilisation)
        self.menuEnregistrer_l_acquisition_en.addAction(self.action_csv_4)
        self.menuEnregistrer_l_acquisition_en.addAction(self.action_txt_4)
        self.menuBar.addAction(self.menuEnregistrer_l_acquisition_en.menuAction())
        self.menuBar.addAction(self.menuEnregister_l_acquisition_en.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_connexion_type.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Connexion avec pyserial :</span></p></body></html>"))
        self.label_bdrate.setText(_translate("MainWindow", "Baudrate"))
        self.label_timeout.setText(_translate("MainWindow", "Timeout"))
        self.label_select_oscillo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Selectionnez l\'oscilloscope :</span></p></body></html>"))
        self.button_params_oscillo.setText(_translate("MainWindow", "Paramètres de l\'oscilloscope"))
        self.label_lambda_c.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Veuillez entrer la longuer d\'onde associée au curseur de l\'analyseur de spectres (nm) :</span></p></body></html>"))
        self.label_vcursor.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt;\">Veuillez placer le curseur 1 de l\'oscilloscope sur le curseur de l\'analyseur :</span></p></body></html>"))
        self.button_appear_vcursor.setText(_translate("MainWindow", "Faire apparaître le curseur"))
        self.checkBox_cursor.setText(_translate("MainWindow", "Valider"))
        self.button_acquire.setText(_translate("MainWindow", "Lancer l\'acquisition"))
        self.label_lambda_pic.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Longueur d\'onde du pic :</span></p></body></html>"))
        self.label_largeur.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Largeur à mi-hauteur :</span></p></body></html>"))
        self.label_date_acquisition.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Date de l\'acquisition :</span></p></body></html>"))
        self.menuEnregister_l_acquisition_en.setTitle(_translate("MainWindow", "Enregister la figure en"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuEnregistrer_l_acquisition_en.setTitle(_translate("MainWindow", "Enregistrer l\'acquisition en"))
        self.action_png.setText(_translate("MainWindow", ".png"))
        self.action_jpg.setText(_translate("MainWindow", ".jpg"))
        self.action_csv.setText(_translate("MainWindow", ".csv"))
        self.action_txt.setText(_translate("MainWindow", ".txt"))
        self.action_png_2.setText(_translate("MainWindow", ".png"))
        self.action_jpg_2.setText(_translate("MainWindow", ".jpg"))
        self.action_csv_2.setText(_translate("MainWindow", ".csv"))
        self.action_txt_2.setText(_translate("MainWindow", ".txt"))
        self.action_png_3.setText(_translate("MainWindow", ".png"))
        self.action_jpg_3.setText(_translate("MainWindow", ".jpg"))
        self.action_csv_3.setText(_translate("MainWindow", ".csv"))
        self.action_txt_3.setText(_translate("MainWindow", ".txt"))
        self.actionGuide_d_utilisation.setText(_translate("MainWindow", "Guide d\'utilisation"))
        self.action_csv_4.setText(_translate("MainWindow", ".csv"))
        self.action_txt_4.setText(_translate("MainWindow", ".txt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
