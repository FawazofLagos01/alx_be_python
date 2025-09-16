import random

def play_game():
    secret_number = random.randint(1,10)
    print("I'm thinking of a number between 1 and 10. Ca you guess it?")
    guess_count = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guess_count += 1
            ...
        except ValueError:
            print("Please eneter a valid number!")

            match guess - secret_number:
                case 0:
                    print("Congratulatios,you guessed it in", guess_count , "tries!")
                    break
                case n if n > 0:
                        print("Oops, your guess is a bit high. Try again!")
                case n if n < 0:
                        print("Nope, your guess is a bit low. Give it another shot!")
                case _:
                    print("Please enter a valid number!.")
    
    while True:
        play_game()
        play_again = input("Play again? (yes/no): ")
        match play_again:
            case "yes":
                  continue
            case "no":
                print("see you next time!")
                break
            case _:
                print("Invalid choice. Goodbye!")
                break

