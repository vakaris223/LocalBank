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
import ClientLogic

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
        
        
    def PopUpMsg(self, title, text, info, icon):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setInformativeText(info)
        msg.exec_()
        return msg.clickedButton()
        
    def login(self):
        if Client.check_login_data(self.FnameLineLogin.text(), self.LnameLineLogin.text(), self.PassLineLogin.text(), self.PinLogin.text()):
            self.LoginFrame.setVisible(False)
            self.RegFrame.setVisible(False)
            self.ClientMenuFrame.setVisible(True)
        else:
            self.PopUpMsg("Login Failed", "Login Failed", "Wrong username or password.", QMessageBox.Warning)
                
    def register(self):
        data = open("data.txt", "w")
        if(self.FnameLine.text() == "" or self.LnameLine.text() == "" or self.PassLine.text() == "" or self.GmailLine.text() == "" or self.AddressLine.text() ==  "" or self.MobileLine.text() ==  "" or self.AgeBox.text() == ""):
            print(ClientLogic.ageValid(self.AgeBox))
            self.PopUpMsg("Register Failed", "Register Failed", "Please fill all the fields.", QMessageBox.Warning)
            
        elif (self.PassLine.text() != self.RPassLine.text()):
            self.PopUpMsg("Register Failed", "Register Failed", "Passwords do not match.", QMessageBox.Warning)
            
        else:
            data.write(self.FnameLine.text())
            data.write(" ")
            data.write(self.LnameLine.text())
            data.write(" ")
            data.write(self.PassLine.text())
            data.write(" ")
            data.write(format(randint(0000,9999)))
            data.write(" ")
            data.write(format(randint(0000000000000000,9999999999999999)))
            data.write(" ")
            data.write(self.GmailLine.text())
            data.write(" ")
            data.write(self.AddressLine.text())
            data.write(" ")
            data.write(self.MobileLine.text())
            data.write(" ")
            data.write(self.AgeBox.text())

            self.PopUpMsg("Register Success", "Register Success", "You have successfully registered.", QMessageBox.Information)
            
        data.close()
        #we will write in data int .txt file
       
    def Exit(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setWindowTitle("Exit")
        msg.setText("Do you want to exit?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.setInformativeText("Are you sure?")
        msg.exec_()
        
        if msg.clickedButton() == msg.button(QMessageBox.Yes):
            sys.exit()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    app.exec_()

