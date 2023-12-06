import random
print("welcome to the rock paper seizure game. Type 0 for rock, 1 for paper and 2 for scissors \n ")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input())
comp_choice = random.randint(0,2)
art = [rock, paper, scissors]
print(comp_choice)
if choice < 0 or choice > 2 :
  print ("please enter a valid choice")
else:
  if choice == 0 and comp_choice == 2 :
      print(f"you choose \n {art[choice]}")
      print(f"computer choose \n {art[comp_choice]}")
      print("you win")
  elif choice > comp_choice : 
      print(f"you choose \n {art[choice]}")
      print(f"computer choose \n {art[comp_choice]}")
      print("you win")
  else:
      print(f"you choose \n {art[choice]}")
      print(f"computer choose \n {art[comp_choice]}")
      print("you lost")
