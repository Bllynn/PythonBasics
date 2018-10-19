print("Enter your favorite animal")
user_input=input()
if user_input:
    if user_input == "dog":
        print(f"Hell yeah! {user_input}'s are MY favorite animal too!")
    else:
        print(f"I guess {user_input}'s are alright.")
else:
    print("Please enter an animal")