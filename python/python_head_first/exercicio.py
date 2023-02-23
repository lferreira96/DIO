import string
x = list(string.ascii_lowercase)
for y in x:
    for z in x:
        print('{}{}'.format(y,z))
