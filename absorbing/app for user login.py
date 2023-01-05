from os.path import exists
from os import system
from datetime import datetime

class AI:
    login_count = 0
    def __init__(self):
        self.family = ""
        self.userName = ""
        self.password = ""
        self.lastLogin = ""


    def ifExist(self):
        if exists("login.txt"):
            self.checkInfo()
        else:
            self.createFile()
    
    def createFile(self):
        print("new login")
        with open("login.txt", "w") as f:
            pass
        self.inputFamily()


    def inputFamily(self):
        self.family = input("input Family: ")
        var = input("do you want to confirm? 1-yes 2-no: ")
        if var == "1":
            self.inputUsername()
        elif var == "2":
            self.inputFamily()
        else:
            print("input is wrong. try again")
            self.inputFamily()

    def inputUsername(self):
        self.userName = input("input UserName: ")
        var = input("do you want to confirm? 1-yes 2-no: ")
        if var == "1":
            self.inputPassword()
        elif var == "2":
            self.inputUsername()
        else:
            print("input is wrong. try again")
            self.inputUsername()
    
    def inputPassword(self):
        self.password = input("input password: ")
        if len(self.password) < 8:
            print("your password is too short. try again")
            self.inputPassword()
        else:
            print(f"your password is: {'*'*len(self.password)}")
            password = input("confirm password: ")
            if self.password != password:
                print("password is not equal. try again")
                self.inputPassword()
            else:
                with open("login.txt", "w") as f:
                    f.write(self.userName+"\n")
                    f.write(self.password+"\n")
                    f.write(self.family+"\n")
                    system("cls")
                
                self.checkInfo()
                
    
    def checkInfo(self):
        print("AI class")
        username = input("User: ")
        password = input("password: ")
        if username == self.userName and password == self.password:
            AI.login_count+=1
            print("your info is correct")
            with open("login.txt", "a") as f:
                current_time = datetime.now()
                self.lastLogin = current_time.strftime("%d/%m/%Y %H:%M:%S")
                f.write(current_time.strftime("%d/%m/%Y %H:%M:%S")+"\n")
                f.write(str(AI.login_count)+"\n")
            self.showInfo()
            
        else:
            print("Wrong Username or Password. try again")
            self.checkInfo()
        

    def showInfo(self):
        print("\n********************")
        print(f"hello {self.family}")
        print(f"last login: {self.lastLogin}")
        print(f"number of login: {AI.login_count}")
        print("1-change family")
        print("2-change username")
        print("3-change password")
        print("4-logout")
        var = input()
        if var == "1":
            self.inputFamily()
        elif var == "2":
            self.inputUsername()
        elif var == "3":
            oldPassword = input("old password: ")
            if oldPassword == self.password:
                self.inputPassword()
            else:
                print("wrong password. try again")
                self.showInfo()
        elif var == "4":
            self.ifExist()



user = AI()
user.ifExist()