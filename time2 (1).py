# Erbol Zamirov
# May 3, 2025
# Input the current time and wait time
str_time = input("What time is it now? (0-23) ")
str_wait_time = input("What is the number of hours to wait? ")

# Convert the inputs to integers
time = int(str_time)
wait_time = int(str_wait_time)

# Calculate when the alarm will go off
time_when_alarm_go_off = (time + wait_time) % 24  # Use modulo to handle times beyond 24 hours

# Print the result
print("The alarm will go off at:", time_when_alarm_go_off)