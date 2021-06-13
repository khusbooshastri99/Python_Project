"A Treasure game."

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You are at a cross road. Where do you want to go? Type "left" or "right"')

if(choice1 == "left"):
  choice2 = input('You have came into a lake. There is an island in the middle of the lake. Type "Wait" to wait for the boat. Type "swim" to swim across.')
  
  if(choice2 == "wait" ):
    choice3 = input('Which colour doo you want to choose? Type "Red", "Blue", "Yellow"')
    
    if(choice3 == "Yellow"):
      print("You win!")
      
    else:
      print("You enter a room of beasts.Game over")
      
  else:
      print("You got attacked by an angry trout.Game over")
      
else:
  print("You fell into a hole. Game over.")

