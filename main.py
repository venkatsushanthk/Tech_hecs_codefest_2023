# Codefest 2023.

# from playsound import playsound
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


# Choice of powers.
while True:
  
  # This is the offer for your powers.
  offer = input("Do you accept the offer? Type yes or no.\n").lower()
  
  if offer == "yes":
    
    print("Guardian - I will take your memories when you have chosen your Element.\n\n")
    #time.sleep(7)
    # This is the powers you choose.
    print("There are 5 element which one do you choose?")
    element = int(input("1. Fire: Attack, 2. Water: Medium Attack, 3. Earth: Passive, 4. Space: Medium Defence, 5. Air: Defence. Type the number according to the power assigned.\n\n"))
    
    # Element: Fire Element
    if element == 1:
      
      # Attacks
      print(" You have chosen the Fire Element , Your memories will now be erased. Your powers are: 1. Flaming song, 2. Turn up the heat, 3. Burn, 4. Inferno\n")
      print("Guardian - I cannot tell you if You made a good choice but i wish you the best of luck on your journey..\n")
      # time.sleep(10)
      print("You enter hell with Your New Fire element.\n")
      # time.sleep(6)
      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        # time.sleep(7)
        boulder = input("Would you like to attempt to use your powers on the boulder?\n Type yes or no.\n").lower()

        # You use your powers for the boulder.
        if boulder == "yes":
          print("You have chosen to use your powers on the boulder.\n")


          # Hp of objects
          boulder_hp_f = 100
          player_hp_1_f = 100
          f_b = boulder_hp_f
          f_p = player_hp_1_f
          while True:
            # Player's move
            f_m = input("You have 4 powers to use on the boulder.\n Your powers are: 1. Flaming song, 2. Turn up the heat, 3. Burn, 4. Inferno.Please type the number assigned for the power.\n\n")

            if f_p == 0:
              print("You have died ..  game over")
              InterruptedError
              break

            if f_b == 0:
              break
            
            # Power 1
            if f_m == "1":
              f_b = f_b - random.randint(1, 30)
              if f_b <= 0:
                f_b = 0
              print("Boulder hp = " + str(f_b))
              print("Player hp = " + str(f_p))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the bolder compeletly destroying it. \n")
                break
                
            # Power 2
            elif f_m == "2":
              f_b = f_b - random.randint(30, 50)
              f_p = f_p - random.randint(1, 20)
              if f_b <= 0:
                f_b = 0
              print("Bolder hp = " + str(f_b))
              print("Player hp = " + str(f_p))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the bolder compeletly destroying it. \n")
                break

            # Power 3    
            elif f_m == "3":
              f_b = f_b - random.randint(50, 70)
              f_p = f_p - random.randint(20, 40)
              if f_b <= 0:
                f_b = 0
              print("Bolder hp = " + str(f_b))
              print("Player hp = " + str(f_p))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the bolder compeletly destroying it. \n")
                break

            # Power 4    
            elif f_m == "4":
              f_b = f_b - random.randint(70, 101)
              f_p = f_p - random.randint(40, 71)
              if f_b <= 0:
                f_b = 0
              print("Bolder hp = " + str(f_b))
              print("Player hp = " + str(f_p))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the bolder compeletly destroying it. Not even 1 of its ashed had the gift of your mercy \n")
                break
            break
        break
            
            
        
      print("As you walk down the barren and dimly lit tunnel you begin to feel nervous, like there is something watching you. You feel a rumble below your feet as you come across a large door.\n")
      # time.sleep(7)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own. \n")
      # time.sleep(6)
      print("In the centre of the room lies a creature. It looks like how you would imagine an earth spirit in a fantasy game to look like. It has brown stone like skin and all its hair was green and filled with flowers. \n")
      # time.sleep(10)
      print("Its eyes however were bright red and its arms and face were riddled with scars as though it had been whipped everyday. \n")
      # time.sleep(6)
      print("After seeing you after you had entered the room it goes into what you can only guess is a crazed frenzy and begins to charge at you. \n")
     
      
      
      # Element: Water element
    elif element == 2:
      
      # Attacks
      print("You have chosen the Water Element , Your memory will now be erased. Your powers are: 1. Tsunami, 2. Water blocker, 3. Washed up, 4. Flash flood.")
      # time.sleep(10)
      print("Guardian - I cannot tell you if You made a good choice but i wish you the best of luck on your journey..")
      # time.sleep(8)
      print("You enter hell with Your New Water element.")
      # time.sleep(6)
      print("You Walk For what feels like an eternity Then you see a huge bolder which blocks your path.")
      break
      
      
      # Element: Earth element
    elif element == 3:

      # Attacks
      print("You have chosen the Earth Element , Your memory will now be erased. Your powers are: 1. Retreat behind the hill, 2. Trash compactor, 3. Dig deep. 4. Earth quake")
      # time.sleep(10)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      # time.sleep(8)
      print("You enter hell with Your New Earth element.")
      # time.sleep(6)
      print("You Walk For what feels like an eternity Then you see a huge bolder which blocks your path.")
      break
      
      # Element: Space element
    elif element == 4:

      # Attacks
      print("You have chosen the Space Element , Your memory will now be erased. Your powers are:  1. Antigravity, 2. Black hole, 3. orbit, 4. fly away.")
      # time.sleep(10)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      # time.sleep(8)
      print("You enter hell with Your New Space element.")
      # time.sleep(6)
      print("You Walk For what feels like an eternity Then you see a huge bolder which blocks your path.")
      break
      
      # Element: Air element
    elif element == 5: 

      # Attacks
      print("You have chosen the Air Element , Your memory will now be erased. Your powers are: 1. Upper Class, 2. tornado, 3.Blow them away, 4. Dizzying speed.")
      # time.sleep(10)
      print("Guardian - I cannot tell you if You made a good choice but i wish you the best of luck on your journey..")
      # time.sleep(8)
      print("You enter hell with Your New Air element.")
      # time.sleep(6)
      print("You Walk For what feels like an eternity Then you see a huge bolder which blocks your path.")
      break
      
    else: 
      print("Please type in one of the numbers.")
      
  elif offer == "no":
    
    print("Guardian - Hmmm")
    # time.sleep(2)
    print("Guardian - It seems you dont want to live. Well, I will still let you through the gates of hell... And maybe I will see you again")
    # time.sleep(4)
    
    # You are vaporised from hell.
    print("You enter hell without any powers, due to you having no powers to fight the forces of hell. The power in hell evaporates you get erased from exsistence.\n\n")
    # time.sleep(10)
    print("This is ending 1.")
    print("!!!GAME OVER!!!")
    break
    
  else:
    # Type one of the answers
    print("Please keep one of the answers.")
  
  
