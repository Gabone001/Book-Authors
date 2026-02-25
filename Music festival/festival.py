# music festival
# gabriel mihail
# create a program with a music festival, 2 lists name and duration, loads data, make changes, print table



names = []
durations = []

# >>>>>>>>>>>>>>>>>>>>>>>>
# Read file and store data
# >>>>>>>>>>>>>>>>>>>>>>>>

try:
    with open("performers.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                name, duration = line.split(",")
                names.append(name)
                durations.append(int(duration))
except FileNotFoundError:
    print("Error: performers.txt file not found.")
    exit()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Allow user to update a performer's duration
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

search_name = input("Enter performer name to update: ")

if search_name in names:
     index = names.index(search_name)
     try:
         new_duration = int(input("Enter new performance duration (minutes): "))
         durations[index] = new_duration
         print("Performance duration updated successfully.")
     except ValueError:
         print("Invalid duration entered. No changes made.")
else:
     print("Performer not found.")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Display formatted summary table
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print("\nFestival Performance Summary")
print("-" * 65)
print(f"{'Performer Name':35} {'Duration':10} {'Performance Type':15}")
print("-" * 65)

# for i in range(len(names)):
#     # Determine performance type directly (no function)
#     if durations[i] <= 30:
#         performance_type = "Opening Act"
#     elif durations[i] <= 60:
#         performance_type = "Main Set"
#     else:
#         performance_type = "Headliner"
#
#     print(f"{names[i]:35} {durations[i]:10} {performance_type:15}")
#
# print("-" * 65)