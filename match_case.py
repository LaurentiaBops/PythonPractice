# Game where user tries to guess secret number chosen by program

#import the random module allow random number generation
import random 

#Generate random number between 1 and 10
secret_number = random.randint(1, 10)

#Prompt user tp guess number
guess =int(input("Guess a random number between 1 and 10: "))

#Compare user's guess with the secret number

match guess:
    case n if n == secret_number:
        print("Congratulations you guessed it!")
        
    case n if n > secret_number:
        print("Oops, your guess is a bit high. Try again!")
    case _:
        print("Nope, your guess is a biy low. Give it another shot!")

#Create a loop until the correct answer is guessed

while guess != secret_number:
    play_again =  input("Play again? (yes/no)")
    if play_again =="yes":
        guess =int(input("Guess a random number between 1 and 10: "))
        match guess:
             case n if n == secret_number:
                 print("Congratulations you guessed it!")
             case n if n > secret_number:
                 print("Oops, your guess is a bit high. Try again!")
             case _:
                 print("Nope, your guess is a biy low. Give it another shot!")
      
    else:
        break
    

      
    
  



