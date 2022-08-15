import random
import own_modules as om
import sys
import os
starters = []
crea = """
    ######   #######    ########          ##  
    #        #      #   #               ##  ##
    #        #      #   #              ##     ##
    #        #######    ########      ###########
    #        #    ##    #            ##         ##
    #        #     ##   #           ##           ##
    ######   #      ##  ########   ##             ##
"""
game = """
###########          ##          ###         ###    #########      
#                  ##  ##        #  ##     ##  #    #          
#                 ##    ##       #   ##   ##   #    #
#   #######      ##########      #    ## ##    #    #########
#         #     ##        ##     #     ##      #    # 
#         #    ##          ##    #             #    # 
###########   ##            ##   #             #    ######### 
"""

over = """
 ########     ##           ##    #########    ########
#        #     ##         ##     #            #       #
#        #      ##       ##      #            #       #
#        #       ##     ##       #########    ######## 
#        #        ##   ##        #            #      ##
#        #         ## ##         #            #       ## 
 ########           ###          #########    #        ## 
"""

#To-Do
#Add a skip function that lets you skip the fight 

#Quit game function
all_input = []
def check_for_quit(input):
  all_input.append(input)
  if "quit" in all_input:
    os.system("clear")
    sys.exit(game + over)

def reset_creatures_stats():
  for creature in list_of_creatures:
    creature.health = creature.original_health
    creature.speed = creature.original_speed
    creature.strength = creature.original_strength

class Attack:
  def __init__(self, name, damage = 0, heal = 0, strength = 0, speed = 0):
    self.name = name
    self.damage = damage
    self.heal = heal
    self.strength = strength
    self.speed = speed
    


  def __repr__(self):
    description = "This attack named {name} does {damage} damage, heals {heal}%, increases strength by {strength}% and increases speed by {speed}%".format(name = self.name, damage = self.damage, heal = self.heal, strength = self.strength, speed = self.speed)
    return description

  def attack(self, own_creature, other_creature):
    if self in own_creature.attacks:
      damage_amount = int(self.damage * (own_creature.strength/100))
      own_creature.health_updated(self.heal)
      own_creature.strength_updated(self.strength)
      own_creature.speed_updated(self.speed)
      other_creature.health_updated(damage_amount)
    else:
      print("Attack not part of the Creature")

#Adding all the attacks
scratch = Attack("Scratch", damage = -20)
leech = Attack("Leech", damage = -16, heal = 8)
crush = Attack("Crush", damage = -24)
destroy = Attack("Destroy", damage = -28)
bloodlust = Attack("Bloodlust", strength = 25, heal = -10)
howl = Attack("Howl", strength = 15, heal = -5)
nourish = Attack("Nourish", strength = 5, heal = 15)
heal = Attack("Heal", heal = 25)
flash = Attack("Flash", speed = 50)

list_of_attacks = (scratch, leech, crush, destroy, bloodlust, howl, nourish, heal, flash)


class Creature:
  def __init__(self, name, speed, strength, health, attacks, starter = False):
    self.name = name
    self.speed = speed
    self.strength = strength
    self.health = health
    self.attacks = attacks
    if starter == True:
      starters.append(self)
    self.original_health = health
    self.original_speed = speed
    self.original_strength = strength


  def __repr__(self):
    attack_names = []
    for attack in self.attacks:
      attack_names.append(attack.name)
    description = "{name} has {health} HP, {strength} strength, {speed} speed and the attacks : {attacks}".format(name = self.name, health = self.health, strength = self.strength, speed = self.speed, attacks = attack_names)
    return description

  def stats(self):
    stats = "{name} has {health} HP, {strength} strength and {speed} speed".format(name = self.name, health = self.health, strength = self.strength, speed = self.speed)
    return stats

  def health_updated(self, amount):
    self.health += amount
    if self.health <= 0:
      print("{creature} has been defeated".format(creature = self.name))
      if self not in trainer_one.creatures and self in list_of_uncaptured_creatures:
        list_of_uncaptured_creatures.remove(self)
        trainer_one.creatures.append(self)

  def strength_updated (self, amount):
    self.strength += amount
  def speed_updated(self, amount):
    self.speed += amount
  
  def use_heal_pot(self):
    self.health = self.original_health
    trainer_one.heal_potions -= 1


#Adding all the creatures
moldblody = Creature("Moldblody", health = 94, strength = 118, speed = 100, attacks = [scratch, leech, bloodlust], starter = True)
nethertooth = Creature("NetherTooth", health = 102, strength = 105, speed = 83, attacks = [destroy, flash, heal], starter = True)
spritebrute = Creature("SpriteBrute", health = 99 ,strength = 96, speed = 80, attacks = [crush, howl, nourish], starter = True)
soulbrood = Creature("SoulBrood", health = 98, strength = 116, speed = 86, attacks = [leech, crush, nourish])
dreadfiend = Creature("Dreadfiend", health = 86, strength = 113, speed = 94, attacks = [flash, destroy, nourish])
steamghoul = Creature("SteamGhoul", health = 94, strength = 98, speed = 81, attacks = [heal, destroy, bloodlust])
rotkat = Creature("Rotkat", health = 118, strength = 97, speed = 87, attacks = [heal, howl, scratch])
soilsnare = Creature("SoilSnare", health = 89, strength = 96, speed = 91, attacks = [bloodlust, leech, crush])
terrortree = Creature("TerrorTree", health = 104, strength = 90, speed = 82, attacks = [flash, leech, crush])
tanglehag = Creature("Tanglehag", health = 114, strength = 112, speed = 99, attacks = [bloodlust, scratch, nourish])
corpsewraith = Creature("CorpseWraith", health = 116, strength = 93, speed = 92, attacks = [flash, heal, scratch])

#Tuple of the creatures and list of attack and creature names
list_of_creatures = (moldblody, nethertooth, spritebrute, soulbrood, dreadfiend, steamghoul, rotkat, soilsnare, terrortree, tanglehag, corpsewraith)
list_of_attack_names = [attack.name for attack in list_of_attacks]
list_of_creature_names = [creature.name for creature in list_of_creatures]
list_of_uncaptured_creatures = list(list_of_creatures)




class Trainer:
  def __init__(self, name, heal_potions = 5):
    self.name = name
    self.creatures = []
    self.heal_potions = heal_potions

in_between = "---------=+=---------"

def creature_choice():
  creature_choice_input = input("Hello {trainer_name} welcome to Crea. You need to choose your starter creature. You can choose between: Moldblody, NetherTooth and SpriteBrute. Their stats are stated below. To choose a creature, type the creatures name.\n{starter1}\n{starter2}\n{starter3}\n:".format(trainer_name = trainer_name, starter1 = starters[0], starter2 = starters[1], starter3 = starters[2]))
  creature_choice_l = creature_choice_input.lower()
  check_for_quit(creature_choice_l)
  if creature_choice_l == "moldblody":
    trainer_one.creatures.append(moldblody)
    list_of_uncaptured_creatures.remove(moldblody)
  elif creature_choice_l == "nethertooth":
    trainer_one.creatures.append(nethertooth)
    list_of_uncaptured_creatures.remove(nethertooth)
  elif creature_choice_l == "spritebrute":
    trainer_one.creatures.append(spritebrute)
    list_of_uncaptured_creatures.remove(spritebrute)
  else:
    om.reset_text(creature_choice)

def fighting():
  enemy = random.choice(list_of_uncaptured_creatures)
  own_creature = random.choice(trainer_one.creatures)
  print(in_between)
  print("You will be fighting the {enemy_name}, his stats are below.".format(enemy_name = enemy.name)), 
  print(enemy)
  
  print(in_between)
  print("{own_creature} wants to fight, his stats are below.".format(own_creature = own_creature.name))
  print(own_creature)
  continue_txt = input("Press ENTER to start the fight!\n:")
  check_for_quit(continue_txt.lower())
  os.system("clear")
  counter = 1
  while enemy.health > 0:

    print("----------------(=ROUND {counter}=)----------------".format(counter = counter))
    if own_creature.speed > enemy.speed:
      own_move = random.choice(own_creature.attacks)
      enemy_move = random.choice(enemy.attacks)
      own_move.attack(own_creature, enemy)
      enemy_move.attack(enemy, own_creature)
      print("{own_creature} is using {move}".format(own_creature = own_creature.name, move = own_move.name))
      print("{enemy} is using {move}".format(enemy = enemy.name, move = enemy_move.name))
      print("The stats of the creatures are : \n{own_creature_stats}\n{enemy_stats}".format(own_creature_stats = own_creature.stats(), enemy_stats = enemy.stats()))
      print(in_between)

    elif enemy.speed > own_creature.speed:
      own_move = random.choice(own_creature.attacks)
      enemy_move = random.choice(enemy.attacks)
      enemy_move.attack(enemy, own_creature)
      own_move.attack(own_creature, enemy)
      print("{enemy} is using {move}".format(enemy = enemy.name, move = enemy_move.name))
      print("{own_creature} is using {move}".format(own_creature = own_creature.name, move = own_move.name))
      print("The stats of the creatures are: \n{enemy_stats}\n{own_creature_stats}".format(own_creature_stats = own_creature.stats(), enemy_stats = enemy.stats()))
      print(in_between)

    if own_creature.health <= 0:
      heal_input = input("Do you want to revive the creature with a health potion? (Yes/No)\nYou have {health_pots} health potions left \nAnd your remaining creatures are: {tamed_creatures}\n:".format(health_pots = trainer_one.heal_potions, tamed_creatures = [creature.name for creature in trainer_one.creatures]))
      check_for_quit(heal_input.lower())
      while heal_input.lower() not in ("yes", "no"):
        print(in_between)
        print("ERROR : Invalid input")
        input("PRESS ENTER TO CONTINUE\n:")
        os.system("clear")
        print(in_between)
        heal_input = input("Do you want to revive the creature with a health potion? (Yes/No)\nYou have {health_pots} health potions left \nAnd your remaining creatures are: {tamed_creatures}\n:".format(health_pots = trainer_one.heal_potions, tamed_creatures = [creature.name for creature in trainer_one.creatures]))
        check_for_quit(heal_input.lower())
      if heal_input.lower() == "yes":
        own_creature.use_heal_pot()
        print("Your creature has been healed")
      elif heal_input.lower() == "no":
        trainer_one.creatures.remove(own_creature)
        if len(trainer_one.creatures) > 0:
          own_creature = random.choice(trainer_one.creatures)
        else:
          sys.exit(game + over)
    continue_text = input("Press ENTER to move onto the next round.\n:")
    check_for_quit(continue_text.lower())
    os.system("clear")
    counter += 1
  print(in_between)
  print("{own_creature} has leveld up! all his stats have been increased by 120%!".format(own_creature = own_creature.name))
  own_creature.original_health = int(own_creature.original_health * 1.2)
  own_creature.original_speed = int(own_creature.original_speed * 1.2)
  own_creature.original_strength = int(own_creature.original_strength * 1.2)
  reset_creatures_stats()

    



#Game starts here
os.system("clear")
print(crea)
print(in_between)
trainer_name = input("Hello welcome to the game Crea. The purpose of this game is to tame all the creatures by killing them. You can quit the game at any time by typing quit. You are the chosen creature trainer, what would you like your name to be?\n:")
trainer_one = Trainer(trainer_name)
check_for_quit(trainer_name.lower())
os.system("clear")
print(in_between)
creature_choice()
os.system("clear")
while len(list_of_uncaptured_creatures) > 0:
  fighting()
  print("You must still catch {creatures_list}".format(creatures_list = [creature.name for creature in list_of_uncaptured_creatures]))
  continue_input = input("Press ENTER to move onto the next creature.\n:")
  check_for_quit(continue_input)
  os.system("clear")
else:
  print("Congratulations you finished \n{crea}".format(crea = crea))
