#multiple inheritence example
class employee:
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print("name:",self.name)

class salary:
    def __init__(self,pay):
        self.pay=pay

    def show_pay(self):
        print("pay:",self.pay)
    

class payroll(employee,salary):
    def __init__(self,name,pay):
         employee.__init__(self,name)
         salary.__init__(self,pay)

    def show_info(self):
       self.show_name()
       self.show_pay()

s1=payroll("saakshi",20)
s1.show_info()
    
    