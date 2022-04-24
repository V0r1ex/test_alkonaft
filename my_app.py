# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QHBoxLayout 
app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Приложение')
main_win.move(900, 100)
main_win.resize(400, 200)

v_line = QVBoxLayout()
h_line1 = QHBoxLayout()


text1 = QLabel('Python')


v_line.addWidget(text1, alignment=Qt.AlignCenter)


v_line.addLayout(h_line1)


main_win.setLayout(v_line)
h_line1 = QHBoxLayout()
h_line2 = QHBoxLayout()
main_win.show()
app.exec_()

