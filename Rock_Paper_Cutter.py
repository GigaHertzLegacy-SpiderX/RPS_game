import random

print("")
print("     ----- Choose Anything -----")
print("1. Rock     - 2. Paper     - 3. Scissors")

# score board
user_score = 0
machine_score = 0



while True:
    try:
        user_score = user_score
        machine_score = machine_score
        print("")
        user_input = int(input("Enter your Choice: "))
        machine_guess = random.randrange(1, 4).__floor__()

        if machine_guess == 1:
            print("Machine Guessed Rock")

        elif machine_guess == 2:
            print("Machine Guessed Paper")

        else:
            print("Machine Guessed Scissors ")

        print("")
        print("<\> Score Board </>")
        print("")

        if user_input == 1 and machine_guess == 1:
            print("Neutral")
            print("User Score:", user_score)
            print("Machine Score:", machine_score)

        elif user_input == 1 and machine_guess == 2:
            machine_score += 1
            print("User Score:", user_score)
            print("Machine Score:", machine_score)

        elif user_input == 1 and machine_guess == 3:
            user_score += 1
            print("User Score:", user_score)
            print("Machine Score:", machine_score)

        elif user_input == 2 and machine_guess == 1:
            user_score += 1
            print("User Score:", user_score)
            print("Machine Score:", machine_score)

        elif user_input == 2 and machine_guess == 2:
            print("neutral")
            print("User Score:", user_score)
            print("Machine Score:", machine_score)

        elif user_input == 2 and machine_guess == 3:
            machine_score += 1
            print("User Score:", user_score)
            print("Machine Score:", machine_score)

        elif user_input == 3 and machine_guess == 1:
            machine_score += 1
            print("User Score:", user_score)
            print("Machine Score:", machine_score)

        elif user_input == 3 and machine_guess == 2:
            user_score += 1
            print("User Score", user_score)
            print("Machine Score:", machine_score)

        elif user_input == 3 and machine_guess == 3:
            print("Neutral")
            print("User Score:", user_score)
            print("Machine Score:", machine_score)

        else:
            print("Type between 1-3 only !")

    except ValueError:
        print("")
        print("Type Something !")
