from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

get_font = open("customize/costumfont.fnt").read()


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.texteditor = QTextEdit()
        codefont = get_font
        codesize = 11
        self.path = ""
        self.texteditor.setFont(QFont(codefont, codesize))
        self.setCentralWidget(self.texteditor)
        self.showMaximized()

        toolbar = QToolBar()
        toolbar.setFont(QFont(codefont, codesize))
        self.addToolBar(toolbar)

        run = QAction("Run", self)
        run.triggered.connect(self.compiler)

        toolbar.addAction(run)
        toolbar.addSeparator()

        make_new_file = QAction("New File", self)
        make_new_file.triggered.connect(self.new_file)

        open_existing_file = QAction("Open File", self)
        open_existing_file.triggered.connect(self.open_file)

        save_a_file = QAction("Save File", self)
        save_a_file.triggered.connect(self.save_file)

        exit = QAction("Exit", self)
        exit.triggered.connect(lambda: quit())

        toolbar.addActions([make_new_file, open_existing_file, save_a_file, exit])

    def compiler(self):
        text = self.texteditor.toPlainText()

        try:
            exec(text)
        except Exception as e:
            print(e)

    def new_file(self):
        self.texteditor.clear()

    def open_file(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Open File", "",
                                                   "all files (*.*)")

        try:
            with open(self.path, "r") as f:
                document = f.read()
        except Exception as e:
            print(e)
        else:
            self.setWindowTitle("Code Editor: " + self.path)
            self.texteditor.setText(document)

    def save_file(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save File", "*.*",
                                                   "Python Files (*.py), Javascript Files (*.js), Html Files(*.html), CSS Files (*.css)")

        get_text = self.texteditor.toPlainText()

        try:
            with open(self.path, "w") as f:
                f.write(get_text)
        except Exception as e:
            print(e)


app = QApplication([])
app.setApplicationName("Code Editor")
app.setWindowIcon(QIcon("icons/exe.png"))
window = MainWindow()
app.exec_()