class Calculator:
    def __init__(self,operand_1,operand_2):
        self.operand_1=operand_1
        self.operand_2=operand_2
    #@staticmethod
    def add(self):
        print('addition',self.operand_1+self.operand_2)
    #@staticmethod
    def sub(self):
        print('subtraction',self.operand_1-self.operand_2)
        
    def mul(self):
        print('multiplication',self.operand_1*self.operand_2)
    def div(self):
        print('division',self.operand_1*self.operand_2)

next="yes"
while next=="yes":
    data=input("enter the string:")
    output=data.split()
    print(output)
    #print(len(output))
    if len(output)==3:
        operand_1=float(output[0])
        operator=output[1]
        operand_2=float(output[2])
        #cal=Calculator()
        cal=Calculator(operand_1,operand_2)
        if operator=='+':
            cal.add()
        elif operator=='-':
            cal.sub()
        elif operator=='*':
            cal.mul()
        elif operator=='/':
            cal.div()
        if next=="no":
                break
    else:
        print("Invalid input")

    