def tuba_time(practice, performance):
    print(f"I spent {practice}, hours practicing.")
    print(f"I then had a {performance} hour concert to play.")

def tuba_ok(practice1, performance2):
    print(f"I get it! {practice1}, hours is a lot of time to practice.")
    print(f"And then you had a {performance2} hour performance!")

print("What did you do today?")
tuba_time(5, 2)

print("Wait, can you repeat that, I wasn't paying attention?")
practice = 5
performance = 2

tuba_time(practice, performance)

print("Sorry, I missed that again, my daughter was just screaming at me?")
print("Wait how many hours did you practice?")
practice = input()
print("And how long was the performance?")
performance = input()

tuba_time(practice, performance)

tuba_ok(5, 2)
