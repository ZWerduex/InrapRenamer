
import logging
LOGGER = logging.getLogger(__name__)

import webbrowser

import PyQt6.QtWidgets as wid

import rsc

class FooterLabel(wid.QLabel):

    def __init__(self) -> None:
        wid.QLabel.__init__(self, rsc.Strings.FOOTER_TEXT)
        self.setStyleSheet(rsc.Styles.FOOTER)
        self.linkActivated.connect(self.clicked)

    def clicked(self, link: str) -> None:
        if link:
            LOGGER.info(f'Opened {link}')
            webbrowser.open(link, new = 0, autoraise = True)