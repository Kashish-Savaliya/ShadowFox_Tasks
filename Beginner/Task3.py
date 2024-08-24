justice_league = ["Superman", "Batman", "Wonder woman", "Flash", "Aquaman", "Green Lantern"]

# 1
print(f"The total members in justice_league are {len(justice_league)}")

# 2
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print(justice_league)

# 3
wonderwoman_idx = justice_league.index("Wonder woman")
# Move wonder woman to first index
justice_league.insert(0, justice_league.pop(wonderwoman_idx))
print(justice_league)

# 4
flash_idx = justice_league.index("Flash")
green_idx = justice_league.index("Green Lantern")
# Insert Green Lantern between Flash and Aquaman
justice_league.insert(flash_idx + 1, justice_league.pop(green_idx))
print(justice_league)


# 5
new_list = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
# replace the old list with new_list
justice_league[0:] = new_list
print(justice_league)

# 6
justice_league.sort()
print(justice_league)
print(f"The hero of the league is {justice_league[0]}")
