from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

app = QApplication([])

title = "Calendar"

cl = QCalendarWidget()
cl.setWindowTitle(title)
cl.setWindowIcon(QIcon("icons/calendar.png"))
cl.setFont(QFont("Segoe UI", 12, QFont.Bold))
cl.showMaximized()

app.exec_()