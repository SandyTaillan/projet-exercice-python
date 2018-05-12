# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sandy/Documents/informatique/mes-scripts/projet-exercice-python/interface/design.ui'
#
# Created: Fri May 11 07:57:26 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_fenetrePrincipale(object):
    def setupUi(self, fenetrePrincipale):
        fenetrePrincipale.setObjectName("fenetrePrincipale")
        fenetrePrincipale.resize(876, 954)
        self.btn_creerNote = QtGui.QPushButton(fenetrePrincipale)
        self.btn_creerNote.setGeometry(QtCore.QRect(9, 9, 122, 27))
        self.btn_creerNote.setObjectName("btn_creerNote")
        self.btn_suppNote = QtGui.QPushButton(fenetrePrincipale)
        self.btn_suppNote.setGeometry(QtCore.QRect(431, 9, 151, 27))
        self.btn_suppNote.setObjectName("btn_suppNote")
        self.la_exercices = QtGui.QLabel(fenetrePrincipale)
        self.la_exercices.setGeometry(QtCore.QRect(9, 42, 117, 16))
        self.la_exercices.setObjectName("la_exercices")
        self.la_enonce = QtGui.QLabel(fenetrePrincipale)
        self.la_enonce.setGeometry(QtCore.QRect(691, 42, 59, 16))
        self.la_enonce.setObjectName("la_enonce")
        self.te_enonceNote = QtGui.QTextEdit(fenetrePrincipale)
        self.te_enonceNote.setGeometry(QtCore.QRect(293, 62, 571, 192))
        self.te_enonceNote.setObjectName("te_enonceNote")
        self.la_resultat = QtGui.QLabel(fenetrePrincipale)
        self.la_resultat.setGeometry(QtCore.QRect(300, 260, 119, 16))
        self.la_resultat.setObjectName("la_resultat")
        self.btn_5lignes = QtGui.QPushButton(fenetrePrincipale)
        self.btn_5lignes.setGeometry(QtCore.QRect(290, 280, 85, 27))
        self.btn_5lignes.setObjectName("btn_5lignes")
        self.btn_10lignes = QtGui.QPushButton(fenetrePrincipale)
        self.btn_10lignes.setGeometry(QtCore.QRect(390, 280, 85, 27))
        self.btn_10lignes.setObjectName("btn_10lignes")
        self.btn_totalite = QtGui.QPushButton(fenetrePrincipale)
        self.btn_totalite.setGeometry(QtCore.QRect(490, 280, 85, 27))
        self.btn_totalite.setObjectName("btn_totalite")
        self.te_contenuNote = QtGui.QTextEdit(fenetrePrincipale)
        self.te_contenuNote.setGeometry(QtCore.QRect(295, 321, 571, 571))
        self.te_contenuNote.setObjectName("te_contenuNote")
        self.btn_miseAJourNote = QtGui.QPushButton(fenetrePrincipale)
        self.btn_miseAJourNote.setGeometry(QtCore.QRect(290, 900, 97, 27))
        self.btn_miseAJourNote.setObjectName("btn_miseAJourNote")
        self.lw_listeNote = QtGui.QListWidget(fenetrePrincipale)
        self.lw_listeNote.setGeometry(QtCore.QRect(20, 60, 256, 871))
        self.lw_listeNote.setObjectName("lw_listeNote")

        self.retranslateUi(fenetrePrincipale)
        QtCore.QMetaObject.connectSlotsByName(fenetrePrincipale)

    def retranslateUi(self, fenetrePrincipale):
        fenetrePrincipale.setWindowTitle(QtGui.QApplication.translate("fenetrePrincipale", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_creerNote.setText(QtGui.QApplication.translate("fenetrePrincipale", "Créer un exercice", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_suppNote.setText(QtGui.QApplication.translate("fenetrePrincipale", "Supprimer un exercice", None, QtGui.QApplication.UnicodeUTF8))
        self.la_exercices.setText(QtGui.QApplication.translate("fenetrePrincipale", "Liste des exercices :", None, QtGui.QApplication.UnicodeUTF8))
        self.la_enonce.setText(QtGui.QApplication.translate("fenetrePrincipale", "Énoncés : ", None, QtGui.QApplication.UnicodeUTF8))
        self.la_resultat.setText(QtGui.QApplication.translate("fenetrePrincipale", "Voir le résultat sur  :", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_5lignes.setText(QtGui.QApplication.translate("fenetrePrincipale", "5 lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_10lignes.setText(QtGui.QApplication.translate("fenetrePrincipale", "10 lignes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_totalite.setText(QtGui.QApplication.translate("fenetrePrincipale", "Totalité", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_miseAJourNote.setText(QtGui.QApplication.translate("fenetrePrincipale", "Mettre à jour", None, QtGui.QApplication.UnicodeUTF8))

