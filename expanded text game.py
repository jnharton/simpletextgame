# rpi hackathon fall 14 submission, Team Gofer Win
#
# edited by jnharton for readability and Python 3 compatibility?
# expanded on by jnharton
import random
import time

# data
classes = ['rogue', 'sorcerer', 'warrior']

''' unused '''
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

'''
# conditions
gauntlet_taken = False
guards_alerted = False
have_light = False
found_trapdoor = False
'''

play = True
skip = False  # if True, skip the next stage that checks (we should reset this any time a skip occurs because of it

while play:
    go_on = True

    # starting conditions
    gauntlet_taken = False
    guards_alerted = False
    have_light = False

    executed_by_guards = False
    killed_by_dragon = False
    found_trapdoor = False
    befriend_dragon = False

    print('\nWhat class would you like to be? We currently support:')
    print('Sorcerer (Stats: 15 Int,  7 Str,  8 Cha, 12 Wis,  9 Dex,  9 Vit) \n'
          'Warrior  (Stats:  6 Int, 14 Str, 11 Cha,  7 Wis, 10 Dex, 13 Vit) \n'
          'Rogue    (Stats:  8 Int,  8 Str, 12 Cha, 10 Wis, 13 Dex,  9 Vit)')
    print("")

    inventory = []
    rpg_class = input('Please input your choice: ').lower()

    print('')

    if rpg_class not in classes:
        print('You are an npc in this world and die immediately because of bears... '
              'and I don\'t mean they attack and kill you... the simple fact of their existence '
              'causes you to die of fear')
        go_on = False

    # player data initialization - based on class choice
    if go_on:
        # set stats
        stats = default_stats[rpg_class]

        # 'randomize' stats around default values
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
            inventory = ['dagger', 'dagger', 'cloak', 'unlit torch', 'flint and steel', 50]

        # tell the player what's in their inventory
        print('You have:')

        for item in inventory:
            print(item)

        print('')

    # begin your adventure
    if go_on:
        doors = random.randint(1, 4)

        print('You are in a room with %s doors' % doors)
        print('')

        while door_chosen not in range(1, doors + 1):
            entry = input('Which one do you enter?(1-%s) ' % doors)

            try:
                door_chosen = int(entry)
            except TypeError:
                print('TypeError: Not an Integer.')
                door_chosen = 0
                continue

    # audience hall
    if go_on:
        print('You are now in a large, but empty audience hall.\n'
              'There are many items lying around.')
        print('')
        
        if rpg_class == 'rogue':
            print('There is a fairly valuable looking gauntlet on the front table, \n'
                  'it might fetch quite a nice price on the market.')
            print('')
        else:
            # TODO find a way to make this work without breaking the game
            guards_alerted = True
        
        entry = input('What do you do? ')

        # risk danger for loot
        if entry == 'steal':
            # TODO should I be checking guards alerted here or after the rogue test
            # TODO should I tell the player if they are thinking about stealing and the guards are alert?

            #if rpg_class == 'rogue' and random.randint(1, 2) == 1:
            if rpg_class == 'rogue' and guards_alerted is False:
                # TODO find a way to make classes have variable max inventory
                inv_size = len(inventory)
                max_inv = len(inventory) + len(items)

                while entry == 'steal':
                    # TODO tweak this random number setup to ensure a certain likelihood of successes/failures
                    test = random.randint(11, 14)
                    #test = 12

                    # stealing: dexterity test (if you fail the guards will be alerted)
                    if stats['dex'] >= test:
                        if gauntlet_taken is False:
                            inventory.append('gauntlet')
                            print('You take the gauntlet.')
                            gauntlet_taken = True
                        else:
                            if len(items) > 0:
                                if inv_size < max_inv:
                                    item = random.randint(0, len(items) - 1)
                                    inventory.append(items.pop(item))
                                    print('You help yourself to another piece of treasure')
                                else:
                                    # TODO randomize the dropped item
                                    item = random.randint(0, len(inventory) - 1)
                                    dropped = items.append(inventory.pop(item))
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
                          'but not before they chop off each of your hands and feet')
                    executed_by_guards = True
                    go_on = False
            else:
                # implied that anyone but a rogue would be a very noisy thief
                # (if you aren't a rogue the guards we're already alert)
                print('Guards rush out of nowhere and proceed to stab you to death'
                      '\n for your crimes against the kingdom.')
                executed_by_guards = True
                go_on = False
        elif entry == 'look':
            # TODO expand with loop to give you a chance to look at the gauntlet too
            entry1 = input('Look at what? ')

            if entry1 == 'items':
                print('You see many interesting items, \n'
                      'the gauntlet laying on the table nearby catches your eye.')
                print('')

                entry1 = input('Look at the gauntlet? ')

                if entry1 == 'y':
                    entry1 = 'gauntlet'
            elif entry1 == 'gauntlet':
                print('You move closer to examine the gauntlet more closely...')
                print('')

                time.sleep(3)

                print('Caught up in examining the gauntlet, you are oblivious to\n'
                      'the guards standing behind you. All of a sudden you see stars, \n'
                      'then nothing.')
                executed_by_guards = True
                go_on = False
            else:
                print('You don\'t see that.')

            entry = input("What next? ")
        elif entry == 'explore':
            # TODO should this be changed, since the other text implies that the guards are watching, perhaps randomize guard alertness
            print('You notice eyes staring at you out of many crevices and are glad\n'
                  'that you did not do anything foolish. You also notice a back door.')
            print('')

            entry = input("Do you run for the door or stay where you are? ")

            if entry == 'stay':
                'The eyes form into soldiers who come out and murder you.'
                executed_by_guards = True
                go_on = False
            elif entry == 'run':
                # TODO fix kludge in that the step I added takes the excitement out of running away
                print('You run headlong through the back door and keep going...')
                skip = True
                door_chosen = 3

        else:
            print('You awkwardly stand around for 30 minutes until a man walks in.')
            print('He slowly walks over to you and proceeds to slit your throat.\n'
                  'Congratulations! You died due to indifference. that\'s...not common')
            go_on = False

    if go_on and skip is False:
        doors = 3

        print('You are in a hallway with %s doors, one leading back, one to your left, and ahead of you' %(doors))
        print('')

        door_chosen = 0

        while door_chosen not in range(1, doors + 1):
            entry = input('Which one do you enter?(1-%s) ' %(doors))

            try:
                door_chosen = int(entry)
            except TypeError:
                print('TypeError: Not an Integer.')
                door_chosen = 0
                continue

        if door_chosen == 1:
            print('You return to the room you left, not the wisest choice all things considered...')
            print('')
            print('The eyes, from before, form into soldiers who come out and murder you.')
            executed_by_guards = True
            go_on = False

    skip = False

    # sort of a light puzzle
    if go_on and door_chosen == 2:
        print('Considering the footprints you have left in the dust and the musty air, \n'
              'you surmise this room has not been used in quite a while. It\'s also quite '
              'dark, excluding the sliver of light coming in through the open door')

        # There will be an opportunity to leave this place by another route through this 'room
        # hints will be supplied to each class so as to enable the player by curiosity or intelligence
        # to discover the alternate exit.
        #
        # If you take too long the guards will come and check. If you haven't escaped they will
        # kill you (after all, they were expecting you to find the dragon and, presumably, your death)
        #
        # Escaping this way is deemed a 'win' condition.

        # TODO write hints below and add the necessary game logic for the described features

        # any class can acquire a lit torch in the hallway, if they notice it (which will help enormously)
        if rpg_class == 'rogue':
            # use flint and steel and your unlit torch, then employ search to find the trapdoor
            print('rogue hint')
            print('It is pretty dark in here. Perhaps your \'flint and steel\' may be of some use \n'
                  'You still have that unlit torch you brought with you, right?')
        elif rpg_class == 'sorcerer':
            # mention a spell that could be used (light? detect doors?) which will improve odds of exploring,
            # finding the door
            print('sorcerer hint')
        elif rpg_class == 'warrior':
            # reference sounds (success through blind exploration, random chance to trip)
            print('warrior hint')

        entry = input('What do you do? ')

        # check entries (generic and class specific)
        # need a leave option that tries the other door (changes door_chosen to 3)
        # should there be a limited number of chances to explore before you are forced to go elsewhere

        if rpg_class == 'rogue' and entry == 'light torch':
            if 'flint and steel' in inventory and 'unlit torch' in inventory:
                print('With some difficulty, you strike the flint and steel against each other \n'
                      'and manage to light the torch')
                have_light = True
            else:
                if 'flint and steel' in inventory:
                    print('Drat, you must have misplaced that \'unlit torch\' somewhere.')
                elif 'unlit torch' in inventory:
                    print('Drat, you must have misplaced your \'flint and steel\' somewhere.')

                print('It\'s pretty useless to scrape around in the dark, so you leave and try the other door.')

                door_chosen = 3
        elif rpg_class == 'sorcerer':
            print('')
            door_chosen = 3
        elif rpg_class == 'warrior':
            print('')
            door_chosen = 3

        if have_light is True:
            print('Well now you can see better, that\'s for sure')

            entry = input('What do you do? ')

            if entry == 'explore':
                count = 3

                while count > 0 and found_trapdoor is False:
                    entry1 = input('Continue exploring (y/n)? ')

                    if entry1 == 'y':
                        count -= 1

                        print('You explore the room, searching for anything of interest.')
                        temp = random.randint(0, 2)

                        found_trapdoor = ([True, False, False])[temp]
                    else:
                        print('You tire of exploring.')
                        break

                if found_trapdoor is True:
                    print('Aha, you found a trapdoor and it appears it may lead out of this place.')
                    go_on = False
                else:
                    print('You tire of exploring and opt to leave')
                    entry = 'leave'

            if entry == 'leave':
                if rpg_class == 'rogue':
                    print('Disappointed by the lack of removable items of value, you leave and try the other door')
                elif rpg_class == 'sorcerer':
                    print('The decor certainly was delightful, but you found nothing of interest. In fact everything \n'
                          'in there was decidedly un-magical if you don\'t count the preservation spells. Bored, you \n'
                          'leave to try the other door.')
                elif rpg_class == 'warrior':
                    print('A dusty room, what joy... or not. Sighing at the lack of a need for action, you leave \n'
                          'hoping whatever is behind door number two is more exciting.')

                door_chosen = 3
        else:
            print('message about the darkness')
            door_chosen = 3

    if go_on and door_chosen == 3:
        print('As you pass through the door, it shuts behind you.')
        print('')

        if rpg_class == 'rogue':
            print('You attempt to open the door but there is no keyhole to pick,\n'
                  'no bolt to budge, it has been magically sealed!!!')
            print('')
        elif rpg_class == 'sorcerer':
            print('You sense a dark aura in the room and a rite of sealing on the door.')
            print('')

            entry = input('Do you try to dispel the seal on the door? y/n: ')

            if entry == 'y':
                'While you attempt to open the door, you feel an instant of searing\n'\
                'pain as you are burned to a crisp.'
                go_on = False

    if go_on and door_chosen == 3:
        print('You are greeted with a large red dragon. It seems a bit peeved.')
        print('')

        # include some output about thieves (rogue) and stolen items (if the player is carrying stolen treasure),
        # otherwise about the foolishness of dragon slayers (warrior)

        entry = input("What do you say? ")

        if rpg_class == 'sorcerer':
            print('You befriend the dragon and have a useful ally in the future.')
        else:
            print('The dragon ignores your words and eats you in one gulp.\n'
                  'You slowly die in it\'s digestive tract over the next few days')

        go_on = False

    print('')

    # end game
    play = False

    # TODO fix this to have a more appropriate end message if the guards caught you stealing and executed you
    # print end game message
    if executed_by_guards is True:
        if rpg_class == 'rogue':
            print('rogue lose message')
        elif rpg_class == 'sorcerer':
            print('sorcerer lose message')
        elif rpg_class == 'warrior':
            print('warrior lose message')

        print('')
        print('You Lost')
    elif killed_by_dragon is True:
        if rpg_class == 'rogue':
            print('Death by being eaten by a dragon, an ignoble end if there ever was one \n'
                  'and well deserved for your thieving ways!')
        elif rpg_class == 'warrior':
            print('warrior lose message')

        print('')
        print('You Lost')
    elif found_trapdoor is True:
        if rpg_class == 'rogue':
            print('You found a way out and escaped with your stolen loot.')
        elif rpg_class == 'sorcerer':
            print('sorcerer win message')
        elif rpg_class == 'warrior':
            print('warrior win message')

        print('You Won!')
    elif befriend_dragon is True:
        # pointless check, since no one else can achieve this
        if rpg_class == 'sorcerer':
            print('sorcerer win message')

        print('You Won!')

    print('')

    # TODO move score calculation into a separate function?
    # calculate and print a score
    score = 0

    if rpg_class == 'rogue' and found_trapdoor:
        treasure = ['golden chalice', 'ruby studded crown', 'gleaming shield', 'gilt handled dagger']

        if gauntlet_taken:
            print('gauntlet: 5')
            score += 5

        for item in inventory:
            if item in treasure:
                print(item + ': 5')
                score += 5

    print('')
    print('Score: ' + str(score))
    print('')

    # see if the player would like to play again
    keep_playing = input('Do you wish to play again? ').lower()

    if keep_playing == 'y' or keep_playing == 'yes' or keep_playing == '':
        play = True