letters_points = [1, 3, 1, 3, 2, 1, 3, 5, 5, 1, 4, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 10, 5, 5, 5, 8, 10, 10, 4, 3, 8, 8, 3, 2]

def letter_to_num(ch):
    if ch == '_':
        return 33
    else:
        return ord(ch) - ord('а')


def num_to_letter(num):
    if num == 33:
        return '_'
    else:
        return chr(ord('a') + num)


class Cell(object):
    def __init__(self, letter_mult, word_mult):
        self.letter_mult = letter_mult
        self.word_mult = word_mult
        self.ch = '_'
        self.type = type

    def fill(self, ch):
        self.ch = num_to_letter(ch)
        return [self.letter_mult * letters_points[ch], self.word_mult]


class NowLetters(object):
    z = [0 for i in range(34)]

    def __init__(self):
        pass

    def addon(self, letters):
        for i in letters:
            self.z[i] += 1


class Field(object):
    h = 15
    w = 15
    data = [['-' for j in range(15)] for i in range(15)]

    def __init__(self, letters_mult_table, words_mult_table):
        for i in range(self.h):
            for j in range(self.w):
                self.data[i][j] = Cell(letters_mult_table[i][j], words_mult_table[i][j])





