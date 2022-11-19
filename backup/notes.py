import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.textedit = QTextEdit()
        self.textedit.setFont(QFont("Consolas", 15))
        self.setCentralWidget(self.textedit)
        self.path = ""
        self.showMaximized()

        toolbar = QToolBar()

        new = QAction("New File", self)
        new.triggered.connect(self.new)

        open = QAction("Open File", self)
        open.triggered.connect(self.open)

        save_as = QAction("Save As", self)
        save_as.triggered.connect(self.save_as)

        delete_file = QAction("Delete File", self)
        delete_file.triggered.connect(self.delete_file)

        exit = QAction("Exit", self)
        exit.triggered.connect(self.exit)

        toolbar.addActions([new, open, delete_file, save_as, exit])

        font_combo_box = QFontComboBox()
        font_combo_box.setCurrentFont(QFont("Consolas"))
        font_combo_box.currentFontChanged.connect(self.textedit.setCurrentFont)

        self.font_size_combo_box = QSpinBox()
        self.font_size_combo_box.valueChanged.connect(self.change_font_size)
        self.font_size_combo_box.setValue(15)

        toolbar.addWidget(font_combo_box)
        toolbar.addWidget(self.font_size_combo_box)

        self.addToolBar(toolbar)

    def new(self):
        self.textedit.clear()

    def open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                              "all files (*.*)")

        with open(path, "rU") as f:
            document = f.read()

        self.textedit.setText(document)

    def save_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                              "all files (*.*)")

        text = self.textedit.toPlainText()

        with open(path, "w") as f:
            f.write(text)

    def delete_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Delete File", "",
                                              "all files (*.*)")

        os.remove(path)

    def exit(self):
        quit(MainWindow)

    def change_font_size(self):
        get_value = self.font_size_combo_box.value()
        self.textedit.setFontPointSize(get_value)

app = QApplication([])
app.setApplicationName("Notes")
app.setWindowIcon(QIcon("icons/Notes.png"))
window = MainWindow()
app.exec_()