#Codefest 2023.


import os
import sys
import subprocess
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
time.sleep(2) 
print("It seems you are in a test tube of sorts.\n")
time.sleep(2)
print("You look around , all you see is People in black suits...\n")
time.sleep(2) 
print("...They seem to be talking to eachother but you can only make out a few words.\n")
time.sleep(3) 
print("You close your eyes... When you open them you are in an unknown place.\n")
time.sleep(3)
print("You Are no longer in the test tube .. But you are now in front of a unknown being...\n")
time.sleep(3)
print("You look around , It seems you are at the entrance of a dungeon.\n")
time.sleep(3)


# The user is told about the gates of hell
print("Unknown being - Hello Human I am The Guardian of these gates.. I will let you pass without any trouble but... you will die in there , These are the gates to what you call hell... I suggest you tread with caution.\n")
time.sleep(5)
print("Guardian - You may wonder why would you want to go through hell... but its your only choice if you want to be reincarnated into a new body.\n")
time.sleep(4)
print("Guardian - I will present you a opportunity to survive in hell... because if you enter with only your mortal strength you will surely die...\n")
time.sleep(4)
print("Guardian - If you decide to trade all your memories before you reached here, I will present you with the opportunity To choose one of the 5 elemental powers to accompany you on your journey through the realm of hell.\n")
time.sleep(5)
print("Guardian - If you dont accept this offer you will most likely die in hell..\n\n\n")
time.sleep(3)


# Choice of powers.
while True:
  
  # This is the offer for your powers.
  offer = input("Do you accept the offer? Type yes or no.\n").lower()
  
  if offer == "yes":
    
    print("Guardian - I will take your memories when you have chosen your Element.\n\n")
    time.sleep(3)
    # This is the powers you choose.
    print("There are 5 element which one do you choose?")
    element = int(input("1. Fire: Attack, 2. Water: Medium Attack, 3. Earth: Passive, 4. Space: Medium Defence, 5. Air: Defence. Type the number according to the power assigned.\n\n"))
    
    # Element: Fire Element
    if element == 1:
      
      # Attacks
      print(" You have chosen the Fire Element , Your memories will now be erased. Your powers are: 1. Flaming song, 2. Turn up the heat, 3. Burn, 4. Inferno.\n")
      time.sleep(4)
      print("Guardian - I cannot tell you if You made a good choice but i wish you the best of luck on your journey..\n")
      time.sleep(3)
      print("You enter hell with Your New Fire element.\n")
      
      while True:
        time.sleep(3)
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        time.sleep(4)
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
              f_b = f_b - random.randint(211111111111111110, 70)
              if f_b <= 0:
                f_b = 0
              print("Boulder hp = " + str(f_b))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 4    
            elif f_m == "4":
              f_b = f_b - random.randint(1, 101)
              if f_b <= 0:
                f_b = 0
              print("Boulder hp = " + str(f_b))
              if f_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. Not even 1 of its ashes had the gift of your mercy \n")
                break
          break
        break        

      # The story continues
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities. \n")
      time.sleep(6)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      time.sleep(5)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      time.sleep(4)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      time.sleep(4)
      print("In the centre of the room there are two creatures lined with armor and holding spears. They had a look resembled that of an fairy, but corrupted with stonelike skin and gleaming red eyes. Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast.\n")
      time.sleep(7)
      print("After the fairy seeing you enter the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n")
      time.sleep(4)

      # Hp of players
      earth_fairy_hp = 500
      player_hp_f = 500
      efh = earth_fairy_hp
      phf = player_hp_f
      while True:

        # Player's move
        f = input("You have 4 powers to use on the fairy\n Your powers are: 1. Flaming song, 2. Turn up the heat, 3. Burn, 4. Inferno. Please type the number assigned for the power.\n\n")

        # Power 1
        if f == "1":
          efh = efh - random.randint(10, 50)
          phf = phf - random.randint(10, 50)
          if efh <= 0:
            efh = 0
          if phf <= 0:
            phf = 0
          print("The fairy lunges at you and uses an blade of leafs coated in fire and stabs you.")
          print("fairy hp = " + str(efh))
          print("Your hp  = "+ str(phf)) 
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phf ==  0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # Power 2   
        if f == "2":
          efh = efh - random.randint(50, 100)
          phf = phf - random.randint(50, 100)  
          if efh <= 0:
            efh = 0
          if phf <= 0:
            phf = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phf))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phf == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # Power 3
        if f == "3":
          efh = efh - random.randint(100, 150)
          phf = phf - random.randint(100, 150)
          if efh <= 0:
            efh = 0
          if phf <= 0: 
            phf = 0
          print("The fairy pushes you far and launches a array of tournado's at you.")
          print("fairy hp = " + str(efh))
          print("Your hp  = "+ str(phf)) 
          if efh <= 0:
            print("You finally defeated the Fairy... \n")
            break
          if phf <= 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # Power 4     1
        if f == "4":
          efh = efh - random.randint(150, 200)
          phf = phf - random.randint(150, 200)
          phf = phf - 50
          if efh <= 0:
            efh = 0
          if phf <= 0:
            phf = 0
          print("The fairy creates fire coated mud bullets and shoots them at you then she creates water tornados.")
          print("fairy hp = " + str(efh))
          print("Your hp  = "+ str(phf))
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phf == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break
          
      # The story continues
            time.sleep(3)
      print("You have finnaly killed the creature and you breath a sigh of relief. prehaps you should just lie down and rest... and you slowly close your eyes. \n")
      time.sleep(4)
      print("This scene feels awfully familiar... no thats impossible the guardian erased all my memories and theres no way i have been here before... \n you hear a small sound at the tip of your ears. \n")
      time.sleep(4)
      print("You slowly open your eyes to see the similar fairy standing over your face peering down at you. 'You must not be a very good man.' In a fright you immideatly move away. \n")
      time.sleep(4)
      print("you finally pull yourself together and get up to notice that the cages had all fallen down. You never noticed it at first but the cages all had creatures inside them and they seem to have broken out of their cages. \n")
      time.sleep(5)
      print("The creature were unexpectedly gentle compared to what you would expect lf creatures from hell. \n")
      time.sleep(3)
      print("The creatures have the ability to communicate and talked to you. The littlest one said that they were not monsters but spirits.\n These are creatures you can trust. \n")
      time.sleep(4)
      print("You continue down the dark tunnel, but it no longer seems so dull as you are just happy to have people by your side that was until... \n")
      time.sleep(4)
      print("You hear a giant rumble as the ground breaks beneath you. A enormous hole is created and you begin to fall enwrapped by darkness not sure when it ends. \n")
      time.sleep(4)
      print("You finally land on ground and your body hurts all over. you look all around you and it seems that the spirits had followed you down. In front of you there is a large gate which feels uncannily familiar. \n")
      time.sleep(5)
      print("By now you remember most of your life, your family, friends, school but nothing after you turned 18. \n")
      time.sleep(3)
      print("Infront of you is a large portal.\n Consumed by curiosity you go through the gate, the spirits following closely behind. \n")
      time.sleep(4)
      print(" You're now in a large elegantly decorated room woth a figure in the middle that seems awfully familiar...\n")
      time.sleep(3)
      print("He turns around and its the guardian! Why? Why is he here? \n")
      time.sleep(2)
      print("Guardian - Human. You have fallen for my charades yet again! Oh how could you be so stupid? I am no guardian, you are not good and this is not hell! \n")
      time.sleep(4)
      print("Guardian - I am actually the Essence of Ohio. You have to battle me to get out of this world.\n")
      time.sleep(3)

      
      print("You meet face to face with the essence of Ohio.. \n")
      time.sleep(3)
      print("Essence of Ohio - Hello again .. i understand that you have conquered hell with my power... and you should understand that you only have an fraction of my power.\n")
      time.sleep(5)
      print("so I will present you with the option for 1 move... it will help you rival my might. this helps you heal damage taken on a random base... it goes from your 1 hp to 100 hp... LET'S START THE BATTLE.\n")
      time.sleep(5)
      player_hp_ohio_f = 600
      essence_of_ohio = 1000
      phof = player_hp_ohio_f
      eoo = essence_of_ohio
      while True:
        ohio = input("Which move do you choose? 1. Flaming song 2. Turn up the heat 3.Burn 4. Inferno 5. Hells embrace.\n\n")
        
        if ohio == "1":
          eoo = eoo - random.randint(10, 70)
          phof = phof - random.randint(10, 100)
          if eoo <= 0:
            eoo = 0
          if phof <= 0:
            phof = 0
          print("The essence of Ohio shoots a fire ball at you ...")
          print("You sing a An amazing fiery song which attacks the essence of Ohio directly")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phof))
          if eoo == 0: 
            print("You have beat the essence of ohio!\n\n")
            break
          if phof == 0:
            print("You have lost ... Game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 2
        if ohio == "2":
          eoo = eoo - random.randint(70 , 140)
          phof = phof - random.randint(100, 170)
          if eoo <= 0:
            eoo = 0
          if phof <= 0:
            phof = 0
          print("The essence of ohio Fire a  bunch of water shots which are infused with air energy to move at extremely fast speeds")
          print("You increase the atmosphoere with heat energy burning the essennce of ohio")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phof))
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phof == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 3
        if ohio == "3":
          eoo = eoo - random.randint(140, 170)
          phof = phof - random.randint(170, 250)
          if eoo <= 0:
            eoo = 0
          if phof <= 0:
            phof = 0
          print("The essence of ohio shoots some tornados with mini mountains in them your way...")
          print("you breath flaming hot fire which burns The essence of ohio!")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phof))
          if eoo <= 0:
            print("You have defeated the essence of ohio!")
            break
          if phof <= 0:
            print("You have died .. game over")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 4
        if ohio == "4":
          eoo = eoo - random.randint(210, 290)
          phof = phof - random.randint(250, 340)
          phof = phof - 50
          if eoo <= 0:
            eoo = 0
          if phof <= 0:
            phof = 0
          print("The essence of ohio uses his space energy magic and pushes you to the ground..")
          print("You Create a fiery inferno which traps the essence of ohio But it does send a few rocks your way....")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phof))
          if eoo <= 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phof <= 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 5  
        if ohio == "5":
          phof = phof + random.randint(1 , 150)
          if eoo <= 0:
            eoo = 0
          if phof <= 0:
            phof = 0
          print("Essence of ohio waits for you to heal...")
          print("you heal a random amount of hp from 1 to 100... ")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phof))
          if phof >= 600:
            print("\nOk. That's too much hp. \n\n")
            phof = 600
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phof == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

      
      print("\n\n\nThe esscence of ohio groans his last moments in pain.\n")
      time.sleep(3)
      print("Essence of Ohio - I am actually a scientist from the lab you saw in before and we are testing your brain.\n As i die we both to the real world.\n")
      time.sleep(4)
      print("You come to the real world and you are in a test tube but you are released and then you are in a room (Begins to remember) you remember as when you changed your clothes for the test to begin.\n")
      time.sleep(6)
      print("You have changed to your old clothes and you left the building to your car and check your phone in the car which says 2023.\n")
      time.sleep(4)
      print("You been out of the real world for 11 years but you are ready to adapt you drive off into the distance not knowing what will happen next.")
      time.sleep(4)
      print("\n\n The End...? \n\n")
      
      break
    
    
    # Element: Water element
    elif element == 2:
      
      # Attacks
      print("You have chosen the Water Element , Your memory will now be erased. Your powers are: 1. Tsunami, 2. Water blocker, 3. Washed up, 4. Flash flood.")
      print(" ")
      time.sleep(4)
      print("Guardian - I cannot tell you if You made a good choice but i wish you the best of luck on your journey..")
      time.sleep(3)
      print("You enter hell with Your New Water element.")
      time.sleep(2)
      
      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        time.sleep(5)
        boulder_w = input("Would you like to attempt to use your powers on the boulder?\n Type yes or no.\n").lower()

        # You use your powers for the boulder.
        if boulder_w == "yes":
          print("You have chosen to use your powers on the boulder.\n")

          # Hp of objects
          boulder_hp_w = 100
          w_b = boulder_hp_w
          while True:
            # Player's move
            w_m = input("You have 4 powers to use on the boulder.\n Your powers are: 1. Tsunami, 2. Water blocker 3. washed up , 4. Flash flood. Please type the number assigned for the power.\n\n")
            
            # Power 1
            if w_m == "1":
              w_b = w_b - random.randint(1, 30)
              if w_b <= 0:
                w_b = 0
              print("Boulder hp = " + str(w_b))
              if w_b == 0:
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
              w_b = w_b - random.randint(20, 70)
              if w_b <= 0:
                w_b = 0
              print("Boulder hp = " + str(w_b))
              if w_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boluder compeletly destroying it. \n")
                break

            # Power 4    
            if w_m == "4":
              w_b = w_b - random.randint(1, 101)
              if w_b <= 0:
                w_b = 0
              print("Boulder hp = " + str(w_b))
              if w_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break
          break     
        break

      # The story continues
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities. \n")
      time.sleep(9)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      time.sleep(9)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      time.sleep(7)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      time.sleep(8)
      print("In the centre of the room there are two creatures lined with armor and holding spears. They had a look resembled that of an fairy, but corrupted with stonelike skin and gleaming red eyes. Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast")
      time.sleep(12)
      print("After the fairy seeing you enter the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n")
      time.sleep(8)
      

      # Hp of players
      earth_fairy_hp = 500
      player_hp_w = 500
      efh = earth_fairy_hp
      phw = player_hp_w
      
      while True:

        # Player's move
        w = input("You have 4 powers to use on the fairy\n Your powers are: 1. Tsunami, 2. Water blocker, 3. Washed up, 4. Flash flood.\n\n")

        # Power 1   
        if w == "1":
          efh = efh - random.randint(10, 50)
          phw = phw - random.randint(10, 50)  
          if efh <= 0:
            efh = 0
          if phw <= 0:
            phw = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phw))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
          if phw == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # Power 2   
        if w == "2":
          efh = efh - random.randint(50, 100)
          phw = phw - random.randint(50, 100)  
          if efh <= 0:
            efh = 0
          if phw <= 0:
            phw = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phw))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phw == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break
          
  
        # Power 3  
        if w == "3":
          efh = efh - random.randint(100, 150)
          phf = phw - random.randint(100, 150)  
          if efh <= 0:
            efh = 0
          if phw <= 0:
            phw = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phw))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phw <= 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break
              
        # Power 4
        if w == "4":
          efh = efh - random.randint(150, 200)
          phw = phw - random.randint(150, 200)  
          if efh <= 0:
            efh = 0
          if phw <= 0:
            phw = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phw))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phw == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break


 # The story continues
      print("You have finnaly killed the creature and you breath a sigh of relief. prehaps you should just lie down and rest... and you slowly close your eyes. \n")
      time.sleep(5)
      print("This scene feels awfully familiar... no thats impossible the guardian erased all my memories and theres no way i have been here before... \n you hear a small sound at the tip of your ears. \n")
      time.sleep(6)
      print("You slowly open your eyes to see the similar fairy standing over your face peering down at you. 'You must not be a very good man.' In a fright you immideatly move away. \n")
      time.sleep(5)
      print("you finally pull yourself together and get up to notice that the cages had all fallen down. You never noticed it at first but the cages all had creatures inside them and they seem to have broken out of their cages. \n")
      time.sleep(6)
      print("The creature were unexpectedly gentle compared to what you would expect lf creatures from hell. \n")
      time.sleep(3)
      print("The creatures have the ability to communicate and talked to you. The littlest one said that they were not monsters but spirits.\n These are creatures you can trust. \n")
      time.sleep(5)
      print("You continue down the dark tunnel, but it no longer seems so dull as you are just happy to have people by your side that was until... \n")
      time.sleep(4)
      print("You hear a giant rumble as the ground breaks beneath you. A enormous hole is created and you begin to fall enwrapped by darkness not sure when it ends. \n")
      time.sleep(4)
      print("You finally land on ground and your body hurts all over. you look all around you and it seems that the spirits had followed you down. Infront of you there is a large gate which feels uncannily familiar. \n")
      time.sleep(6)
      print("By now you remember most of your life, your family, friends, school but nothing after you turned 18. \n")
      time.sleep(3)
      print("Infront of you is a large portal.\n Consumed by curiosity you go through the gate, the spirits following closely behind. \n")
      time.sleep(4)
      print(" You're now in a large elegantly decorated room woth a figure in the middle that seems awfully familiar...")
      time.sleep(4)
      print("He turns around and its the guardian! Why? Why is he here? \n")
      time.sleep(2)
      print("Guardian - Human. You have fallen for my charades yet again! Oh how could you be so stupid? I am no guardian, you are not good and this is not hell! \n")
      time.sleep(5)
      print("Guardian - I am actually the Essence of Ohio. You have to battle me to get out of this world.\n")
      time.sleep(3)


      print("You meet face to face with the essence of Ohio.. \n")
      time.sleep(2)
      print("Essence of Ohio - Hello again .. i understand that you have conquered hell with my power... and you should understand that you only have an fraction of my power.\n")
      time.sleep(5)
      print("so I will present you with the option for 1 move... it will help you rival my might. this helps you heal damage taken on a random base... it goes from your 1 hp to 100 hp... LET'S START THE BATTLE.\n")
      time.sleep(6)
      player_hp_ohio_w = 600
      essence_of_ohio = 1000
      phow = player_hp_ohio_w
      eoo = essence_of_ohio
      while True:
        ohio = input("Which move do you choose? 1. Tsunami, 2. Water blocker 3. Washed up , 4. Flash flood. 5. Oceans embrace.\n\n")
        
        if ohio == "1":
          eoo = eoo - random.randint(10, 70)
          phow = phow - random.randint(10, 100)
          if eoo <= 0:
            eoo = 0
          if phow <= 0:
            phow = 0
          print("The essence of Ohio shoots a ball of fire at you ...")
          print("You make a huge tsunami which attacks the essence of Ohio directly")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phow))
          if eoo == 0: 
            print("You have beat the essence of ohio!\n\n")
            break
          if phow == 0:
            print("You have lost ... Game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 2
        if ohio == "2":
          eoo = eoo - random.randint(70 , 140)
          # phow = phow - random.randint(100, 170)
          if eoo <= 0:
            eoo = 0
          if phow <= 0:
            phow = 0
          print("The essence of ohio Fire a  bunch of water shots which are infused with air energy to move at extremely fast speeds")
          print("You block the attack so you have pushed all the water to the essennce of ohio")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phow))
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phow == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 3
        if ohio == "3":
          eoo = eoo - random.randint(140, 210)
          phow = phow - random.randint(170, 250)
          if eoo <= 0:
            eoo = 0
          if phow <= 0:
            phow = 0
          print("The essence of ohio shoots some tornados with mini mountains in them on your way...")
          print("You wash youself ashore but one of the tornados caught you and push the tornado to The essence of ohio!")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phow))
          if eoo <= 0:
            print("You have defeated the essence of ohio!")
            break
          if phow <= 0:
            print("You have died .. game over")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 4
        if ohio == "4":
          eoo = eoo - random.randint(210, 290)
          phow = phow - random.randint(250, 350)
          phow = phow - 50
          if eoo <= 0:
            eoo = 0
          if phow <= 0:
            phow = 0
          print("The essence of ohio uses his space energy magic and pushes you to the ground..")
          print("You Create a flash flood which traps the essence of ohio But it does send a few rocks your way....")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phow))
          if eoo <= 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phow <= 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 5  
        if ohio == "5":
          phow = phow + random.randint(1 , 150)
          if eoo <= 0:
            eoo = 0
          if phow <= 0:
            phow = 0
          print("Essence of ohio waits for you to heal..")
          print("you heal a random amount of hp from 1 to 100... ")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phow))
          if phow >= 600:
            print("\nOk. That's too much hp. \n\n")
            phow = 600
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phow == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

      print("\n\n\nThe esscence of ohio groans his last moments in pain.\n")
      time.sleep(3)
      print("Essence of Ohio - I am actually a scientist from the lab you saw in before and we are testing your brain.\n As i die we both to the real world.\n")
      time.sleep(4)
      print("You come to the real world and you are in a test tube but you are released and then you are in a room (Begins to remember) you remember as when you changed your clothes for the test to begin.\n")
      time.sleep(6)
      print("You have changed to your old clothes and you left the building to your car and check your phone in the car which says 2023.\n")
      time.sleep(4)
      print("You been out of the real world for 11 years but you are ready to adapt you drive off into the distance not knowing what will happen next.")
      time.sleep(4)
      print("\n\n The End...? \n\n")
      break
      
      
      # Element: Earth element
    elif element == 3:

      # Attacks
      print("You have chosen the Earth Element , Your memory will now be erased. Your powers are: 1. Retreat behind the hill, 2. Trash compactor, 3. Dig deep. 4. Earth quake.")
      time.sleep(4)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      time.sleep(3)
      print("You enter hell with Your New Earth element.")
      time.sleep(2)

      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        time.sleep(5)
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
              e_b = e_b - random.randint(20, 70)
              if e_b <= 0:
                e_b = 0
              print("Boulder hp = " + str(e_b))
              if e_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 4    
            if e_m == "4":
              e_b = e_b - random.randint(1, 101)
              if e_b <= 0:
                e_b = 0
              print("Boulder hp = " + str(e_b))
              if e_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break
          break     
        break

        # The story continues
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities. \n")
      time.sleep(9)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      time.sleep(9)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      time.sleep(7)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      time.sleep(8)
      print("In the centre of the room there are two creatures lined with armor and holding spears. They had a look resembled that of an fairy, but corrupted with stonelike skin and gleaming red eyes. Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast")
      time.sleep(12)
      print("After the fairy seeing you enter the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n")
      time.sleep(8)
      

      # Hp of players
      earth_fairy_hp = 500
      player_hp_e = 500
      efh = earth_fairy_hp
      phe = player_hp_e
      while True:
        
        # Player's move
        e = input("You have 4 powers to use on the fairy\n Your powers are: 1. Retreat behind the hill, 2. Trash compactor, 3. Dig deep. 4. Earth quake.\n\n")

        
        # Power 1   
        if e == "1":
          efh = efh - random.randint(10, 50)
          phe = phe - random.randint(10, 50)  
          if efh <= 0:
            efh = 0
          if phe <= 0:
            phe = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phe))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phe == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

            
        # Power 2   
        if e == "2":
          efh = efh - random.randint(50, 100)
          phe = phe - random.randint(0, 0)  
          if efh <= 0:
            efh = 0
          if phe <= 0:
            phe = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phe))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phe == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # Power 3   
        if e == "3":
          efh = efh - random.randint(100, 150)
          phe = phe - random.randint(100, 150)  
          if efh <= 0:
            efh = 0
          if phe <= 0:
            phe = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phe))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phe == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break
              
        # Power 4
        if e == "4":
          efh = efh - random.randint(150, 200)
          phe = phe - random.randint(150, 200)  
          if efh <= 0:
            efh = 0
          if phe <= 0:
            phe = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(phe))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if phe == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # The story continues
      print("You have finnaly killed the creature and you breath a sigh of relief. prehaps you should just lie down and rest... and you slowly close your eyes. \n")
      time.sleep(4)
      print("This scene feels awfully familiar... no thats impossible the guardian erased all my memories and theres no way i have been here before... \n you hear a small sound at the tip of your ears. \n")
      time.sleep(6)
      print("You slowly open your eyes to see the similar fairy standing over your face peering down at you. 'You must not be a very good man.' In a fright you immideatly move away. \n")
      time.sleep(5)
      print("you finally pull yourself together and get up to notice that the cages had all fallen down. You never noticed it at first but the cages all had creatures inside them and they seem to have broken out of their cages. \n")
      time.sleep(6)
      print("The creature were unexpectedly gentle compared to what you would expect lf creatures from hell. \n")
      time.sleep(3)
      print("The creatures have the ability to communicate and talked to you. The littlest one said that they were not monsters but spirits.\n These are creatures you can trust. \n")
      time.sleep(5)
      print("You continue down the dark tunnel, but it no longer seems so dull as you are just happy to have people by your side that was until... \n")
      time.sleep(4)
      print("You hear a giant rumble as the ground breaks beneath you. A enormous hole is created and you begin to fall enwrapped by darkness not sure when it ends. \n")
      time.sleep(4)
      print("You finally land on ground and your body hurts all over. you look all around you and it seems that the spirits had followed you down. Infront of you there is a large gate which feels uncannily familiar. \n")
      time.sleep(6)
      print("By now you remember most of your life, your family, friends, school but nothing after you turned 18. \n")
      time.sleep(3)
      print("Infront of you is a large portal.\n Consumed by curiosity you go through the gate, the spirits following closely behind. \n")
      time.sleep(4)
      print(" You're now in a large elegantly decorated room woth a figure in the middle that seems awfully familiar...")
      time.sleep(3)
      print("He turns around and its the guardian! Why? Why is he here? \n")
      time.sleep(2)
      print("Guardian - Human. You have fallen for my charades yet again! Oh how could you be so stupid? I am no guardian, you are not good and this is not hell! \n")
      time.sleep(4)
      print("Guardian - I am actually the Essence of Ohio. You have to battle me to get out of this world.\n")
      time.sleep(3)

      

      
      print("You meet face to face with the essence of Ohio.. \n")
      time.sleep(2)
      print("Essence of Ohio - Hello again .. i understand that you have conquered hell with my power... and you should understand that you only have an fraction of my power.\n")
      time.sleep(5)
      print("so I will present you with the option for 1 move... it will help you rival my might. this helps you heal damage taken on a random base... it goes from your 1 hp to 100 hp... LET'S START THE BATTLE.\n")
      time.sleep(6)
      player_hp_ohio_e = 600
      essence_of_ohio = 1000
      phoe = player_hp_ohio_e
      eoo = essence_of_ohio
      while True:
        ohio = input("You have 4 powers to use on the boulder.\n Your powers are: 1. Retreat behind the hill, 2. Trash compactor, 3. Dig deep, 4. Earth quake, 5. Earth embrace \n\n")
        
        if ohio == "1":
          eoo = eoo - random.randint(10, 70)
          phoe = phoe - random.randint(10, 100)
          if eoo <= 0:
            eoo = 0
          if phoe <= 0:
            phoe = 0
          print("The essence of Ohio shoots a ball of fire at you ...")
          print("You make a retreat behind a hill and use the ground to make a hole which attacks the essence of Ohio directly")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phow))
          if eoo == 0: 
            print("You have beat the essence of ohio!\n\n")
            break
          if phoe == 0:
            print("You have lost ... Game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 2
        if ohio == "2":
          eoo = eoo - random.randint(70 , 140)
          # phoe = phoe - random.randint(100, 170)
          if eoo <= 0:
            eoo = 0
          if phoe <= 0:
            phoe = 0
          print("The essence of ohio Fire a  bunch of water shots which are infused with air energy to move at extremely fast speeds")
          print("You compact the attack so you have slowed it and made it heavier and threw it to the essennce of ohio")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoe))
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phoe == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 3
        if ohio == "3":
          eoo = eoo - random.randint(140, 210)
          phoe = phoe - random.randint(170, 250)
          if eoo <= 0:
            eoo = 0
          if phoe <= 0:
            phoe = 0
          print("The essence of ohio shoots some tornados with mini mountains in them on your way...")
          print("You have dug a deep hole but still a tornado picks you up so you chuck it to The essence of ohio!")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoe))
          if eoo <= 0:
            print("You have defeated the essence of ohio!")
            break
          if phoe <= 0:
            print("You have died .. game over")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 4
        if ohio == "4":
          eoo = eoo - random.randint(210, 290)
          phoe = phoe - random.randint(250, 340)
          phoe = phoe - 50
          if eoo <= 0:
            eoo = 0
          if phoe <= 0:
            phoe = 0
          print("The essence of ohio uses his space energy magic and pushes you to the ground..")
          print("You Create a earth quake which traps the essence of ohio But it does send a few rocks your way....")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoe))
          if eoo <= 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phoe <= 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 5  
        if ohio == "5":
          phoe = phoe + random.randint(1 , 150)
          if eoo <= 0:
            eoo = 0
          if phoe <= 0:
            phoe = 0
          print("Essence of ohio waits for you to heal..")
          print("you heal a random amount of hp from 1 to 100... ")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoe))
          if phoe >= 600:
            print("\nOk. That's too much hp. \n\n")
            phoe = 600
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phoe == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

      print("\n\n\nThe esscence of ohio groans his last moments in pain.\n")
      time.sleep(3)
      print("Essence of Ohio - I am actually a scientist from the lab you saw in before and we are testing your brain.\n As i die we both to the real world.\n")
      time.sleep(4)
      print("You come to the real world and you are in a test tube but you are released and then you are in a room (Begins to remember) you remember as when you changed your clothes for the test to begin.\n")
      time.sleep(6)
      print("You have changed to your old clothes and you left the building to your car and check your phone in the car which says 2023.\n")
      time.sleep(4)
      print("You been out of the real world for 11 years but you are ready to adapt you drive off into the distance not knowing what will happen next.")
      time.sleep(4)
      print("\n\n The End...? \n\n")
      break
      
      # Element: Space element
    elif element == 4:

      # Attacks
      print("You have chosen the Space Element , Your memory will now be erased. Your powers are:  1. Antigravity, 2. Black hole, 3. orbit, 4. fly away.")
      time.sleep(4)
      print("Guardian - I see. I cannot guarantee it was a good choice I do however, wish you luck on your journey. \n")
      time.sleep(3)
      print("You enter hell with Your New Space element.")
      time.sleep(2)
      
      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        time.sleep(5)
        boulder_s = input("Would you like to attempt to use your powers on the boulder?\n Type yes or no.\n").lower()

        # You use your powers for the boulder.
        if boulder_s == "yes":
          print("You have chosen to use your powers on the boulder.\n")

          # Hp of objects
          boulder_hp_s = 100
          s_b = boulder_hp_s
          while True:
            # Player's move
            s_m = input("You have 4 powers to use on the boulder.\n Your powers are:  1. Antigravity, 2. Black hole, 3. orbit, 4. fly away.\n\n")
            
            # Power 1
            if s_m == "1":
              s_b = s_b - random.randint(10, 60)
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
              s_b = s_b - random.randint(20, 70)
              if s_b <= 0:
                s_b = 0
              print("Boulder hp = " + str(s_b))
              if s_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break

            # Power 4    
            if s_m == "4":
              s_b = s_b - random.randint(1, 101)
              if s_b <= 0:
                s_b = 0
              print("Boulder hp = " + str(s_b))
              if s_b == 0:
                print("In a fit of rage you unleash a godly  amount of power on the boulder compeletly destroying it. \n")
                break
          break       
        break

        # The story continues
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities. \n")
      time.sleep(9)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      time.sleep(9)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      time.sleep(7)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      time.sleep(8)
      print("In the centre of the room there are two creatures lined with armor and holding spears. They had a look resembled that of an fairy, but corrupted with stonelike skin and gleaming red eyes. Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast")
      time.sleep(12)
      print("After the fairy seeing you enter the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n")
      time.sleep(8)

      earth_fairy_hp = 500
      efh = earth_fairy_hp
      player_hp_s = 500
      pha = player_hp_s
      while True:
        s = input("You have 4 powers to use on the fairy\n Your powers are: 1. orbit,2. anti gravity 3. Fly away  , 4. Blackhole .Please type the number assigned for the power.\n\n")
      
        # Power 1
        if s == "1":
          efh = efh - random.randint(10, 50)
          pha = pha - random.randint(10, 50)  
          if efh <= 0:
            efh = 0
          if pha <= 0:
            pha = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(pha))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if pha == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # Power 2
        if s == "2":
          efh = efh - random.randint(50, 100)
          pha = pha - random.randint(50, 100)  
          if efh <= 0:
            efh = 0
          if pha <= 0:
            pha = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(pha))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if pha == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # Power 3
        if s == "3":
          efh = efh - random.randint(100, 150)
          pha = pha - random.randint(100, 150)  
          if efh <= 0:
            efh = 0
          if pha <= 0:
            pha = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(pha))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if pha == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break  

        # Power 4
        if s == "4":
          efh = efh - random.randint(150, 200)
          pha = pha - random.randint(150, 200)  
          if efh <= 0:
            efh = 0
          if pha <= 0:
            pha = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(pha))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if pha == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        
    # The story continues
      print("You have finnaly killed the creature and you breath a sigh of relief. prehaps you should just lie down and rest... and you slowly close your eyes. \n")
      time.sleep(4)
      print("This scene feels awfully familiar... no thats impossible the guardian erased all my memories and theres no way i have been here before... \n you hear a small sound at the tip of your ears. \n")
      time.sleep(6)
      print("You slowly open your eyes to see the similar fairy standing over your face peering down at you. 'You must not be a very good man.' In a fright you immideatly move away. \n")
      time.sleep(5)
      print("you finally pull yourself together and get up to notice that the cages had all fallen down. You never noticed it at first but the cages all had creatures inside them and they seem to have broken out of their cages. \n")
      time.sleep(6)
      print("The creature were unexpectedly gentle compared to what you would expect lf creatures from hell. \n")
      time.sleep(3)
      print("The creatures have the ability to communicate and talked to you. The littlest one said that they were not monsters but spirits.\n These are creatures you can trust. \n")
      time.sleep(5)
      print("You continue down the dark tunnel, but it no longer seems so dull as you are just happy to have people by your side that was until... \n")
      time.sleep(4)
      print("You hear a giant rumble as the ground breaks beneath you. A enormous hole is created and you begin to fall enwrapped by darkness not sure when it ends. \n")
      time.sleep(4)
      print("You finally land on ground and your body hurts all over. you look all around you and it seems that the spirits had followed you down. Infront of you there is a large gate which feels uncannily familiar. \n")
      time.sleep(6)
      print("By now you remember most of your life, your family, friends, school but nothing after you turned 18. \n")
      time.sleep(3)
      print("Infront of you is a large portal.\n Consumed by curiosity you go through the gate, the spirits following closely behind. \n")
      time.sleep(3)
      print(" You're now in a large elegantly decorated room woth a figure in the middle that seems awfully familiar...")
      time.sleep(3)
      print("He turns around and its the guardian! Why? Why is he here? \n")
      time.sleep(2)
      print("Guardian - Human. You have fallen for my charades yet again! Oh how could you be so stupid? I am no guardian, you are not good and this is not hell! \n")
      time.sleep(4)
      print("Guardian - I am actually the Essence of Ohio. You have to battle me to get out of this world.\n")
      time.sleep(3)


      print("You meet face to face with the essence of Ohio.. \n")
      time.sleep(2)
      print("Essence of Ohio - Hello again .. i understand that you have conquered hell with my power... and you should understand that you only have an fraction of my power.\n")
      time.sleep(4)
      print("so I will present you with the option for 1 move... it will help you rival my might. this helps you heal damage taken on a random base... it goes from your 1 hp to 100 hp... LET'S START THE BATTLE.\n")
      time.sleep(6)
      player_hp_ohio_s = 600
      essence_of_ohio = 1000
      phos = player_hp_ohio_s
      eoo = essence_of_ohio
      while True:
        ohio = input("Which move do you choose.\n Your powers are: 1. orbit, 2. anti gravity, 3. Fly away, 4. Blackhole, 5. Space embrace. \n\n")
        
        if ohio == "1":
          eoo = eoo - random.randint(10, 70)
          phos = phos - random.randint(10, 100)
          if eoo <= 0:
            eoo = 0
          if phos <= 0:
            phos = 0
          print("The essence of Ohio shoots a ball of fire at you ...")
          print("You make a orbit around the essecnce of ohio any you make the essence of Ohio get dizzy from your orbit")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phos))
          if eoo == 0: 
            print("You have beat the essence of ohio!\n\n")
            break
          if phos == 0:
            print("You have lost ... Game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 2
        if ohio == "2":
          eoo = eoo - random.randint(70 , 140)
          # phos = phos - random.randint(100, 170)
          if eoo <= 0:
            eoo = 0
          if phos <= 0:
            phos = 0
          print("The essence of ohio Fire a  bunch of water shots which are infused with air energy to move at extremely fast speeds")
          print("You have turned on anti-gravity and all the water shots go up and you turn it off then the water droplets com directly at the essennce of ohio")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phos))
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phos == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 3
        if ohio == "3":
          eoo = eoo - random.randint(140, 210)
          phos = phos - random.randint(170, 250)
          if eoo <= 0:
            eoo = 0
          if phos <= 0:
            phos = 0
          print("The essence of ohio shoots some tornados with mini mountains in them on your way...")
          print("You have flown away but still a tornado picks you up so you chuck it to The essence of ohio!")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phos))
          if eoo <= 0:
            print("You have defeated the essence of ohio!")
            break
          if phos <= 0:
            print("You have died .. game over")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 4
        if ohio == "4":
          eoo = eoo - random.randint(210, 290)
          phos = phos - random.randint(250, 340)
          phos = phos - 50
          if eoo <= 0:
            eoo = 0
          if phos <= 0:
            phos = 0
          print("The essence of ohio uses his space energy magic and pushes you to the ground..")
          print("You Create a blackhole which traps the essence of ohio But it does send a few rocks your way....")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phos))
          if eoo <= 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phos <= 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 5  
        if ohio == "5":
          phos = phos + random.randint(1 , 150)
          if eoo <= 0:
            eoo = 0
          if phos <= 0:
            phos = 0
          print("Essence of ohio waits for you to heal..")
          print("you heal a random amount of hp from 1 to 100... ")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phos))
          if phos >= 600:
            print("\nOk. That's too much hp. \n\n")
            phos = 600
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phos == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break
      
      print("\n\n\nThe esscence of ohio groans his last moments in pain.\n")
      time.sleep(3)
      print("Essence of Ohio - I am actually a scientist from the lab you saw in before and we are testing your brain.\n As i die we both to the real world.\n")
      time.sleep(4)
      print("You come to the real world and you are in a test tube but you are released and then you are in a room (Begins to remember) you remember as when you changed your clothes for the test to begin.\n")
      time.sleep(6)
      print("You have changed to your old clothes and you left the building to your car and check your phone in the car which says 2023.\n")
      time.sleep(4)
      print("You been out of the real world for 11 years but you are ready to adapt you drive off into the distance not knowing what will happen next.")
      time.sleep(4)
      print("\n\n The End...? \n\n")
      break
    

      # Element: Air element
    elif element == 5: 

      # Attacks
      print("You have chosen the Air Element , Your memory will now be erased. Your powers are: 1. Upper Class, 2. tornado, 3.Blow them away, 4. Dizzying speed.")
      time.sleep(4)
      print("Guardian - I cannot tell you if You made a good choice but i wish you the best of luck on your journey..")
      time.sleep(3)
      print("You enter hell with Your New Air element.")
      time.sleep(2)
      
      while True:
        print("The gates open into a dimly lit tunnel and you walk for what seems like an infinite amount of time when you come accros a large boulder blocking your path.\n")
        time.sleep(5)
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
              a_b = a_b - random.randint(1, 100)
              if a_b <= 0:
                a_b = 0
              print("Boulder hp = " + str(a_b))
              if a_b <= 0:
                print("In a fit of rage, you unleash a massive tornado on the boulder, compeletly destroying it. \n")
                break

            # Power 3     
            if a_m == "3":
              a_b = a_b - random.randint(40,70 )
              if a_b <= 0:
                a_b = 0
              print("Boulder hp = " + str(a_b))
              if a_b <= 0:
                print("In a fit of rage you unleash a godly  amount of power and the boulder smashes into a wall, compeletly destroying it. \n")
                break
                
            # Power 4
            if a_m == "4":
              a_b = a_b - random.randint(0, 0)
              print("The boulder spins! Nothing happens. try Again!")
              
          break
        break
        
      # The story continues
      print("As you walk aimlessly you begin to feel nervous, like there is something watching you. you feel an incline in the tunnel and walk for what was probably hours but felt like days coming across more boulders while testing your newfound abilities. \n")
      time.sleep(9)
      print("At one point you hit a hard wall but quickly realise it is actually a large door. You are brought back to your senses because of the door instead of a boulder obstructing your path instead. \n")
      time.sleep(9)
      print("Having nowhere else to go you use a little of your strength to push the door open but to your suprise it opens on its own.\n")
      time.sleep(7)
      print("When you enter there are spikes all over the room exept on the floor. it somewhat looks like a jailcell with cages hanging from the cieling. \n")
      time.sleep(8)
      print("In the centre of the room there are two creatures lined with armor and holding spears. They had a look resembled that of an fairy, but corrupted with stonelike skin and gleaming red eyes. Their mouthes were dripping with what you dould only guess was blood and had demeanor was that of a angered beast")
      time.sleep(12)
      print("After the fairy seeing you enter the room they go into what you can only guess is a crazed frenzy and begin to charge at you.\n")
      time.sleep(8)

      
      earth_fairy_hp = 500
      player_hp_a = 500
      efh = earth_fairy_hp
      pha = player_hp_a
      while True:
        # Player's moves
        a = input("You have 4 powers to use on the fairy\n our powers are: 1. Upper Class, 2. tornado, 3.Blow them away, 4. Dizzying speed.\n\n")

        # Power 1
        if a == "1":
          efh = efh - random.randint(100, 150)
          pha = pha - random.randint(100, 150)  
          if efh <= 0:
            efh = 0
          if pha <= 0:
            pha = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(pha))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if pha == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

        # Power 2
        if a == "2":
          efh = efh - random.randint(100, 150)
          pha = pha - random.randint(100, 150)  
          if efh <= 0:
            efh = 0
          if pha <= 0:
            pha = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(pha))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if pha == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

          # Power 3
        if a == "3":
          efh = efh - random.randint(100, 150)
          pha = pha - random.randint(100, 150)  
          if efh <= 0:
            efh = 0
          if pha <= 0:
            pha = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(pha))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if pha == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

          # Power 4
        if a == "4":
          efh = efh - random.randint(100, 150)
          pha = pha - random.randint(100, 150)  
          if efh <= 0:
            efh = 0
          if pha <= 0:
            pha = 0
          print("The fairy shoots water bullets infused with some mud in it at you")
          print("Fairy hp = " + str(efh))
          print("Your hp  = "+ str(pha))  
          if efh == 0:
            print("You finally defeated the Fairy... \n")
            break
          if pha == 0: 
            print("You have died ..  game over. \n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
            break

            
      # The story continues
      print("You have finnaly killed the creature and you breath a sigh of relief. prehaps you should just lie down and rest... and you slowly close your eyes. \n")
      time.sleep(4)
      print("This scene feels awfully familiar... no thats impossible the guardian erased all my memories and theres no way i have been here before... \n you hear a small sound at the tip of your ears. \n")
      time.sleep(6)
      print("You slowly open your eyes to see the similar fairy standing over your face peering down at you. 'You must not be a very good man.' In a fright you immideatly move away. \n")
      time.sleep(5)
      print("you finally pull yourself together and get up to notice that the cages had all fallen down. You never noticed it at first but the cages all had creatures inside them and they seem to have broken out of their cages. \n")
      time.sleep(6)
      print("The creature were unexpectedly gentle compared to what you would expect lf creatures from hell. \n")
      time.sleep(3)
      print("The creatures have the ability to communicate and talked to you. The littlest one said that they were not monsters but spirits.\n These are creatures you can trust. \n")
      time.sleep(5)
      print("You continue down the dark tunnel, but it no longer seems so dull as you are just happy to have people by your side that was until... \n")
      time.sleep(4)
      print("You hear a giant rumble as the ground breaks beneath you. A enormous hole is created and you begin to fall enwrapped by darkness not sure when it ends. \n")
      time.sleep(4)
      print("You finally land on ground and your body hurts all over. you look all around you and it seems that the spirits had followed you down. Infront of you there is a large gate which feels uncannily familiar. \n")
      time.sleep(6)
      print("By now you remember most of your life, your family, friends, school but nothing after you turned 18. \n")
      time.sleep(3)
      print("In front of you is a large portal.\n Consumed by curiosity you go through the gate, the spirits following closely behind. \n")
      time.sleep(4)
      print(" You're now in a large elegantly decorated room woth a figure in the middle that seems awfully familiar...")
      time.sleep(3)
      print("He turns around and its the guardian! Why? Why is he here? \n")
      time.sleep(2)
      print("Guardian - Human. You have fallen for my charades yet again! Oh how could you be so stupid? I am no guardian, you are not good and this is not hell! \n")
      time.sleep(5)
      print("Guardian - I am actually the Essence of Ohio. You have to battle me to get out of this world.\n")
      time.sleep(3)


      print("You meet face to face with the essence of Ohio.. \n")
      time.sleep(2)
      print("Essence of Ohio - Hello again .. i understand that you have conquered hell with my power... and you should understand that you only have an fraction of my power.\n")
      time.sleep(5)
      print("so I will present you with the option for 1 move... it will help you rival my might. this helps you heal damage taken on a random base... it goes from your 1 hp to 100 hp... LET'S START THE BATTLE.\n")
      time.sleep(6)
      player_hp_ohio_a = 600
      essence_of_ohio = 1000
      phoa = player_hp_ohio_a
      eoo = essence_of_ohio
      while True:
        ohio = input("You have 4 powers to use.\n Your powers are: 1. Upper Class, 2. tornado, 3.Blow them away, 4. Dizzying speed, 5. Wind embrace \n\n")
        
        if ohio == "1":
          eoo = eoo - random.randint(10, 70)
          phoa = phoa - random.randint(10, 100)
          if eoo <= 0:
            eoo = 0
          if phoa <= 0:
            phoa = 0
          print("The essence of Ohio shoots a ball of fire at you ...")
          print("You make a retreat over a hill and use the air to suffocate the essence of Ohio directly")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoa))
          if eoo == 0: 
            print("You have beat the essence of ohio!\n\n")
            break
          if phoa == 0:
            print("You have lost ... Game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 2
        if ohio == "2":
          eoo = eoo - random.randint(70 , 140)
          # phow = phow - random.randint(100, 170)
          if eoo <= 0:
            eoo = 0
          if phoa <= 0:
            phoa = 0
          print("The essence of ohio Fire a  bunch of water shots which are infused with air energy to move at extremely fast speeds")
          print("You make a tornado countering the attack but some water pellets hit you and the tornado reaches the essennce of ohio")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoa))
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phoa == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 3
        if ohio == "3":
          eoo = eoo - random.randint(140, 210)
          phoa = phoa - random.randint(170, 250)
          if eoo <= 0:
            eoo = 0
          if phoa <= 0:
            phoa = 0
          print("The essence of ohio shoots some tornados with mini mountains in them on your way...")
          print("You have tried to push the tornado away but still a tornado picks you up so you chuck it to The essence of ohio!")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoa))
          if eoo <= 0:
            print("You have defeated the essence of ohio!")
            break
          if phoa <= 0:
            print("You have died .. game over")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 4
        if ohio == "4":
          eoo = eoo - random.randint(210, 290)
          phoa = phoa - random.randint(250, 340)
          phoa = phoa - 50
          if eoo <= 0:
            eoo = 0
          if phoa <= 0:
            phoa = 0
          print("The essence of ohio uses his space energy magic and pushes you to the ground..")
          print("You Create a earth quake which traps the essence of ohio But it does send a few rocks your way....")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoa))
          if eoo <= 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phoa <= 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break

        # Power 5  
        if ohio == "5":
          phoa = phoa + random.randint(1 , 150)
          if eoo <= 0:
            eoo = 0
          if phoa <= 0:
            phoa = 0
          print("Essence of ohio waits for you to heal..")
          print("you heal a random amount of hp from 1 to 100... ")
          print("Essence of Ohio hp = " + str(eoo))
          print("Your hp  = "+ str(phoa))
          if phoa >= 600:
            print("\nOk. That's too much hp. \n\n")
            phoa = 600
          if eoo == 0:
            print("You have defeated the essence of ohio!\n\n")
            break
          if phoa == 0:
            print("You have died .. game over.\n\n\n")
            subprocess.call([sys.executable, os.path.realpath(__file__)] +
      sys.argv[1:])
            break
      print("\n\n\nThe esscence of ohio groans his last moments in pain.\n")
      time.sleep(3)
      print("Essence of Ohio - I am actually a scientist from the lab you saw in before and we are testing your brain.\n As i die we both to the real world.\n")
      time.sleep(4)
      print("You come to the real world and you are in a test tube but you are released and then you are in a room (Begins to remember) you remember as when you changed your clothes for the test to begin.\n")
      time.sleep(6)
      print("You have changed to your old clothes and you left the building to your car and check your phone in the car which says 2023.\n")
      time.sleep(4)
      print("You been out of the real world for 11 years but you are ready to adapt you drive off into the distance not knowing what will happen next.")
      time.sleep(4)
      print("\n\n The End...? \n\n")
      break
    break
      
    
      
  elif offer == "no":
    
    print("Guardian - Hmmm")
    time.sleep(1)
    print("Guardian - It seems you dont want to live. Well, I will still let you through the gates of hell... And maybe I will see you again")
    time.sleep(4)
    
    # You are vaporised from hell.
    print("You enter hell without any powers, due to you having no powers to fight the forces of hell. The power in hell evaporates you get erased from exsistence.\n\n")
    time.sleep(4)
    print("This is ending 1.")
    print("!!!GAME OVER!!!")
    break
    
  else:
    # Type one of the answers
    print("Please keep one of the answers.")
  
  break


while True:
  start_again = input("Would you like to start again. Type yes or no").lower()
    
  if start_again == "yes":
    subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:]) 
  elif start_again == "no":
    print("Congratulations you made it to the end.")
  else:
    print("please type yes or no.")



