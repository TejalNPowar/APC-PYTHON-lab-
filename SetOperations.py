days={"Mon","Tue","Wed","Thu","Fri","Sat","Sun"}
print("Days of the week:", days)
# Adding a new day
days.add("Funday")
print("After adding a new day:", days)
# Removing a day
days.remove("Funday")
print("After removing a day:", days)


#declaring set in a different way
days2=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
print("Days of the week (from list):", days2)

# Union of two sets
weekdays = {"Mon", "Tue", "Wed", "Thu", "Fri"}
weekend = {"Sat", "Sun"}
all_days = weekdays.union(weekend)
print("All days of the week (union):", all_days)

# Intersection of two sets
workdays = {"Mon", "Tue", "Wed", "Thu", "Fri"}
workoffdays = {"Sat", "Sun"}
workdays_and_weekend = workdays.intersection(workoffdays)
print("Workdays and weekend (intersection):", workdays_and_weekend)


