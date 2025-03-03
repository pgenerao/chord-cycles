from main import *

# Getting path scores for some examples

c_major_7 = Chord([c, e, g, b])
d_minor_7 = Chord([d, f, a, c])

maximal_consonance_paths = get_scored_paths(d_minor_7, c_major_7, maximal_consonance_score)
minimal_dissonance_paths = get_scored_paths(d_minor_7, c_major_7, minimal_dissonance_score)

for path in maximal_consonance_paths:
    print(path)

print("\n")

for path in maximal_consonance_paths:
    print(path)

print("\n")

print(max(maximal_consonance_paths, key=lambda triplet: triplet[2]))
print(min(minimal_dissonance_paths, key=lambda triplet: triplet[2]))
