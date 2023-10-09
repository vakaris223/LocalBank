

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
                        
                        
print(checkdata("c", "a", "a", "1111"))
