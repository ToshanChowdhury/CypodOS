import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        label = QLabel()
        label.setFont(QFont("Segoe UI", 11))
        label.setText("There are only 30+ Apps 'recommended', so you can go to the application website and download the application on to your system.")
        toolbar.addWidget(label)

        self.webbrowser = QWidget()

        self.layout = QVBoxLayout()

        google_chrome = QPushButton("Google Chrome", self)
        google_chrome.setFixedSize(100, 40)
        google_chrome.clicked.connect(lambda: os.startfile("https://www.google.com/chrome/?brand=YTUH&gclid=Cj0KCQjwwfiaBhC7ARIsAGvcPe65X7mtDONSl1p-Ng_VsSEUPIASKEjw81WUakvDBc-H3JocMVCAFk0aAliPEALw_wcB&gclsrc=aw.ds"))
        self.layout.addWidget(google_chrome)

        microsoft_edge = QPushButton("Microsoft Edge", self)
        microsoft_edge.setFixedSize(100, 40)
        microsoft_edge.clicked.connect(lambda: os.startfile("https://www.microsoft.com/en-us/edge?form=MA13FJ"))
        self.layout.addWidget(microsoft_edge)

        opera = QPushButton("Opera", self)
        opera.clicked.connect(lambda: os.startfile("https://www.opera.com/"))
        opera.setFixedSize(100, 40)
        self.layout.addWidget(opera)

        opera_gx = QPushButton("Opera GX", self)
        opera_gx.setFixedSize(100, 40)
        opera_gx.clicked.connect(lambda: os.startfile("https://www.opera.com/download#opera-gx"))
        self.layout.addWidget(opera_gx)

        crypto_browser = QPushButton("Opera Crypto Browser", self)
        crypto_browser.setFixedSize(200, 40)
        crypto_browser.clicked.connect(lambda: os.startfile("https://www.opera.com/download#crypto-browser"))
        self.layout.addWidget(crypto_browser)

        firefox_quantum = QPushButton("FireFox Quantum", self)
        firefox_quantum.setFixedSize(150, 40)
        firefox_quantum.clicked.connect(lambda: os.startfile("https://www.mozilla.org/en-US/firefox/browsers/quantum/"))
        self.layout.addWidget(firefox_quantum)

        vivaldi = QPushButton("Vivaldi", self)
        vivaldi.setFixedSize(100, 40)
        vivaldi.clicked.connect(lambda: os.startfile("https://vivaldi.com/download/"))
        self.layout.addWidget(vivaldi)

        brave = QPushButton("Brave", self)
        brave.setFixedSize(100, 40)
        brave.clicked.connect(lambda: os.startfile("https://try.bravesoftware.com/jma500/?msclkid=fbcabc619bd61e8a715ddf3f585a6020"))
        self.layout.addWidget(brave)

        slim_browser = QPushButton("Slim Browser", self)
        slim_browser.clicked.connect(lambda: os.startfile("https://www.slimbrowser.net/"))
        slim_browser.setFixedSize(100, 40)
        self.layout.addWidget(slim_browser)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(spacer)

        self.webbrowser.setLayout(self.layout)
        self.tabs.addTab(self.webbrowser, "Web Browsers")

        self.coding_software = QWidget()

        layout = QVBoxLayout()

        python_3 = QPushButton("Python 3", self)
        python_3.setFixedSize(100, 40)
        python_3.clicked.connect(lambda: os.startfile("https://www.python.org/downloads/release/python-3110/"))
        layout.addWidget(python_3)

        pycharm = QPushButton("JetBrains PyCharm", self)
        pycharm.clicked.connect(lambda: os.startfile("https://www.jetbrains.com/pycharm/download/download-thanks.html"))
        pycharm.setFixedSize(150, 40)
        layout.addWidget(pycharm)

        visual_studio_code = QPushButton("Microsoft Visual Studio Code", self)
        visual_studio_code.clicked.connect(lambda: os.startfile("https://code.visualstudio.com/Download"))
        visual_studio_code.setFixedSize(200, 40)
        layout.addWidget(visual_studio_code)

        notepadplusplus = QPushButton("Notepad++", self)
        notepadplusplus.clicked.connect(lambda: os.startfile("https://notepad-plus-plus.org/downloads/v8.4.6/"))
        notepadplusplus.setFixedSize(100, 40)
        layout.addWidget(notepadplusplus)

        sublime_text = QPushButton("Sublime Text", self)
        sublime_text.clicked.connect(lambda: os.startfile("https://www.sublimetext.com/download"))
        sublime_text.setFixedSize(100, 40)
        layout.addWidget(sublime_text)

        pyqt5 = QPushButton("Python PyQt5 Library", self)
        pyqt5.clicked.connect(lambda: os.startfile("https://pypi.org/project/PyQt5/"))
        pyqt5.setFixedSize(150, 40)
        layout.addWidget(pyqt5)

        pyqtwebengine = QPushButton("Python PyQtWebEngine Library", self)
        pyqtwebengine.clicked.connect(lambda: os.startfile("https://pypi.org/project/PyQtWebEngine/"))
        pyqtwebengine.setFixedSize(200, 40)
        layout.addWidget(pyqtwebengine)

        opencv_python = QPushButton("Python OpenCV", self)
        opencv_python.setFixedSize(150, 40)
        opencv_python.clicked.connect(lambda: os.startfile("https://pypi.org/project/opencv-python/"))
        layout.addWidget(opencv_python)

        scratch = QPushButton("Scratch Offline Editor", self)
        scratch.setFixedSize(150, 40)
        scratch.clicked.connect(lambda: os.startfile("https://scratch.mit.edu/download"))
        layout.addWidget(scratch)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(spacer)

        self.coding_software.setLayout(layout)

        self.tabs.addTab(self.coding_software, "Coding Software")

        cloud = QWidget()

        layout = QVBoxLayout()

        onedrive = QPushButton("Microsoft OneDrive", self)
        onedrive.clicked.connect(lambda: os.startfile("https://go.microsoft.com/fwlink/p/?LinkID=2182910&clcid=0x4009&culture=en-in&country=US"))
        onedrive.setFixedSize(150, 40)
        layout.addWidget(onedrive)

        drop_box = QPushButton("Dropbox", self)
        drop_box.clicked.connect(lambda: os.startfile("https://www.dropbox.com/download?os=#"))
        drop_box.setFixedSize(100, 40)
        layout.addWidget(drop_box)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(spacer)

        cloud.setLayout(layout)

        self.tabs.addTab(cloud, "Cloud Applications")

        self.office_suite = QWidget()

        officesuite_layout = QVBoxLayout()

        caligra = QPushButton("Caligra Suite", self)
        caligra.clicked.connect(lambda: os.startfile("https://userbase.kde.org/Calligra/Download#MS_Windows"))
        caligra.setFixedSize(100, 40)
        officesuite_layout.addWidget(caligra)

        wps_office = QPushButton("WPS Office", self)
        wps_office.clicked.connect(lambda: os.startfile("https://www.wps.com/"))
        wps_office.setFixedSize(100, 40)
        officesuite_layout.addWidget(wps_office)

        libre_office = QPushButton("Libre Office", self)
        libre_office.clicked.connect(lambda: os.startfile("https://www.libreoffice.org/download/download-libreoffice/"))
        libre_office.setFixedSize(100, 40)
        officesuite_layout.addWidget(libre_office)

        free_office = QPushButton("FreeOffice", self)
        free_office.clicked.connect(lambda: os.startfile("https://www.freeoffice.com/en/download"))
        free_office.setFixedSize(100, 40)
        officesuite_layout.addWidget(free_office)

        softmaker_office = QPushButton("SoftMaker Office", self)
        softmaker_office.clicked.connect(lambda: os.startfile("https://www.softmaker.com/en/softmaker-office"))
        softmaker_office.setFixedSize(150, 40)
        officesuite_layout.addWidget(softmaker_office)

        free_office_pdf = QPushButton("FreeOffice PDF", self)
        free_office_pdf.clicked.connect(lambda: os.startfile("https://www.getfreepdf.com/en/"))
        free_office_pdf.setFixedSize(100, 40)
        officesuite_layout.addWidget(free_office_pdf)

        quip = QPushButton("Quip", self)
        quip.clicked.connect(lambda: os.startfile("https://quip.com/"))
        quip.setFixedSize(100, 40)
        officesuite_layout.addWidget(quip)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        officesuite_layout.addWidget(spacer)

        self.office_suite.setLayout(officesuite_layout)

        self.tabs.addTab(self.office_suite, "Office Suites")

        self.antivirus = QWidget()
        antivirus_layout = QVBoxLayout()

        avast = QPushButton("Avast Free Antivirus", self)
        avast.clicked.connect(lambda: os.startfile("https://www.avast.com/en-us/index#pc"))
        avast.setFixedSize(150, 40)
        antivirus_layout.addWidget(avast)

        avg = QPushButton("AVG", self)
        avg.clicked.connect(lambda: os.startfile("https://www.avg.com/en-ww/ppc/protection-offer-comparison-04?ppc_code=013&ppc=a&&msclkid=f4a073ddb32111db724410b60167cc6a&utm_source=bing&utm_medium=cpc&utm_campaign=en-ww_bav_sch_brn_exc_bng_dtp&utm_term=avg%20download&utm_content=top-avg_download-exact&gclid=f4a073ddb32111db724410b60167cc6a&gclsrc=3p.ds#pc"))
        avg.setFixedSize(100, 40)
        antivirus_layout.addWidget(avg)

        malware_bytes = QPushButton("Malwarebytes", self)
        malware_bytes.clicked.connect(lambda: os.startfile("https://www.malwarebytes.com/mwb-download/thankyou"))
        malware_bytes.setFixedSize(100, 40)
        antivirus_layout.addWidget(malware_bytes)

        avira = QPushButton("Avira", self)
        avira.clicked.connect(lambda: os.startfile("https://www.avira.com/en/start-download/product/2262/-I12e2mvtstLKUkGnG-U3eKJ0uofLc0hU9xCRx-aYuBBOiLOFMgKktbw-KT6YPslY3X0hFL4yXlTfNsbPfqL_A"))
        avira.setFixedSize(100, 40)
        antivirus_layout.addWidget(avira)

        norton_360 = QPushButton("Norton 360 Antivirus", self)
        norton_360.clicked.connect(lambda: os.startfile("https://us.norton.com/downloads#trials"))
        norton_360.setFixedSize(150, 40)
        antivirus_layout.addWidget(norton_360)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        antivirus_layout.addWidget(spacer)

        self.antivirus.setLayout(antivirus_layout)
        self.tabs.addTab(self.antivirus, "Antivirus")

        self.showMaximized()


app = QApplication([])
app.setApplicationName("Cypod Store")
window = MainWindow()
app.exec_()