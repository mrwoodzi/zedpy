practice = ['Tuba', 'Contra-bass trombone', 'Contra-bari sax']
brown_note = ['28.23546hz', '31.635hz', '29.73674876hz']
brownnote_hertz = [28.23546, 31.635, 29.73674876]
hertz_change = [1.0, 1.0, 1.0]
print('\n')

for frequencies in brown_note:
   # print("\n")  for in cycles through every time so it adds a return to every line
    print(f'\tThis is a brown note frequency {frequencies}.')

print('\n')

for instruments in practice:
    print(f'\t{instruments} is an instrument that can hit the brown note.')


# Let's try to build a list
print("\n")
tubas = []

for increase in range(0, 3):
    print(f'\tYou can add more potential brown notes frequencies by adding {increase} hertz per frequency.')

print("\n")

# I am trying to add 2 lists together, Zed doesn't go over this yet so I did an interweb search
# I'm getting an error on add, don't know what to do 

# more_hertz = list(map(add, hertz_change, brownnote_hertz)) 
# my py didn't like add so let's try something else

more_hertz = [sum(i) for i in zip(brownnote_hertz, hertz_change)]  # I don't know what the i does in this
# It works this way, maybe because it's all kept in a list
for more in more_hertz:
    print(f"\t{more} is another brown note frequency that can be hit.")

