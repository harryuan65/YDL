import sys
import YDL as ydl
from PyQt5.QtWidgets import QDialog, QApplication
from UI import Ui_Form



class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pb_dl.clicked.connect(self.onClick_pbdl)
        self.ui.pb_mp3.clicked.connect(self.onClick_pbmp3)
        self.ui.pb_mp4.clicked.connect(self.onClick_pbmp4)
        self.ui.lb_display.setWordWrap(True)
        self.urlstr=""
        self.mode=""
        self.show()
        self.onClickStyle="background-color: red;"
    def onClick_pbdl(self):
        try:
            if self.mode!='':
                self.urlstr=self.ui.te_url.toPlainText()
                self.ui.lb_display.setText(self.ui.lb_display.text() + '\n' +self.urlstr)
                str = ydl.dl(self.mode,self.urlstr)
                self.ui.lb_display.setText(self.ui.lb_display.text() + '\n'+ydl.stat + '\n'+str)
            else:
                self.ui.lb_display.setText('[Error]No type specified.')
        except Exception as e:
            print(e)
           
    def onClick_pbmp3(self):
        try:
            self.ui.pb_mp3.setStyleSheet(self.onClickStyle)
            self.ui.pb_mp4.setStyleSheet("")
            self.mode='mp3'
            self.ui.lb_display.setText('As Mp3')
        except Exception as e:
            print(e)
    def onClick_pbmp4(self):
        try:
            self.ui.pb_mp4.setStyleSheet(self.onClickStyle)
            self.ui.pb_mp3.setStyleSheet("")
            self.mode='mp4'
            self.ui.lb_display.setText('As Mp4')
#self.ui.lb_display.text()
        except Exception as e:
            print(e)
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())