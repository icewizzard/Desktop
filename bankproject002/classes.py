from datetime import date

    
"""
class User:
    def __init__(self, accountnumber, username, password, email, name, dateofbirth):
        self.accountnumber=accountnumber
        self.username=username
        self.password=password
        self.email=email
        self.name=name
        self.dateofbirth=dateofbirth
        self.access_level=1

    def moneytransfer(self):
        pass
    def changename(self, name):
        if True:
            name = input("emter your name:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
            self.name = name

    def changepassword(self, password):
        if True:
            password = input("enter new password:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
            self.password=password
            
    def insertmoney(self):
        pass

    def changeemail(self, email):
        email = input("enter your email:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
        self.email=email        

    def checkbalance(self):
        pass

    def sendmessage(self):
        pass    

class Banker(User(accountnumber, username, password, email, name, dateofbirth), salary):
    def __init__(self, salary):
        self.access_level=2
        self.salary=salary

    def createuser(self, primary_key, accountnumber, username, password, email, name, dateofbirth):
        accountnumber = input("number of account:")
        username = input("username of the client:")
        password = input("password of the client:")     #ליצור דף html עם פעולות של הכנסת משתמש
        email = input("email of the client:")           # להוסיף פעולות של הוצאת מספר לקוח מהDB
        name = input("name of the client:")             # להוסיף עוד עמודות לכל DB של לקוח
        dateofbirth = input("dateofbirth of the client:")               # להוסיף פעולה של דחיפה של לקוח חדש לDB


    def removemoney(self):
        pass

    def combineusers(self):
        pass

class Manger(Banker(salary), Account(money, currency), position):
    def __init__(self, position):
        self.access_level=3
        self.position=position

    def deleteuser(self):
        pass                    #להוסיף פעולה של מחיקה מהDB USERS

    def createbanker(self):
        accountnumber = input("number of banker:")
        username = input("username of the banker:")
        password = input("password of the banker:")     #ליצור דף html עם פעולות של הכנסת משתמש
        email = input("email of the banker:")           # להוסיף פעולות של הוצאת מספר לקוח מהDB
        name = input("name of the banker:")             # להוסיף עוד עמודות לכל DB של לקוח
        dateofbirth = input("dateofbirth of the banker:")               # להוסיף פעולה של דחיפה של בנקאי חדש לDB
        salary = input("salary of banker:")

    def checksalery(self):
        pass

    def deletebanker(self):
        pass                    #להוסיף פעולה של מחיקה מהDB BANKERS

    def schedule(self):
        pass          #להעזר בפרויקט הזה על מנת לבנות לוח עבודה https://github.com/lbiedma/shift-scheduling                    


class Account(User(accountnumber, username, password, email, name, dateofbirth), money, currency):
    def __init__(self,money,currency):
        self.money=money
        self.currency=currency
"""
"""
class User:
    def __init__(self, accountnumber, username, password, email, name, dateofbirth, amount):
        self.access_level=1
        self.accountnumber=accountnumber
        self.username=username
        self.password=password
        self.email=email
        self.name=name
        self.dateofbirth=dateofbirth
        self.amount=amount

    def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def moneyminus(self, amount, accountnumber):
        if True:
            money= self.amount 
            self.amount= self.amount-money
            return self.amount+self.accountnumber

    def moneyplus(self, amount, accountnumber):
        if True:
            plusmoney = self.moneyminus
            self.amount += plusmoney
            return f"this account number {self.accountnumber} recived, {plusmoney} nis and the total amount of money now is {self.amount} " 
    
    def changename(self, name):
        if True:
            name = input("emter your name:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
            self.name = name
            return name
        
    def changepassword(self, password):
        if True:
            password = input("enter new password:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
            self.password=password
            return password
    

    def setphonenumber(self):
        if True:
            phonenumber = input("set your phone number:")
            return phonenumber

    def changeemail(self, email):
        email = input("enter your email:") # לקשר את זה לדף משתמש לקוח באת לחיצה של onclick
        self.email=email 
    
    def changeage(self, newdateofbirth):
        self.dateofbirth = newdateofbirth

class Banker(User):
    def __init__(self, accountnumber, username, password, email, name, dateofbirth, salary):
        super().__init__(accountnumber, username, password, email, name, dateofbirth)
        self.access_level=2
        self.salary = salary
    
    def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    
    def createuser(self, accountnumber, username, password, email, name, dateofbirth):
        if True:
            accountnumber = input("set account number:")
            username = input("set username:")
            password = input("set password:")
            email = input("set email:")
            name = input("set name:")
            dateofbirth = input("set date of birth:")
            newuser = User(accountnumber, username, password, email, name, dateofbirth)
            return newuser
        
    def changeage(self, newdateofbirth):
        return super().changeage(newdateofbirth)
    
    def changeemail(self, email):
        return super().changeemail(email)
    
    def changepassword(self, password):
        return super().changepassword(password)
    
    def changename(self, name):
        return super().changename(name)
    
class Manger(User):
    def __init__(self, accountnumber, username, password, email, name, dateofbirth ):
        super().__init__(accountnumber, username, password, email, name, dateofbirth)

    def createuser(self, accountnumber, username, password, email, name, dateofbirth):
        if True:
            accountnumber = input("set account number:")
            username = input("set username:")
            password = input("set password:")
            email = input("set email:")
            name = input("set name:")
            dateofbirth = input("set date of birth:")
            newuser = User(accountnumber, username, password, email, name, dateofbirth)
            return newuser    
    
    def age(birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def createbanker(self, accountnumber, username, password, email, name, dateofbirth, salary):
        if True:
            accountnumber = input("set banker number:")
            username = input("set username:")
            password = input("set password:")
            email = input("set email:")
            name = input("set name:")
            dateofbirth = input("set date of birth:")
            salary = input("set worker salary:")
            newbanker = Banker(accountnumber, username, password, email, name, dateofbirth, salary)
            return newbanker   
        
    def changeage(self, newdateofbirth):
        return super().changeage(newdateofbirth)
    
    def changeemail(self, email):
        return super().changeemail(email)
    
    def changepassword(self, password):
        return super().changepassword(password)
    
    def changename(self, name):
        return super().changename(name)
"""

