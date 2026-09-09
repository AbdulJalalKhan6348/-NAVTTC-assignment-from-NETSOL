#Line Plot
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [25, 27, 26, 30, 29]

plt.plot(days, temperature, color="red", linestyle="--")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.grid(True)
plt.title("Temperature During the Week")
plt.show()

# Change line to solid and color to red

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [25, 27, 26, 30, 29]

plt.plot(days, temperature, color="red", linestyle="-", marker="o")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.grid(True)
plt.title("Temperature During the Week")
plt.show()

# Use triangle markers and remove grid

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [25, 27, 26, 30, 29]

plt.plot(days, temperature, color="red", linestyle="-", marker="^")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Temperature During the Week")
plt.show()

# # Add two temperature lines (e.g., this week vs last week)

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

this_week = [25, 27, 26, 30, 29]
last_week = [23, 25, 24, 28, 27]

plt.plot(days, this_week, color="red", marker="^", label="This Week")
plt.plot(days, last_week, color="blue", linestyle='--' ,  marker="o", label="Last Week")

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Temperature Comparison")
plt.legend()
plt.show()
# Reverse the temperature list with one graph
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [25, 27, 26, 30, 29]

reversed_temperature = temperature[::-1]

plt.plot(days, reversed_temperature, color="red", marker="o")

plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("Reversed Temperature")
plt.show()

# Custom figure size and font sizes
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [25, 27, 26, 30, 29]

plt.figure(figsize=(10, 6))

plt.plot(days, temperature, color="red", marker="o")

plt.xlabel("Day", fontsize=14)
plt.ylabel("Temperature", fontsize=14)
plt.title("Temperature During the Week", fontsize=18)

plt.show()

#Bar Chart
#Clinic Visits Per Day
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visits = [25, 35, 20, 40, 30]

plt.bar(days, visits)

plt.xlabel("Day")
plt.ylabel("Clinic Visits")
plt.title("Clinic Visits Per Day")

plt.show()

# Change bar color to blue and adjust bar width

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visits = [25, 35, 20, 40, 30]

plt.bar(days, visits, color="blue", width=0.5)

plt.xlabel("Day")
plt.ylabel("Clinic Visits")
plt.title("Clinic Visits Per Day")

plt.show()

# Flip the bars horizontally
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visits = [25, 35, 20, 40, 30]

plt.barh(days, visits, color="blue", height=0.5)

plt.xlabel("Clinic Visits")
plt.ylabel("Day")
plt.title("Clinic Visits Per Day")

plt.show()

# Add numeric labels above each bar

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visits = [25, 35, 20, 40, 30]

plt.bar(days, visits, color="blue", width=0.5)

for i, value in enumerate(visits):
    plt.text(i, value, str(value), ha="center", va="bottom")

plt.xlabel("Day")
plt.ylabel("Clinic Visits")
plt.title("Clinic Visits Per Day")

plt.show()

# Add value labels

import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visits = [25, 35, 20, 40, 30]

plt.bar(days, visits, color="blue")

for i, value in enumerate(visits):
    plt.text(i, value, str(value), ha="center", va="bottom")

plt.xlabel("Day")
plt.ylabel("Clinic Visits")
plt.title("Clinic Visits Per Day")

plt.show()

