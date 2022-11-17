
import logging
LOGGER = logging.getLogger(__name__)

import os

import PyQt6.QtCore as core
import PyQt6.QtGui as gui
import PyQt6.QtWidgets as wid

import rsc

class DirectoryChooserWidget(wid.QWidget):

    directoryChanged = core.pyqtSignal(object)

    def __init__(self) -> None:
        wid.QWidget.__init__(self)

        button = wid.QPushButton(
            gui.QIcon(rsc.Images.DIRECTORY),
            rsc.Strings.CHOOSE_DIR
        )
        button.setMinimumSize(135, 30)
        button.setSizePolicy(wid.QSizePolicy.Policy.Expanding, wid.QSizePolicy.Policy.Expanding)
        button.clicked.connect(self._openFileDialog)

        self._entry = wid.QLineEdit()
        self._entry.setPlaceholderText(rsc.Strings.NO_DIR_SELECTED)
        self._entry.setStyleSheet(rsc.Styles.EMPTY_BACKGROUND)
        self._entry.setSizePolicy(wid.QSizePolicy.Policy.Minimum, wid.QSizePolicy.Policy.Minimum)
        self._entry.setReadOnly(True)

        self._label = wid.QLabel()
        self._label.setText('-')
        self._label.setMinimumHeight(30)

        fLay = wid.QFormLayout()
        fLay.addRow(button, self._entry)
        fLay.addRow('{} :'.format(rsc.Strings.DIR_NAME), self._label)

        self.setLayout(fLay)

    def _openFileDialog(self) -> None:
        fd = wid.QFileDialog()
        fd.setModal(True)
        fd.setViewMode(wid.QFileDialog.ViewMode.Detail)
        fd.setFileMode(wid.QFileDialog.FileMode.Directory)

        if fd.exec():
            dir = fd.selectedFiles()[0]
            LOGGER.info('Selected directory : %s', dir)

            self._entry.setText(dir)
            self._entry.setToolTip(dir)
            self._label.setText(os.path.basename(dir))
            
            self.directoryChanged.emit(dir)
        else:
            LOGGER.warning('No directory was provided')

    def directory(self) -> str:
        return self._entry.text()

