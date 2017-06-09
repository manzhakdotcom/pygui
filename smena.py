from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class Color(QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle(u"Смена")

        pageLayout = QVBoxLayout()
        buttonLayout = QHBoxLayout()
        layout = QStackedLayout()

        pageLayout.addLayout(buttonLayout)
        pageLayout.addLayout(layout)

        for n, color in enumerate(['red', 'green', 'blue']):
            btn = QPushButton(str(color))
            btn.pressed.connect(lambda n=n: layout.setCurrentIndex(n))
            buttonLayout.addWidget(btn)
            layout.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec_()
