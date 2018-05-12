#!/usr/bin/env python
# -*- coding: utf-8 -*-

# fichier permettant de lier l'interface graphique au code pur
# c'est le fichier à lancer pour exécuter le programme
# todo : améliorer la présentation générale
# todo : mettre du css
# todo : gérer les exceptions
# todo : Ce script est en python 2.7 et Pyside 1, le passer en python 3.5 et PySide 2

import os
from PySide import QtGui, QtCore
from interface.design import Ui_fenetrePrincipale              # import le fichier de l'interface
import Pythonnerie


class LaPythonnerie(QtGui.QWidget, Ui_fenetrePrincipale):
    """Cette classe sert de liaison entre le code de gestion des fichiers et le code de l'interface."""

    def __init__(self):
        super(LaPythonnerie, self).__init__()

        self.setupUi(self)                       # lance la fonction de l'interface
        self.recupererNotes()                    # lance la fonction pour récupérer le contenu du dossier data
        self.setupConnections()                  # lance la fonction de connection entre l'interface et le calcul
        self.show()                              # permet d'afficher à l'écran la fenêtre

    def setupConnections(self):
        """Connection des boutons aux fonctions."""

        self.btn_creerNote.clicked.connect(self.creationNote)
        self.lw_listeNote.itemClicked.connect(self.affichNote)
        self.btn_miseAJourNote.clicked.connect(self.mettreAJourNote)
        self.btn_suppNote.clicked.connect(self.supprimerNote)
        self.btn_5lignes.clicked.connect(self.affich5lignes)
        self.btn_10lignes.clicked.connect(self.affich10lignes)
        self.btn_totalite.clicked.connect(self.affichConttotal)

    def recupererNotes(self):
        """Fonction permettant d'afficher les notes récupérées par la fonction du fichier notemanager."""

        self.lw_listeNote.clear()                       # nettoie la liste de note
        notes = Pythonnerie.affichNote()
        self.lw_listeNote.addItems(notes)               # permet d'afficher la liste des notes

    def recupNoteSelect(self):
        """Fonction permettant de récupérer les notes sélectionnées"""

        notesSelect = self.lw_listeNote.selectedItems() # permet d'indiquer la note que l'on veut supprimer
        if not notesSelect:
            return
        nomNote = notesSelect[-1].text()                # permet de récupérer juste le nom sélectionné
        chNote = os.path.join(Pythonnerie.DOS_DATA, nomNote + '.txt')
        print(nomNote, chNote)
        return nomNote, chNote

    def creationNote(self):
        """Affichage de la création de la note"""

        # la ligne suivante permet de créer une fenêtre de dialogue :
        nomNote, ok = QtGui.QInputDialog.getText(self, 'Créer une note', 'Entrez le nom de la note : ')   # demander le nom de la note graphiquement
        if not ok:                                  # si on ne clique pas sur ok
            return
        Pythonnerie.creerNote(nomNote)              # si on clique sur ok
        self.recupererNotes()

    def mettreAJourNote(self):
        """Affichage de la mise à jour de la note"""

        nomNote, chNote = self.recupNoteSelect()
        contenu = self.te_enonceNote.toPlainText()          # permet de récupérer le contenu de la note
        Pythonnerie.creerNote(nomNote, contenu)             # en va recréer la note pour la mettre à jour

    def supprimerNote(self):
        """Affichage de la suppression de la note"""

        nomNote, chNote = self.recupNoteSelect()
        Pythonnerie.suppNote(nomNote)                       # permet de lancer la fonction Supprimer la note
        self.recupererNotes()
        self.te_enonceNote.setText('')

    def affichNote(self):
        """Affichage de l'énoncé de la note"""

        nomNote, chNote = self.recupNoteSelect()
        enonce = Pythonnerie.recupEnonceNote(nomNote)
        self.te_enonceNote.setText(enonce)                 # le texte est placé dans l'interface

    def affich5lignes(self):
        """Affichage de 5 lignes du contenu de la note"""

        nomNote, chNote = self.recupNoteSelect()
        contenu5 = Pythonnerie.recupContenu5Note(nomNote)
        self.te_contenuNote.setText(contenu5)                 # le texte est placé dans l'interface

    def affich10lignes(self):
        """Affichage de 10 lignes du contenu de la note"""

        nomNote, chNote = self.recupNoteSelect()
        contenu10 = Pythonnerie.recupContenu10Note(nomNote)
        self.te_contenuNote.setText(contenu10)                 # le texte est placé dans l'interface

    def affichConttotal(self):
        """Affichage du contenu complet de la note"""

        nomNote, chNote = self.recupNoteSelect()
        contenuNote = Pythonnerie.recupContenuNote(nomNote)
        self.te_contenuNote.setText(contenuNote)                 # le texte est placé dans l'interface





app = QtGui.QApplication([])                    #création de l'application Il doit avoir au moins 1 argument d'où les crochets
lp = LaPythonnerie()

app.exec_()										# exécution de l'application et
												# le programme ne se terminera quand cliquant sur la croix
												# de la fenêtre