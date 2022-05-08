from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout

from pycalc.ui.board import Board
from pycalc.ui.display import DisplayWidget, ResultWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyCalc")
        self.setFixedSize(QSize(256, 300))

        layout = self.createLayout()
        self.addCentralWidget(layout)

    def addCentralWidget(self, layout):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(layout)

    def createLayout(self):
        layout = QVBoxLayout()

        self.display = DisplayWidget()
        layout.addWidget(self.display)

        self.result = ResultWidget()
        layout.addWidget(self.result)

        self.board = Board()
        layout.addLayout(self.board)

        self.layout = layout

        return layout