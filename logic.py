#client class for bank

def writeData(Fname, Lname, Pass, Gmail, Address, Mobile, Age):
    with open("data.txt", "w") as f:
        
        f.write(self.Fname)
        f.write(" ")
        
        f.write(self.Lname)
        f.write(" ")
        
        f.write(self.Pass)
        f.write(" ")
        
        #pin
        f.write(format(randint(0000,9999)))
        f.write(" ")
        
        #credit card num
        f.write(format(randint(0000000000000000,9999999999999999)))
        f.write(" ")
        
        f.write(self.Gmail)
        f.write(" ")
        
        f.write(self.Address)
        f.write(" ")
        
        f.write(self.Mobile)
        f.write(" ")
        
        f.write(self.Age)
        
        return True
        f.close()
    
        
        
def FindUsersData(fname, lname):
    with open("data.txt", "r") as f:
        for line in f.readlines():
            login_info = line.split()
            if lname in login_info and fname in login_info:
                return login_info
        return False
    
def checkdata(fname, lname, password, pin):
            log = FindUsersData(fname, lname)
            
            if not log:
                return False
            else:
                with open("data.txt", "r") as f:
                    for line in f.readlines():
                        login_info = line.split()
                        if(fname == log[0] 
                        and lname == log[1]
                        and password == log[2] 
                        and pin == log[3]):
                            print(log)
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
 