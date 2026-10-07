# Starting file for LAB 2
# Include your course number, student first and last name, and date in the comment header
#CS31 Olvin M. 10/7/2026

print ("My Awesome Quiz on Python Concepts") 
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
q1 = int(input("what is 2 x 10"))
if q1 == 20:
    counter += 1
    print("Yes! you are correct gang. Python would solve this as 20.")
else: 
    print("Sorry. you aint get this one right gang.")

print("what is 30 divided by 3?")
print(" A - output (5)")
print(" B - output (11)")
print(" C - output (10)")
print(" D - output (7)")
q2 = input ("Your Answer - Choose A/B/C/D: ")
if q2.upper() =="C":
    counter += 1
    print ("Yes! You are correct gang. Python would use the print() function to output something to the terminal.")
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
