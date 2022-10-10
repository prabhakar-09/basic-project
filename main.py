print("Welcome to my basic game!")
name = input("What is your name?? ")
age  = int(input("What is your age? "))
print(f"Hello {name} and you are {age} years old")
health = 10


if age >= 19:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print(f"you are starting with {health} health")
        print("Lets playyy..")
        left_or_right = input("First choice, left or right? ").lower()
        if left_or_right == "left":
            ans = input("Nice.. you followed the path and reach a lake, "
                  "do you wanna swim across or go around(across/around)? ").lower()
            if ans == "around":
                print("You went around and reached other side of the lake ..")

            elif ans == "across":
                print("You managed to get across, but were bit by a fish and you lost 5 health")
                health -=5
            ans = input("You notice a house and a river. which one "
                        "do you wanna go to..(river/house)? ").lower()

            if ans == "house":
                print("you go to the house and are greeted by the owner..."
                      "He doesn't like you and you loose 5 health")
                health -=5
                if health <= 0:
                    print("you now have 0 health and lost the game...")
                else:
                    print("You have survived... You winn!!")
            else:
                print("You fell in the river boy.. You LOST:/")
        else:
            print("You fell down and lost..:/")
else:
    print("You are not old enough to play...")