# rpi hackathon fall 14 submission, Team Gofer Win
#
# edited by jnharton for readability and Python 3 compatibility?
import random

play = True

while play:
    go_on = True

    print('\nWhat class would you like to be? We currently support:')
    print('Sorcerer (Stats:15 Int, 7 Str, 8 Char, 12 Wis, 9 Dex, 9 Vit) \n'
          'Warrior (Stats:6 Int, 14 Str, 11 Char, 7 Wis, 10 Dex, 13 Vit) \n'
          'Rogue (Stats:8 Int, 8 Str, 12 Char, 10 Wis, 13 Dex, 9 Vit)')
    print("")

    inventory = []
    rpg_class = input('Please input your choice: ').lower()

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
            if rpg_class == 'rogue' and random.randint(1, 2) == 1:
                inventory.append('gauntlet')
                entry = input("What next? ")
            else:
                print('Guards rush out of nowhere and proceed to stab you to death'
                      '\n for your crimes against the kingdom.')
                go_on = False
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