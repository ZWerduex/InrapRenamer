
from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import rsc

class HorizontalLine(wid.QFrame):

    def __init__(self):
        wid.QFrame.__init__(self)
        self.setFrameShape(wid.QFrame.Shape.HLine)
        self.setFrameShadow(wid.QFrame.Shadow.Sunken)

# ---------------------------------

class _BaseTextDialog(wid.QDialog):

    def __init__(self,
        parent: wid.QWidget,
        title: str,
        text: str,
        image: str,
        informativeText: list[str] = None,  # type: ignore
        withLinks: bool = False
    ) -> None:
        wid.QDialog.__init__(self, parent)
        self.setModal(True)
        self.setWindowFlags(
            Qt.WindowType.Dialog |
            Qt.WindowType.WindowCloseButtonHint |
            Qt.WindowType.WindowTitleHint
        )
        self.setWindowTitle(title)

        imageLabel = wid.QLabel()
        imageLabel.setPixmap(
            gui.QPixmap(image)
            .scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        )
        label = wid.QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hLayout = wid.QHBoxLayout()
        hLayout.addStretch()
        hLayout.addWidget(imageLabel)
        hLayout.addWidget(label)
        hLayout.addStretch()

        vLayout = wid.QVBoxLayout()
        vLayout.addLayout(hLayout)
        
        if informativeText is not None:
            informativeLabel = wid.QLabel()
            if withLinks:
                informativeLabel.setText('<br>'.join(informativeText))
                informativeLabel.setTextFormat(Qt.TextFormat.RichText)
                informativeLabel.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
                informativeLabel.setOpenExternalLinks(True)
            else:
                informativeLabel.setText('\n'.join(informativeText))
            vLayout.addWidget(informativeLabel)

        self.setLayout(vLayout)


class Dialog(_BaseTextDialog):

    def __init__(self,
        parent: wid.QWidget,
        titleDesc: str,
        text: str,
        image: str,
        informativeText: list[str] = None  # type: ignore
    ) -> None:
        _BaseTextDialog.__init__(self,
            parent,
            '{} - {}'.format(rsc.Strings.APPLICATION_NAME, titleDesc),
            text,
            image,
            informativeText
        )
        okButton = wid.QPushButton(rsc.Strings.Words.OK)
        okButton.clicked.connect(self.accept)
        okButton.setFixedSize(100, 25)
        
        hLayout = wid.QHBoxLayout()
        hLayout.addStretch()
        hLayout.addWidget(okButton)
        hLayout.addStretch()

        self.layout().addLayout(hLayout)  # type: ignore
