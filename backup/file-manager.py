import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.maineditor = QTextEdit()
        font = "Segoe UI"
        fontsize = 14
        self.maineditor.setFont(QFont(font, fontsize))
        self.setCentralWidget(self.maineditor)
        self.showMaximized()

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        open = QAction("Open", self)
        open.triggered.connect(self.open)

        insert_image = QAction("Insert Image", self)
        insert_image.triggered.connect(self.image)

        delete_file = QAction("Delete File", self)
        delete_file.triggered.connect(self.delete)

        self.search_files = QLineEdit()
        self.search_files.returnPressed.connect(self.search)

        toolbar.addActions([open, insert_image, delete_file])
        toolbar.addWidget(self.search_files)

    def open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                              "all files (*.*)")

        with open(path, "r") as f:
            document = f.read()

        self.maineditor.setText(document)

    def image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                              "jpeg files (*.jpeg), jpg files (*.jpg), png files (*.png)")

        document = self.maineditor.document()
        cursor = QTextCursor(document)

        cursor.insertImage(path)

    def delete(self):
        path, _ = QFileDialog.getOpenFileName(self, "Delete File", "",
                                              "all files (*.*)")

        os.remove(path)

    def search(self):
        text = self.search_files.text()
        self.search_files.clear()

        try:
            os.startfile(text)
        except Exception as e:
            print(e)


app = QApplication([])
app.setApplicationName("File Manager")
app.setWindowIcon(QIcon("icons/file-explorer.png"))
window = MainWindow()
app.exec_()