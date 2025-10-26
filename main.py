from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint 

app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Penentu Pemenang')
# setting the point where the window will show up on the computer screen
main_win.move(900, 70)
# setting the window size (width and height)
main_win.resize(400, 200)
but = QPushButton('Generate')
text = QLabel('Klik untuk mengetahui pemenang')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(but, alignment = Qt.AlignCenter)
main_win.setLayout(line)

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Pemenang:')
but.clicked.connect(show_winner)

main_win.show()
app.exec_()