from functools import partial
import math


class Controller:
    def __init__(self, view):
        self._view = view
        self._hasResult = False

        self._connectToView()

    def _connectToView(self):
        for character, button in self._view.board.buttons.items():
            button.clicked.connect(partial(self.appendToExpression, character))

    def appendToExpression(self, character):
        display = self._view.display
        result = self._view.result

        if self._hasResult:
            display.expression = ''
            result.clear()
            self._hasResult = False

        if character == "=":
            if display.expression == '':
                return

            try:
                value = self.evaluateExpression()
                result.setValue(value)
            except BaseException as e:
                print(e)
                result.setError(str(e))

            self._hasResult = True
        elif character == "C":
            display.expression = ""
        elif character == "!":
            display.expression = f"factorial({display.expression})"
        else:
            display.expression += character

            if character == "sqrt":
                display.expression += "("        
    
    def evaluateExpression(self):
        env = {
            'factorial': math.factorial,
            'sqrt': math.sqrt,
        }

        return eval(self._view.display.expression, env)