from classes.game import Person, Bcolors
import random

spells = [{
    'name': 'Fireball',
    'cost': 20,
    'damage': 50
}, {
    'name': 'Ice shard',
    'cost': 10,
    'damage': 30
}, {
    'name': 'Gust',
    'cost': 5,
    'damage': 10
}, {
    'name': 'Heal',
    'cost': 15,
    'damage': 40
}]

player = Person(200, 70, 50, 30, 30)
print('You encounter an enemy!')
action = input('Choose an action: Attack | Spells: ')

if action == 'Attack' or action == 'attack':
    print('You dealt', player.physical_dmg(), 'in damage!')

if action == 'spells' or action == 'Spells':
    for spell in spells:
        print('Choose a spell to cast: ')
        print(spell['name'])
        selected_spell = input()
        print('You cast ', selected_spell, '!')
