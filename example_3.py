from main import *

# Getting path scores for some examples

c_maj_7 = Chord([c, e, g, b])
d_min_7 = Chord([d, f, a, c])
e_min_7 = Chord([e, g, b, d])
f_maj_7 = Chord([f, a, c, e])
g_7 = Chord([g, b, d, f])
a_min_7 = Chord([a, c, e, g])
b_dim_7 = Chord([b, d, f, a])

b_flat_maj_7 = Chord([b_flat, d, f, a])

e_7 = Chord([e, a_flat, b, d])
f_min_sharp_7 = Chord([f, a_flat, c, e])

def f_min_min(x_1, x_2, y_2):
    x_1 = d_min_7
    x_2 = e_7
    y_2 = f_maj_7

    xx_maximal_consonance_paths = get_scored_paths(x_1, x_2, maximal_consonance_score)
    xx_minimal_dissonance_paths = get_scored_paths(x_1, x_2, minimal_dissonance_score)

    xx_max_consonant_path = max(xx_maximal_consonance_paths, key=lambda triplet: triplet[2])
    xx_min_dissonant_path = min(xx_maximal_consonance_paths, key=lambda triplet: triplet[2])

    # Decision Point for x_2 permutation
    x_2 = xx_min_dissonant_path[1]
    # x_2 = xx_max_consonant_path[1]

    xy_maximal_consonance_paths = get_scored_paths(x_2, y_2, maximal_consonance_score)
    xy_minimal_dissonance_paths = get_scored_paths(x_2, y_2, minimal_dissonance_score)

    xy_max_consonant_path = max(xy_maximal_consonance_paths, key=lambda triplet: triplet[2])
    xy_min_dissonant_path = min(xy_maximal_consonance_paths, key=lambda triplet: triplet[2])

    # Decision Point for y_2 permutation
    y_2 = xy_min_dissonant_path[1]
    # y_2 = xy_max_consonant_path[1]

    # Complete the cycle
    y_1 = complete_cycle(x_1, x_2, y_2)

    return y_1

def f_min_max(x_1, x_2, y_2):
    x_1 = d_min_7
    x_2 = e_7
    y_2 = f_maj_7

    xx_maximal_consonance_paths = get_scored_paths(x_1, x_2, maximal_consonance_score)
    xx_minimal_dissonance_paths = get_scored_paths(x_1, x_2, minimal_dissonance_score)

    xx_max_consonant_path = max(xx_maximal_consonance_paths, key=lambda triplet: triplet[2])
    xx_min_dissonant_path = min(xx_maximal_consonance_paths, key=lambda triplet: triplet[2])

    # Decision Point for x_2 permutation
    x_2 = xx_min_dissonant_path[1]
    # x_2 = xx_max_consonant_path[1]

    xy_maximal_consonance_paths = get_scored_paths(x_2, y_2, maximal_consonance_score)
    xy_minimal_dissonance_paths = get_scored_paths(x_2, y_2, minimal_dissonance_score)

    xy_max_consonant_path = max(xy_maximal_consonance_paths, key=lambda triplet: triplet[2])
    xy_min_dissonant_path = min(xy_maximal_consonance_paths, key=lambda triplet: triplet[2])

    # Decision Point for y_2 permutation
    # y_2 = xy_min_dissonant_path[1]
    y_2 = xy_max_consonant_path[1]

    # Complete the cycle
    y_1 = complete_cycle(x_1, x_2, y_2)

    return y_1

def f_max_min(x_1, x_2, y_2):
    x_1 = d_min_7
    x_2 = e_7
    y_2 = f_maj_7

    xx_maximal_consonance_paths = get_scored_paths(x_1, x_2, maximal_consonance_score)
    xx_minimal_dissonance_paths = get_scored_paths(x_1, x_2, minimal_dissonance_score)

    xx_max_consonant_path = max(xx_maximal_consonance_paths, key=lambda triplet: triplet[2])
    xx_min_dissonant_path = min(xx_maximal_consonance_paths, key=lambda triplet: triplet[2])

    # Decision Point for x_2 permutation
    # x_2 = xx_min_dissonant_path[1]
    x_2 = xx_max_consonant_path[1]

    xy_maximal_consonance_paths = get_scored_paths(x_2, y_2, maximal_consonance_score)
    xy_minimal_dissonance_paths = get_scored_paths(x_2, y_2, minimal_dissonance_score)

    xy_max_consonant_path = max(xy_maximal_consonance_paths, key=lambda triplet: triplet[2])
    xy_min_dissonant_path = min(xy_maximal_consonance_paths, key=lambda triplet: triplet[2])

    # Decision Point for y_2 permutation
    y_2 = xy_min_dissonant_path[1]
    # y_2 = xy_max_consonant_path[1]

    # Complete the cycle
    y_1 = complete_cycle(x_1, x_2, y_2)

    return y_1

def f_max_max(x_1, x_2, y_2):
    x_1 = d_min_7
    x_2 = e_7
    y_2 = f_maj_7

    xx_maximal_consonance_paths = get_scored_paths(x_1, x_2, maximal_consonance_score)
    xx_minimal_dissonance_paths = get_scored_paths(x_1, x_2, minimal_dissonance_score)

    xx_max_consonant_path = max(xx_maximal_consonance_paths, key=lambda triplet: triplet[2])
    xx_min_dissonant_path = min(xx_maximal_consonance_paths, key=lambda triplet: triplet[2])

    # Decision Point for x_2 permutation
    # x_2 = xx_min_dissonant_path[1]
    x_2 = xx_max_consonant_path[1]

    xy_maximal_consonance_paths = get_scored_paths(x_2, y_2, maximal_consonance_score)
    xy_minimal_dissonance_paths = get_scored_paths(x_2, y_2, minimal_dissonance_score)

    xy_max_consonant_path = max(xy_maximal_consonance_paths, key=lambda triplet: triplet[2])
    xy_min_dissonant_path = min(xy_maximal_consonance_paths, key=lambda triplet: triplet[2])

    # Decision Point for y_2 permutation
    # y_2 = xy_min_dissonant_path[1]
    y_2 = xy_max_consonant_path[1]

    # Complete the cycle
    y_1 = complete_cycle(x_1, x_2, y_2)

    return y_1

x_1 = f_maj_7
x_2 = d_min_7
y_2 = a_min_7

print(f_min_min(x_1, x_2, y_2))
print(f_min_max(x_1, x_2, y_2))
print(f_max_min(x_1, x_2, y_2))
print(f_max_max(x_1, x_2, y_2))