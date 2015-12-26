import itertools

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

class Spell:
  def __init__(self, mana_cost, mana_heal, damage, armor, heal, turns):
    self.mana_cost = mana_cost
    self.mana_heal = mana_heal
    self.damage = damage
    self.armor = armor
    self.heal = heal
    self.turns = turns

  def __eq__(self, other):
      return other and self.mana_cost == other.mana_cost and self.mana_heal = other.mana_heal and self.damage == other.damage and self.armor == other.armor and self.heal == other.heal and self.turns == other.turns

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
      return hash((self.mana_cost, self.mana_heal, self.damage, self.armor, self.heal, self.turns))

  def __str__(self):
    return "Mana Cost: %s, Mana Heal: %s, Damage: %s, Armor: %s, Cost: %s, Turns: %s" % (self.mana_cost,self.mana_heal,self.damage,self.armor, self.heal,self.turns)

  def __repr__(self):
    return self.__str__()

magic_missile = Spell(53,0,4,0,0,1)
drain = Spell(73,0,2,0,2,1)
shield = Spell(113,0,0,7,0,6)
poison = Spell(173,0,3,0,0,6)
recharge = Spell(229,101,0,0,0,5)

# construct all spell sets
spells = set([magic_missile, drain, shield, poison, recharge])

boss_damage = 8
min_cost = 1000
max_losing_cost = 0

current_spells = set()
win = False
while True:
  if mana < min_mana:
    break
  spell = pick_spell(current_spells)
  boss_hp -= (player_damage - boss_armor)
  if boss_hp <= 0 or mana < 53:
    win=True
    break
  player_hp -= (boss_damage - player_armor)
  if (player_hp <= 0):
    break


  if player_hp > 0:
    print "Player wins!"
    if (cost < min_cost):
      min_cost = cost
  else:
    print "Player loses!"
    if (cost > max_losing_cost):
      max_losing_cost = cost

print "Min winning cost: ", min_cost
print "Max losing cost: ", max_losing_cost
