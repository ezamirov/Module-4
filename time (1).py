# Erbol Zamirov
# May 3, 2025
# Taking input for current time and wait time
currentTimeStr = input("What is the current time (in hours 0-23)? ")
waitTimeStr = input("How many hours do you want to wait? ")

# Convert the inputs into integers
currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)

# Calculate the final time
finalTimeInt = currentTimeInt + waitTimeInt

# Adjust for times beyond 24 hours
finalTimeInt = finalTimeInt % 24

# Print the final time
print("The final time is: ", finalTimeInt)
