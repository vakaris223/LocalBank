import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


def RegPage():
    RegPage = QMainWindow()
    RegPage.setWindowTitle("Registration")
    RegPage.resize(600, 600)
    RegPage.show()
    
def loginPage():
    loginPage = QMainWindow()
    loginPage.setWindowTitle("Login")
    loginPage.resize(600, 600)
    loginPage.show()

# class LoginPage(QMainWindow):
#     def __init__(self):
#         super().__init__()    
#         self.setWindowTitle("Login")
#         self.resize(600, 600)

def exitWarning():
    mbox = QMessageBox()
    mbox.setWindowTitle("Exit")
    mbox.setText("Are you sure you want to exit?")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    if(mbox.exec_() == QMessageBox.Ok):
        sys.exit()  
    

#same as window = QWidget()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LocalBank")
        self.resize(1200, 600)
        
        Login_Button = QPushButton(self)
        Login_Button.setText("Login")
        ##on the left side of the window
        Login_Button.move(0, 60)
        Login_Button.resize(200,60)
        
        Login_Button.clicked.connect(loginPage)
        
        Reg_Button = QPushButton(self)
        Reg_Button.setText("Registration")
        Reg_Button.move(0, 120)
        Reg_Button.resize(200,60)
        
        Reg_Button.clicked.connect(RegPage)
        
        Reg_Button = QPushButton(self)
        Reg_Button.setText("Exit")
        Reg_Button.move(0, 180)
        Reg_Button.resize(200,60)
       
        Reg_Button.clicked.connect(exitWarning)
        
        Login_Button.show()
        Reg_Button.show()
        Reg_Button.show()

        
    

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
