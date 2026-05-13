import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
display = ""
before_display = []

while display != chosen_word:
    guess = input("Guess a letter: ").lower()

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    if len(before_display) > 0:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                before_display[i] = chosen_word[i]
            print(f"before_display #1 :  {before_display}")
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                before_display += chosen_word[i]
            elif before_display != "_":
                before_display += "_"
            print(f"before_display  #2 : {before_display}")

    print(f"before_display #3 :  {before_display}")

    display =""
    for i in range(len(before_display)):
        display += before_display[i]

    print("display #1 : " + display)