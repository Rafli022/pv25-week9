import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QInputDialog, QVBoxLayout,
    QLabel, QPushButton, QGroupBox, QGridLayout, QHBoxLayout
)
from PyQt5.QtGui import QFont

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input Dialog Demo')
        self.setFixedSize(450, 250)
        self.initUI()

    def initUI(self):
        # Font
        label_font = QFont("Arial", 10)
        title_font = QFont("Arial", 12, QFont.Bold)

        # Layout utama
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Judul
        title_label = QLabel("Input Data Anda")
        title_label.setFont(title_font)
        main_layout.addWidget(title_label)

        # Group box untuk input
        group_box = QGroupBox("Input Section")
        grid = QGridLayout()
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(10)

        # 1. Language input
        lbl_lang = QLabel("Choose from list:")
        lbl_lang.setFont(label_font)
        self.result_lang = QLabel("Not selected")
        self.result_lang.setFont(label_font)
        btn_lang = QPushButton("Select")
        btn_lang.clicked.connect(self.get_choice)

        # 2. Name input
        lbl_name = QLabel("Get name:")
        lbl_name.setFont(label_font)
        self.result_name = QLabel("No name entered")
        self.result_name.setFont(label_font)
        btn_name = QPushButton("Enter")
        btn_name.clicked.connect(self.get_name)

        # 3. Number input
        lbl_num = QLabel("Enter an integer:")
        lbl_num.setFont(label_font)
        self.result_num = QLabel("No number entered")
        self.result_num.setFont(label_font)
        btn_num = QPushButton("Input")
        btn_num.clicked.connect(self.get_number)

        # Tambahkan ke grid layout: label, hasil, tombol
        grid.addWidget(lbl_lang, 0, 0)
        grid.addWidget(self.result_lang, 0, 1)
        grid.addWidget(btn_lang, 0, 2)

        grid.addWidget(lbl_name, 1, 0)
        grid.addWidget(self.result_name, 1, 1)
        grid.addWidget(btn_name, 1, 2)

        grid.addWidget(lbl_num, 2, 0)
        grid.addWidget(self.result_num, 2, 1)
        grid.addWidget(btn_num, 2, 2)

        group_box.setLayout(grid)
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)

    def get_choice(self):
        items = ("C", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "Select Input Dialog", "List of languages:", items, 0, False)
        if ok and item:
            self.result_lang.setText(item)

    def get_name(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.result_name.setText(text)

    def get_number(self):
        num, ok = QInputDialog.getInt(self, "Integer Input Dialog", "Enter a number:")
        if ok:
            self.result_num.setText(str(num))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
