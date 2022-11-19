import os
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from tkinter import messagebox as m

toolbar_color = open("customize/color_toolbar.txt")
read_toolbar_color = toolbar_color.read()

menu_bar_color = open("customize/menu_bar_color.txt")
read_menu_bar_color = menu_bar_color.read()

customize_color = open("customize/costumfont.fnt").read()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)
        self.showMaximized()

        self.maintab = QWebEngineView()
        self.maintab.setUrl(QUrl("https://www.google.com"))
        self.tabs.addTab(self.maintab, "Main")

        self.menu_bar = QMenuBar()
        self.menu_bar.setStyleSheet("background-color: "+read_menu_bar_color)
        self.menu_bar.setFont(QFont(customize_color, 11))
        self.setMenuBar(self.menu_bar)

        self.functions_menu = QMenu("Functions", self)
        self.functions_menu.setStyleSheet("background-color: "+read_menu_bar_color)
        self.functions_menu.setFont(QFont(customize_color, 11))
        self.menu_bar.addMenu(self.functions_menu)

        self.settings_menu = QMenu("Settings", self)
        self.settings_menu.setStyleSheet("background-color: "+read_menu_bar_color)
        self.settings_menu.setFont(QFont(customize_color, 11))
        self.functions_menu.addMenu(self.settings_menu)

        self.add_tab = QAction("Add Tab", self)
        self.add_tab.triggered.connect(self.new_tab)
        self.settings_menu.addAction(self.add_tab)

        self.customiziation = QAction("Color Customization", self)
        self.customiziation.triggered.connect(lambda: os.startfile("color.py"))
        self.settings_menu.addAction(self.customiziation)

        self.set_font = QAction("Font Customization", self)
        self.set_font.triggered.connect(self.font)
        self.settings_menu.addAction(self.set_font)

        self.apps_menu = QMenu("Apps", self)
        self.apps_menu.setStyleSheet("background-color: " + read_menu_bar_color)
        self.apps_menu.setFont(QFont(customize_color, 11))
        self.functions_menu.addMenu(self.apps_menu)

        file_manager = QAction(QIcon("icons/file-explorer.png"), "File Manager", self)
        file_manager.triggered.connect(lambda: os.startfile("file-manager.py"))

        calculator = QAction(QIcon("icons/Calculator.png"), "Calculator", self)
        calculator.triggered.connect(lambda: os.startfile("Calculator.py"))

        codeeditor = QAction(QIcon("icons/exe.png"), "Code Editor", self)
        codeeditor.triggered.connect(lambda: os.startfile("codeeditor.py"))

        notes = QAction(QIcon("icons/notes.png"), "Notes", self)
        notes.triggered.connect(lambda: os.startfile("notes.py"))

        terminal = QAction(QIcon("icons/terminal.png"), "Terminal", self)
        terminal.triggered.connect(lambda: os.startfile("terminal.py"))

        webbrowser = QAction(QIcon("icons/Web Browser.png"), "Web Browswer", self)
        webbrowser.triggered.connect(lambda: os.startfile("webbrowser.py"))

        calendar = QAction(QIcon("icons/calendar.png"), "Calendar", self)
        calendar.triggered.connect(lambda: os.startfile("calendar.py"))

        time_app = QAction(QIcon("icons/clock.png"), "Time", self)
        time_app.triggered.connect(lambda: os.startfile("app_time.py"))

        google_docs = QAction(QIcon("icons/google-docs.png"), "Google Docs", self)
        google_docs.triggered.connect(lambda: self.tabs.currentWidget().setUrl(QUrl("https://www.google.com/docs")))

        google_sheets = QAction(QIcon("icons/google-sheets.png"), "Google Sheets", self)
        google_sheets.triggered.connect(lambda: self.tabs.currentWidget().setUrl(QUrl("https://www.google.com/sheets")))

        google_slides = QAction(QIcon("icons/google-slides.png"), "Google Slides", self)
        google_slides.triggered.connect(lambda: self.tabs.currentWidget().setUrl(QUrl("https://www.google.com/slides")))

        self.apps_menu.addActions([file_manager, calculator, codeeditor, notes, terminal, webbrowser,  calendar, time_app, google_docs, google_sheets, google_slides])

        power_menu = QMenu("Power Options", self)
        power_menu.setStyleSheet("background-color: "+read_menu_bar_color)
        power_menu.setFont(QFont(customize_color, 11))
        self.functions_menu.addMenu(power_menu)

        shut_down = QAction(QIcon("icons/Shut Down.png"), "Shut Down", self)
        shut_down.triggered.connect(self.shut_down)

        restart = QAction(QIcon("icons/Restart.png"), "Restart", self)
        restart.triggered.connect(self.restart)

        power_menu.addActions([shut_down, restart])

        self.toolbar = QToolBar()
        self.toolbar.setStyleSheet("background-color: "+read_toolbar_color)
        self.addToolBar(Qt.BottomToolBarArea, self.toolbar)

        file_manager = QAction(QIcon("icons/file-explorer.png"), "File Manager", self)
        file_manager.triggered.connect(lambda: os.startfile("file-manager.py"))

        calculator = QAction(QIcon("icons/Calculator.png"), "Calculator", self)
        calculator.triggered.connect(lambda: os.startfile("Calculator.py"))

        codeeditor = QAction(QIcon("icons/exe.png"), "Code Editor", self)
        codeeditor.triggered.connect(lambda: os.startfile("codeeditor.py"))

        notes = QAction(QIcon("icons/notes.png"), "Notes", self)
        notes.triggered.connect(lambda: os.startfile("notes.py"))

        terminal = QAction(QIcon("icons/terminal.png"), "Terminal", self)
        terminal.triggered.connect(lambda: os.startfile("terminal.py"))

        webbrowser = QAction(QIcon("icons/Web Browser.png"), "Web Browswer", self)
        webbrowser.triggered.connect(lambda: os.startfile("webbrowser.py"))

        calendar = QAction(QIcon("icons/calendar.png"), "Calendar", self)
        calendar.triggered.connect(lambda: os.startfile("calendar.py"))

        time_app = QAction(QIcon("icons/clock.png"), "Time", self)
        time_app.triggered.connect(lambda: os.startfile("app_time.py"))

        google_docs = QAction(QIcon("icons/google-docs.png"), "Google Docs", self)
        google_docs.triggered.connect(lambda: self.tabs.currentWidget().setUrl(QUrl("https://www.google.com/docs")))

        google_sheets = QAction(QIcon("icons/google-sheets.png"), "Google Sheets", self)
        google_sheets.triggered.connect(lambda: self.tabs.currentWidget().setUrl(QUrl("https://www.google.com/sheets")))

        google_slides = QAction(QIcon("icons/google-slides.png"), "Google Slides", self)
        google_slides.triggered.connect(lambda: self.tabs.currentWidget().setUrl(QUrl("https://www.google.com/slides")))

        self.toolbar.addActions([file_manager, calculator, codeeditor, notes, terminal, webbrowser,  calendar, time_app, google_docs, google_sheets, google_slides])

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.toolbar.addWidget(spacer)

        self.datetime = time.strftime("%I:%M %p")

        self.time = QAction(self.datetime, self)
        self.time.triggered.connect(self.update_time)
        self.toolbar.addAction(self.time)


    def close_tab(self, i):
        self.tabs.removeTab(i)

    def new_tab(self):
        new_tab = QWebEngineView()
        new_tab.setUrl(QUrl("https://www.google.com/"))
        self.tabs.addTab(new_tab, "New Tab")

    def shut_down(self):
        try:
            quit()
        except Exception as e:
            m.showinfo(title="Settings", message=e)

    def restart(self):
        try:
            reopen = "loginsystem.py"
            os.startfile(reopen)
            quit()
        except Exception as e:
            m.showinfo(title="Settings", message=e)

    def update_time(self):
        try:
            gettime = time.strftime("%I:%M %p")
            self.time.setText(gettime)
        except Exception as e:
            m.showinfo(title="Settings", message=e)

    def font(self):
        os.startfile("fonts.py")

app = QApplication([])
app.setApplicationName("CypodOS 2.0")
app.setWindowIcon(QIcon("icons/Cypod_icon.png"))
window = MainWindow()
app.exec_()