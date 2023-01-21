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
      
      while True:
        # time.sleep(6)
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        # time.sleep(7)
        boulder_f = input("Would you like to attempt to use your powers on the boulder?\n Type yes or no.\n").lower()

        # You use your powers for the boulder.
        if boulder_f == "yes":
          print("You have chosen to use your powers on the boulder.\n")


          # Hp of objects
          boulder_hp_f = 100
          f_b = boulder_hp_f
          while True:
            # Player's move
            f_m = input("You have 4 powers to use on the boulder.\n Your powers are: 1. Flaming song, 2. Turn up the heat, 3. Burn, 4. Inferno.Please type the number assigned for the power.\n\n")
            
            # Power 1
            if f_m == "1":
              f_b = f_b - random.randint(1, 30)
              if f_b <= 0:
                f_b = 0
              print("Boulder hp = " + str(f_b))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                # time.speed(6)
                break
                
            # Power 2
            elif f_m == "2":
              f_b = f_b - random.randint(30, 50)
              if f_b <= 0:
                f_b = 0
              print("Boulder hp = " + str(f_b))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 3    
            elif f_m == "3":
              f_b = f_b - random.randint(50, 70)
              if f_b <= 0:
                f_b = 0
              print("Boulder hp = " + str(f_b))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 4    
            elif f_m == "4":
              f_b = f_b - random.randint(70, 101)
              if f_b <= 0:
                f_b = 0
              print("Boulder hp = " + str(f_b))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. Not even 1 of its ashes had the gift of your mercy \n")
                break
          break
        break        

        
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities. \n")
      # time.sleep(12)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      # time.sleep(12)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      # time.sleep(10)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      # time.sleep(11)
      print("In the centre of the room there are two creatures lined with armor and holding spears. They had a look resembled that of an fairy, but corrupted with stonelike skin and gleaming red eyes. Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast")
      # time.sleep(15)
      print("After the fairy seeing you enter the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n")
      # time.sleep(11)

      # Hp of players
      earth_fairy_hp = 500
      player_hp_f = 400
      efh = earth_fairy_hp
      phf = player_hp_f
      while True:
        
        f = input("You have 4 powers to use on the fairy\n Your powers are: 1. Flaming song, 2. Turn up the heat, 3. Burn, 4. Inferno.Please type the number assigned for the power.\n\n")
      
        if f == "1":
          efh = efh - random.randint(30, 101)
          phf = phf - random.randint(30, 101)
          print("The fairy lunges at you and uses an blade of leafs coated in fire and stabs you.")
          print("fairy hp = " + str(efh))
          print("Your hp  = "+ str(phf)) 
          if efh <= 0:
            print("You finally defeated the Fairy... \n")
          if phf <=  0: 
            print("You have died ..  game over")
          break
        if f == "2":
          Earth_fairy_hp = Earth_fairy_hp - random.randint(10, 90)
          Player_hp_f = Player_hp_f - random.randint(10 , 90)             
          print("The fairy shoots water bullets infused with some mud in it at you")
          
          print("Fairy hp = " + str(Earth_fairy_hp))
          print("Your hp  = "+ str(Player_hp_f))  
          Earth_fairy_hp < 0
          Earth_fairy_hp > 0
          if Earth_fairy_hp <= 0:
            print("You finally defeated the Fairy... \n")
          if Player_hp_f  <=  0: 
            print("You have died ..  game over")
            break
        if f == "3":
            Earth_fairy_hp = Earth_fairy_hp - random.randint(20, 100)
            Player_hp_f = Player_hp_f - random.randint(20 , 100)
            print("The fairy pushes you far and launches a array of tournado's at you.")
            print("fairy hp = " + str(Earth_fairy_hp))
            print("Your hp  = "+ str(Player_hp_f)) 
            Earth_fairy_hp < 0  
            Earth_fairy_hp < 0
            Earth_fairy_hp > 0
            if Earth_fairy_hp <= 0:
             print("You finally defeated the Fairy... \n")
            if Player_hp_f  <=  0: 
              print("You have died ..  game over")
              
              
              break
        if f == "4":
          efh = efh - random.randint(1, 160)
          phf = phf - random.randint(1, 160)
          phf = phf - 50
          print("The fairy creates fire coated mud bullets and shoots them at you then she creates water tornado's .")
          if efp <= 0:
            efh = 0
          print("fairy hp = " + str(efh))
          print("Your hp  = "+ str(phf)))
          if efh <= 0:
            print("You finally defeated the Fairy... \n")
            break
          if phf  <=  0: 
            print("You have died ..  game over")
            break
          
      
      print("You have finnaly killed the creature and you breath a sigh of relief. prehaps you should just lie down and rest... \n")
      # time.sleep(4)
      print("This scene feels awfully familiar... no thats impossible ")
      
           # time.sleep(10)
      
      
      # Element: Water element
    elif element == 2:
      
      # Attacks
      print("You have chosen the Water Element , Your memory will now be erased. Your powers are: 1. Tsunami, 2. Water blocker, 3. Washed up, 4. Flash flood.")
      print(" ")
      # time.sleep(10)
      print("Guardian - I cannot tell you if You made a good choice but i wish you the best of luck on your journey..")
      # time.sleep(8)
      print("You enter hell with Your New Water element.")
      # time.sleep(6)
      
      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        # time.sleep(7)
        boulder_w = input("Would you like to attempt to use your powers on the boulder?\n Type yes or no.\n").lower()

        # You use your powers for the boulder.
        if boulder_w == "yes":
          print("You have chosen to use your powers on the boulder.\n")

          # Hp of objects
          boulder_hp_w = 100
          w_b = boulder_hp_w
          while True:
            # Player's move
            w_m = input("You have 4 powers to use on the boulder.\n Your powers are: 1. Tsunami, 2. Water blocker 3. washed up , 4. Flash flood .Please type the number assigned for the power.\n\n")
            
            # Power 1
            if w_m == "1":
              w_b = w_b - random.randint(1, 30)
              if w_b <= 0:
                w_b = 0
              print("Boulder hp = " + str(w_b))
              if Bolder_hp == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 2    
            if w_m == "2":
              w_b = w_b - random.randint(30, 50)
              if w_b <= 0:
                w_b = 0
              print("Boulder hp = " + str(w_b))
              if w_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 3    
            if w_m == "3":
              w_b = w_b - random.randint(50, 70)
              if w_b <= 0:
                w_b = 0
              print("Boulder hp = " + str(w_b))
              if w_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boluder compeletly destroying it. \n")
                break

            # Power 4    
            if w_m == "4":
              w_b = w_b - random.randint(70, 101)
              if w_b <= 0:
                w_b = 0
              print("Boulder hp = " + str(w_b))
              if w_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break
          break     
        break

      
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities and occasionaly collapsing from the lack of food. \n")
      # time.sleep(12)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      # time.sleep(6)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      # time.sleep(5)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      # time.sleep(5)
      print("In the centre of the room there are two creatures lined with armor and holding spears.\n They resembled that of an  fairy, but corrupted with stonelike skin and gleaming red eyes.\n Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast.\n")
      # time.sleep(12)
      print("After seeing you after you had entered the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n\n")
      Earth_fairy_hp_w = 500
      Player_hp_w = 400

      while True:

        
        w = input("You have 4 powers to use on the fairy\n Your powers are: 1. Tsunami, 2. Water blocker, 3. Washed up, 4. Flash flood.\n\n")
      
        if  w  == "1":
          Earth_fairy_hp = Earth_fairy_hp - random.randint(30, 100)
          Player_hp_w = Player_hp_w - random.randint(30,100)
          print("The fairy lunges at you and uses an blade of leafs coated in fire and stabs you.")
          print("fairy hp = " + str(Earth_fairy_hp))
          print("Your hp  = "+ str(Player_hp_w)) 
          Earth_fairy_hp< 0
          Earth_fairy_hp > 0
          if Earth_fairy_hp <= 0:
            print("You finally defeated the Fairy... \n")
          if Player_hp_w  <=  0: 
            print("You have died ..  game over")
          break
        if w == "2":
          Earth_fairy_hp = Earth_fairy_hp - random.randint(10, 90)
          Player_hp_w = Player_hp_w - random.randint(10 , 90)             
          print("The fairy shoots water bullets infused with some mud in it at you")
          
          print("Fairy hp = " + str(Earth_fairy_hp))
          print("Your hp  = "+ str(Player_hp_w))  
          Earth_fairy_hp < 0
          Earth_fairy_hp > 0
          if Earth_fairy_hp <= 0:
            print("You finally defeated the Fairy... \n")
          if Player_hp_w  <=  0: 
            print("You have died ..  game over")
            break
        if w == "3":
            Earth_fairy_hp = Earth_fairy_hp - random.randint(20, 100)
            Player_hp_w = Player_hp_w - random.randint(20 , 100)
            print("The fairy pushes you far and launches a array of tournado's at you.")
            print("fairy hp = " + str(Earth_fairy_hp))
            print("Your hp  = "+ str(Player_hp_w)) 
            Earth_fairy_hp < 0  
            Earth_fairy_hp < 0
            Earth_fairy_hp > 0
            if Earth_fairy_hp <= 0:
             print("You finally defeated the Fairy... \n")
            if Player_hp_w  <=  0: 
              print("You have died ..  game over")
              
              
              break
        if w == "4":
            Earth_fairy_hp = Earth_fairy_hp - random.randint(1, 160)
            Player_hp_w = Player_hp_w - random.randint(1 , 160)
            print("The fairy creates fire coated mud bullets and shoots them at you then she creates water tornado's .")
            print("fairy hp = " + str(Earth_fairy_hp))
            print("Your hp  = "+ str(Player_hp_w)) 
            Player_hp_w = Player_hp_w - 50
            Earth_fairy_hp< 0   
            Earth_fairy_hp< 0
            Earth_fairy_hp > 0
            if Earth_fairy_hp <= 0:
              print("You finally defeated the Fairy... \n")
              break
            if Player_hp_w  <=  0: 
              print("You have died ..  game over")
              break
      
        if Player_hp_w ==  0: 
          print("You have died ..  game over")
          break
      
      # Element: Earth element
    elif element == 3:

      # Attacks
      print("You have chosen the Earth Element , Your memory will now be erased. Your powers are: 1. Retreat behind the hill, 2. Trash compactor, 3. Dig deep. 4. Earth quake.")
      # time.sleep(10)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      # time.sleep(8)
      print("You enter hell with Your New Earth element.")
      # time.sleep(6)

      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        # time.sleep(7)
        boulder_e = input("Would you like to attempt to use your powers on the boulder?\n Type yes or no.\n").lower()

        # You use your powers for the boulder.
        if boulder_e == "yes":
          print("You have chosen to use your powers on the boulder.\n")

          # Hp of objects
          boulder_hp_e = 100
          e_b = boulder_hp_e
          while True:
            # Player's move
            e_m = input("You have 4 powers to use on the boulder.\n Your powers are: 1. Retreat behind the hill, 2. Trash compactor, 3. Dig deep. 4. Earth quake.\n\n")
            
            # Power 1
            if e_m == "1":
              e_b = e_b - random.randint(1, 30)
              if e_b <= 0:
                e_b = 0
              print("Boulder hp = " + str(e_b))
              if e_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 2    
            if e_m == "2":
              e_b = e_b - random.randint(30, 50)
              if e_b <= 0:
                e_b = 0
              print("u hp = " + str(e_b))
              if e_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 3    
            if e_m == "3":
              e_b = e_b - random.randint(50, 70)
              if e_b <= 0:
                e_b = 0
              print("Boulder hp = " + str(e_b))
              if e_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 4    
            if e_m == "4":
              e_b = e_b - random.randint(70, 101)
              if e_b <= 0:
                e_b = 0
              print("Boulder hp = " + str(e_b))
              if e_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break
          break     
        break

        
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities and occasionaly collapsing from the lack of food. \n")
      # time.sleep(12)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      # time.sleep(6)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      # time.sleep(5)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      # time.sleep(5)
      print("In the centre of the room there are two creatures lined with armor and holding spears.\n They resembled that of a fairy, but corrupted with stonelike skin and gleaming red eyes.\n Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast.\n")
      # time.sleep(12)
      print("After seeing you after you had entered the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n\n")
      Earth_fairy_hp = 500
      Player_hp_f = 400
      while True:
        
        e = input("You have 4 powers to use on the fairy\n Your powers are: 1. orbit,2. anti gravity 3. Fly away  , 4. Blackhole .Please type the number assigned for the power.\n\n")
      
        if  e <= "1":
          Earth_fairy_hp = Earth_fairy_hp - random.randint(30, 100)
          Player_hp_e = Player_hp_e - random.randint(30,100)
          print("The fairy lunges at you and uses an blade of leafs coated in fire and stabs you.")
          print("fairy hp = " + str(Earth_fairy_hp))
          print("Your hp  = "+ str(Player_hp_e)) 
          Earth_fairy_hp< 0
          Earth_fairy_hp > 0
          if Earth_fairy_hp <= 0:
            print("You finally defeated the Fairy... \n")
          if Player_hp_e  <=  0: 
            print("You have died ..  game over")
          break
        if e == "2":
          Earth_fairy_hp = Earth_fairy_hp - random.randint(10, 90)
          Player_hp_e = Player_hp_e - random.randint(10 , 90)
          print("The fairy shoots water bullets infused with some mud in it at you")
          
          print("Fairy hp = " + str(Earth_fairy_hp))
          print("Your hp  = "+ str(Player_hp_e))  
          Earth_fairy_hp < 0
          Earth_fairy_hp > 0
          if Earth_fairy_hp <= 0:
            print("You finally defeated the Fairy... \n")
          if Player_hp_e  <=  0: 
            print("You have died ..  game over")
            break
        if e == "3":
            Earth_fairy_hp = Earth_fairy_hp - random.randint(20, 100)
            Player_hp_e = Player_hp_e - random.randint(20 , 100)
            print("The fairy pushes you far and launches a array of tournado's at you.")
            print("fairy hp = " + str(Earth_fairy_hp))
            print("Your hp  = "+ str(Player_hp_e)) 
            Earth_fairy_hp < 0  
            Earth_fairy_hp < 0
            Earth_fairy_hp > 0
            if Earth_fairy_hp <= 0:
             print("You finally defeated the Fairy... \n")
            if Player_hp_e  <=  0: 
              print("You have died ..  game over")
              
              
              break
        if e == "4":
            Earth_fairy_hp = Earth_fairy_hp - random.randint(1, 160)
            Player_hp_e = Player_hp_e - random.randint(1 , 160)
            print("The fairy creates fire coated mud bullets and shoots them at you then she creates water tornado's .")
            print("fairy hp = " + str(Earth_fairy_hp))
            print("Your hp  = "+ str(Player_hp_e)) 
            Player_hp_e = Player_hp_e - 50
            Earth_fairy_hp< 0   
            Earth_fairy_hp< 0
            Earth_fairy_hp > 0
            if Earth_fairy_hp <= 0:
              print("You finally defeated the Fairy... \n")
              break
            if Player_hp_e  <=  0: 
              print("You have died ..  game over")
              break
      
        if Player_hp_e ==  0: 
          print("You have died ..  game over")
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
      
      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        # time.sleep(7)
        boulder_s = input("Would you like to attempt to use your powers on the boulder?\n Type yes or no.\n").lower()

        # You use your powers for the boulder.
        if boulder_s == "yes":
          print("You have chosen to use your powers on the boulder.\n")

          # Hp of objects
          boulder_hp_s = 100
          s_b = boulder_hp_e
          while True:
            # Player's move
            s_m = input("You have 4 powers to use on the boulder.\n Your powers are:  1. Antigravity, 2. Black hole, 3. orbit, 4. fly away.\n\n")
            
            # Power 1
            if s_m == "1":
              s_b = s_b - random.randint(1, 30)
              if s_b <= 0:
                s_b = 0
              print("Boulder hp = " + str(s_b))
              if s_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 2    
            if s_m == "2":
              s_b = s_b - random.randint(30, 50)
              if s_b <= 0:
                s_b = 0
              print("u hp = " + str(s_b))
              if s_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 3    
            if s_m == "3":
              s_b = s_b - random.randint(50, 70)
              if s_b <= 0:
                s_b = 0
              print("Boulder hp = " + str(s_b))
              if s_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 4    
            if s_m == "4":
              s_b = s_b - random.randint(70, 101)
              if s_b <= 0:
                s_b = 0
              print("Boulder hp = " + str(s_b))
              if s_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break
          break     
        break

        
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you.\n you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities and occasionaly collapsing from the lack of food. \n")
      # time.sleep(12)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead.\n")
      # time.sleep(6)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      # time.sleep(5)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      # time.sleep(5)
      print("In the centre of the room there are two creatures lined with armor and holding spears.\n They resembled that of an earth fairy, but corrupted with stonelike skin and gleaming red eyes.\n Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast.\n")
      # time.sleep(12)
      print("After seeing you after you had entered the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n\n")
      
import random


Earth_fairy_hp = 300
Player_hp_s = 300
while True:
  v = input("You have 4 powers to use on the fairy\n Your powers are: 1. orbit,2. anti gravity 3. Fly away  , 4. Blackhole .Please type the number assigned for the power.\n\n")

  if v <= "1":
    Earth_fairy_hp = Earth_fairy_hp - random.randint(30, 100)
    Player_hp_s = Player_hp_s - random.randint(30 , 100)
    print("The fairy lunges at you and uses an blade of leafs coated in fire and stabs you.")
    print("fairy hp = " + str(Earth_fairy_hp))
    print("Your hp  = "+ str(Player_hp_s)) 
    Earth_fairy_hp< 0
    Earth_fairy_hp > 0
    if Earth_fairy_hp <= 0:
      print("You finally defeated the Fairy... \n")
    if Player_hp_s  <=  0: 
      print("You have died ..  game over")
    break
  if v == "2":
    Earth_fairy_hp = Earth_fairy_hp - random.randint(10, 90)
    Player_hp_s = Player_hp_s - random.randint(10 , 90)             
    print("The fairy shoots water bullets infused with some mud in it at you")
    
    print("Fairy hp = " + str(Earth_fairy_hp))
    print("Your hp  = "+ str(Player_hp_s))  
    Earth_fairy_hp < 0
    Earth_fairy_hp > 0
    if Earth_fairy_hp <= 0:
      print("You finally defeated the Fairy... \n")
    if Player_hp_s  <=  0: 
      print("You have died ..  game over")
      break
  if v == "3":
      Earth_fairy_hp = Earth_fairy_hp - random.randint(20, 100)
      Player_hp_s = Player_hp_s - random.randint(20 , 100)
      print("The fairy pushes you far and launches a array of tournado's at you.")
      print("fairy hp = " + str(Earth_fairy_hp))
      print("Your hp  = "+ str(Player_hp_s)) 
      Earth_fairy_hp < 0  
      Earth_fairy_hp < 0
      Earth_fairy_hp > 0
      if Earth_fairy_hp <= 0:
       print("You finally defeated the Fairy... \n")
      if Player_hp_s  <=  0: 
        print("You have died ..  game over")
        
        
        break
  if v == "4":
      Earth_fairy_hp = Earth_fairy_hp - random.randint(1, 160)
      Player_hp_s = Player_hp_s - random.randint(1 , 160)
      print("The fairy creates fire coated mud bullets and shoots them at you then she creates water tornado's .")
      print("fairy hp = " + str(Earth_fairy_hp))
      print("Your hp  = "+ str(Player_hp_s)) 
      Player_hp_s = Player_hp_s - 50
      Earth_fairy_hp< 0   
      Earth_fairy_hp< 0
      Earth_fairy_hp > 0
      if Earth_fairy_hp <= 0:
        print("You finally defeated the Fairy... \n")
        break
      if Player_hp_s  <=  0: 
        print("You have died ..  game over")
        break

  if Player_hp_s  ==  0: 
    print("You have died ..  game over")
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
      
      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        # time.sleep(7)
        boulder_a = input("Would you like to attempt to use your powers on the boulder?\n Type yes or no.\n").lower()

        # You use your powers for the boulder.
        if boulder_a == "yes":
          print("You have chosen to use your powers on the boulder.\n")
          
          boulder_hp_a = 100
          a_b = boulder_hp_a
          while True:
            a_m = input("You have 4 powers to use on the boulder.\n Your powers are: 1. Upper Class, 2. tornado, 3.Blow them away, 4. Dizzying speed.\n\n")

            # Power 1
            if a_m == "1":
              a_b = a_b - random.randint(0, 0)
              print("You fly into the air,but you're in a cavern. try something else.")

            # Power 2
            if a_m == "2":
              a_b = a_b - random.randint(110, 120)
              if a_b <= 0:
                a_b = 0
              print("Boulder hp = " + str(a_b))
              if a_b <= 0:
                print("In a fit of rage you unleash a massive tornado on the boulder compeletly destroying it. \n")
                break

            # Power 3     
            if a_m == "3":
              a_b = a_b - random.randint(100, 130)
              if a_b <= 0:
                a_b = 0
              print("Boulder hp = " + str(a_b))
              if a_b <= 0:
                print("In a fit of rage you unleash a godly  amount of power and the boulder smashes into a wall, compeletly destroying it. \n")
                break
                
            # Power 4
            if a_m == "4":
              a_b = a_b - random.randint(70, 101)
              if a_b <= 0:
                a_b = 0
              print("Boulder hp = " + str(a_b))    
              if a_b <= 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break
          break
        break

        
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities and occasionaly collapsing from the lack of food. \n")
      # time.sleep(12)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      # time.sleep(6)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      # time.sleep(5)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      # time.sleep(5)
      print("In the centre of the room there are two creatures lined with armor and holding spears.\n They resembled that of an earth fairy, but corrupted with stonelike skin and gleaming red eyes.\n Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast.\n")
      # time.sleep(12)
      print("After seeing you after you had entered the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n\n")
  
      
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
  
  break






