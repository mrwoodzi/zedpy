people = 40
cars = 40
trucks = 40

#Is testing wether something is true and if so prints that
if cars > people: #asks if this is true, in this case yes so prints "We should take the cars."
    print("We should take the cars.")
elif cars < people: 
    print("We should not take the cars.")
else: #if neither of the above are true print this
    print("We can't decide.")
#repeats the above process 
if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")