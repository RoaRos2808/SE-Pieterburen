import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc
from PyQt5.QtCore import pyqtSlot
import pandas as pd


class StatisticsView(qtw.QFrame):
    def __init__(self, parent, backEnd):
        super().__init__(parent)
        self.parent = parent
        self.setLayout(qtw.QGridLayout())
        self.setStyleSheet("background-color:lightblue")
        self.layout().setContentsMargins(20, 20, 20, 20)

        self.columnHeaders = []
        self.backEnd = backEnd
