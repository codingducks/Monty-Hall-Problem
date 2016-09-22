import random

def switch_doors():
    imp = raw_input(">")
    if imp == 'yes':
        doors.remove(choice)
        doors.remove(montyschoice)
        new_choice = random.choice(doors)
        print "you won a ", new_choice
    elif imp == 'no':
        print 'you won a ', choice

doors = ["goat","sheep","car"]

choice = random.choice(doors)

if choice == "car":
    montys_sample = ['goat','sheep']
    montyschoice = random.choice(montys_sample)
    print'monty opens a door, theres a',montyschoice,'changedoors?'
    switch_doors()
  

elif choice == 'sheep':
    montyschoice = 'goat'
    print'monty opens a door, theres a goat changedoors?'
    switch_doors()


elif choice == 'goat':
    montyschoice = 'sheep'
    print'monty opens a door, theres a sheep changedoors?'
    switch_doors()




