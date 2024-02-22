import random

print("Welcome to the quiz!")

score = 0

while True:
    playing = input("Do you want to play the game? ( y/n )")
    if playing.lower() in ['y', 'yes']:
        break
    elif playing.lower() in ['n', 'no']:
        print("Bye bye!")
        quit()
    else:
        print("Wrong Input. Try again!")
        playing = input("Do you want to play the game? ( y/n )")

print("Let's play!")

original_questions = {"What is 1 + 1?" : "2",
                      "What is 39 divided by 3?" : "13",
                      "What is 5 * 5?" : "25",
                      "What is 0 * 11" : "0",
                      "What is 100 + 200?" : "300",
                      "What is 50 * 1?" : "50",
                      "What is square root of 144?" : "12"}


##Shuffle the dict items
list_questions = list(original_questions.items())
random.shuffle(list_questions)
questions = dict(list_questions)


for i in questions:
    print(i)
    answer = input("").lower()
    if answer == questions[i]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print(f"Your score is: {score} / {len(questions)} ({int((score / len(questions)) * 100)}%)")



