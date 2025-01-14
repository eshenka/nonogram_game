from PyQt5.QtWidgets import QGridLayout, QPushButton, QHBoxLayout

def toggle_color(button):
    if button.styleSheet() == "background-color: white;":
        button.setStyleSheet("background-color: black;")
    else:
        button.setStyleSheet("background-color: white;")

def submit_grid(button_grid, dim, grid_window, window):
    save_grid = {}
    answer = []

    rows = []
    for row in button_grid:
        row_numbers = []
        cnt = 0
        for button in row:
            if button.styleSheet() == "background-color: white;":
                if cnt != 0:
                    row_numbers.append(cnt)
                cnt = 0
                answer.append(0)
            else:
                cnt += 1
                answer.append(1)
        if cnt != 0:
            row_numbers.append(cnt)
        rows.append(row_numbers)
    
    cols = []
    for i in range(dim):
        col_number = []
        cnt = 0
        for j in range(dim):
            if button_grid[j][i].styleSheet() == "background-color: white;":
                if cnt != 0:
                    col_number.append(cnt)
                cnt = 0
            else:
                cnt += 1
        if cnt != 0:
            col_number.append(cnt)
        cols.append(col_number)

    save_grid['rows'] = rows
    save_grid['cols'] = cols
    save_grid['answer'] = answer

    # json_file = open("nonograms.json", "w")
    # json.dump(save_grid, json_file)
    # json_file.close()

    nonograms_file = open("nonograms.txt", "a")
    nonograms_file.write(str(save_grid))
    nonograms_file.write("\n")
    nonograms_file.close()

    print(save_grid)
    grid_window.layout().deleteLater()
    grid_window.close()
    window.show()

def clear_grid(button_grid, dim):
    for i in range(dim):
        for j in range(dim):
            button_grid[i][j].setStyleSheet("background-color: white;")

def create_grid(grid_window, window):
    grid_window.resize(500, 500)
    grid_layout = QGridLayout()

    btns = []

    for i in range(10):
        btns_row = []
        for j in range(10):
            button = QPushButton()
            button.setStyleSheet("background-color: white;")
            button.setFixedSize(50, 50)
            button.clicked.connect(lambda _, b=button: toggle_color(b))
            grid_layout.addWidget(button, i, j)
            btns_row.append(button)
        btns.append(btns_row)

    btns_layout = QHBoxLayout()
    
    submit_btn = QPushButton("Submit")
    submit_btn.clicked.connect(lambda: submit_grid(btns, 10, grid_window, window))

    clear_btn = QPushButton("Clear")
    clear_btn.clicked.connect(lambda: clear_grid(btns, 10))

    btns_layout.addWidget(clear_btn)
    btns_layout.addWidget(submit_btn)

    grid_layout.addLayout(btns_layout, 11, 0, 1, 10)

    grid_window.setLayout(grid_layout)
    