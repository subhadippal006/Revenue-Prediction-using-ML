def calculaction (num1,num2):
    add=num1+num2
    sub=num1-num2
    return add,sub
    n1=int(input("Enter the first number:"))
    n2=int(input("Enter the second number"))
    sum,sub1=calculaction (n1,n2)
    print("Addition=sum")
    print("Substraction=sub1")