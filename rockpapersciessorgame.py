import random
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
print("welcome to the rock paper seizure game. Type 0 for rock, 1 for paper and 2 for scissors \n ")
choice = int(input())
comp_choice = random.randint(0,2)
print(comp_choice)
if choice == 0:
  print(rock)
  if comp_choice == 0:
    print(rock)
    print("draw")
  elif comp_choice == 1 :
    print(scissors)
    print("loose")
  else:
    print(paper)
    print("won")
elif choice == 1:
  print(scissors)
  if comp_choice == 0:
    print(rock)
    print("win")
  elif comp_choice == 1 :
    print(paper)
    print("draw")
  else:
    print(scissors)
    print("loose")
else:
  print(paper)
  if comp_choice == 0:
    print(rock)
    print("loose")
  elif comp_choice == 1 :
    print(scissors)
    print("won")
  else:
    print(paper)
    print("draw")









