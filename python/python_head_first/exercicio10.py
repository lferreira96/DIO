# resolução do site
print(len(__import__("re").findall(r"[a-zA-Z]+", "Turmoil has engulfed the Galactic Republic. The\ntaxation of trade routes to outlying star systems is in\ndispute. Hoping to resolve the matter with a blockade of deadly\nbattleships, the greedy Trade Federation has stopped all shipping to\nthe small planet of Naboo. While the congress of the Republic\nendlessly debates this alarming chain of events, the Supreme\nChancellor has secretly dispatched two Jedi Knights, the guardians of\npeace and justice in the galaxy, to settle the conflict")))

# minha resolução

#!/usr/bin/env python3

whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object oriented programming. This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. For a description of standard objects and modules..."

# Enter your code below:

DADOS = whetting_your_appetite.split()
print(len(DADOS))
