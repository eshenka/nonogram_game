import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from create_nonogram import create_grid
from solve_nonogram import create_solve

app = QApplication(sys.argv)
window = QWidget()
create_grid_window = QWidget()
solve_window = QWidget()
success_window = QWidget()
failure_window = QWidget()

def solve_rnd_nonogram():
    print("Solve random")
    window.hide()
    create_solve(solve_window, window, success_window, failure_window)
    solve_window.show()

def add_new_nonogram():
    print("Add new")
    window.hide()
    create_grid(create_grid_window, window)
    create_grid_window.show()

def show_main_window():
    window.show()

def hide_main_window():
    window.hide()

def show_create_grid_window():
    create_grid_window.show()

def hide_create_grid_window():
    create_grid_window.hide()

def init_result_windows():
    message = QLabel("Correct!", success_window)
    message.setAlignment(Qt.AlignCenter)
    message.setStyleSheet("color: green;")

    success_window.resize(100, 100)

    failure_message = QLabel("Incorrect!", failure_window)
    failure_message.setAlignment(Qt.AlignCenter)
    failure_message.setStyleSheet("color: red;")

    failure_window.resize(100, 100)



window.setWindowTitle("Nonogram")
window.resize(500, 500)
# window.resize(400, 300)

init_result_windows()

layout = QVBoxLayout()

title_label = QLabel("Nonogram")
title_label.setStyleSheet("font-size: 24px; font-weight: bold;");
layout.addWidget(title_label, alignment=Qt.AlignCenter)

btns_layout = QHBoxLayout()

solve_btn = QPushButton("Solve random")
solve_btn.clicked.connect(solve_rnd_nonogram)
btns_layout.addWidget(solve_btn, alignment=Qt.AlignCenter)

add_btn = QPushButton("Add new")
add_btn.clicked.connect(add_new_nonogram)
btns_layout.addWidget(add_btn, alignment=Qt.AlignCenter)

layout.addLayout(btns_layout)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
