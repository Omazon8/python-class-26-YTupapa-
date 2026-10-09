# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
#CS31 Olvin M. 10/7/2026

print ("My Awesome Quiz Video Game History Knowledge") 
print ()
print("* " *20)

print() 
username = input("What is your name?")
print(f"Hello, {username}!")

print()
start_quiz = input("Do You want to take my awesome quiz? Y/N ")
if start_quiz.upper () == "Y":
    print("Great! Let's get started!")

elif start_quiz == "N":
    print("Sorry, maybe next time!")

else: 
    print("Sorry. That is an invalid response. Try again")

counter = 0 
q1 = int(input("What Year did World Of Warcraft Come Out?"))
if q1 == 2004:
    counter += 1
    print("Yes! you are correct gang.")
else: 
    print("Sorry. you aint get this one right gang.")


print("what is the name of the first video game ever created?")
print(" A - output (tetris)")
print(" B - output (galica)")
print(" C - output (pong)")
print(" D - output (super mario bros.)")
q2 = input ("Your Answer - Choose A/B/C/D: ")
if q2.upper() =="C":
    counter += 1
    print ("Yes! You are correct gang. Python would use the print() function to output something to the terminal.")
else:
    print("Sorry. That is not correct.")

print("First 3D video game that was made?")
print(" A - output (Maze War)")
print(" B - output (Super Mario 64)")
print(" C - output (Star Fox 64)")
print(" D - output (DOOM)")
q3 = input ("Your Answer - Choose A/B/C/D: ")
if q3.upper() =="A":
    counter += 1
    print ("Yes! You are correct gang. Python would use the print() function to output something to the terminal.")
else:
    print("Sorry. That is not correct.")

q4 = int(input("What Year was the Super Nintendo Released in America?"))
if q4 == 1991:
    counter += 1
    print("Yes! you are correct gang.")
else: 
    print("Sorry. you aint get this one right gang.")

print("The Year Grand Theft Auto V Released?")
print(" A - output (2010)")
print(" B - output (2011)")
print(" C - output (2012)")
print(" D - output (2013)")
q5 = input ("Your Answer - Choose A/B/C/D: ")
if q5.upper() =="D":
    counter += 1
    print ("Yes! You are correct gang Great Job Gamer!")
else:
    print("Sorry. That is not correct.")

if counter == 5:
    print("You are a Pro! You got them all correct!")
elif counter >= 3 and counter < 5:
    print("Great work gang!")
elif counter >= 1 and counter < 3: 
    print("Maybe this subject isn't for you gang!")


    print ("* * * * YOUR FINAl SCORE *  * * *")
    print(f"your final score is: {counter}")
