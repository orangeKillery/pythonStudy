flag=1
while(flag):
    temp=input("请输入一个带符号的温度值：")
    if temp[-1] in {'c','C'}:
        fah=eval(temp[0:-1])*1.8+32
        print("相应的华氏度是{:.2f}F".format(fah))
    elif temp[-1] in {'f','F'}:
        cel=(eval(temp[0:-1])-32)/1.8
        print("相应的摄氏度是{:.2f}C".format(cel))
    else:
        print("输入错误，重新输入")
    print("退出输入0，继续输入1")
    flag=input()


