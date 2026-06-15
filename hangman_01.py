import random
import hangman_stages

word_list = ["apple", "mango", "grapes"]
chosen_word = random.choice(word_list)
print(chosen_word)  # debugging

display = ["_"] * len(chosen_word)
print(display)

wrong_guesses = 0   # ✅ start at 0 mistakes
max_wrong = len(hangman_stages.stages) - 1

game_over = False
while not game_over:
    guessed_letter = input("guess a letter : ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    print(display)

    if guessed_letter not in chosen_word:
        wrong_guesses += 1
        print(hangman_stages.stages[wrong_guesses])  # ✅ build step by step
        if wrong_guesses == max_wrong:
            game_over = True
            print("you lose !!")

    if "_" not in display:
        game_over = True
        print("you win !!!")
