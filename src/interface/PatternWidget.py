
import PyQt6.QtWidgets as wid

import rsc

class PatternWidget(wid.QWidget):

    def __init__(self) -> None:
        wid.QWidget.__init__(self)
        
        title = wid.QLabel(rsc.Strings.PATTERN_WIDGET_TITLE)
        title.setStyleSheet(rsc.Styles.TITLE)

        prefixTitle = wid.QLabel(rsc.Strings.Words.PREFIX)
        suffixTitle = wid.QLabel(rsc.Strings.Words.SUFFIX)
        numberTitle = wid.QLabel(rsc.Strings.NUMBER_EXAMPLE)

        self._prefix = wid.QLineEdit()
        self._prefix.setPlaceholderText(rsc.Strings.Words.PREFIX)
        self._prefix.textChanged.connect(self.updateExample)

        self._number = wid.QLineEdit()
        self._number.setStyleSheet(rsc.Styles.EMPTY_BACKGROUND)
        self._number.setText('0361')
        self._number.setReadOnly(True)

        self._suffix = wid.QLineEdit()
        self._suffix.setPlaceholderText(rsc.Strings.Words.SUFFIX)
        self._suffix.textChanged.connect(self.updateExample)

        self._example = wid.QLabel()
        self.updateExample()

        gLay = wid.QGridLayout()
        gLay.addWidget(title, 0, 0, 1, 3)
        gLay.addWidget(prefixTitle, 1, 0)
        gLay.addWidget(self._prefix, 2, 0)
        gLay.addWidget(numberTitle, 1, 1)
        gLay.addWidget(self._number, 2, 1)
        gLay.addWidget(suffixTitle, 1, 2)
        gLay.addWidget(self._suffix, 2, 2)
        gLay.addWidget(self._example, 3, 0, 1, 3)

        self.setLayout(gLay)

    def updateExample(self) -> None:
        self._example.setText(
            '{} : {}{}{}.jpg'.format(
                rsc.Strings.PATTERN_EXAMPLE,
                self.prefix(),
                self._number.text(),
                self.suffix()
            )
        )

    def setPrefix(self, prefix: str) -> None:
        self._prefix.setText(prefix)

    def prefix(self) -> str:
        return self._prefix.text()

    def setSuffix(self, suffix: str) -> None:
        self._suffix.setText(suffix)

    def suffix(self) -> str:
        return self._suffix.text()