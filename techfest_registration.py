print ("Welcome to SMIT TechFest!")
print ("Event organized by Sean Athan Scott L. Ibay of APPDAET BTCS2\n")

try:
    num_participants = int(input("How many participants will register? "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()