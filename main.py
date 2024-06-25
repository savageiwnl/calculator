import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QGridLayout
from PyQt5.QtGui import QPalette, QColor

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        self.display = QLineEdit()
        grid.addWidget(self.display, 0, 0, 1, 4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        positions = [(i, j) for i in range(1, 5) for j in range(4)]

        for position, button in zip(positions, buttons):
            if button == '=':
                btn = QPushButton(button)
                btn.clicked.connect(self.calculate_result)
                grid.addWidget(btn, *position)
            else:
                btn = QPushButton(button)
                btn.clicked.connect(self.update_display)
                grid.addWidget(btn, *position)

        self.clear = QPushButton('Clear')
        self.clear.clicked.connect(self.clear_display)
        grid.addWidget(self.clear, 5, 0, 1, 4)

        self.setLayout(grid)

    def update_display(self):
        button_text = self.sender().text()
        new_display = self.display.text() + button_text
        self.display.setText(new_display)

    def calculate_result(self):
        result = eval(self.display.text())
        self.display.setText(str(result))

    def clear_display(self):
        self.display.clear()


app = QApplication(sys.argv)

app.setStyle('Fusion')

palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
palette.setColor(QPalette.Base, QColor(15, 15, 15))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
palette.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
palette.setColor(QPalette.Text, QColor(255, 255, 255))
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
palette.setColor(QPalette.BrightText, QColor(255, 0, 0))
palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
palette.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

app.setPalette(palette)

calc = Calculator()
calc.show()

sys.exit(app.exec_())
