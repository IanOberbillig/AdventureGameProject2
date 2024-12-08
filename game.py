# game.py
# Ian Oberbillig
# 12/08/24

import gamefunctions


#Main game loop

quit_status = False

while not quit_status:

    #Initialize player stats and starting inventory
    axe = {
        'name':'Axe',
        'type':'Weapon',
        'durability':10,
        'equipped':'No',
        'power':10
        }
    leather_armour = {
        'name':'Leather Armour',
        'type':'Armour',
        'durability':100,
        'equipped':'No',
        'health':50
        }

    player = {
        'name':'',
        'power':25,
        'max_hp':100,
        'current_hp':100,
        'gold':20,
        'inventory':[axe, leather_armour]
        }

    input('Welcome to a text based adventure (hit enter to continue)')

    player['name'] = input('What is your name: ')
    print('')
    gamefunctions.print_welcome(player['name'])
    input()

    #Adventure loop
    
    adventure_status = True
    
    while adventure_status:

        #Game over
        
        if player['current_hp'] <= 0:
            answer = gamefunctions.game_over()
            quit_status = answer[0]
            adventure_status = answer[1]

        else:
        
            input(f'Current HP: {player["current_hp"]}, Current Gold: {player["gold"]}')
            print(
                'What would you like to do? \n'
                '1) Fight Monster \n'
                '2) Sleep (Restore HP for 5 Gold) \n'
                '3) Go Shopping \n'
                '4) Check inventory \n'
                '5) Check stats \n'
                '6) Quit \n'
            )
            user_input = input('Select an option: ')
            
            #Handle invalid inputs
            
            if not user_input in ['1', '2', '3', '4', '5', '6']:
                input('Invalid input')
                
            #Fight a monster
                
            elif user_input == '1':
                monster = gamefunctions.new_random_monster()
                input(f'You go searching until you find a {monster["name"]}')
                input(monster['description'])
                gamefunctions.fight_monster(player, monster)
                
            #Rests at inn (players can go in debt to the innkeeper)
                
            elif user_input == '2':
                input('You buy a room at an Inn for 5 gold')
                player['gold'] -= 5
                player['current_hp'] = player['max_hp']
                input('You feel refreshed')
                
            #Go shopping
                
            elif user_input == '3':
                gamefunctions.shopping(player)

            #View inventory
                
            elif user_input == '4':
                item = gamefunctions.check_inventory(player['inventory'])
                if item != {}:
                    player['inventory'].remove(item)
                    item['equipped'] = 'Yes'
                    player['inventory'].append(item)
                    player['power'] += item.get('power', 0)
                    player['max_hp'] += item.get('health', 0)
                    
            #Check stats
                    
            elif user_input == '5':
                input(
                    f'Name: {player["name"]} \n'
                    f'Max HP: {player["max_hp"]} \n'
                    f'Power: {player["power"]} \n'
                      )
                
            #Quits game

            elif user_input == '6':
                adventure_status = False
                quit_status = True


        
    

        
    


    




