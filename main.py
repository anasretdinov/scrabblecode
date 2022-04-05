import ru_scrabble
from ru_scrabble import Field, NowLetters
import json
import pprint
words_list = open("russian_nouns_with_definition.json", "r", encoding="utf8")
# print(words_list.readline())
data = json.load(words_list)

letters_mult_table = [['-' for j in range(15)] for i in range(15)]
words_mult_table = [['-' for j in range(15)] for i in range(15)]

with open("letters_mult_field.txt", "r") as letters_mult:
    with open("words_mult_field.txt", "r") as words_mult:
        for i in range(15):
            letters_mult_table[i] = list(map(int, letters_mult.read(30).split()))
            words_mult_table[i] = list(map(int, words_mult.read(30).split()))


f = Field(letters_mult_table, words_mult_table)
