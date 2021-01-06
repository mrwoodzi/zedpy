tuba = 40
trombones = 20
trumpets = 20
french_horns = 20
tuba_players_sick = 10
trombone_players_sick = 5
french_horns_players_sick = 0
trumpets_players_sick = 0
Number_of_band_members_sick = tuba_players_sick + trombone_players_sick + french_horns_players_sick + trumpets_players_sick
Number_of_tuba_players_at_football_game = tuba - tuba_players_sick
Number_of_trombone_players_at_football_game = trombones - trombone_players_sick
Total_number_band_members_attending_game = tuba + trombones + trumpets + french_horns - tuba_players_sick - trombone_players_sick


print("The band will be missing a number of players for the football game.")
print("How may will be missing?")
print("There will be", Number_of_band_members_sick, "members of the band out.")
print("Will there be any tubas absent?")
print("Yes", tuba_players_sick)
print("How many trombones?")
print(trombone_players_sick)
print("Any french horns or trumpets?")
print("No.")
print("What's the total number of band students attending the game?")
print(Total_number_band_members_attending_game)
