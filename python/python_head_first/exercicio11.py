'''

# resolução do site
from math import pi


def circle_perimeter(radius):
    return 2 * pi * radius


if __name__ == "__main__":
    print(circle_perimeter(1))

'''

'''
# primeira resolução

# Type your code here:
import math

def circle_perimeter(radius):
    return (radius * math.pi)*2

print(circle_perimeter(1))
print(circle_perimeter(10))
print(circle_perimeter(100))

'''
# resolução incluindo o from

# Type your code here:
from math import pi

def circle_perimeter(radius):
    return (radius * pi)*2

print(circle_perimeter(1))
print(circle_perimeter(10))
print(circle_perimeter(100))