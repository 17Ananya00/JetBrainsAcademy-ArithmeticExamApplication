a,oper,b = input().split()

if oper == "+":
    print(int(a) + int(b))
elif oper == "-":
    print(int(a) - int(b))
elif oper == "*":
    print(int(a) * int(b))
elif oper == "/":
    print(int(a) / int(b))
else:
    print("Error")
