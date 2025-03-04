
# class Student:
#     def __init__(self,name,phymarks,chemmarks,csmarks):
#         self.name=name
#         self.phymarks=phymarks
#         self.chemmarks=chemmarks
#         self.csmarks=csmarks

#     def calcaverage(self):
#         avg=self.csmarks+self.chemmarks+self.phymarks/3
#         return int(avg)
     
# s1=Student("Karan",33,66,99)
# print(s1.calcaverage())
        
class Account:
    balnc=0
    def __init__(self,balnc,acctno):
        self.accntno=acctno
        self.balnc=balnc
    def debit(self,amnt):
        if(amnt>self.balnc):
            print("Not enough balance")
        else:
         self.balnc=self.balnc-amnt
         print("Balance debited, remaining amount is",self.balnc)

    def credit(self,amnt):
       self.balnc=self.balnc+amnt
       print("Amount debited",self.balnc)

cus1=Account(500,12956)
cus1.debit(300)
cus1.credit(1000)

        