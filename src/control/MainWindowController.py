from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import interface as i

import logging
LOGGER = logging.getLogger(__name__)

import os
import math

import PyQt6.QtCore as core

import rsc

class MainWindowController():

    def __init__(self, window: i.MainWindow) -> None:
        self._window = window

    def _onDirectoryChanged(self, dir: str) -> None:
        self._window._pattern.setEnabled(True)
        self._window._pattern.setPrefix('{}-'.format(os.path.basename(dir)))
        self._window._validate.setEnabled(True)
        self._window._tracker.hide()

    def _onStartRenaming(self) -> None:
        dir = self._window._directoryChooser.directory()
        prefix = self._window._pattern.prefix()
        suffix = self._window._pattern.suffix()

        self._window._tracker.show()

        self._thread = RenamerThread(dir, prefix, suffix)

        self._thread.statusUpdated.connect(self._window._tracker.setLabel)
        self._thread.progressUpdated.connect(self._window._tracker.setValue)
        self._thread.completed.connect(self._onCompleted)
        self._thread.errorRaised.connect(self._reportError)

        self._thread.start()

        self._window._directoryChooser.setDisabled(True)
        self._window._pattern.setDisabled(True)
        self._window._validate.setDisabled(True)

    def _onCompleted(self) -> None:
        self._enableWidgets()

    def _reportError(self, e: Exception) -> None:
        LOGGER.error('%s : %s', type(e).__name__, e)
        self._window._tracker.hide()
        self._window.showDialog(
            rsc.Strings.Words.ERROR,
            rsc.Strings.Errors.AN_ERROR_OCCURED_DURING_RENAMING,
            rsc.Images.ERROR,
            [type(e).__name__, str(e)],
        )
        self._enableWidgets()

    def _enableWidgets(self) -> None:
        self._window._directoryChooser.setEnabled(True)
        self._window._pattern.setEnabled(True)
        self._window._validate.setEnabled(True)

# --------------------------------

class RenamerThread(core.QThread):

    statusUpdated = core.pyqtSignal(object)
    progressUpdated = core.pyqtSignal(object)
    completed = core.pyqtSignal()
    errorRaised = core.pyqtSignal(object)

    def __init__(self, dir: str, prefix: str, suffix: str) -> None:
        core.QThread.__init__(self)
        self._dir = dir
        self._prefix = prefix
        self._suffix = suffix

    def run(self) -> None:
        LOGGER.debug("Started renaming with prefix '%s' and suffix '%s'", self._prefix, self._suffix)
        try:
            self.updateStatusProcess(rsc.Strings.FILTERING_SUBDIRECTORIES)
            LOGGER.info('Filtering out subdirectories ...')

            # Filter out subdirectories
            files = [file for file in os.listdir(self._dir) if os.path.isfile(os.path.join(self._dir, file))]
            nbFiles = len(files)
            LOGGER.debug('Found %d files', nbFiles)
            if nbFiles <= 0:
                self.errorRaised.emit(FileNotFoundError(rsc.Strings.Errors.NO_FILES_FOUND))
                return
            numLength = max(int(math.log10(nbFiles)) + 1, 4)

            LOGGER.info('Sorting files by older file first ...')
            # Sort by older file first
            files.sort(key = lambda f: os.path.getctime(os.path.join(self._dir, f)))

            self.updateStatusProcess(rsc.Strings.RENAMING_FILES)
            LOGGER.info('Renaming files ...')

            # Rename
            for i, file in enumerate(files):
                extension = os.path.splitext(file)[1]
                old = os.path.join(self._dir, file)
                new = os.path.join(
                    self._dir,
                    '{}{}{}{}'.format(
                        self._prefix,
                        str(i + 1).zfill(numLength),
                        self._suffix,
                        extension
                    )
                )
                os.rename(old, new)
                self.progressUpdated.emit(math.floor(i * 100 / nbFiles))

            LOGGER.info('Renaming completed')
            self.statusUpdated.emit(rsc.Strings.RENAMING_DONE)
            self.progressUpdated.emit(100)
            self.completed.emit()

            self.exit(0)
        except Exception as e:
            self.errorRaised.emit(e)

    def updateStatusProcess(self, status: str) -> None:
        self.statusUpdated.emit('{} ...'.format(status))