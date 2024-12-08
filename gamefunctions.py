
"""Contains useful functions for a text based adventure game.

Leave one blank line.  The rest of this docstring should contain an
overall description of the module or program.  Optionally, it may also
contain a brief description of exported classes and functions and/or usage
examples.

This module contains fuctions: purchase_item, new_random_monster,
print_welcome, and print_shop_menu. Consult individual functions docstrings
for more information."""


#Adventure functions
#Ian Oberbillig
#12/08/24
import random

def purchase_item(itemPrice, startingMoney, quantity = 1):
    '''
    Returns the number of items purchased and the quantity of money remaining.

    Parameters:
        itemPrice(float): The price of the item.
        startingMoney(float): The amount of money owned by the player.
        quantity(int): The number of items the player wants to buy.

    Returns:
        (quantity_purchased, remainingMoney): A tuple whose contents are as follows:
            quantity_purchased(int): Number of items purchased.
            remainingMoney(float): The players remaining money.
    Example:
        >>> x = purchase_item(3, 22, 4)
        >>> print(x)
        (3, 10)
    '''
    totalPrice = quantity * itemPrice
    # Calculates how many items the player can afford
    canAfford = startingMoney // itemPrice
    # If the player can afford the quantity they want they purchase that quantity
    if canAfford >= quantity:
        quantity_purchased = quantity
        remainingMoney = startingMoney - itemPrice * quantity
    # If they can't afford what they want they purchase as much as they can
    else:
        quantity_purchased = canAfford
        remainingMoney = startingMoney - itemPrice * canAfford

    return (quantity_purchased, remainingMoney)

def new_random_monster():
    '''
    Generates a random monster.

    Paramters:
        None

    Returns:
        monster(dict): A dictionary with the following keys:
            name(str): the monster's name.
            description(str): A description of the monster.
            health(int): The monster's health.
            power(int): The monster's power.
            money(int): The monster's money.

    Example:
        >>> randomEncounter = new_random_monster()
        >>> print(randomEncounter['name']
        Blimp
        >>> print(randomEncounter['money']
        1223
    '''
    monster = {
        'name': '',
        'description' : '',
        'health' : '',
        'power' : '',
        'money' : ''
        }
    monsterLibrary = (
        'Chimp',
        'Simp',
        'Blimp'
        )
    #Assigns a name
    monster['name'] = monsterLibrary[random.randint(0,len(monsterLibrary) - 1)]
    #Assigns other stats based on name
    if monster['name'] == 'Chimp':
        monster['description'] = 'He\'s coming at you fast.'
        monster['health'] = random.randint(7,10)
        monster['power'] = random.randint(17, 23)
        monster['money'] = random.randint(0, 5)
    if monster['name'] == 'Simp':
        monster['description'] = 'He\'s crouched in the corner.'
        monster['health'] = random.randint(1,3)
        monster['power'] = random.randint(0, 3)
        monster['money'] = random.randint(100, 200)
    if monster['name'] == 'Blimp':
        monster['description'] = 'He\'s just floating around.'
        monster['health'] = random.randint(150, 200)
        monster['power'] = random.randint(15, 20)
        monster['money'] = random.randint(1000, 2000)
        
    return monster

def print_welcome(name, width=20):
    '''
    Prints a welcome to "name", centered inside a whitespace of length "width".

    Paramaters:
        name(str): The players name.
        width(int): The desired amount of whitespace, default value of 20.

    Returns:
        None

    Example:
        >>> print_welcome('John', 22)
            Greetings John    
    '''
    #Creates the greeting for the given name
    new_string = f'Greetings {name}'
    print(f'{new_string:^{width}}')

def print_shop_menu(item1Name, item1Price, item2Name, item2Price):
    '''
    Prints a shop menu with two items.

    Paramaters:
        item1Name(str): The name of the first item.
        item1Price(float): The price of the first item.
        item2Name(str): The name of the second item.
        item2Price(float): The price of the second item.

    Returns:
        None

    Example:
        >>> print_shop_menu('Egg', 2.2, 'Milk', 32)
       /----------------------\\
       | Egg            $2.20 |
       | Milk          $32.00 |
       \\----------------------/ 
    '''
    #Shortens item names if they're too long
    if len(item1Name) > 12:
        item1Name = f'{item1Name[0:9]}...'
        
    if len(item2Name) > 12:
        item2Name = f'{item2Name[0:9]}...'
    #Lowers item price to 9999 if greater than 9999
    if item1Price > 9999:
        item1Price = 9999
    if item2Price > 9999:
        item2Price = 9999
    
    #puts a dollar sign on the prices and rounds to 2 decimal places
    item1Price = f'${item1Price:.2f}'
    item2Price = f'${item2Price:.2f}'

    #opening border
    print('/', end='')
    print('-' * 22, end='')
    print('\\')
    
    #body
    
    print('|', end = ' ')
    print(f'{item1Name:12}{item1Price:>8}', end = ' ')
    print('|')
    print('|', end = ' ')
    print(f'{item2Name:12}{item2Price:>8}', end = ' ')
    
    #closing border
    print('|')
    print('\\', end='')
    print('-' * 22, end='')
    print('/')
    

def game_over():
    '''
    Handles the death of a player.

    Paramaters:
        None

    Returns:
        (Bool, Bool): A tuple of booleans, which track whether the
            player wants to try again or quit the game entirely.
    '''

    user_input = ''
    input('You died \n')
    while not user_input in ['1', '2']:
        print(
             'What would you like to do? \n'
             '1) Play again \n'
             '2) Quit'
              )
        user_input = input('Select an option: ')
        if not user_input in ['1', '2']:
            input('Invalid input')
        elif user_input == '1':
            return (False, False)
        elif user_input == '2':
            return(True, False)
            

def fight_monster(player, monster):
    '''
    Initiates a fight between a player and a monster.

    Paramaters:
        player(dict): Player information
        monster(dict): Monster information
        
    Returns:
        None
    '''
    #Initializes an input
    user_input = ''
    leave = False
    #Main fight loop
    while user_input != '2' and not leave:
        input(f'You\'re in combat with a {monster["name"]}\n')
        input(
              f'Your hp: {player["current_hp"]}\n'
              f'Monster hp: {monster["health"]}\n'
              )
        
        print(
              'What do you want to do?\n\n'
              '\t 1) Attack\n'
              '\t 2) Run'
              )
        #Special pin interaction
        hasPin = False
        pin = {}
        for item in player['inventory']:
            if item['name'] == 'Pin':
                hasPin = True
                pin = item
        if monster['name'] == 'Blimp' and hasPin:
            print('\t 3) Use pin?')
        
        user_input = input('What do you want to do?: ')
            
        # Attack sequence
        if user_input == '1':
            monster['health'] = monster['health'] - player['power']
            player['current_hp'] = player['current_hp'] - monster['power']
            
            #Checks if player died
            if player['current_hp'] <= 0:
                leave = True
            
            #Checks if monster died
            elif monster['health'] <= 0:
                print('You are victorious')
                player['gold'] += monster['money']
                user_input = '2'
        elif user_input == '2':
            print('Got away safely')

        elif user_input == '3' and hasPin and monster['name'] == 'Blimp':
            print('You pop the Blimp!')
            player['gold'] += monster['money']
            player['inventory'].remove(pin)
            user_input = '2'
            
        else:
            print('Invalid input')


def shopping(player):
    '''
    Sends the player to the shop.

    Paramaters:
        player(dict): Player information

    Returns:
        None
    '''

    input('You go into town and find a shop labeled "AdventureCo"')
    input('The shopkeeper gives you a friendly smile and invites you to browse her wares')
    shop_input = ''
    while shop_input != '3':
        print_shop_menu('Magic Sword', 9999, 'Pin', 1)
        input(f'Your gold: {player["gold"]}')
        print(
            'Make a purchase? \n'
            '1) Purchase Sword \n'
            '2) Purchase Pin \n'
            '3) Leave \n'
            )
        shop_input = input('Select an option: ')
        if shop_input not in ['1', '2', '3']:
            print('Invalid input')
        
        elif shop_input == '1':
            answer = purchase_item(9999, player["gold"])
            player["gold"] = answer[1]

            if answer[0] == 0:
                input('Not enough gold')
            else:
                sword = {
                    'name':'Magic Sword',
                    'type':'Weapon',
                    'durability':20,
                    'equipped': 'No',
                    'power':100
                    }
                player['inventory'].append(sword)
                input('You purchased a sword!')
            
        elif shop_input == '2':
            answer = purchase_item(1, player["gold"])
            player["gold"] = answer[1]
            if answer[0] == 0:
                input('Not enough gold')
            else:
                pin = {
                    'name':'Pin',
                    'type':'Misc',
                    'durability':1,
                    'equipped': 'No'
                    }
                player['inventory'].append(pin)
                input('You purchased a pin!')

def check_inventory(inventory):
    '''
    Allows the player to check their inventory and equip items.

    Paramaters:
        inventory(list): Player's inventory

    Returns:
        item(dict): The item the player wants to equip
    '''

    descript = []
    for item in inventory:
        if item['type'] not in descript:
            descript.append(item['type'])
    number_of_types = 1
    for title in descript:
        print(f'{number_of_types}) {title}')
        number_of_types +=1
    number_of_types -= 1


    print(f'{number_of_types + 1}) Quit')
    
    #Error handling for non int inputs
    getmeout = False
    user_input = ''
    while not getmeout:
        user_input = input('Select a type: ')
        try:
            user_input = int(user_input)
            getmeout = True
        except:
            print('Input must be a number')
    
    if user_input not in range(number_of_types + 2):
        print('Invalid input')
        return({})
        
    elif user_input == number_of_types + 1:
        return({})

    else:
        item_count = 1
        items = []
        for item in inventory:
            if item['type'] == descript[user_input - 1]:
                print(f'{item_count}) Name: {item["name"]}, Durability: {item["durability"]}, Equipped: {item["equipped"]}')
                item_count +=1
                items.append(item)
        item_count -=1
        print(f'{item_count + 1}) Quit')
    #Error handling for non int inputs
        getmeout2 = False
        user_input2 = ''
        while not getmeout2:
            user_input2 = input('Equip an item?: ')
            try:
                user_input2 = int(user_input2)
                getmeout2 = True
            except:
                print('Input must be a number')
        if user_input2 in range(item_count + 1):
            selected_item = items[user_input2 - 1]

        if user_input2 not in range(item_count + 2):
            print('Invalid input')

        elif user_input2 == item_count + 1:
            return({})

        elif user_input2 in range(item_count + 1) and selected_item['equipped'] == 'No':
            print(f'Equipped {items[user_input2 - 1]["name"]}')
            return items[user_input2 - 1]

        else:
            return({})
            

        
        
                
    
        
    
        




    
    
#Function Calls to demonstrate code functionality:
#Note for Ian: use 'control 3' to comment out highlighted code blocks


def test_functions():
    
    print('Sample run of each function 3 times, to demonstrate functionality:')
    print('')
        
    print('purchase_item(300, 4000)')
    print(purchase_item(300, 4000))
    print('')
    print('purchase_item(2000, 31)')
    print(purchase_item(2000, 31))
    print('')
    print('purchase_item(11, 422, 13)')
    print(purchase_item(11, 422, 13))

    print('')
    print('')


    print('new_random_monster()')
    print(new_random_monster())
    print('')
    print('new_random_monster()')
    print(new_random_monster())
    print('')
    print('new_random_monster()')
    print(new_random_monster())

    print('')
    print('')


    print('print_welcome("Felicity")')
    print_welcome('Felicity')
    print('')
    print('print_welcome("Ian", 30)')
    print_welcome('Ian', 30)
    print('')
    print('print_welcome("Alex", 100)')
    print_welcome('Alex', 100)

    print('')
    print('')

    print("print_shop_menu('Egg',2.2,'Milk',32)")
    print_shop_menu('Egg',2.2,'Milk',32)
    print('')
    print("print_shop_menu('Cursed Object',6.66, 'Pie',3.141592)")
    print_shop_menu('Cursed Object',6.66, 'Pie',3.141592)
    print('')
    print("print_shop_menu('Newt', 8.5, 'Mace of Extordinary Might', 100000000000)")
    print_shop_menu('Newt', 8.5, 'Mace of Extordinary Might', 100000000000)

    print('')
    print('')

    print("game_over()")
    
    game_over()

    print('')
    print('')
    
    sword = {
            'name':'Sword',
            'type':'Weapon',
            'durability':10,
            'equipped':'No'
            }
    
    pin = {
        'name':'Pin',
        'type':'Misc',
        'durability':1,
        'equipped':'No'
        }
    
    axe = {
            'name':'Axe',
            'type':'Weapon',
            'durability':15,
            'equipped':'Yes'
            }

    player = {
    'name':'',
    'power':25,
    'max_hp':100,
    'current_hp':100,
    'gold':2000,
    'inventory':[pin, sword, axe]
    }
    print("fight_monster(player, new_random_monster())")
    fight_monster(player, new_random_monster())

    print('')
    print('')
    
    print("shopping(player)")
    shopping(player)

    print('')
    print('')


    print("check_inventory(player['inventory'])")
    check_inventory(player['inventory'])

if __name__ == '__main__':
    test_functions()
    




