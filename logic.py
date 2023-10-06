#client class for bank


class logic():
    
    def FindUsersData(self, lname, fname):
            user = []
            for line in open("data.txt", "r").readlines():
                login_info = line.split()
                if(fname == login_info[0] and lname == login_info[1]):
                    return login_info
            return False

    def checkdata(self):
                if(self.FindUsersData(self.LnameLineLogin.text(), self.FnameLineLogin.text()) == False):
                    return False
                else:
                    for line in open("data.txt", "r").readlines():
                        login_info = line.split()
                        if(self.FnameLineLogin.text() == self.FindUsersData[0] 
                        and self.LnameLineLogin.text() == self.FindUsersData[1]
                        and self.PassLineLogin.text() == self.FindUsersData[2] 
                        and self.PinLogin.text() == self.FindUsersData[4]):
                            return True
                        else:
                            return False 
    
    
    

#def goexit_func():

# def winthdraw():

# def deposit():

# def CheckBalance(client):

# def balance():

# def CheckLogin():

# def StoreRegistration():
 