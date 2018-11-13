import sys
import YDL as ydl
from PyQt5.QtWidgets import QDialog, QApplication
from UI import Ui_Form



class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setstr='Hello'
        self.teststr='T'
        self.ui.pb.clicked.connect(self.pushButton_Click)
        self.show()
    def pushButton_Click(self):
        self.setstr = self.setstr + self.teststr
        self.ui.lbd.setText(self.setstr)
		

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())