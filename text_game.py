#Python Treasure Hunt Game

import random, time

def display_game_intro():
    print('''

    ---> Willkommen bei  'Rysavys Schatzsuchen-Spiel'
    
    ... das krasseste Spiel, was jemals gemacht wurde !

    Prolog:

        Nach einer langen Reise , entdeckst du plötzlich zwei Höhlen,
        einer der Höhlen führt zu dem Schatz, auf dessen Suche du schon seid langer Zeit bist.
        Die andere Höhle jedoch , ist gefüllt mir Messerscharfen Steinen die zum sicheren Tot
        führen würden... Mutig wie du bist, und auch ein wenig gierig auf den Schatz,
        entscheidest du dich das Risiko einzugehen und die Höhlen zu erkunden !


        Viel Glück !! Möge die Macht mir dir sein ! . . . . 



        ''')

def choose_cave():
    cave = ''
    while cave !='1' and cave !='2':
        time.sleep(8)
        print("Welche Höhle willst du betreten ? (Drücke die Taste '1' ,für  Höhle 1, oder die Taste '2' , für Höhle 2.) ? ")
        cave = input()
    return cave


def enter_cave(choosen_cave):
    print('\nDu hast die Höhle betreten ... ')
    time.sleep(1)

    random_cave = random.randint(1,2)
    #print("random_cave = " + str(random_cave))
    
    if random_cave == int(choosen_cave):
        print("---> Du Glücklicher ! Du hast den Schatz gefunden !!")

    else:
        print("--> Du hast erwartet einen Schatz zu finden \n ... aber alles was du gefunden hast war der TOT !! ")
        

def main_loop():


    '''The main_loop() function controls the flow of the game by calling functions and using conditionals'''
    play_game_again = "ja"

    while play_game_again =="ja" or play_game_again =="j":
        
            display_game_intro()
            chosen_cave = choose_cave()
            enter_cave(chosen_cave)

            print("\n\n Willst du es nochmal versuchen ? (ja oder nein)")
            play_game_again = input()
            print("Du hast " + play_game_again + input() +  gesagt : ")
            time.sleep(1)

            if play_game_again == "ja" or play_game_again =="j":
                print("\n Lass es uns nocheinmal versuchen!")

            else:
                print("\n Ok, bis zum nächsten mal ! Danke fürs Spielen ! ")

main_loop()







    

    
