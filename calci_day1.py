# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello world")
#calci
def func():
    try:
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
                if operator == '+':
                    print("adding two numbers",operand_1+operand_2)
                elif operator == '-':
                    print("sub two numbers",operand_1-operand_2)
                elif operator == '*':
                    print("sub two numbers",operand_1*operand_2)
                elif operator == "/":
                    print("sub two numbers",operand_1/operand_2)
                next=input("whether you want perform another operation(yes/no):")
                if next=="no":
                    break
             else:
                print("Invalid input")
    except Exception as e:
        print(e)
func()
        
        
        