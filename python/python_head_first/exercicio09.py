'''
# Resposta do site
import random

the_list = [143266561, 1738152473, 312377936, 1027708881, 1495785517,
            1858250798, 1693786723, 1871655963, 374455497, 430158267]

# Let's invent some different algorithms for fun
ALGORITHMS = (
    # Total simplification
    lambda: 1871655963,
    # Some real solution (not very interesting)
    lambda: max(the_list),
    # Random try
    lambda: (lambda f: f(f))(lambda g: 1871655963 if random.choice(the_list) == 1871655963 else g(g)),
    # Useless For and If
    lambda: [number for number in the_list if number == max(the_list)][0],
)
# Pick a random algorithm and use it
print(ALGORITHMS[random.randint(0,len(ALGORITHMS)-1)]())


# Minha primeira resposta


the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]

maior = 0
for i in the_list:
    if (i>maior):
        maior = i
print(maior)

'''
# minha segunda resposta
the_list = [143266561, 1738152473, 312377936, 1027708881, 1871655963,
            1495785517, 1858250798, 1693786723, 374455497, 430158267]

print(max(the_list))
