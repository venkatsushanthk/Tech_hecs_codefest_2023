# Codefest 2023.

import time



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
# time.sleep(6) 
print("It seems you are in a test tube of sorts.\n")
# time.sleep(6)
print("You look around , all you see is People in black suits...\n")
# time.sleep(7) 
print("...They seem to be talking to eachother but you can only make out a few words.\n")
# time.sleep(7) 
print("You close your eyes... When you open them you are in an unknown place.\n")
# time.sleep(7)
print("You Are no longer in the test tube .. But you are now in front of a unknown being...\n")
# time.sleep(8)
print("You look around , It seems you are at the entrance of a dungeon.\n")
# time.sleep(7)


# The user is told about the gates of hell
print("Unknown being - Hello Human I am The Guardian of these gates.. I will let you pass without any trouble but... you will die in there , These are the gates to what you call hell... I suggest you tread with caution.\n")
# time.sleep(15)
print("Guardian - You may wonder why would you want to go through hell... but its your only choice if you want to be reincarnated into a new body.\n")
# time.sleep(15)
print("Guardian - I will present you a opportunity to survive in hell... because if you enter with only your mortal strength you will surely die...\n")
# time.sleep(15)
print("Guardian - If you decide to trade all your memories before you reached here, I will present you with the opportunity To choose one of the 5 elemental powers to accompany you on your journey through the realm of hell.\n")
# time.sleep(20)
print("Guardian - If you dont accept this offer you will most likely die in hell..\n\n\n")
# time.sleep(14)
#Choice of powers.
while True:
  # This is the offer for your powers.
  offer = input("Do you accept the offer? Type yes or no.\n").lower()
  if offer == "yes":
    print("Guardian - I will take your memories when you have chosen your power.\n\n")
    time.sleep(7)
    # This is the powers you choose.
    print("There are 5 powers which one do you choose?")
    power = int(input("1. Fire: Attack, 2. Water: Medium Attack, 3. Earth: Passive, 4. Space: Medium Defence, 5. Air: Defence. Type the number according to the number assigned"))
    if power == 1:
      print(" You have chosen the Fire Element , Your memories will now be erased.  Your powers are: 1. flaming speech, 2. turn up the heat, 3. burn, 4. inferno")
      break
    elif power == 2:
      print("You have chosen the Water Element , Your memory will now be erased... Your powers are: 1.tsunami, 2. water blocker, 3. washed up, 4. flash flood.")
      break
    elif power == 3:
      print("You have chosen the Earth element , Your memory will now be erased. Your powers are: 1. earth block, 2. earth quake, 3")
      break
    elif power == 4:
      print("You have chosen the Space element , Your memory will now be erased.")
      break
    elif power == 5: 
      print("You have chosen the Air element , Your memory will now be erased.")
      break
    else: 
   print("")
    
    
  elif offer == "no":
    print("Guardian - Hmmm")
    time.sleep(2)
    print("Guardian - It seems you dont want to live. Well, I will still let you through the gates of hell... And maybe I will see you again")
    time.sleep(4)
    # You are vaporised from hell.
    print("You enter hell without any powers, due to you having no powers to fight the forces of hell. The power in hell evaporates you get erased from exsistence.\n\n")
    time.sleep(10)
    print("!!!GAME OVER!!!")
    break
  else:
    print("Please keep one of the answers.")





    
