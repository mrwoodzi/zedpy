#Well this didn't run when I ran it and I had forgot about the (f) function so 
#the variable would be picked up by py
#Works the way I want it to now 
#These are Zed's examples
#I wrote code to run it as a complete file
#He only coded the boolean examples to be run individually
#>>>True and True
#True
Que_1 = True and True #true
print(f"1. true {Que_1}")
Que_2 = False and True #false
print(f"2. false {Que_2}")
Que_3 = 1 == 1 and 2 == 1 #false
print(f"3. false {Que_3}")
Que_4 = "test" == "test" #true
print(f"4. true {Que_4}")
Que_5 = 1 == 1 or 2 != 1 #true
print(f"5.true {Que_5}")
Que_6 = True and 1 == 1 #true
print(f"6.true {Que_6}")
Que_7 = False and 0 != 0 #false
print(f"7.false {Que_7}")
Que_8 = True or 1 == 1 #true
print(f"8. true {Que_8}")
Que_9 = "test" == "Testing" #false
print(f"9. false {Que_9}")
Que_10 = 1 != 0 and 2 == 1 #false
print(f"10. false {Que_10}")
Que_11 = "test" != "testing" #true
print(f"11. true {Que_11}")
Que_12 = "test" == 1 #false
print(f"12. false {Que_12}")
Que_13 = not (True and False) #true
print(f"13. true {Que_13}")
Que_14 = not (1 == 1 and 0 !=1) #false
print(f"14. false {Que_14}")
Que_15 = not (10 == 1 or 1000 == 1000) #false
print(f"15. false {Que_15}")
Que_16 = not(1 != 10 or 3 or 4) #false
print(f"16. false {Que_16}")
Que_17 = not("testing" == "testing" and "Zed" == "Cool Guy") #true
print(f"17. true {Que_17}")
Que_18 = 1 == 1 and (not ("testing" == 1 or  1 == 0)) #true
print(f"18. true {Que_18}")
Que_19 = "chunky" == "bacon" and (not(3 == 4 or 3 == 3)) #false
print(f"19. false {Que_19}")
Que_20 = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) #false
print(f"20. false {Que_20}")
