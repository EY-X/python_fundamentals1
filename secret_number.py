secret_number = 50
user_number = input("Enter a number! ")
if int(user_number) == 50:
    print("You win!")
elif int(user_number) == 51 or int(user_number) == 49:
    print("So close!")
else:
    print("go home!")
