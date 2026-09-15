import random
from wonderwords import RandomWords
R = RandomWords()
from PIL import Image
import numpy as np

    

letters = {'a': ['11011', '10101', '10001', '10101', '10101'], 'b': ['10001', '10110', '10001', '10110', '10001'], 'c': ['10001', '01111', '01111', '01111', '10001'], 'd': ['10001', '10110', '10110', '10110', '10001'], 'e': ['00001', '01111', '00001', '01111', '00001'], 'f': ['10000', '10111', '10011', '10111', '10111'], 'g': ['10001', '01111', '01100', '01110', '10001'], 'h': ['10101', '10101', '10001', '10101', '10101'], 'i': ['10001', '11011', '11011', '11011', '10001'], 'j': ['10001', '11101', '11101', '10101', '11011'], 'k': ['10110', '10101', '10011', '10101', '10110'], 'l': ['10111', '10111', '10111', '10111', '10001'], 'm': ['10101', '01010', '01110', '01110', '01110'], 'n': ['01110', '00110', '01010', '01100', '01110'], 'o': ['10001', '01110', '01110', '01110', '10001'], 'p': ['10001', '10110', '10001', '10111', '10111'], 'q': ['10001', '01110', '01110', '10001', '11110'], 'r': ['00011', '01101', '00011', '01011', '01101'], 's': ['10000', '01111', '10001', '11110', '00001'], 't': ['00000', '11011', '11011', '11011', '11011'], 'u': ['01110', '01110', '01110', '01110', '10001'], 'v': ['01110', '01110', '10101', '10101', '11011'], 'w': ['01110', '01110', '01110', '01010', '10101'], 'x': ['01110', '10101', '11011', '10101', '01110'], 'y': ['01110', '10101', '11011', '11011', '11011'], 'z': ['00000', '11101', '11011', '10111', '00000'],'blank':['11111','11111','11111','11111','11111']}
colors = {'grey':[128,128,128], 'green': [0,128,0], 'yellow': [255,255,0],'black':[0,0,0],'white':[255,255,255],'light_grey':[211,211,211]}

def letters_used_to_grid(letters_used):
    grid = [''] * len(letters_used)
    for letter in letters_used:
        letter = letters[letter]
        for i in range(5):
            grid[i]+=letter[i]
    return grid


def show_image(pixel_grid):
    img = Image.fromarray(np.array(pixel_grid).astype(np.uint8), "RGB")
    img.show()

def output_image(pixel_grid,filename):
    img = Image.fromarray(np.array(pixel_grid).astype(np.uint8), "RGB")
    img.save(filename)

def grid_to_color(score,grid):
    new_grid = [[] for _ in range(9)] 
    for i, _ in enumerate(grid):
        for j, block in enumerate(grid[i]):
            if j % 5 == 0:
                if j != 0:
                    score_index = j//5 - 1
                    color = score[score_index]
                    if block == '3':
                        new_grid[i].append(colors['black'])
                    else:    
                        new_grid[i].append(colors[color])
                new_grid[i].append(colors['black'])
                score_index = j//5
                color = score[score_index]
                if block == '3':
                    new_grid[i].append(colors['black'])
                else:    
                    new_grid[i].append(colors[color])
            if block == '0':
                new_grid[i].append(colors['black'])
            elif block == '3':
                new_grid[i].append(colors['black'])
            else:
                score_index = j//5
                color = score[score_index]
                new_grid[i].append(colors[color])
        score_index = j//5
        color = score[score_index]
        if block == '3':
            new_grid[i].append(colors['black'])
        else:    
            new_grid[i].append(colors[color])
        new_grid[i].append(colors['black'])

    return new_grid

def word_to_grid(guess):
    grid = [''] * 5
    for letter in guess:
        letter = letters[letter]
        for i in range(5):
            grid[i]+=letter[i]
    grid.insert(0,'1'*25)
    grid.insert(0,'3'*25)
    grid.append('1'*25)
    grid.append('3'*25)
    return grid

def DoubleLetterChecker(guess,word,score,letter,i):
    if score[i] == 'green':
        return False
    correct_count = 0
    for j, l in enumerate(guess):
        if l == letter and score[j] == 'green':
            correct_count += 1
    if correct_count == word.count(letter):
        return True
    if i > word.count(letter):
        return True
    else:
        return False
    
def WordleChecker(guess,word):
    score = ['green' if letter == word[i] else 'yellow' if letter in word else 'grey' for i,letter in enumerate(guess)]
    for i, letter in enumerate(guess):
        if word.count(letter) > 1 or guess.count(letter) > 1:
            if DoubleLetterChecker(guess,word,score,letter,i) == True:
                score[i] = 'grey' 
    return score

if __name__ == "__main__":
    wordle_word = R.get_random_word()
    while len(wordle_word) != 5:
        wordle_word = R.get_random_word()
    wordle_letters = [[letter] for letter in wordle_word]
    guess_results = []
    letters_used = []
    for num_guesses in range(6):
        guess = input('GUESS>').lower()
        while len(guess) != 5 or not guess.isalpha():
            guess = input('GUESS>').lower()
            if len(guess) == 5 and guess.isalpha():
                break
        guess_letters = [[letter] for letter in guess]
        score = WordleChecker(guess_letters,wordle_letters)
        pixel_grid = word_to_grid(guess)
        new_grid = grid_to_color(score,pixel_grid)
        guess_results = guess_results + new_grid 
        show_image(guess_results)
        if score == ['green', 'green', 'green', 'green', 'green']:
            break
        [letters_used.append(letter) for letter in guess if letter not in letters_used]
        letters_used.sort()

    output_image(guess_results,'wordle_run.png')
  
        

        

    
    