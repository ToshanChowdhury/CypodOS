from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

get_font = open("customize/costumfont.fnt").read()

app = QApplication([])

title = "Calendar"
defaultcodefont = get_font
defaultcodesize = 11

cl = QCalendarWidget()
cl.setWindowTitle(title)
cl.setWindowIcon(QIcon("icons/calendar.png"))
cl.setFont(QFont(get_font, defaultcodesize))
cl.showMaximized()

app.exec_()