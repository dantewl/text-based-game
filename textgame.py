#test based game
import time
import random

print('Welcome!')

startgame = int(input('Start the game (1):    '
                          
                          'Exit the game  (2): '))

    
if startgame == 1:
    
    chapters = ['Chapter 0', 'Chapter 1 - The Forest', 'Chapter 1 - The Mountains', 'Chapter 2']
    
    dream_sequence = ['After a long day at work... You came back to home and went directly to your bed',
                    'Once you sleep... You start dreaming...', 'Once you sleep... You start dreaming...',
                    'You hear some voices in your head, voices you cannot understand', 
                    'You start feeling tired... more than you ever felt...',
                    'You try to keep dreaming... But the voices get stronger...',
                    'Before you realize...', 'You faint in your dreams.']
    
    afterdream_sequence = ['You hear the voices again... But you can understand it now...',
                           'You hear screams... Flames... People running...', 
                           'You slowly start opening your eyes...', 'You see a old lady "Oh my son... ',
                           'You dont know why... You feel that she is really your mother', 
                           'ow can you feel such feeling for a woman you have never seen before...',
                           'You look around, you are in a little village house...',
                           'The house is burning... the screams outside get closer',
                           'Mom: "My son..." "cof cof" "It is time..."',
                           'Mom: "Please... Take this book... *She takes a book under the bed* "',
                           'You hear hard knocks at the door...',
                           '*A man screams at the door* Man: "Open this door now!" *he kicks the door*',
                           'Mom: *She gives you a book* "Now run! We dont have any time left..."',
                           'Mom: "I love you my son... Please stay alive..."',
                           '*She opens the backdoor* Mom: "Run!"',
                           'You start running as fast as you can...',
                           '*You stop and look behind*',
                           'You see the back-door closing... And the front-door breaking...',
                           '*You see 2 paths you can follow*', 
                           ]
    
    print('Chapter 0')
    time.sleep(2.5)
    print('...')
    time.sleep(1)
    print('After a long day at work... You came back to home and went directly to your bed')
    time.sleep(2.5)
    print('Once you sleep... You start dreaming... ')
    time.sleep(2.5)
    print('You hear some voices in your head, voices you cannot understand')
    time.sleep(2.5)
    print('You start feeling tired... more than you ever felt...')
    time.sleep(2.5)
    print('You try to keep dreaming... But the voices get stronger...')
    time.sleep(2.5)
    print('Before you realize...')
    time.sleep(2.5)
    print('You faint in your dreams.')
    time.sleep(2.5)

    print('...')
    time.sleep(1)

    print('You hear the voices again... But you can understand it now...')
    time.sleep(2.5)
    print('You hear screams... Flames... People running... ')
    time.sleep(2.5)
    print('You slowly start opening your eyes...')
    time.sleep(2.5)
    print('You see a old lady "Oh my son... "')
    time.sleep(2.5)
    print('You dont know why... You feel that she is really your mother')
    time.sleep(2.5)
    print('How can you feel such feeling for a woman you have never seen before...')
    time.sleep(2.5)
    print('You look around, you are in a little village house...')
    time.sleep(2.5)
    print('The house is burning... the screams outside get closer')
    time.sleep(2.5)
    print('Mom: "My son..." "cof cof" "It is time..."')
    time.sleep(2.5)
    print('Mom: "Please... Take this book... *She takes a book under the bed* "')
    time.sleep(2.5)
    print('You hear hard knocks at the door...')
    time.sleep(2.5)
    print(' *A man screams at the door* Man: "Open this door now!" *he kicks the door*')
    time.sleep(2.5)
    print('Mom: *She gives you a book* "Now run! We dont have any time left..."')
    time.sleep(2.5)
    print('Mom: "I love you my son... Please stay alive..."')
    time.sleep(2.5)
    print('*She opens the backdoor* Mom: "Run!"')
    time.sleep(2.5)
    print('You start running as fast as you can...')
    time.sleep(2.5)
    print('*You stop and look behind*')
    time.sleep(2.5)
    print('*You see the back-door closing... And the front-door breaking...')
    time.sleep(2.5)
    print('*You see 2 paths you can follow*')
    time.sleep(1.5)
    
    biome_choice1 = input('"The Forest" or "The Mountain" *Make your choice*: ')
    
    if biome_choice1.lower() == 'forest' or 'the forest':
        print('Chapter 2: The Forest')
        time.sleep(2)
        print('After running into the forest... you find a abandoned camping')
        time.sleep(2)
        decision1 = int(input('Sit in the camping (1) Go away (2)'))
        
        if decision1 == 1:
            print('*You sit on the log and take the book*')
            time.sleep(2)
            print('The book is strange... you havent saw nothing like it')
            time.sleep(2)
            print('*You open the book*')
            time.sleep(2)
            print('Dice System: When you need to perfom an action, you roll a dice, the number decides your destiny...')
            time.sleep(2)
            
            book = print('🎲', random.randint(1, 20))

            if book >= 12:
                print('There is nothing wrote there, but somehow you know everything what the book says...')
                time.sleep(2)
                print('???: Find me in the Kings castle...')
                time.sleep(2)
                print('You feel that you have no choice but agreeing with it')
                time.sleep(2)
                print('You feel ')
            elif book < 12:
                print('You feel an strange energy')
                time.sleep(2)
                print('')



        elif decision1 == 2:
            print('*You keep running into the forest*')
        
        else:
            print('Unexpected Error')



    elif biome_choice1.lower() == 'the mountains' or 'mountains':
        print('Chapter 2: The Mountains')
        time.sleep(2)
        print('The end')
    
    else:
        print('Unexpected Error')








elif startgame == 2:
    print('You have closed the game')

else:
    print('Unexpected Error')





