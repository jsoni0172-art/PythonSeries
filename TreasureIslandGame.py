print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to the treasure island")
print("your mission is to find treasure")
choice1 = (input('you are at the crossroad where do you want to go? Type "Left" or "Right".\n')).lower()
if choice1 ==  'right' :
  print("You have fell into the Hole.Game Over")
else: 
  choice2 = (input('you have come to take. There is an island in the middle of the lake.Type "wait" to wait for the boat or Type "swim" for the swim \n')).lower()
  if choice2 == 'wait':
    choice3 = input('You \'ve arrived at the island unharmed. There is a house with 3 doors. One Red, One Blue, one Yellow. Type which you choose "red","blue","Yellow" \n').lower()
    if choice3 == 'yellow' :
      print("You found the treasure.You win\n")
      print('''
      
         ___________
        '._==_==_=_.'
        .-\:      /-.
       | (|:.     |) |
        '-|:.     |-'
          \::.    /
           '::. .'
             ) (
           _.' '._
      ----`"""""""`----
      ''')
    else:
      print("you fell down in the burning fire.Game Over")
    
  else:
    print("You got an attacked by angry trout. Game Over")  
