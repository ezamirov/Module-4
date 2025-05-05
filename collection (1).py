# Erbol Zamirov
# May 3, 2025

# Dictionary with authors and their year of death
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

# Description of what the code does
# This code creates a collection of authors and the years they died.
# For each author in the collection, it prints their name along with the year of their death.

# Loop through the dictionary and print each author's name and year of death
for author, date in authors.items():
    print(f"{author} died in {date}.")

