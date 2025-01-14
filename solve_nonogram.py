from random import randint
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
import ast

def clear_grid(button_grid, dim):
    for i in range(dim):
        for j in range(dim):
            button_grid[i][j].setStyleSheet("background-color: white;")


def toggle_color(button):
    if button.styleSheet() == "background-color: white;":
        button.setStyleSheet("background-color: black;")
    else:
        button.setStyleSheet("background-color: white;")

def leave_window(grid_window, main_window):
    grid_window.layout().deleteLater()
    grid_window.close()
    main_window.show()

def check_grid(button_grid, dim, success_window, failure_window, answer):
    correct = True
    for i in range(dim):
        for j in range(dim):
            if button_grid[i][j].styleSheet() == "background-color: black;" and answer[i*dim + j] == 0:
                correct = False
            elif button_grid[i][j].styleSheet() == "background-color: white;" and answer[i*dim + j] == 1:
                correct = False
    
    if correct:
        success_window.show()
    else:
        failure_window.show()

def create_solve(grid_window, main_window, success_window, failure_window):
    nonograms = open('nonograms.txt', 'r')
    
    lines_number = sum(1 for line in nonograms)
    nonograms.seek(0)
    
    number = randint(0, lines_number-1)
    nonogram_str = ""

    for cur_number, line in enumerate(nonograms, start=1):
        if cur_number == number:
            nonogram_str = line.strip()
    
    nonograms.close()
    
    nonogram_dict = ast.literal_eval(nonogram_str)

    grid_window.resize(500, 500)
    grid_layout = QGridLayout()

    btns = []

    for j in range(10):
        label = ""
        if not nonogram_dict['cols'][j]:
            label = "0"
        else:
            for num in nonogram_dict['cols'][j]:
                label += str(num)
                label += "\n"

        col_label = QLabel(label, grid_window)
        grid_layout.addWidget(col_label, 0, j+1, alignment=Qt.AlignCenter)
    
    for i in range(10):
        label = ""
        if not nonogram_dict['rows'][i]:
            label = "0"
        else:
            for num in nonogram_dict['rows'][i]:
                label += str(num)
                label += " "

        row_label = QLabel(label, grid_window)
        grid_layout.addWidget(row_label, i+1, 0)

        row_buttons = []
        for j in range(10):
            button = QPushButton("", grid_window)
            button.setStyleSheet("background-color: white;")
            button.setFixedSize(50, 50)
            button.clicked.connect(lambda _, b=button: toggle_color(b))
            grid_layout.addWidget(button, i+1, j+1)
            row_buttons.append(button)
        btns.append(row_buttons)

    btns_layout = QHBoxLayout()
    
    check_btn = QPushButton("Check")
    check_btn.clicked.connect(lambda: check_grid(btns, 10, success_window, failure_window, nonogram_dict['answer']))

    clear_btn = QPushButton("Clear")
    clear_btn.clicked.connect(lambda: clear_grid(btns, 10))

    leave_btn = QPushButton("Leave")
    leave_btn.clicked.connect(lambda: leave_window(grid_window, main_window))

    btns_layout.addWidget(leave_btn)
    btns_layout.addWidget(clear_btn)
    btns_layout.addWidget(check_btn)

    grid_layout.addLayout(btns_layout, 11, 0, 1, 10)

    grid_window.setLayout(grid_layout)