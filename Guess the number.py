a=12
number_of_attempts=1
print("Number of guesses are limited to nine times only: ")
while(number_of_attempts<=9):
    b=int(input("Guess the number: \n"))
    if b < a:
        print("Your guess is lesser than the right number.\n")
    elif b > a:
        print("Your guess is greater than the right number.\n")
    else:
        print("Congrats!! you have guessed the right number.\n",'You have won.')
        print("Number of attempts you took to guess the right number:",number_of_attempts)
        break
    print(9-number_of_attempts,"more chances are left\n")
    number_of_attempts=number_of_attempts+1
if(number_of_attempts>9):
       print("Game Over")





