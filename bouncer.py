print("How old are you?")
age = input()
if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but you need a wristband!")
    elif age >= 21:
        print("You can enter, please drink responsibly")
    else:
        print("You are not old enough to enter")
else:
    print("You must tell me how old you are")