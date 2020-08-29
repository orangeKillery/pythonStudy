num1=int(input("输入一个被除数："))
num2=int(input("输入一个除数："))
if num2!=0:
    result=num1/num2
    if result==int(num1/num2):
        print( int(result),":integer")
    else:
        print(result,":decimal" )
else:
    print("error")

