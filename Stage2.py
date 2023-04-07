import random

random_one = random.randint(2, 9)
random_two = random.randint(2, 9)
oper = ["+", "-", "*"]
random_oper = random.choice(oper)
result = 0
if random_oper == "+":
    result = (int(random_one) + int(random_two))
elif random_oper == "-":
    result = (int(random_one) - int(random_two))
elif random_oper == "*":
    result = (int(random_one) * int(random_two))
elif random_oper == "/":
    result = (int(random_one) / int(random_two))
else:
    print("Error")

print(str(random_one) + " " + str(random_oper) + " " + str(random_two))
user = int(input())
if user == result:
    print("Right!")
else:
    print("Wrong!")


    
