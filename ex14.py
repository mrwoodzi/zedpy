from sys import argv

script, user_name = argv # the variable user_name is called a value in powershell
prompt = '< '

print(f"Hi {user_name}, I'm the {script} script.") # f stnads for function? has to be there so atom knows there are variables
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?") #f
likes = input(prompt)

print(f"Where do yo live {user_name}?") #f-
lives = input(prompt)

print("What kind of computer do you have?")#f
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
