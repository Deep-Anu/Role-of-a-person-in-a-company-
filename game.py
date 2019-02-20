import random
import time 
n = random.randint(1, 5) 
guess = int(input("Guess a number from 1 - 5 : "))
while n != "guess":
    print
    if guess < n:
        print('sorry you are disqualified to begin the Game, try once again')
        guess = int(input("Guess a number from 1 - 5: "))
    elif guess > n:
        print('sorry you are disqualified to begin the Game, try once again')
        guess = int(input("guess a number from 1 -5 :"))
    else:
        print("you guessed it!")
        break
    print

name =input("Enter your name ")
print("Hello, " + name, "Time to play guess the word!")
print("")
time.sleep(0.5)
print("Start guessing...")
time.sleep(0.5)
word = "love" 
guesses = '' 
turns = 8 
while turns > 0:
    failed = 0               
    for i in word:      
        if i in guesses:    
            print(i),      
        else:
            print("_"),      
            failed += 1    

    
    if failed == 0:        
        print("You won")  

    
        break              

    print

    
    guess = input("guess a letter:") 

    
    guesses += guess                    

    
    if guess not in word:  
 
     # turns counter decreases with 1 (now 9)
        turns -= 1        
 
    # print wrong
        print("Wrong guess")    
 
    # how many turns are left
        print("You have", + turns, 'more guesses') 
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print "You Loose"
            print("You Loose")  

