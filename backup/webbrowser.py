from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.internet = QWebEngineView()
        self.internet.setUrl(QUrl("https://www.google.com/"))
        self.setCentralWidget(self.internet)

        toolbar = QToolBar("Toolbar", self)

        back = QAction("Back", self)
        back.triggered.connect(lambda: self.internet.back())

        forward = QAction("Forward", self)
        forward.triggered.connect(lambda: self.internet.forward())

        reload = QAction("Reload", self)
        reload.triggered.connect(lambda: self.internet.reload())

        toolbar.addActions([back, forward, reload])

        self.line_edit = QLineEdit()
        self.line_edit.setText("https://www.google.com")
        self.line_edit.returnPressed.connect(self.gotowebsite)
        toolbar.addWidget(self.line_edit)

        home = QAction("Home", self)
        home.triggered.connect(self.gohome)

        stop = QAction("Stop", self)
        stop.triggered.connect(lambda: self.internet.stop())

        toolbar.addActions([home, stop])

        self.addToolBar(toolbar)

    def gotowebsite(self):
        text = self.line_edit.text()

        if "https://" in text:
            self.internet.setUrl(QUrl(text))
            self.line_edit.setText(text)
        else:
            self.internet.setUrl(QUrl("https://"+text))
            self.line_edit.setText("https://"+text)


    def gohome(self):
        self.line_edit.setText("https://www.google.com")
        self.internet.setUrl(QUrl("https://www.google.com"))


app = QApplication([])
app.setApplicationName("Web Browser")
app.setWindowIcon(QIcon("icons/Web Browser.png"))
window = MainWindow()
window.showMaximized()
app.exec_()