
from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import rsc

class HeaderWidget(wid.QWidget):

    def __init__(self) -> None:
        wid.QWidget.__init__(self)

        title = wid.QLabel()
        title.setText(rsc.Strings.APPLICATION_NAME)
        title.setStyleSheet(rsc.Styles.MAIN_TITLE)

        desc = wid.QLabel()
        desc.setText(rsc.Strings.APPLICATION_DESCRIPTION)
        desc.setStyleSheet(rsc.Styles.SUBTITLE)
        
        img = wid.QLabel()
        img.setPixmap(
            gui.QPixmap(rsc.Images.APPLICATION)
            .scaled(
                128, 128,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
        )

        vLay = wid.QVBoxLayout()
        vLay.addWidget(title)
        vLay.addWidget(desc)
        vLay.setContentsMargins(30, 0, 0, 0)

        hLay = wid.QHBoxLayout()
        hLay.addWidget(img)
        hLay.addLayout(vLay, 1)

        self.setLayout(hLay)
