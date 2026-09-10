#Multi-Line Plot with Matplotlib
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
product_a = [15, 18, 14, 22, 25, 28]
product_b = [10, 13, 16, 18, 20, 24]

plt.plot(months, product_a, color='blue', marker='o', label='Product A')

plt.plot(months, product_b, color='red', marker='s', label='Product B')

plt.title('Product Sales Over Months')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.legend()
plt.grid(True)

plt.show()

#Grouped Bar Chart with Matplotlib

import numpy as np

subjects = ['Math', 'Science', 'English', 'History']
class_a  = [72, 85, 78, 65]
class_b  = [68, 80, 74, 70]

# Create x positions using np.arange
x = np.arange(len(subjects))

# Set bar width
width = 0.35

# Plot Class A bars (offset left)
bars_a = plt.bar(x - width/2, class_a, width, label='Class A', color='blue')

# Plot Class B bars (offset right)
bars_b = plt.bar(x + width/2, class_b, width, label='Class B', color='orange')

# Add value labels above each bar
for bar in bars_a:
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 1,
             str(bar.get_height()),
             ha='center')

for bar in bars_b:
    plt.text(bar.get_x() + bar.get_width()/2,
             bar.get_height() + 1,
             str(bar.get_height()),
             ha='center')

# Add title and axis labels
plt.title('Class A vs Class B Scores')
plt.xlabel('Subjects')
plt.ylabel('Scores')

# Add x-tick labels
plt.xticks(x, subjects)

# Add legend
plt.legend()

plt.show()

#Histogram Analysis with Matplotlib

scores = [45, 55, 60, 62, 65, 65, 68, 70, 70, 72,
          75, 75, 78, 80, 82, 85, 88, 90, 92, 95]

plt.figure(figsize=(12, 4))

# Part A: Histogram with 5 bins (subplot 1)
plt.subplot(1, 2, 1)
plt.hist(scores, bins=5, color='blue', edgecolor='black')
plt.title('Histogram with 5 Bins')
plt.xlabel('Scores')
plt.ylabel('Frequency')

# Part B: Histogram with 10 bins (subplot 2)
plt.subplot(1, 2, 2)
plt.hist(scores, bins=10, color='green', edgecolor='black')
plt.title('Histogram with 10 Bins')
plt.xlabel('Scores')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

#Dashboard of 4 Plots with Matplotlib Subplots
months     = ['Jan','Feb','Mar','Apr','May','Jun']
sales      = [200, 240, 180, 300, 350, 320]

cities     = ['Karachi','Lahore','Islamabad','Peshawar']
population = [16, 13, 2, 4]   # millions

hours      = [1, 2, 3, 4, 5, 6, 7, 8]
grades     = [50, 55, 60, 65, 72, 78, 85, 90]

categories = ['Food', 'Rent', 'Transport', 'Entertainment']
expenses   = [40, 30, 15, 15]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Top-left: line plot of sales over months
axes[0, 0].plot(months, sales, marker='o', color='blue')
axes[0, 0].set_title('Monthly Sales')
axes[0, 0].set_xlabel('Month')
axes[0, 0].set_ylabel('Sales')

# Top-right: bar chart of city populations
axes[0, 1].bar(cities, population, color='green')
axes[0, 1].set_title('City Population')
axes[0, 1].set_xlabel('City')
axes[0, 1].set_ylabel('Population (millions)')

# Bottom-left: scatter plot of hours vs grades
axes[1, 0].scatter(hours, grades, color='red')
axes[1, 0].set_title('Study Hours vs Grades')
axes[1, 0].set_xlabel('Study Hours')
axes[1, 0].set_ylabel('Grades')

# Bottom-right: pie chart of expenses
axes[1, 1].pie(expenses, labels=categories, autopct='%1.1f%%')
axes[1, 1].set_title('Expenses')

fig.suptitle("Monthly Dashboard", fontsize=14)
plt.tight_layout()
plt.show()

tips = sns.load_dataset('tips')

# Part 1: Scatter plot colored by smoker status
sns.scatterplot(
    data=tips,
    x='total_bill',
    y='tip',
    hue='smoker'
)

plt.title('Total Bill vs Tip by Smoker Status')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()


# Part 2: Regression plot (total_bill vs tip)
sns.regplot(
    data=tips,
    x='total_bill',
    y='tip'
)

plt.title('Regression Plot: Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

#Seaborn Scatter Plot with Regression Line

import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset('tips')

# Part 1: Scatter plot
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker')
plt.title('Total Bill vs Tip by Smoker Status')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()

# Part 2: Regression plot
sns.regplot(data=tips, x='total_bill', y='tip')
plt.title('Regression Plot: Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
