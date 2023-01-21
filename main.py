# Codefest 2023.

import time
import random


# The user is told about the game.
print("Hello welcome to the game.\n"
      "This is a text-adventure game.\n"
      "It has different ending and stories so please play.\n\n")



# The user is asked if he wants to play.
while True:
    if input("Are you ready? ").lower() == "yes":
        break
   
    else:
        print("Take your time it's fine.\n")


      
# Game begins here
      
# The story is told.
print("\n\n")
print("You wake up in a dark isolated room...\n")
time.sleep(6) 
print("It seems you are inn a test tube of sorts.\n")
time.sleep(6)
print("You look around , all you see is People in black suits...\n")
time.sleep(7) 
print("...They seem to be talking to eachother but you can only make out a few words.\n")
time.sleep(7) 
print("You close your eyes... When you open them you are in an unknown place.\n")
time.sleep(7)
print("You Are no longer in the test tube .. But you are now in front of a unknown being...\n")
time.sleep(8)
print("You look around , It seems you are at the entrance of a dungeon.\n")
time.sleep(7)


# The user is told about the gates of hell
print("Unknown being - Hello Human I am The Guardian of these gates.. I will let you pass without any trouble but... you will die in there , These are the gates to what you call hell... I suggest you tread with caution.\n")
time.sleep(15)
print("Guardian - You may wonder why would you want to go through hell... but its your only choice if you want to be reincarnated into a new body.\n")
time.sleep(15)
print("Guardian - I will present you a opportunity to survive in hell... because if you enter with only your mortal strength you will surely die...\n")
time.sleep(15)
print("Guardian - If you decide to trade all your memories before you reached here, I will present you with the opportunity To choose one of the 5 elemental powers to accompany you on your journey through the realm of hell.\n")
time.sleep(20)
print("Guardian - If you dont accept this offer you will most likely die in hell..\n\n\n")
time.sleep(14)


# Choice of powers.
while True:
  
  # This is the offer for your powers.
  offer = input("Do you accept the offer? Type yes or no.\n").lower()
  
  if offer == "yes":
    
    print("Guardian - I will take your memories when you have chosen your power.\n\n")
    time.sleep(6)
    
    # This is the powers you choose.
    print("There are 5 powers which one do you choose?")
    time.sleep(5)
    power = input("1. Fire: Attack, 2. Water: Medium Attack, 3. Earth: Passive, 4. Space: Medium Defence, 5. Air: Defence. Type the number according to the power assigned.\n\n")
    
    # Power: Fire Element
    if power == "1":
      
      # Attacks
      print(" You have chosen the Fire Element , Your memories will now be erased. Your powers are: 1. Flaming song, 2. Turn up the heat, 3. Burn, 4. Inferno.\n")
      time.sleep(10)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      time.sleep(8)
      print("You enter hell with Your New Fire power.\n")
      time.sleep(6)
      print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n\n")
      time.sleep(10)
      break
      
      # Power: Water element
    elif power == "2":
      
      # Attacks
      print("You have chosen the Water Element , Your memory will now be erased. Your powers are: 1. Tsunami, 2. Water blocker, 3. Washed up, 4. Flash flood.\n")
      time.sleep(10)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      time.sleep(8)
      print("You enter hell with Your New Water power.\n")
      time.sleep(6)
      print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n\n")
      time.sleep(10)
      break
      
      # Power: Earth element
    elif power == "3":

      # Attacks
      print("You have chosen the Earth element , Your memory will now be erased. Your powers are: 1. Retreat behind the hill, 2. Earth quake, 3. Dig deep. 4. Trash compacter.\n")
      time.sleep(10)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      time.sleep(8)
      print("You enter hell with Your New Earth powers.\n")
      time.sleep(6)
      print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n\n")
      time.sleep(10)
     
      break
      
      # Power: Space element
    elif power == "4":

      # Attacks
      print("You have chosen the Space element , Your memory will now be erased. Your powers are:  1. Antigravity, 2. Black hole, 3. orbit, 4. fly away.\n")
      time.sleep(10)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      time.sleep(8)
      print("You enter hell with Your New Space powers.\n")
      time.sleep(6)
      print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n\n")
      time.sleep(10)
      break

      
      # Power: Air element
    elif power == "5": 

      # Attacks
      print("You have chosen the Air element , Your memory will now be erased. Your powers are: 1. Upper Class, 2. tornado, 3.Blow them away, 4. Dizzying speed.")
      time.sleep(10)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      time.sleep(8)
      print("You enter hell with Your New Air powers.\n")
      time.sleep(6)
      print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n\n")
      time.sleep(10)
      break

      
    else: 
      print("Please type in one of the numbers.")
      
  elif offer == "no":
    
    print("Guardian - Hmmm")
    time.sleep(2)
    print("Guardian - It seems you dont want to live. Well, I will still let you through the gates of hell... And maybe I will see you again")
    time.sleep(4)
    
    # You are vaporised from hell.
    print("You enter hell without any powers, due to you having no powers to fight the forces of hell. The power in hell evaporates you get erased from exsistence.\n\n")
    time.sleep(10)
    print("This is ending 1.")
    print("!!!GAME OVER!!!")
    break
    
  else:
    # Type one of the answers
    print("Please keep one of the answers.")


