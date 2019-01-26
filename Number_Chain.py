user_play="y"
start_number=0
while user_play=="y"
    user_number=input("How many numbers")
    for x in range(start_number, int(user_number)+start_number):
        print(x)
    start_number=start_number+int(user_name)
    user_play=input("Continue the chain:(y)es or (n)o?")
