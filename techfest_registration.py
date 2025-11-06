print ("Welcome to SMIT TechFest!")
print ("Event organized by Sean Athan Scott L. Ibay of APPDAET BTCS2\n")

try:
    num_participants = int(input("How many participants will register? "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

if num_participants <= 0:
    print("Invalid number of participants.")
    exit()

participants = []

for i in range (num_participants):
    name = input ("Enter participant name: ").strip()
    track = input ("Enter chosen track: ").strip()
    participants.append({"name": name, "track": track})

print("\nRegistered participants:")
for i, p in enumerate(participants, start=1):
    print(f"{i}. {p['name']} - {p['track']}")

unique_tracks = {p["track"] for p in participants}

if len(unique_tracks) < 2:
    print("\nNot enough variety in tracks.")
else:
    print("\nTracks offered in this event:")
    print(", ".join(unique_tracks))

seen_names = set()
duplicates = set()

for p in participants:
    name = p["name"]
    if name in seen_names:
        duplicates.add(name)
    else:
        seen_names.add(name)

if duplicates:
    for name in duplicates:
        print (f"\nDuplicate name found: {name}")

else:
    print("\nNo duplicate names.")