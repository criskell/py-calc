from PyQt5.QtWidgets import QGridLayout, QPushButton
from functools import partial


class Board(QGridLayout):
    def __init__(self):
        super().__init__()

        board = [
            ['7', '8', '9', '+', 'C'],
            ['4', '5', '6', '-', '('],
            ['1', '2', '3', '*', ')'],
            ['0', '**', '.', '/', '%'],
            ['//', '00', 'sqrt', '!', '=']
        ]

        self.buttons = {}

        for y, row in enumerate(board):
            for x, character in enumerate(row):
                button = QPushButton(character)

                button.setFixedSize(40, 40)

                self.buttons[character] = button

                self.addWidget(button, y, x)