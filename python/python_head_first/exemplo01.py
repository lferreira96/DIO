'''def print_even_numbers(start, stop):
    for x in range(start,stop):
        if (x%2==0):
            print("{}".format(x))

print_even_numbers(0,10)
'''
def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9


def celsius_to_fahrenheit(temp):
    return temp * 9/5 + 32

print(fahrenheit_to_celsius(212))
print(celsius_to_fahrenheit(100))
