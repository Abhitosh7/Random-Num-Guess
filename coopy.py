
print("====NUMBER GUESSING GAME===")
print("Select Difficulty: \n1.Easy \n2.Medium \n3.Hard")

difficulty = int(input("Enter the Difficulty"))

import random
attempts = 1

while True:
    while True:
    # try:
        match difficulty:
            case 1:
                print("********** Easy Mode! ***********")
                ran_num_guess = random.randint(1, 10)  
                while True:
                    a = int(input("Guess the num between "))
                    print(ran_num_guess)

                    if(a==ran_num_guess):
                        print("Congratulations! You guessed the number")
                        print("The number is: ",ran_num_guess)
                        print("Attempts= ",attempts)
                        break
                    elif(a>ran_num_guess):
                        print("Too high!")
                    elif(a<ran_num_guess):
                        print("Too low")
                    print("Attempts= ",attempts)
                    attempts = attempts+1
                    
                break

            case 2:
                print("********** Medium Mode! *************")
                ran_num_guess = random.randint(1, 50)
                # print(ran_num_guess)
                while True:
                        attempts = 0
                        for attempts in range(0,10):
                            a = int(input("Guess the num between "))
                            print(ran_num_guess)
                
                            if(a==ran_num_guess):
                                print("Congratulations! You guessed the number")
                                print("The number is: ",ran_num_guess)
                                print("Attempts= ",attempts)
                                break
                            elif(a>ran_num_guess and a>=50):
                                print("Invalid Guess")
                                print("Please enter a number between 1 and 50")

                            elif(a>ran_num_guess and a > 50):
                                print("Too high")
                
                            elif(a<ran_num_guess):
                                print("Too low")

                            else:
                                print("Better luck next time")
        
                            attempts = attempts+1
                            # attempts == 11
                            print("Attempts= ",attempts)
                        break
                if(a!=ran_num_guess):
                    print("Your 10 attempts finished")
                break

            case 3:
                print("*********** Hard Mode! ***************")
                ran_num_guess = random.randint(1, 500)
                print(ran_num_guess)
                # print(ran_num_guess)
                # print(ran_num_guess)
                # print(ran_num_guess)
                while True:
                            attempts = 0
                            for attempts in range(0,7):
                                a = int(input("Guess the num between "))
                                print(ran_num_guess)
                    
                                if(a==ran_num_guess):
                                    print("Congratulations! You guessed the number")
                                    print("The number is: ",ran_num_guess)
                                    print("Attempts= ",attempts)
                                    break
                                elif(a>ran_num_guess and a > 500):
                                    print("Invalid Guess")
                                    print("Please enter a number between 1 and 500")

                                elif a > ran_num_guess:
                                    print("Too high!")
                                    
                                elif(a<ran_num_guess):
                                    print("Too low")

                                else:
                                    print("Better luck next time")
                                attempts = attempts+1
                                print("Attempts= ",attempts)
                                print("Remaining attempts:", 7 - attempts)
                            break
                if(a!=ran_num_guess):
                     print("You used all your atempts")
                print("Game Over!")
                print("The correct num was", ran_num_guess)
                break

    print("Do you want to play again. (yes/no)")
    text = input("Suggest me: ")
    if text=="yes":
        print("Select Difficulty: \n1.Easy \n2.Medium \n3.Hard")
        difficulty = int(input("Enter the Difficulty"))
    elif text != "yes":
        print("Thank You", "\U0001F600")
        break

    # match "text":
    #         case "yes":
    #             print("Select Difficulty: \n1.Easy \n2.Medium \n3.Hard")
    #         case "no":
    #             break
    # break