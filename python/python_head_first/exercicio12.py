def print_even_numbers(start, stop):
    for i in range(start + start%2, stop, 2): # range(inicio,fim,passo)
        print(i)


print_even_numbers(0,10)