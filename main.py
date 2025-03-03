import numpy as np

from functools import reduce
from itertools import permutations

minimal_intervals = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 5,
    8: 4,
    9: 3,
    10: 2,
    11: 1,
}

note_names_sharps = {
    0: "C",
    1: "C♯",
    2: "D",
    3: "D♯",
    4: "E",
    5: "F",
    6: "F♯",
    7: "G",
    8: "G♯",
    9: "A",
    10: "A♯",
    11: "B",
}

note_names_flats = {
    0: "C",
    1: "D♭",
    2: "D",
    3: "E♭",
    4: "E",
    5: "F",
    6: "G♭",
    7: "G",
    8: "A♭",
    9: "A",
    10: "B♭",
    11: "B",
}

class Note():
    def __init__(self, note):
        # Assertions
        assert isinstance(note, int)

        # Set value of note
        self.note = note % 12
    
    def __sub__(self, operand):
        assert isinstance(operand, Note) or isinstance(operand, int)

        if isinstance(operand, Note):
            x = self.note
            y = operand.note
            z = (x - y) % 12

            return z
        elif isinstance(operand, int):
            x = self.note
            y = operand
            z = (x - y) % 12

            return Note(z)
        else:
            raise ValueError

    def __add__(self, operand):
        assert isinstance(operand, int)

        x = self.note

        return Note(x + operand)
    
    def __repr__(self):
        return note_names_flats[self.note]

class Chord():
    def __init__(self, notes):
        # Assertions (difference between notes)
        assert isinstance(notes, list)

        for note in notes:
            assert isinstance(note, Note)
        
        # Set values of the chord
        self.notes = notes
    
    def __sub__(self, operand):
        assert isinstance(operand, Chord) | isinstance(operand, list)

        if isinstance(operand, Chord):
            assert len(self.notes) == len(operand.notes)

            x = self.notes
            y = operand.notes

            z = list(map(lambda pair: pair[0] - pair[1], zip(x,y)))

            return z
        elif isinstance(operand, list):
            # Assertions (subtracting intervals)
            for note in operand:
                assert isinstance(note, int)
            
            assert len(operand) == len(self.notes)

            # Addition
            x = self.notes
            y = operand

            # List of notes obtained after addition
            z = list(map(lambda pair: pair[0] - pair[1], zip(x,y)))

            # Create new chord
            return Chord(z)
        else:
            raise ValueError
    
    def __add__(self, operand):
        # Assertions (adding intervals)
        assert isinstance(operand, list)

        for note in operand:
            assert isinstance(note, int)
        
        assert len(operand) == len(self.notes)

        # Addition
        x = self.notes
        y = operand

        # List of notes obtained after addition
        z = list(map(lambda pair: pair[0] + pair[1], zip(x,y)))

        # Create new chord
        return Chord(z)

    def __repr__(self):
        return self.notes.__repr__()

def intervals_to_string(intervals):
    return reduce(lambda x, y: str(x) + str(y), intervals)

################################################################################

##############
# ALGORITHMS #
##############

# Given two chords x1 & x2, present possible "paths" by pairings and their scores

def get_scored_paths(chord_1, chord_2, path_score_func):
    # Compare chord_1 to chord_2

    # Setup
    chord_2_notes = chord_2.notes
    indices = list(range(0, len(chord_2_notes)))

    paths = []

    # Iterate through all permutations of chord_2
    for permutated_indices in permutations(indices):
        # Get chord permutation
        permutated_chord_2_notes = list(map(lambda i: chord_2_notes[i], permutated_indices))
        chord_2_permutation = Chord(permutated_chord_2_notes)

        # Find the difference between chord_1 and permutation of chord_2
        diff = chord_1 - chord_2_permutation
        score = path_score_func(diff)

        paths.append((chord_1, chord_2_permutation, score))
    
    paths.sort(key=lambda triplet: triplet[2])

    return paths

# Given three chords x1, x2, y2, complete the commutative diagram and solve for y1:
#   x_1 → y_1 (?)
#    ↓     ↓
#   x_2 → y_2
def complete_cycle(x1, x2, y2):
    phi_1 = x2 - x1
    phi_1_inv = x1 - x2

    y1 = y2 + phi_1_inv

    return y1

###########################
# Lexical scoring methods #
###########################

# Minima of this gives the minimum dissonance
def minimal_dissonance_score(intervals):
    _ = intervals.copy()
    distances = list(map(lambda interval: minimal_intervals[interval], _))

    # decimal for legibility, switch to higher k-ary number system for note overflow
    
    # Representation allows us to have a counter in the digits...
    # 0 >> 0s place     (1s place is a counter for 0-intervals)
    # 1 >> 10s place    (10s place is a counter for 1-intervals)
    # 2 >> 100s place   (100s place is a counter for 2-intervals)
    # etc...

    k = max(10, len(intervals)+1)

    # k-ary representation of the number
    representation = reduce(lambda x, y: x + y, map(lambda d: k**d, distances))

    return representation

# Maxima of this gives the maximum consonance
def maximal_consonance_score(intervals):
    # Create a list of intervals
    _ = intervals.copy()
    distances = list(map(lambda interval: minimal_intervals[interval], _))

    # decimal for legibility, switch to higher k-ary number system for note overflow
    k = max(10, len(intervals)+1)

    # k-ary representation of the number

    # Lexical mirror of the minimal dissonance_score (has different properties)
    representation = reduce(lambda x, y: x + y, map(lambda d: k**(6-d), distances))

    return representation

################################################################################

c = Note(0)
d_flat = Note(1)
d = Note(2)
e_flat = Note(3)
e = Note(4)
f = Note(5)
g_flat = Note(6)
g = Note(7)
a_flat = Note(8)
a = Note(9)
b_flat = Note(10)
b = Note(11)