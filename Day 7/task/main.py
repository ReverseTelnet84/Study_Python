import random
from operator import truediv

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.

game_over = False
correct_letters = []

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    # if len(correct_letters) > 0:
    #     for i in range(len(chosen_word)):
    #         if chosen_word[i] == guess:
    #             correct_letters[i] = guess
    #         print(f"correct_letters #2 :  {correct_letters}")
    # else:
    #     for i in range(len(chosen_word)):
    #         if chosen_word[i] == guess:
    #             correct_letters += chosen_word[i]
    #         elif correct_letters != "_":
    #             correct_letters += "_"
    #         print(f"correct_letters  #1 : {correct_letters}")
    #
    # print(f"correct_letters #3 :  {correct_letters}")
    #
    # for i in range(len(correct_letters)):
    #     display += correct_letters[i]

    for word in chosen_word:
        if word == guess:
            display += word
            correct_letters.append(word)
        elif word in correct_letters:
            display += word
        else:
            display += "_"

    if "_" not in display:
        game_over = True

    print("display #1 : " + display)