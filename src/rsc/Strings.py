
import logging
LOGGER = logging.getLogger(__name__)

import os
import sys

# ----- Chaînes de caractères

class Strings():
    APPLICATION_NAME = 'InrapRenamer'
    APPLICATION_DESCRIPTION = "Application de renommage d'image"

    CHOOSE_DIR = 'Choisir un dossier'
    NO_DIR_SELECTED = 'Aucun dossier sélectionné'
    DIR_NAME = 'Nom du dossier'

    PATTERN_WIDGET_TITLE = 'Modèle des noms des fichiers'
    PATTERN_EXAMPLE = 'Exemple de nom de fichier'
    NUMBER_EXAMPLE = 'Numéro (exemple)'

    CONFIRM_RENAME_FILES = 'Lancer le renommage'

    FILTERING_SUBDIRECTORIES = 'Filtrage des sous-dossiers'
    RENAMING_FILES = 'Renommage des fichiers'
    RENAMING_DONE = 'Renommage terminé !'

    FOOTER = 'Luc Le Gaillard - Copyright 2022'

    class Words():

        PREFIX = 'Préfixe'
        SUFFIX = 'Suffixe'
        ERROR = 'Erreur'
        OK = 'OK'
        CLOSE = 'Fermer'

    class Errors():

        TOO_MANY_FILES = 'Il y a trop de fichier à renommer. Le numéro maximal dépasse la limite de 9999.'
        AN_ERROR_OCCURED_DURING_RENAMING = 'Une erreur a eu lieu durant le renommage des fichiers.'

# ----- Chemins

class Paths():

    IMAGES = os.path.join(sys._MEIPASS, 'img')  # type: ignore

    LOG_FILE = os.path.join(os.path.abspath('.'), Strings.APPLICATION_NAME.lower() + '.log')

# Images
class Images():
    
    APPLICATION = os.path.join(Paths.IMAGES, 'image.png')
    DIRECTORY = os.path.join(Paths.IMAGES, 'directory.png')
    VALID = os.path.join(Paths.IMAGES, 'valid.png')

    ERROR = os.path.join(Paths.IMAGES, 'error.png')

# ----- Styles

class Styles():

    EMPTY_BACKGROUND = 'background: rgba(0, 0, 0, 0);'

    MAIN_TITLE = """
        font-family: sans-serif;
        font-size: 25px;
        letter-spacing: 1px;
    """
    SUBTITLE = """
        font-family: sans-serif;
        font-size: 14px;
        color: grey;
    """
    TITLE = """
        font-weight: bold;
        font-size: 12px;
    """
    FOOTER = """
        font-size: 9px;
        color: grey;
    """