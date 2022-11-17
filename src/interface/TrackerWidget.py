
import PyQt6.QtWidgets as wid

class TrackerWidget(wid.QWidget):

    def __init__(self) -> None:
        wid.QWidget.__init__(self)
        
        self._bar = wid.QProgressBar()
        self._bar.setValue(0)
        
        self._label = wid.QLabel()

        vLay = wid.QVBoxLayout()
        vLay.addWidget(self._label)
        vLay.addWidget(self._bar)
        self.setLayout(vLay)

    def setValue(self, value: int) -> None:
        self._bar.setValue(value)

    def setLabel(self, text: str) -> None:
        self._label.setText(text)