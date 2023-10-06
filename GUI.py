import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *
from random import randint
from client import Client
import time

class GUI(QMainWindow):
    def __init__(self):
        super(GUI, self).__init__()
        #load the ui file
        uic.loadUi("./LocalBank.ui", self)
        
        #set background color
        self.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.setWindowTitle("LocalBank")
        self.setWindowIcon(QIcon("./pictures/MiniLogo.png"))
        #load logo
        self.NameLbl.setPixmap(QPixmap("./pictures/LocalBankLogoResize.png"))
        
        #center the picture
        self.NameLbl.setAlignment(Qt.AlignCenter)
        
        #show the window
        self.show()
        
        #set the pages and turn on login page (starting page)
        self.LoginFrame.setVisible(False)
        self.RegFrame.setVisible(False)
        self.ClientMenuFrame.setVisible(False)
        self.UserMainMenuFrame.setVisible(True)
        
        #set the background color of the frames
        self.LoginFrame.setStyleSheet("background-color: rgb(170, 170, 170);") 
        self.ClientMenuFrame.setStyleSheet("background-color: rgb(170, 170, 170);") 
        self.RegFrame.setStyleSheet("background-color: rgb(170, 170, 170);") 
        self.UserMainMenuFrame.setStyleSheet("background-color: rgb(170, 170, 170);") 
        
        
        #buttons that calls functions
        self.RegBtn.clicked.connect(self.register)
        self.LoginBtn.clicked.connect(self.login)
        
        #exit button on main page
        self.ExitBtn.clicked.connect(self.Exit)
        
        #button that direct to page that you can login or register
        self.LoginPageBtn.clicked.connect(self.loginPage)
        self.RegPageBtn.clicked.connect(self.regPage)
        self.BackBtn.clicked.connect(self.loginPage)
        
        #client.py is running
        Client.run()
        
        
    def loginPage(self):
        #clear all fields and show login page
        self.LoginFrame.setVisible(True)
        self.RegFrame.setVisible(False)
        self.ClientMenuFrame.setVisible(False)
        #hide password
        self.PassLineLogin.setEchoMode(QLineEdit.Password)
        self.PinLogin.setEchoMode(QLineEdit.Password)
        
    def regPage(self):
        #clear all fields and show reg page
        self.LoginFrame.setVisible(False)
        self.RegFrame.setVisible(True)
        
        
    def PopUpMsg(self, title, text, info, icon, DButton, SButton):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setStandardButtons(SButton)
        msg.setDefaultButton(DButton)

        msg.setInformativeText(info)
        msg.exec_()
        return msg.clickedButton()
        
    # def FindUsersData(self, lname, fname):
    #     user = []
    #     for line in open("data.txt", "r").readlines():
    #         login_info = line.split()
    #         if(fname == login_info[0] and lname == login_info[1]):
    #             return login_info
    #     return False
    
    # def checkdata(self):
    #         if(self.FindUsersData(self.LnameLineLogin.text(), self.FnameLineLogin.text()) == False):
    #             msg = QMessageBox()
    #             msg.setIcon(QMessageBox.Warning)
    #             msg.setWindowTitle("Login Failed")
    #             msg.setText("No user")
    #             msg.setStandardButtons(QMessageBox.Ok)
    #             msg.setDefaultButton(QMessageBox.Ok)
    #             msg.setInformativeText("No user that name was found.")
    #             msg.exec_()  
    #         else:
    #             for line in open("data.txt", "r").readlines():
    #                 login_info = line.split()
    #                 if(self.FnameLineLogin.text() == self.FindUsersData[0] 
    #                 and self.LnameLineLogin.text() == self.FindUsersData[1]
    #                 and self.PassLineLogin.text() == self.FindUsersData[2] 
    #                 and self.PinLogin.text() == self.FindUsersData[4]):
    #                     return True
    #                 else:
    #                     return False 
                
   
    def login(self):
        if client.check_login_data(self.FnameLineLogin.text(), self.LnameLineLogin.text(), self.PassLineLogin.text(), self.PinLogin.text()):
            self.LoginFrame.setVisible(False)
            self.RegFrame.setVisible(False)
            self.ClientMenuFrame.setVisible(True)
        else:
            self.PopUpMsg("Login Failed", "Login Failed", "Wrong username or password.", QMessageBox.Warning, QMessageBox.Ok, QMessageBox.Ok)
                
    def register(self):
        data = open("data.txt", "w")
        if(self.FnameLine.text() == "" 
           or self.LnameLine.text() == "" 
           or self.PassLine.text() == "" 
           or self.GmailLine.text() == "" 
           or self.AddressLine.text() ==  "" 
           or self.MobileLine.text() ==  "" 
           or self.AgeBox.text() == ""):
            self.PopUpMsg("Register Failed", "Register Failed", "Please fill all the fields.", QMessageBox.Warning, QMessageBox.Ok, QMessageBox.Ok)

        elif (self.PassLine.text() != self.RPassLine.text()):
            self.PopUpMsg("Register Failed", "Register Failed", "Passwords do not match.", QMessageBox.Warning, QMessageBox.Ok, QMessageBox.Ok)
        else:
            data.write(self.FnameLine.text())
            data.write(" ")
            data.write(self.LnameLine.text())
            data.write(" ")
            data.write(self.PassLine.text())
            data.write(" ")
            data.write(format(randint(0000000000000000,9999999999999999)))
            data.write(" ")
            data.write(format(randint(0000,9999)))
            data.write(" ")
            data.write(self.GmailLine.text())
            data.write(" ")
            data.write(self.AddressLine.text())
            data.write(" ")
            data.write(self.MobileLine.text())
            data.write(" ")
            data.write(self.AgeBox.text())

            self.PopUpMsg("Register Success", "Register Success", "You have successfully registered.", QMessageBox.Information, QMessageBox.Ok, QMessageBox.Ok)
            
        data.close()
        #we will write in data int .txt file
       
    def Exit(self):
        #are you sure?\
        #self, title, text, info, icon, DButton, SButton
        
        if(self.PopUpMsg("Exit", "Exit", "Are you sure you want to exit?", QMessageBox.Warning, QMessageBox.Yes, QMessageBox.Yes) == QMessageBox.Yes):
            self.close()
        else:
            pass
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    app.exec_()

