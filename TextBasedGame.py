# Jeremy McNatt
# Chris Decker
# Southern New Hampshire University

import time     # For time.sleep breaks

# Dict for rooms, directions, and items
rooms = {
    'Entryway': {'north': 'Longhall', 'item': None},
    'Longhall': {'north': 'Canals', 'south': 'Entryway', 'east': 'Spillway', 'west': 'Embalming Room',
                 'item': 'Yellow Jewel'},
    'Embalming Room': {'east': 'Longhall', 'item': 'Red Jewel'},
    'Spillway': {'north': 'Forgotten Grotto', 'west': 'Longhall', 'item': 'Blue Jewel'},
    'Forgotten Grotto': {'south': 'Spillway', 'north': 'Descent of Kings', 'west': 'Canals', 'item': 'Ancient Sword'},
    'Canals': {'north': 'Lost Corridor', 'south': 'Longhall', 'east': 'Forgotten Grotto',
               'west': 'Blacksmith Quarters', 'item': 'Green Jewel'},
    'Blacksmith Quarters': {'east': 'Canals', 'item': None},
    'Lost Corridor': {'west': 'Lost Caverns', 'east': 'Descent of Kings', 'south': 'Canals', 'item': 'White Jewel'},
    'Lost Caverns': {'east': 'Lost Corridor', 'item': 'Ancient Armor'},
    'Descent of Kings': {'west': 'Lost Corridor', 'east': 'Hall of the Fathers', 'south': 'Forgotten Grotto',
                         'item': 'Lore Book'},
    'Hall of the Fathers': {'west': 'Descent of Kings', 'item': None}

}

# Extra dict for items, not sure if this is needed but just in case
items = {
    'Entryway': {'item': ['None']},
    'Longhall': {'item': ['Yellow Jewel']},
    'Embalming Room': {'item': ['Red Jewel']},
    'Spillway': {'item': ['Blue Jewel']},
    'Forgotten Grotto': {'item': ['Ancient Sword']},
    'Canals': {'item': ['Green Jewel']},
    'Blacksmith Quarters': {'item': ['None']},
    'Lost Corridor': {'item': ['White Jewel']},
    'Lost Caverns': {'item': ['Ancient Armor']},
    'Descent of Kings': {'item': ['Lore Book']},
    'Hall of the Fathers': {'item': ['None']}
}

# String type variable instructions
user_instruction = ('Welcome to the Ruins of the Fallen Kings. \nFind the items hidden within to aide you in defeating '
                    'the High King.\n'
                    '\nValid commands are North, South, East, West, and Get Item. \n')

# Room scenarios with no items
room_intro_noItem = {
    'Entryway': 'The entrance to the ruins is dank and musty. \nLooks like some animals may have slept here.',
    'Longhall': 'A well decorated room, with a well decorated table throughout the length of it. \nThe center '
                'chandelier makes the chairs just visible.',
    'Embalming Room': 'Stone beds and medical devices. \nSome half mummified bodies are laying about the room.',
    'Spillway': 'Water from the surrounding hills outside seem to funnel here and create some sort of \nriver system '
                'that feeds through the ruins. \nA bridge leads across the water to the north.',
    'Forgotten Grotto': 'Luscious vines and plants strangle the room in a fascinating array.'
                        '\nLight from the roof pours into the center of the room, illuminating a boulder now ridden of '
                        'the sword. \nThe roots and ferns shy away from the boulder.',
    'Canals': 'A run off of water and what smells to be ancient sewage pool here. \nStagnant and repulsive, the '
              'winding passage leads you around an L shaped hall. \nAncient art seems to be carved into the walls.',
    'Blacksmith Quarters': 'Forges and anvils, which have not seen use in some time. '
                           '\nA skeletal figure sits in a chair next to a pedestal with his hand reached out. '
                           '\nLooks like maybe a book goes here, perhaps bringing it back will do something. ',
    'Lost Corridor': 'A lengthy hallway that extends to the east and west. \nSome candles light the way.',
    'Lost Caverns': 'The Lost Corridor breaks off to the west, but through the rubble you find a path in. \nMore '
                    'of a cave system than a room, you see crates and barrels, some still in one piece, and others'
                    ' not so much.',
    'Descent of Kings': 'A massive staircase showcasing portraits of ancient kings leads down deep '
                        'into the ruins. \nEach king seems to be wearing the same helmet, \na frightening '
                        'helm with massive points made of some wierd jewels.',
    'Hall of the Fathers': 'A mighty room fit for a mighty king. It seems some of the ancient kings were not '
                           'buried, \nbut instead were displayed in thrones along the walls of the room. '
                           '\nFour large pillars stand strong before the largest, and most foreboding throne. '
                           '\nThe light seems to wane as you continue further...',
}

# Room scenarios
room_intro = {
    'Entryway': 'The entrance to the ruins is dank and musty. \nLooks like some animals may have slept here.',
    'Longhall': 'A well decorated room, with a well decorated table throughout the length of it. \nThe center '
                'chandelier makes the chairs just visible. A small yellow jewel rests in the headboard of the '
                'tallest chair. '
                '\nYou can see doors at each end of the room.',
    'Embalming Room': 'Stone beds and medical devices. \nSome half mummified bodies are laying about the room.'
                      '\nOne body has a faintly glowing red jewel in the eye socket.',
    'Spillway': 'Water from the surrounding hills outside seem to funnel here and create some sort of \nriver system '
                'that feeds through the ruins. You can see a blue jewel between some rocks where the water all meets.'
                '\nA bridge leads across the water to the north.',
    'Forgotten Grotto': 'Luscious vines and plants strangle the room in a fascinating array.'
                        '\nLight from the roof pours into the center of the room, illuminating a sword stabbed into a '
                        'boulder. \nThe roots and ferns shy away from the boulder.',
    'Canals': 'A run off of water and what smells to be ancient sewage pool here. \nStagnant and repulsive, the '
              'winding passage leads you around an L shaped hall. \nAncient art seems to be carved into the walls, '
              'and a green jewel sits in what looks to be a crocodile mouth.',
    'Blacksmith Quarters': 'Forges and anvils, which have not seen use in some time. '
                           '\nA skeletal figure sits in a chair next to a pedestal with his hand reached out. '
                           '\nLooks like maybe a book goes here, perhaps bringing it back will do something. ',
    'Lost Corridor': 'A lengthy hallway that extends to the east and west. \nSome candles light the way. \nA white '
                     'jewel sits on a chair next to a round table with drawings of an ancient town on them.',
    'Lost Caverns': 'The Lost Corridor breaks off to the west, but through the rubble you find a path in. \nMore '
                    'of a cave system than a room, you see crates and barrels, some still in one piece, and others'
                    ' not so much. \nOn one of the furthest crates rests some pretty solid looking armor. '
                    '\nSome shin guards, bracers, and a whole chest plate. \nThe chest plate seems to have holes '
                    'big enough to fit a jewel of some kind into.',
    'Descent of Kings': 'A massive staircase showcasing portraits of ancient kings leads down deep '
                        'into the ruins. \nEach king seems to be wearing the same helmet, \na frightening '
                        'helm with massive points made of some wierd jewels. \nHalfway down you see a book laying on '
                        'the stairs.',
    'Hall of the Fathers': 'A mighty room fit for a mighty king. It seems some of the ancient kings were not '
                           'buried, \nbut instead were displayed in thrones along the walls of the room. '
                           '\nFour large pillars stand strong before the largest, and most foreboding throne. '
                           '\nThe light seems to wane as you continue further...',
}

current_position_room = 'Entryway'  # Where the player starts

# Intro/Instructions
print('-----------------------------------------------------------------------------------')
print()
print('You cautiously enter the derelict entrance to the Ruins of the Fallen Kings.')
print('The stale air of the Entryway fills your lungs with bated breath.')
print('The High King is rumored to be at the end of these ruins.')
print()
time.sleep(7)
print('-----------------------------------------------------------------------------------')
print()
print('You know the items found in each room will aide you in vanquishing the High King.')
print('Find the Ancient Sword, Ancient Armor, the many Jewels of the ruins. \nUse the Lore Book to fuse the Jewels '
      'into your armor and sword to finish your quest.')
print()
print('-----------------------------------------------------------------------------------')
time.sleep(7)


direction_of_moves = ['north', 'south', 'east', 'west']  # Stores the valid moves

player_inventory = []  # List is going to start empty

villain_room = 'Hall of the Fathers'  # Setting a variable for the villain_room

blacksmith = 'Blacksmith Quarters'  # Setting a variable for the blacksmith room

print(user_instruction)  # Displaying the instruction on the screen
time.sleep(7)


# item_pickup function for 'get item' input
def item_pickup():
    global player_inventory
    if rooms[current_position_room]['item'] and rooms[current_position_room]['item'] not in player_inventory:
        player_inventory.append(rooms[current_position_room]['item'])
        print('--------------------------------------------------------------------')
        print(f'You grab the {rooms[current_position_room]['item']}.')
        rooms[current_position_room]['item'] = None
    else:
        print('--------------------------------------------------------------------')
        print()
        print('There is nothing of value in here, despite your best efforts to root around.')
        print()


# Loop to display current position of player
while True:  # Gameplay loop
    # Conditions to win game
    # Blacksmith item upgrade condition
    if current_position_room == blacksmith:
        if len(player_inventory) == 8:
            player_inventory.append('Legendary Sword and Armor')
            print('----------------------------------------------------------------------')
            print()
            print('As you place the book on the pedestal, the inanimate blacksmith comes to life. ')
            print('He flips some pages in the book, then makes his way to the forge, now alight with blue flame. ')
            print()
            print('----------------------------------------------------------------------')
            print()
            print('The blacksmith begins bellowing the flame and the jewels float from your inventory to his '
                  'hands. ')
            print('He asks for your sword and armor, and places them both on his forge.')
            print('The book begins to glow, the jewels begin to radiate, they seem to socket perfectly into '
                  'the armor and weapon.')
            print()
            time.sleep(7)
            print('-----------------------------------------------------------------------')
            print()
            print('With a few swings from his mighty hammer, the weapons and armor you had now seem to be stronger. ')
            print('Satisfied, the blacksmith hands you the Legendary Sword and Armor.')
            print('His work now complete, the skeletal figure seems to become inanimate, and wind down...')
            print()
            time.sleep(7)
        else:
            print('--------------------------------------------------------------------')
            print()
            print('The blacksmith is still awaiting the book...')
            print()
    # Victory scenario
    if current_position_room == villain_room:
        if len(player_inventory) == 9:
            print('---------------------------------------------------------------------------------')
            print(room_intro[current_position_room])
            time.sleep(7)
            print('---------------------------------------------------------------------------------')
            print()
            print('As you enter the room a foul smell creeps to your nostrils.')
            print('The High King sits on his throne, unmoving...')
            print('As you make your way closer, lights begin to illuminate the room.')
            print()
            time.sleep(7)
            print('---------------------------------------------------------------------------------')
            print()
            print('The High King laughs a hollow, gurgling laugh as his eyes come to life with blue fire.')
            print('He rises from the throne in an ethereal manner, clutching his Great Axe.')
            print('In the blink of an eye, he charges you, slashing down with all his weight.')
            print()
            time.sleep(7)
            print('---------------------------------------------------------------------------------')
            print()
            print('You dodge the blow successfully, only to stand firm at the edge of a spike trap.')
            print('The High King swings at you before you have time to react...')
            print()
            time.sleep(7)
            print('---------------------------------------------------------------------------------')
            print()
            print('His axe shatters against your Ancient Armor, now imbued with the jewels.')
            print('You turn to face him with the Ancient Sword held high,')
            print('with the power of the jewels radiating from within!')
            print()
            time.sleep(7)
            print('---------------------------------------------------------------------------------')
            print()
            print('As the High King rears back for an unarmed smash attack, the sword urges you to finish your quest.')
            print('With a sound and precise lunge, you stab into what seems like bones,')
            print('but the sword connects, surging with light and turning the High King to ash!')
            print()
            time.sleep(8)
            print()
            print('*********************************************************************************')
            print('*********************************************************************************')
            print()
            print('Congratulations! You have completed your quest and vanquished the High King and his evils.')
            print('Thanks for playing! Try again sometime!')
            time.sleep(20)
            break
        # Lose scenario
        elif player_inventory != 9:
            print('--------------------------------------------------------------------------------')
            print(room_intro[current_position_room])
            time.sleep(7)
            print('--------------------------------------------------------------------------------')
            print()
            print('You did not collect the items required to slay the High King.')
            print()
            print('With a hideous laugh, he raises from his throne and begins charging towards you.')
            print()
            time.sleep(7)
            print('--------------------------------------------------------------------------------')
            print('With seconds to spare you leap to the side and avoid his attack.')
            print('But as you roll away you notice a spike pit full of dead adventurers.')
            print('As you steady yourself before the pit, the High King takes another swing at you with his Great Axe.')
            time.sleep(7)
            print('--------------------------------------------------------------------------------')
            print('You feel the cold steel pierce your feeble armor.')
            print('Soon all becomes cold, and the world goes dark as you lean in towards the pit...')
            time.sleep(7)
            print()
            print('*********************************************************************************')
            print('*********************************************************************************')
            print()
            print('You lose, try again!')
            time.sleep(20)
            break
    # Display current position
    print('--------------------------------------------------------------------')
    print()
    print('You are in the {}.'.format(current_position_room))
    print()
    print(player_inventory)
    print()
    print('--------------------------------------------------------------------')
    if rooms[current_position_room]['item'] is None:
        print()
        print(room_intro_noItem[current_position_room])
    else:
        print()
        print(room_intro[current_position_room])

    # Moving through rooms
    user_command_move = input('\nType a direction to move between the rooms. \nType'
                              ' get item to retrieve the item in the room.'
                              '\nEnter exit to exit the game. ------------------->: ').lower()
    # To control player movement
    if user_command_move in direction_of_moves:
        user_command_move = user_command_move.replace("go", "")
        if user_command_move in rooms[current_position_room].keys():
            current_position_room = rooms[current_position_room][user_command_move]
        else:
            # Invalid Moves
            print('--------------------------------------------------------------------')
            print()
            print('You cannot go that way.')
            print()

    # Get item function
    elif user_command_move.lower() == 'get item':
        item_pickup()

    # Exit command
    elif user_command_move == 'exit':
        print('----------------------------------------------------------------------')
        print('You are leaving the ruins. Thanks for playing!')
        time.sleep(10)
        break
    # Invalid input
    else:
        print('That is not a valid command, please try again. Type North, South, East, West, or Get Item.')
