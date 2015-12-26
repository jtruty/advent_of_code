import itertools

class Item:
  def __init__(self, cost, damage, armor):
    self.cost = cost
    self.damage = damage
    self.armor = armor

  def __eq__(self, other):
      return other and self.cost == other.cost and self.damage == other.damage and self.armor == other.armor

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
      return hash((self.cost, self.damage, self.armor))

  def __str__(self):
    return "Damage: %s, Armor: %s, Cost: %s" % (self.damage,self.armor,self.cost)

  def __repr__(self):
    return self.__str__()

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3

# Boss Stats
# Hit Points: 109
# Damage: 8
# Armor: 2

weapons = [Item(8,4,0),Item(10,5,0),Item(25,6,0),Item(40,7,0),Item(74,8,0)]
armors = [Item(13,0,1),Item(31,0,2),Item(53,0,3),Item(75,0,4),Item(102,0,5)]
rings = [Item(25,1,0),Item(50,2,0),Item(100,3,0),Item(20,0,1),Item(40,0,2),Item(80,0,3)]

item_sets = set()
# construct item sets
for weapon in weapons:
  item_sets.add(frozenset([weapon]))
  for armor in armors:
    item_sets.add(frozenset([weapon, armor]))
    for ring_set in itertools.combinations(rings, 2):
     for ring in ring_set:
       item_sets.add(frozenset([weapon, armor, ring]))
    for ring in rings:
      item_sets.add(frozenset([weapon, armor, ring]))

for items in item_sets:
  print items

boss_damage = 8
boss_armor = 2
min_cost = 1000
max_losing_cost = 0
# loop over weapons, armor and rings
for item_set in item_sets:
  boss_hp = 109
  player_hp = 100

  player_damage = sum(i.damage for i in item_set)
  player_armor = sum(i.armor for i in item_set)
  cost = sum(i.cost for i in item_set)

  print "Damage: %s, Armor: %s, Cost: %s" % (player_damage,player_armor,cost)


  while True:
    boss_hp -= (player_damage - boss_armor)
    if (boss_hp <= 0):
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
