import itertools

class Character:
  def __init__(self, hp, armor, damage, mana):
    self.hp = hp
    self.armor = armor
    self.damage = damage
    self.mana = mana

class InstantEffect:
  def __init__(self, damage, heal):
    self.damage = damage
    self.heal = heal

  def perform(self, player, boss):
    player.hp += self.heal
    boss.hp -= self.damage

class Effect:
  def __init__(self, name, turns, armor_boost, damage, mana_heal):
    self.name = name
    self.mana_heal = mana_heal
    self.damage = damage
    self.armor_boost = armor_boost
    self.turns = turns
    self.total_turns = turns

  def reset(self):
    return Effect(self.name, self.total_turns, self.armor_boost, self.damage, self.mana_heal)

  def __eq__(self, other):
    return other and self.name == other.name

  def __ne__(self, other):
    return not self.__eq__(other)

  def __hash__(self):
      return hash(self.name)

  def use(self, player, boss):
    if self.turns == self.total_turns:
      player.armor += self.armor_boost
    boss.hp -= self.damage
    player.mana += self.mana_heal
    self.turns -= 1
    if self.turns == 0:
      player.armor -= self.armor_boost

EMPTY_EFFECT = Effect(-1, 0, 0, 0, 0)

class Spell:
  def __init__(self, name, mana, effect, instant_effect):
    self.name = name
    self.mana = mana
    self.effect = effect
    self.instant_effect = instant_effect

  def cast_spell(self, player, boss, effects):
    player.mana -= self.mana
    if player.mana < 0 or self.effect in effects:
      return False
    if self.instant_effect is not None:
      #print "Instant Effect: %s" % self.name
      self.instant_effect.perform(player, boss)
    if self.effect != EMPTY_EFFECT:
      #print "Casting: %s" % self.name
      effects.add(self.effect)
    return True

def total_mana(spells):
    return sum([sp.mana for sp in spells])

def use_effects(effects, player, boss):
    for effect in effects:
      effect.use(player, boss)
    return set([e for e in effects if e.turns > 0])


def simulate_battle(spell_order):
  spell_order = [Spell(s.name, s.mana, s.effect.reset(), s.instant_effect) for s in spell_order]
  boss = Character(55, 0, 8, 0)
  player = Character(50, 0, 0, 500)

  effects = set()
  for sp in xrange(len(spell_order)):
    if player.hp <= 0:
      return -3
    effects = use_effects(effects, player, boss)
    if boss.hp <= 0:
      return total_mana(spell_order[:sp])
    if not spell_order[sp].cast_spell(player, boss, effects):
      return -2
    effects = use_effects(effects, player, boss)
    if boss.hp <= 0:
      return total_mana(spell_order[:sp+1])
    player.hp -= max(1, boss.damage - player.armor)
    if player.hp <= 0:
      return -3
  return -1

# Magic Missile costs 53 mana. It instant_effectntly does 4 damage.
# Drain costs 73 mana. It instant_effectntly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
spells = [
  Spell('Magic Missile', 53, EMPTY_EFFECT, InstantEffect(4, 0)),
  Spell('Drain', 73, EMPTY_EFFECT, InstantEffect(2, 2)),
  Spell('Shield', 113, Effect(1, 6, 7, 0, 0), None),
  Spell('Poison', 173, Effect(2, 6, 0, 3, 0), None),
  Spell('Recharge', 229, Effect(3, 5, 0, 0, 101), None)
]

min_spells = 9
max_spells = 10
min_mana_cost = -1
for i in range(min_spells,max_spells):
  min_mana_cost = -1
  spell_perms = itertools.product(spells, repeat=i)
  for spell_tuple in spell_perms:
    spells_to_cast = []
    for spell in spell_tuple:
      spells_to_cast.append(spell)
    battle_result = simulate_battle(spells_to_cast)
    if battle_result == -1 or battle_result == -2 or battle_result == -3:
      continue
    if min_mana_cost == -1 or battle_result < min_mana_cost:
      min_mana_cost = battle_result
      print "Min candidate: "
      for spell in spells_to_cast:
        print spell.name
  if min_mana_cost != -1:
    break
print min_mana_cost
