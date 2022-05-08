import sys
from PyQt5.QtWidgets import QApplication

from pycalc.controller import Controller
from pycalc.ui.window import MainWindow


def main():
    app = QApplication(sys.argv)

    view = MainWindow()
    view.show()

    Controller(view)

    sys.exit(app.exec())