from random import shuffle


##### SHUFFLE A LIST #####
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


##### PLAYER GUESS #####
def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0,1 or 2: ")

    return int(guess)


#### CHECK THE INPUT GUESS #####
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
        print(mylist)
    else:
        print("Wrong guess!")
        print(mylist)


# INITIAL LIST
mylist = [' ', 'O', ' ']
# SHUFFLE LIST
mixed_list = shuffle_list(mylist)
# USER GUESS
guess = player_guess()
# CHECK GUESS
check_guess(mixed_list, guess)
