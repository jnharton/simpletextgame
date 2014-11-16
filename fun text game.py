#rpi hackathon fall 14 submission, Team Gofer Win
import random
play=True
while play:
    go_on=True
    print "\nWhat class would you like to be? We currently support:"
    print "Sorcerer (Stats:15 Int, 7 Str, 8 Char, 12 Wis, 9 Dex, 9 Vit) \n",\
          "Warrior (Stats:6 Int, 14 Str, 11 Char, 7 Wis, 10 Dex, 13 Vit) \n",\
          "Rogue (Stats:8 Int, 8 Str, 12 Char, 10 Wis, 13 Dex, 9 Vit)"
    print
    rpgclass=raw_input('Please input your choice: ').lower()
    #sets starting gear
    if rpgclass=='sorcerer':
        inventory=['staff','book','robes','ingredients bag',20]
    elif rpgclass=='warrior':
        inventory=['sword','shield','armor','flask',25]
    elif rpgclass=='rogue':
        inventory=['dagger','dagger','cloak','',50]
    else:
        print "you are an npc in this world and die immediately because of bears..."\
              "and I don't mean they attack and kill you...simply their existence"\
              "causes you to die of fear"
        go_on=False
    
    if go_on:
        doors=random.randint(1,4)
        print 'you are in a room with %s doors' %(doors)
        print
        entry=raw_input("which one do you enter?(1-%s) "%(doors))
        print 'you are now in a large, but empty audience hall.\nThere are many items '\
              'lying around'
        print
        
        if rpgclass=='rogue':
            print "there is a fairly valuable looking gauntlet on the front table, \n"\
                  'it might fetch quite a nice price on the market'
            print
        
        entry=raw_input("What do you do? ")
        
        if entry=='steal':
            if rpgclass=='rogue' and random.randint(1,2)==1:
                inventory.append('gauntlet')
                entry=raw_input("What next? ")
            else:
                print "Guards rush out of nowhere and proceed to stab you to death"\
                      '\n for you crimes against the kingdom'
                go_on=False
        elif entry=='explore':
            print "You notice eyes staring at you out of many crevices and are glad\n"\
                "that you did not do anything foolish. You also notice a back door"
            print
            entry=raw_input("Do you run for the door or stay where you are? ")
            if entry=='stay':
                "the eyes form into soldiers who come out and murder you"
                go_on=False
        else:
            print 'you awkwardly stand around for 30 minutes until a man walks in.'
            print 'he slowly walks over to you and proceeds to slit your throat.\n'\
                  'Congratulations! You died due to indiference. that\'s...not common'
            go_on=False
        
    if go_on:
        print "As you pass through the door, it shuts behind you."
        if rpgclass=='rogue':
            print 'you attempt to open the door but there is no keyhole to pick,\n'\
                  'no bolt to budge, it has been magically sealed!!!'
        elif rpgclass=='sorcerer':
            print 'you sense a dark aura in the room and a rite of sealing on the door'
            entry=raw_input('do you try to dispel the seal on the door? y/n: ')
            if entry=='y':
                "while you attempt to open the door, you feel an instant of searing\n'\
                'pain as you are burned to a crisp."
                go_on=False
    if go_on:
        print "you are greeted with a large red dragon. It seems a bit peeved."
        print
        entry=raw_input("What do you say? ")
        if rpgclass=='sorcerer':
            print 'You befriend the dragon and have a useful ally in the future.'
        else:
            print 'the dragon ignores your words and eats you in one gulp.\n'\
                  'You slowly die in it\'s digestive tract over the next few days'
    print
    play=raw_input('do you wish to play again? ').lower()
    if play=='y' or play=='yes' or play=='':
        play=True
    else:
        break