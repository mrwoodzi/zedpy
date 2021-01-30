practice = ['Tuba', 'Contra-bass trombone', 'Contra-bari sax']
brown_note = ['28.23546hz', '31.635hz', '29.73674876hz']
brownnote_hertz = [28.23546, 31.635, 29.73674876]
hertz_change = [1.0, 1.0, 1.0]
print('\n')

for frequencies in brown_note:
    print("\n") # for in cycles through every time so it adds a return to every line
    print(f'\tThis is a brown note frequency {frequencies}.')

print('\n')

for instruments in practice:
    print(f'\t{instruments} is an instrument that can hit the brown note.')


# Let's try to build a list

tubas = []

for increase in range(0, 3):
    print(f'\tYou can add more potential brown notes frequencies by adding {increase} hertz per frequency.')

more_hertz = list(map(add, hertz_change, brownnote_hertz)) 

