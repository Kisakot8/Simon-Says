# ██╗███╗░░░███╗██████╗░░█████╗░██████╗░████████╗░██████╗
# ██║████╗░████║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
# ██║██╔████╔██║██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░
# ██║██║╚██╔╝██║██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗
# ██║██║░╚═╝░██║██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝
# ╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░

from time import sleep
from colorama import Fore, Style
from random import choices, random, choice as random_choice

# ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
# ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
# █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
# ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
# ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
# ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

def play(stns:list) -> int:
    loss = False
    score = -1

    while not loss:
        loss = play_round(score+1,stns[0],stns[1],stns[2])
        score += 1

    print(f'You had a score of {score}.')
    input('Press enter to return...')

    return score

def play_round(num:int,difficulty:int,colour_count:int,simon_chance:float) -> bool:
    difficulty_to_speed_dict = {
1: 2,
2: 1.5,
3: 1,
4: 1}

    num_to_initial_dict = {
0: 'R',
1: 'Y',
2: 'G',
3: 'B',
4: 'C',
5: 'M'}
    speed = difficulty_to_speed_dict[difficulty] # Speed at which text is overwritten.

    if difficulty != 4:
        colours = fonted_colours
    elif difficulty == 4:
        fake_colours = colours_lst
        colours = fonts
    current_colours = choices(range(0,colour_count),k=(num+1))

    simon_says = (random() < simon_chance)
    if simon_says:
        print('Simon says...         ',end='\r')
    for i in range(len(current_colours)-1):
        sleep(speed)
        if difficulty == 4:
            print(f'{colours[current_colours[i]] + random_choice(fake_colours) + Fore.RESET} ({i+1}),         ',end='\r')
            # Need spaces at the end to clear longer colours, e.g. Yellow, and then Blue, otherwise Yellow, -> Blue,w
        else:
            print(f'{colours[current_colours[i]]} ({i+1}),         ',end='\r')
    sleep(speed)
    if difficulty == 4:
        print(f'{colours[current_colours[-1]] + random_choice(fake_colours) + Fore.RESET} ({len(current_colours)}).         ')
    else:
        print(f'{colours[current_colours[-1]]} ({len(current_colours)}).         ')
    
    guess = input('Enter colour initials: ')
    if simon_says:
        correct_answer = [num_to_initial_dict[x] for x in current_colours]
        if len(guess) == 0:
            print('Oh no! You entered nothing when Simon said something :(')
            print(f'The correct answer was: {"".join(correct_answer)}')
            sleep(2)
            return True
        if guess.upper() != ''.join(correct_answer):
            print('Oh no! You entered the wrong initials :(')
            print(f'The correct answer was: {"".join(correct_answer)}')
            sleep(2)
            return True
    elif not simon_says:
        if len(guess) != 0:
            print('Oh no! You entered an answer when Simon didn\'t say anything :(')
            sleep(2)
            return True


def tutorial() -> None:
    input(f'''{Style.BRIGHT}================ SIMON SAYS ================{Style.RESET_ALL}
Simon Says is a game of memory. The point of the game is to remember as many combinations of
colours as you can, which are displayed temporarily, one after another.
Press enter to continue...
''')
    input(f'''Here's an example:
The game tells you “Simon says {Fore.GREEN}Green,{Fore.RED} Red,{Fore.BLUE} Blue,{Fore.RESET}” and then says GO! You then
have 2 seconds per colour (6 in this case) to type out the initials of the colours (i.e. GRB).
If you are correct, you move on to 4 colours, then 5, etc., but remember - only answer if Simon
says it, or you will lose. If the colours are not said by Simon, do not type anything and then
press enter.
Press enter to continue...
''')
    input(f'''There are 4 difficulties: {Fore.GREEN}Easy, {Fore.YELLOW}Medium, {Fore.RED}Hard {Fore.RESET}and {Fore.RED + Style.BRIGHT} Oh God{Style.RESET_ALL}. The difference between the first 3 is that
the time to view each colour is 2, 1.5 and 1 seconds (respectively). The last difficulty, {Fore.RED + Style.BRIGHT}Oh God{Style.RESET_ALL}, will
use 1 second of time and make each colour mismatched with its text, e.g. {Fore.BLUE}Blue{Fore.RESET} becomes {Fore.BLUE}Red{Fore.RESET}. Always
type the {Style.BRIGHT}colour{Style.RESET_ALL} of the text, not the colour printed. In this case, Typing B as the answer is
correct, even though the text says {Fore.BLUE}Red{Fore.RESET}.

Have fun!
Press enter to return...
''')
    return
    # Marcel will write this
    # welp oops seems i got bored and did it myself ¯\_(ツ)_/¯

def settings(old_stns:list) -> list:
    new_stns = old_stns[:] # can't just do new_stns = old_stns bc then they reference the same list; changing one changes both

    while True:
        choice = enter_choice(f'''{Style.BRIGHT}   ******** SETTINGS ******** {Style.RESET_ALL}
1. Change difficulty
2. Change colour count
3. Change Simon chance
4. Exit settings
''',['1','2','3','4'])

        if choice == '1':
            difficulty = int(enter_choice(f'''{Style.BRIGHT}   ******** DIFFICULTY ******** {Style.RESET_ALL}
1. Easy (2 seconds per colour)
2. Medium (1.5 seconds per colour)
3. Hard (1 second per colour)
4. Oh God (1 second per colour, mixed colours)
(Current settings = {new_stns[0]})
''',['1','2','3','4']))
            new_stns[0] = difficulty

        elif choice == '2':
            colour_count = int(enter_choice(f'''{Style.BRIGHT}   ******** COLOUR COUNT ******** {Style.RESET_ALL}
Choose in a range of 2-6 colours (Red, Yellow, Green, Blue, Cyan, Magenta) to play with.
(Current settings = {new_stns[1]})
''',['2','3','4','5','6']))
            new_stns[1] = colour_count

        elif choice == '3':
            simon_chance = float(enter_choice(f'''{Style.BRIGHT}   ******** SIMON CHANCE ******** {Style.RESET_ALL}
Choose how often Simon says the colours, i.e. how often you need to type them (as opposed to NOT typing).
Chance is determined by a decimal, e.g. 0.65 = 65% chance, 1.0 = 100% chance.
(Current settings = {new_stns[2]})
''',choices_range_float=[0.25,1.0]))
            new_stns[2] = simon_chance

        elif choice == '4':
            if new_stns != old_stns:
                if confirm_choice(f'''Confirm changes?
{'Difficulty':12}: {old_stns[0]} -> {new_stns[0]}
{'Colour Count':12}: {old_stns[1]} -> {new_stns[1]}
{'Simon Chance':12}: {old_stns[2]} -> {new_stns[2]}
'''):
                    print('Changes saved!')
                    return new_stns
            
            print('No changes made, returning to menu...')
            return old_stns

def leaderboard():
    pass # Marcel will also write this

def exit_program():
    print('Have a good day!')
    exit('Program ended by user.')


# ██╗░░░██╗████████╗██╗██╗░░░░░██╗████████╗██╗░░░██╗
# ██║░░░██║╚══██╔══╝██║██║░░░░░██║╚══██╔══╝╚██╗░██╔╝
# ██║░░░██║░░░██║░░░██║██║░░░░░██║░░░██║░░░░╚████╔╝░
# ██║░░░██║░░░██║░░░██║██║░░░░░██║░░░██║░░░░░╚██╔╝░░
# ╚██████╔╝░░░██║░░░██║███████╗██║░░░██║░░░░░░██║░░░
# ░╚═════╝░░░░╚═╝░░░╚═╝╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░

def enter_choice(q:str,choices:list[str]=[],choices_range_float:list[float]=[]) -> any:
    if len(choices) > 0:
        choice = ''
        while choice not in choices:
            choice = input(f'{q}\n(Enter {", ".join(choices)})\n')
        return choice

    elif len(choices_range_float) == 2:
        print(q)
        while True:
            try:
                choice = float(input(f'(Enter decimal number between {choices_range_float[0]} and {choices_range_float[1]})\n'))
            except ValueError:
                print('Please enter a valid float (decimal number)')
                continue
            if choice >= choices_range_float[0] and choice <= choices_range_float[1]:
                print(f'You entered: {choice}')
                break
            else:
                print(f'Float must be between {choices_range_float[0]} and {choices_range_float[1]} (inclusive)')
        return choice

def confirm_choice(q:str) -> bool:
    choice = enter_choice(q,['y','n'])
    if choice == 'y':
        return True
    return False

# ███╗░░░███╗░█████╗░██╗███╗░░██╗
# ████╗░████║██╔══██╗██║████╗░██║
# ██╔████╔██║███████║██║██╔██╗██║
# ██║╚██╔╝██║██╔══██║██║██║╚████║
# ██║░╚═╝░██║██║░░██║██║██║░╚███║
# ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝

def main():
    # Initialising default variables
    global colours_lst
    global fonts
    global fonted_colours
    colours_lst = ['Red','Yellow','Green','Blue','Cyan','Magenta']
    fonts = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]
    fonted_colours = [Fore.RED + 'Red' + Fore.RESET,Fore.YELLOW + 'Yellow' + Fore.RESET,Fore.GREEN + 'Green' + Fore.RESET, Fore.BLUE + 'Blue' + Fore.RESET,Fore.CYAN + 'Cyan' + Fore.RESET,Fore.MAGENTA + 'Magenta' + Fore.RESET]
    stns = [1,4,0.75]
    # stns = [difficulty,colour_count,simon_chance]

    while True:
        choice = enter_choice(f'''   {Style.BRIGHT}======== SIMON SAYS ========{Style.RESET_ALL}
1. Play
2. Tutorial
3. Settings
4. Hi-scores
5. Exit''',['1','2','3','4','5'])
        if choice == '1':
            play(stns)
        elif choice == '2':
            tutorial()
        elif choice == '3':
            stns = settings(stns)
        elif choice == '4':
            leaderboard()
        elif choice == '5':
            exit_program()

if __name__ == '__main__':
    main()
