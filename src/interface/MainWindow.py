
import logging
LOGGER = logging.getLogger(__name__)

from PyQt6.QtCore import Qt
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import control as ctrl
import interface as i
import rsc

class MainWindow(wid.QMainWindow):

    def __init__(self, minWidth: int, minHeight: int) -> None:
        wid.QMainWindow.__init__(self)
        
        self._controller = ctrl.MainWindowController(self)
        
        self._initWindow(minWidth, minHeight)

        self._bakeWidgets()


    def _initWindow(self, minWidth: int, minHeight: int) -> None:
        LOGGER.info('Building %dx%d window', minWidth, minHeight)
        
        self.setWindowTitle(rsc.Strings.APPLICATION_NAME)
        self.setWindowIcon(gui.QIcon(rsc.Images.APPLICATION))
        self.setFixedSize(minWidth, minHeight)
        self.setWindowFlags(Qt.WindowType.WindowCloseButtonHint | Qt.WindowType.WindowMinimizeButtonHint)
        
        # Centers window
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def _bakeWidgets(self) -> None:

        self._directoryChooser = i.DirectoryChooserWidget()
        self._directoryChooser.directoryChanged.connect(self._controller._onDirectoryChanged)

        self._pattern = i.PatternWidget()
        self._pattern.setDisabled(True)

        self._validate = wid.QPushButton(
            gui.QIcon(rsc.Images.VALID),
            rsc.Strings.CONFIRM_RENAME_FILES
        )
        self._validate.setMinimumWidth(225)
        self._validate.clicked.connect(self._controller._onStartRenaming)
        self._validate.setDisabled(True)

        self._tracker = i.TrackerWidget()
        sp = self._tracker.sizePolicy()
        sp.setRetainSizeWhenHidden(True)
        self._tracker.setSizePolicy(sp)
        self._tracker.hide()

        footer = wid.QLabel(rsc.Strings.FOOTER)
        footer.setStyleSheet(rsc.Styles.FOOTER)

        vLay = wid.QVBoxLayout()
        vLay.addWidget(i.HeaderWidget())
        vLay.addWidget(self._directoryChooser)
        vLay.addWidget(i.HorizontalLine())
        vLay.addWidget(self._pattern)
        vLay.addWidget(i.HorizontalLine())

        hLay = wid.QHBoxLayout()
        hLay.addStretch()
        hLay.addWidget(self._validate)
        hLay.addStretch()

        vLay.addLayout(hLay)
        vLay.addWidget(self._tracker)
        vLay.addWidget(footer)

        vLay.addStretch(1)

        container = wid.QWidget()
        container.setLayout(vLay)

        self.setCentralWidget(container)

    def showDialog(self, titleDesc: str, text: str, image: str, informativeText: list[str] = None) -> int:  # type: ignore
        return i.Dialog(self, titleDesc, text, image, informativeText).exec()
