#!/usr/bin/env python
# -*- coding: utf-8 -*-

# d'abord le faire en python 2.7 puis en 3
# Faire en PySide puis en PySide 2
# Je devrais donc avoir au moins 2 ou 3 versions de mon script

# En python 2.7 PySide 1

# on va toucher au fichiers de système d'exploitation,
#               => On va donc importer le module os

import os
from glob import glob

# déclaration des variables

BASEFI = os.path.dirname(__file__)             # J'indique le chemin du dossier principal en relatif
DOS_DATA = os.path.join(BASEFI, 'data')       # J'indique le chemin du fichier data par rapport au fichier principal



def creerNote(nomNote, contenu=''):
    """Création et écriture du contenu dans la note"""

    chNote = os.path.join(DOS_DATA, nomNote + '.txt')           # chemin du nouveau fichier

    with open(chNote, 'w') as f:                                # Ouverture du fichier en mode écriture
        f.write(contenu)

    if os.path.isfile(chNote):                                  # permet de vérifier que tous c'est bien passer
        print('La note "{}" a bien été créée'.format(nomNote))  # En vérifiant que la note à bien été créée


def suppNote(nomNote):
    """Suppression d'une note"""

    chNote = os.path.join(DOS_DATA, nomNote + '.txt')

    if os.path.isfile(chNote):
        os.remove(chNote)                                        # suppression de la note
        print('La note {} a bien été supprimée'.format(nomNote))    # permet de vérifier que tous c'est bien passer
    else:                                                                # En vérifiant que la note à bien été supprimée
        print("La note {} ,n'existe pas'".format(nomNote))

def affichNote():
    """Permet de récupérer toutes les notes qui sont dans le dossiers data."""

    notes = glob(DOS_DATA + '/*.txt')                                    # permet de récupérer tous les fichiers de type .txt
    notes = [os.path.splitext(os.path.split(n)[-1])[0] for n in notes]      # va nous permettre de récupérer juste le nom du fichier dans le chemin
                                                                            # c'est une compréhension de liste
    return notes


def recupEnonceNote(nomNote):
    """Permet de récupérer  l'énoncé de la note"""

    chNote = os.path.join(DOS_DATA, nomNote + '.txt')       # lit le chemin de la note
    with open(chNote, 'r') as f:                            # lit le contenu de la note
        contenonce = f.read().splitlines()                  # on met le contenu dans une liste par ligne                                       # on met le contenu dans une variable
        index1 = contenonce.index('# enonce')               # indice du début de l'énoncé dans la liste
        index2 = contenonce.index('# code')                 # indice de fin de l'énoncé dans la liste
        texte = (contenonce[index1: index2])                # le texte est compris entre énoncé et code en liste
        contenuNote = ""                                    # transformation de la liste en string
        for line in texte:
            contenuNote  = contenuNote + str(line) + '\n'

    return contenuNote                                      # on retourne le contenu de la variable


def recupContenu5Note(nomNote):
    """Permet de récupérer  le contenu de la note"""

    chNote = os.path.join(DOS_DATA, nomNote + '.txt')       # lit le chemin de la note
    with open(chNote, 'r') as f:                            # lit le contenu de la note
        cont5 = f.read().splitlines()                  # on met le contenu dans une liste par ligne                                       # on met le contenu dans une variable
        index1 = cont5.index('# code')               # indice du début du code dans la liste
        index2 = index1 + 5
        texte = (cont5[index1: index2])                # le texte est compris entre énoncé et code en liste
        contenu5 = ""                                    # transformation de la liste en string
        for line in texte:
            contenu5 = contenu5 + str(line) + '\n'
    return contenu5                                     # on retourne le contenu de la variable

def recupContenu10Note(nomNote):
    """Permet de récupérer  le contenu de la note"""

    chNote = os.path.join(DOS_DATA, nomNote + '.txt')       # lit le chemin de la note
    with open(chNote, 'r') as f:                            # lit le contenu de la note
        cont10 = f.read().splitlines()                  # on met le contenu dans une liste par ligne                                       # on met le contenu dans une variable
        index1 = cont10.index('# code')               # indice du début du code dans la liste
        index2 = index1 + 10
        texte = (cont10[index1: index2])                # le texte est compris entre énoncé et code en liste
        contenu10 = ""                                    # transformation de la liste en string
        for line in texte:
            contenu10 = contenu10 + str(line) + '\n'
    return contenu10                                     # on retourne le contenu de la variable

def recupContenuNote(nomNote):
    """Permet de récupérer  le contenu de la note"""

    chNote = os.path.join(DOS_DATA, nomNote + '.txt')    # lit le chemin de la note
    with open(chNote, 'r') as f:                         # lit le contenu de la note
        contenuNote = f.read()                           # on met le contenu dans une variable
    return contenuNote                                   # on retourne le contenu de la variable


