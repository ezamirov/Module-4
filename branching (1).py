# Erbol Zamirov
# May 3, 2025
# # Ask the traveler for their year of origin
year = int(input("Greetings! What is your year of origin? "))

# Conditional checks to determine the time period
if year < 1900:
    print("Woah, that's the past!")
elif 1900 <= year <= 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")
2