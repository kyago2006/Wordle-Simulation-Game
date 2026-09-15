from random_word import RandomWords
R = RandomWords()

def letter_used(letters_used):
    empty_row = '1' * 51
    print(empty_row)

    
if __name__ == "__main__":
    wordle_word = R.get_random_word()
    while len(wordle_word) != 5:
        wordle_word = R.get_random_word()
    wordle_letters = [[letter] for letter in wordle_word]

    guess_results = []
    letters_used = []
    for num_guesses in range(6):
        guess = input().lower()
        while len(guess) != 5 or not guess.isalpha():
            guess = input().lower()
            if len(guess) == 5 and guess.isalpha():
                break
        guess_letters = [[letter] for letter in guess]
        [letters_used.append(letter) for letter in guess if letter not in letters_used]
        letters_used.sort()
        letter_used(letter_used)
    print(wordle_letters)