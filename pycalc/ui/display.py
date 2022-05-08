from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit, QLabel

class ResultWidget(QLabel):
    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignRight)

    def clear(self):
        self.setText('')
        self.setStyleSheet('')

    def setValue(self, result):
        self.setStyleSheet('color: green')
        self.setText(f'= {result}')

    def setError(self, error):
        self.setStyleSheet('color: red')
        self.setText(f'ERRO!! {error}')

class DisplayWidget(QLineEdit):
    def __init__(self):
        super().__init__()

        self.expression = ''

        self.setFixedHeight(35)
        self.setAlignment(Qt.AlignRight)
        self.setReadOnly(True)

    @property
    def expression(self):
        return self._expression

    @expression.setter
    def expression(self, expr):
        self._expression = expr
        self.setText(self._expression)