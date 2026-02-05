import random
a=random.randrange(1,1001)
guess=0
while True:
    try:
        b=int(input("Enter any number between 1 to 1000:"))
        if(a==b):
           print("Congratulations! You guessed it right.")
           guess += 1
           break
        elif(a>b):
            print("Please guess  a bigger number.")
            guess += 1
        else:
            print("Please guess a smaller number.")
            guess += 1
    except ValueError:
        print("Please enter the correct input number.")
print(f"The number of turns you took to guess the number is {guess}. Thanks for playing...")



