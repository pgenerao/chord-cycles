from main import *

# Completing chord paths

x1 = Chord([c, a, f, d])
x2 = Chord([b, g, f, d])
y2 = Chord([b, g, e, c])

c_maj_7 = Chord([c, e, g, b])
d_min_7 = Chord([d, f, a, c])
e_min_7 = Chord([e, g, b, d])
f_maj_7 = Chord([f, a, c, e])
g_7 = Chord([g, b, d, f])
a_min_7 = Chord([a, c, e, g])
b_dim_7 = Chord([b, d, f, a])

x1 = d_min_7
x2 = c_maj_7
y2 = d_min_7

print(x1)
print(x2)
print(y2)
print(complete_cycle(x1, x2, y2))