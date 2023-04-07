import random

marks = 0
user = 0
for _ in range(5):
    oper = [" + ", " - ", " * "]
    question = str(random.randint(2, 9)) + random.choice(oper) + str(random.randint(2, 9))
    print(question)
    while True:
        try:
            user = int(input())
            if user == eval(question):
                print("Right!")
                marks += 1
            else:
                print("Wrong!")
            break
        except ValueError:
            print("Incorrect format.")
            continue
print("Your mark is {}/5.".format(marks))