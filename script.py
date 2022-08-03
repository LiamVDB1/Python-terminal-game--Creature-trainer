import random
list_of_attacks = []
list_of_creatures = []

class Attack:
  def __init__(self, name, damage = 0, heal = 0, strength = 0, speed = 0):
    self.name = name
    self.damage = damage
    self.heal = heal
    self.strength = strength
    self.speed = speed
    list_of_attacks.append(self)
    


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

    

    
    


  

#Adding all the attacks added
scratch = Attack("Scratch", damage = -20)
leech = Attack("Leech", damage = -16, heal = 8)
crush = Attack("Crush", damage = -24)
destroy = Attack("Destroy", damage = -28)
bloodlust = Attack("Bloodlust", strength = 25, heal = -10)
howl = Attack("Howl", strength = 15, heal = -5)
nourish = Attack("Nourish", strength = 5, heal = 15)
heal = Attack("Heal", heal = 25)
flash = Attack("Flash", speed = 50)






class Creature:
  def __init__(self, name, speed, strength, health, attacks, starter = False):
    self.name = name
    self.speed = speed
    self.strength = strength
    self.health = health
    self.attacks = attacks
    self.starter = starter
    list_of_creatures.append(self)


  def __repr__(self):
    attack_names = []
    for attack in self.attacks:
      attack_names.append(attack.name)
    description = "This Creature named {name} has {health} HP, {strength} strength, {speed} speed and the attacks : {attacks}".format(name = self.name, health = self.health, strength = self.strength, speed = self.speed, attacks = attack_names)
    return description
  
  def health_updated(self, amount):
    self.health += amount
    if self.health <= 0:
      print("Creature has been defeated")
      trainer_one.creatures.append(self)
  def strength_updated (self, amount):
    self.strength += amount
  def speed_updated(self, amount):
    self.speed += amount




#Adding all the creatures
moldblody = Creature("Moldblody", health = 94, strength = 118, speed = 100, attacks = [scratch, leech, bloodlust], starter = True)
nethertooth = Creature("NetherTooth", health = 102, strength = 105, speed = 83, attacks = [destroy, flash, heal], starter = True)
spritebrute = Creature("SpriteBrute", health = 99 ,strength = 96, speed = 80, attacks = [crush, howl, nourish], starter = True)
soulbrood = Creature("SoulBrood", health = 98, strength = 116, speed = 86, attacks = [leech, crush, heal])
dreadfiend = Creature("Dreadfiend", health = 86, strength = 113, speed = 94, attacks = [flash, destroy, nourish])
steamghoul = Creature("SteamGhoul", health = 94, strength = 98, speed = 81, attacks = [heal, destroy, bloodlust])
rotkat = Creature("Rotkat", health = 118, strength = 97, speed = 87, attacks = [heal, howl, scratch])
soilsnare = Creature("SoilSnare", health = 89, strength = 96, speed = 91, attacks = [bloodlust, leech, crush])
terrortree = Creature("TerrorTree", health = 104, strength = 90, speed = 83, attacks = [flash, leech, crush])
tanglehag = Creature("Tanglehag", health = 114, strength = 112, speed = 99, attacks = [bloodlust, scratch, nourish])
corpsewraith = Creature("CorpseWraith", health = 116, strength = 93, speed = 92, attacks = [flash, heal, scratch])

#making a list of the attack and creature names
list_of_attack_names = [list_of_attacks[i].name for i in range(len(list_of_attacks))]
list_of_creature_names = [list_of_creatures[i].name for i in range(len(list_of_creatures))]




class Trainer:
  def __init__(self, name):
    self.name = name
    self.creatures = []


print(moldblody,"\n", nethertooth)
leech.attack(moldblody, nethertooth)
print(moldblody, "\n", nethertooth)



""" trainer_name = input("Hello welcome to the game. The purpose of this game is to tame all the creatures by killing them. You are the chosen creature trainer, what would you like your name to be?\n")

trainer_one = Trainer(trainer_name)

creature_choice_input = input("Hello {trainer_name} welcome to the game. You need to choose your starter creature. You can choose between: Moldblody, NetherTooth and SpriteBrute. Their stats are stated below.. To choose a creature, type the creatures name and confirm.\n{moldblody}\n{nethertooth}\n{spritebrute}\n".format(trainer_name = trainer_name, moldblody = moldblody, nethertooth = nethertooth, spritebrute = spritebrute))


if "confirm" in creature_choice_input.lower():
  creature_choice_lst = creature_choice_input.lower().split()
  creature_choice = creature_choice_lst[0]
  if creature_choice == "moldblody":
    trainer_one.creatures.append(moldblody)
  elif creature_choice == "nethertooth":
    trainer_one.creatures.append(nethertooth)
  elif creature_choice == "spritebrute":
    trainer_one.creatures.append(spritebrute)
else:
  print("ERROR : Invalid input")

print() """

