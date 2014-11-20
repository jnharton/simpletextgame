# rpi hackathon fall 14 submission, Team Gofer Win
#
# edited by jnharton for readability and Python 3 compatibility?
# expanded on by jnharton
import random
import time

valid_actions = {
    'rogue':    ['backstab', 'search', 'sneak', 'hide', 'pick'],
    'sorcerer': ['cast', 'sense aura', 'reason'],
    'warrior':  ['attack', 'block'],
    'all':      ['explore']
}

default_stats = {
    'rogue':    {'str': 8,  'dex': 13, 'vit': 9,  'int': 8,  'cha': 12, 'wis': 10},
    'sorcerer': {'str': 7,  'dex': 9,  'vit': 9,  'int': 15, 'cha': 8,  'wis': 12},
    'warrior':  {'str': 14, 'dex': 10, 'vit': 13, 'int': 6,  'cha': 11, 'wis': 7},
}

items = ['golden chalice', 'ruby studded crown', 'gleaming shield', 'gilt handled dagger']

gauntlet_taken = False
guards_alerted = False

play = True

while play:
    go_on = True

    print('\nWhat class would you like to be? We currently support:')
    print('Sorcerer (Stats: 15 Int,  7 Str,  8 Cha, 12 Wis,  9 Dex,  9 Vit) \n'
          'Warrior  (Stats:  6 Int, 14 Str, 11 Cha,  7 Wis, 10 Dex, 13 Vit) \n'
          'Rogue    (Stats:  8 Int,  8 Str, 12 Cha, 10 Wis, 13 Dex,  9 Vit)')
    print("")

    inventory = []
    rpg_class = input('Please input your choice: ').lower()

    # set stats
    #stats = default_stats[rpg_class]
    stats = default_stats.get(rpg_class)

    # 'randomize'
    stats['str'] = random.randint(stats['str'] - 2, stats['str'] + 2)
    stats['dex'] = random.randint(stats['dex'] - 2, stats['dex'] + 2)
    stats['vit'] = random.randint(stats['vit'] - 2, stats['vit'] + 2)
    stats['int'] = random.randint(stats['int'] - 2, stats['int'] + 2)
    stats['cha'] = random.randint(stats['cha'] - 2, stats['cha'] + 2)
    stats['wis'] = random.randint(stats['wis'] - 2, stats['wis'] + 2)

    # sets starting gear
    if rpg_class == 'sorcerer':
        inventory = ['staff', 'book', 'robes', 'ingredients bag', 20]
    elif rpg_class == 'warrior':
        inventory = ['sword', 'shield', 'armor', 'flask', 25]
    elif rpg_class == 'rogue':
        inventory = ['dagger', 'dagger', 'cloak', '', 50]
    else:
        print('You are an npc in this world and die immediately because of bears...'
              'and I don\'t mean they attack and kill you...simply their existence'
              'causes you to die of fear')
        go_on = False

    # begin your adventure
    if go_on:
        #stage = 1
        doors = random.randint(1, 4)

        print('You are in a room with %s doors' %(doors))
        print('')

        entry = input('Which one do you enter?(1-%s) ' %(doors))

        print('You are now in a large, but empty audience hall.\n'
              'There are many items lying around.')
        print('')
        
        if rpg_class == 'rogue':
            print('There is a fairly valuable looking gauntlet on the front table, \n'
                  'it might fetch quite a nice price on the market.')
            print('')
        
        entry = input('What do you do? ')

        if entry == 'steal':
            #if rpg_class == 'rogue' and random.randint(1, 2) == 1:
            if rpg_class == 'rogue' and guards_alerted is False:
                    print('entry: ' + '\'' + str(entry) + '\'')

                    inv_size = len(inventory)
                    max_inv = len(inventory) + len(items)

                    while entry == 'steal':
                        test = random.randint(12, 14)
                        #test = 12

                        print('test: ' + str(test))
                        print('dex:  ' + str(stats['dex']))

                        if stats['dex'] >= test:
                            if gauntlet_taken is False:
                                inventory.append('gauntlet')
                                print('You take the gauntlet.')
                                gauntlet_taken = True
                            else:
                                if len(items) > 0:
                                    if len(inventory) < max_inv:
                                        item = random.randint(0, len(items) - 1)
                                        inventory.append(items.pop(item))
                                        print('You help yourself to another piece of treasure')
                                    else:
                                        dropped = items.append(inventory.pop())
                                        print('In your greed, you drop something.')

                                        treasure = ['golden chalice', 'ruby studded crown', 'gleaming shield', 'gilt handled dagger']

                                        if dropped in treasure:
                                            print(str(dropped) + ' clatters noisily to the ground...')
                                            guard_alerted = True
                                        else:
                                            print('Phew, that was close. At least that didn\'t make much noise.')
                                else:
                                    print('That\'s quite a haul. You figure you can make it out safely if you '
                                          'don\'t take anything else.')
                        elif stats['dex'] < test:
                            guards_alerted = True

                        entry = input("What next? ")

                    if guards_alerted is True:
                        print('A voice in the distance cries: \'Thief!\'')
                        print('Guards rush out of nowhere to surround you, \n'
                              'then they summarily execute you (by beheading of course), \n'
                              'but not before the chop off each of your hands and feet')
                        go_on = False
            else:
                print('Guards rush out of nowhere and proceed to stab you to death'
                      '\n for your crimes against the kingdom.')
                go_on = False
        elif entry == 'look':
            entry1 = input('Look at what? ')

            if entry1 == 'items':
                print('You see many interesting items, \n'
                      'the gauntlet laying on the table nearby catches your eye.')
                print('')

                time.sleep(3)

                print('Caught up in examining the gauntlet, you are oblivious to\n'
                      'the guards standing behind you. All of a sudden you see stars, \n'
                      'then nothing.')
                go_on = False
            else:
                print('You don\'t see that.')
        elif entry == 'explore':
            print('You notice eyes staring at you out of many crevices and are glad\n'
                  'that you did not do anything foolish. You also notice a back door.')
            print('')

            entry = input("Do you run for the door or stay where you are? ")

            if entry == 'stay':
                'The eyes form into soldiers who come out and murder you.'
                go_on = False
        else:
            print('You awkwardly stand around for 30 minutes until a man walks in.')
            print('He slowly walks over to you and proceeds to slit your throat.\n'
                  'Congratulations! You died due to indifference. that\'s...not common')
            go_on = False

    if go_on:
        doors = 2

        print('You are in a room with %s doors' %(doors))
        print('')

        while int(entry) != 1 and int(entry) != 2:
            entry = input('Which one do you enter?(1-%s) ' %(doors))

            door_chosen = int(entry)

    if go_on and door_chosen == 1:

        print('Considering the footprints you have left in the dust and the musty air, you surmise this room has not been used in quite a while.')



    if go_on and door_chosen == 2:
        print('As you pass through the door, it shuts behind you.')

        if rpg_class == 'rogue':
            print('You attempt to open the door but there is no keyhole to pick,\n'
                  'no bolt to budge, it has been magically sealed!!!')
        elif rpg_class == 'sorcerer':
            print('You sense a dark aura in the room and a rite of sealing on the door.')

            entry = input('Do you try to dispel the seal on the door? y/n: ')

            if entry == 'y':
                'While you attempt to open the door, you feel an instant of searing\n'\
                'pain as you are burned to a crisp.'
                go_on = False

    if go_on:
        print('You are greeted with a large red dragon. It seems a bit peeved.')
        print('')

        entry = input("What do you say? ")

        if rpg_class == 'sorcerer':
            print('You befriend the dragon and have a useful ally in the future.')
        else:
            print('The dragon ignores your words and eats you in one gulp.\n'
                  'You slowly die in it\'s digestive tract over the next few days')

        go_on = False

    print('')

    play = False

    keep_playing = input('Do you wish to play again? ').lower()

    if keep_playing == 'y' or keep_playing == 'yes' or keep_playing == '':
        play = True