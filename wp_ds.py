# TODO: Import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns 
# Also set sns theme to 'whitegrid' and default figure size to (10,5) 

# Data manipulation 
import pandas as pd
import numpy as np 

# Data visualization 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Visualization settings 
sns.set_theme(style="whitegrid") 
plt.rcParams["figure.figsize"] = (10, 5)
# Load the dataset
#df = pd.read_csv('world_population.csv')
df = pd.read_csv(r"C:\Users\jalal1122\Desktop\world_population.csv")


# View the first few rows
print("Dataset Head:")
print(df.head())

# Shape of the dataset
print(f"\nDimensions: {df.shape[0]} rows, {df.shape[1]} columns")

# Dataset Summary / Data Types
print("\nDataset Info:")
df.info()

# Summary statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())

# 1. Check missing values per column and drop NaNs
print("Missing values per column:")
print(df.isnull().sum())
df = df.dropna()

# 2. Check for and remove duplicate rows
print(f"Duplicates found: {df.duplicated().sum()}")
df = df.drop_duplicates()

# 3. Clean string text and set categorical types
df['Continent'] = df['Continent'].astype('category')
df['Country/Territory'] = df['Country/Territory'].str.strip().str.lower()

# 4. Define categorical and numerical column lists
cat_cols = ['CCA3', 'Country/Territory', 'Capital', 'Continent']
num_cols = [
    'Rank', '2022 Population', '2020 Population', '2015 Population', 
    '2010 Population', '2000 Population', '1990 Population', 
    '1980 Population', '1970 Population', 'Area (km²)', 
    'Density (per km²)', 'Growth Rate', 'World Population Percentage'
]
# Create population growth feature over 22 years (2000 to 2022)
df['Population_Growth_2000_2022'] = df['2022 Population'] - df['2000 Population']

# Categorize population density into levels (Low, Medium, High)
df['Density_Level'] = pd.cut(
    df['Density (per km²)'], 
    bins=[-1, 50, 150, float('inf')], 
    labels=['Low', 'Medium', 'High']
)

# Display sample output
print(df[['Country/Territory', '2022 Population', 'Population_Growth_2000_2022', 'Density_Level']].head())

#Task 5 — Categorical EDA
# Categorical Feature Engineering for world_population dataset
df['Area_Category'] = pd.cut(df['Area (km²)'], bins=[-1, 10000, 100000, 1000000, np.inf], labels=['Very Small', 'Small', 'Medium', 'Large'])
df['Density_Level'] = pd.cut(df['Density (per km²)'], bins=[-1, 50, 150, np.inf], labels=['Low', 'Medium', 'High'])
df['Growth_Category'] = pd.cut(df['Growth Rate'], bins=[-np.inf, 1.00, 1.01, np.inf], labels=['Low/Negative', 'Moderate', 'High'])

# 1. Grid of Subplots (2x2)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.countplot(data=df, x='Continent', ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title('Countries by Continent')
axes[0, 0].tick_params(axis='x', rotation=30)

sns.countplot(data=df, x='Density_Level', ax=axes[0, 1], palette='plasma')
axes[0, 1].set_title('Countries by Density Level')

sns.countplot(data=df, x='Area_Category', ax=axes[1, 0], palette='magma')
axes[1, 0].set_title('Countries by Area Category')

sns.countplot(data=df, x='Growth_Category', ax=axes[1, 1], palette='coolwarm')
axes[1, 1].set_title('Countries by Growth Category')

plt.tight_layout()
plt.show()
# 2. Print Proportion (%) of Dominant Classes
print("--- Dominant Class Proportions ---")
for col in ['Continent', 'Density_Level', 'Area_Category']:
    dominant_class = df[col].value_counts().idxmax()
    proportion = df[col].value_counts(normalize=True).max() * 100
    print(f"Dominant class for '{col}': {dominant_class} ({proportion:.2f}%)")
    # 3. Crosstab & Bar Chart Visualization
density_continent_ct = pd.crosstab(df['Density_Level'], df['Continent'])
print("\n--- Crosstab: Density Level vs Continent ---")
print(density_continent_ct)

density_continent_ct.plot(kind='bar', figsize=(10, 5), colormap='Set2')
plt.title('Density Level Distribution across Continents')
plt.xlabel('Density Level')
plt.ylabel('Number of Countries')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# 4. Countplot of Density Level grouped by Continent
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Continent', hue='Density_Level', palette='Set1')
plt.title('Density Level Grouped by Continent')
plt.xlabel('Continent')
plt.ylabel('Count')
plt.tick_params(axis='x', rotation=30)
plt.tight_layout()
plt.show()

#Task 6 — Numerical EDA
# 1. Histograms + KDE and Boxplots in a grid (n_cols rows x 2 columns)
n_rows = len(num_cols)
fig, axes = plt.subplots(n_rows, 2, figsize=(12, 4 * n_rows))

for i, col in enumerate(num_cols):
    # Histogram + KDE
    sns.histplot(df[col], kde=True, ax=axes[i, 0], color='skyblue')
    axes[i, 0].set_title(f'Distribution of {col}')
    
    # Boxplot
    sns.boxplot(x=df[col], ax=axes[i, 1], color='salmon')
    axes[i, 1].set_title(f'Boxplot of {col}')

plt.tight_layout()
plt.show()

# 2. Tukey Outliers Function (IQR Rule)
def tukey_outliers(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return series[(series < lower_bound) | (series > upper_bound)]

# Print outlier counts per numerical column
print("--- Outlier Counts per Numerical Column (Tukey Rule) ---")
for col in num_cols:
    outliers = tukey_outliers(df[col])
    print(f"{col}: {len(outliers)} outliers")

# 3. Correlation Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(df[num_cols].corr(), annot=True, fmt=".2f", cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()
plt.show()
# 4. Pairplot of selected key numerical columns colored by Density Level
key_num_cols = ['2022 Population', 'Area (km²)', 'Density (per km²)', 'Growth Rate']
sns.pairplot(df[key_num_cols + ['Density_Level']], hue='Density_Level', palette='Set1')
plt.suptitle('Pairplot of Numerical Columns Grouped by Density Level', y=1.02)
plt.show()

#7 — Numerical vs Categorical
# 1. Boxenplots of numerical features grouped by categorical region ('Continent')
fig, axes = plt.subplots(
    1, len(num_cols), figsize=(4 * len(num_cols), 5), squeeze=False
)
axes = axes.flatten()

for i, col in enumerate(num_cols):
    sns.boxenplot(
        data=df,
        x="Continent",
        y=col,
        ax=axes[i],
        hue="Continent",
        palette="Set2",
        legend=False,
    )
    axes[i].set_title(f"{col} by Continent")
    axes[i].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
# 2. Violinplots of numerical features grouped by categorical level ('Density_Level')
fig, axes = plt.subplots(
    1, len(num_cols), figsize=(4 * len(num_cols), 5), squeeze=False
)
axes = axes.flatten()

for i, col in enumerate(num_cols):
    sns.violinplot(
        data=df,
        x="Density_Level",
        y=col,
        ax=axes[i],
        hue="Density_Level",
        palette="Set3",
        inner="quartile",
        legend=False,
    )
    axes[i].set_title(f"{col} by Density Level")
    axes[i].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.show()
# 3. Line chart showing mean population per census year across history
pop_cols = [
    "1970 Population",
    "1980 Population",
    "1990 Population",
    "2000 Population",
    "2010 Population",
    "2015 Population",
    "2020 Population",
    "2022 Population",
]
years = [1970, 1980, 1990, 2000, 2010, 2015, 2020, 2022]
mean_pop_by_year = df[pop_cols].mean()

plt.figure(figsize=(10, 5))
plt.plot(
    years,
    mean_pop_by_year / 1e6,
    marker="o",
    color="crimson",
    linewidth=2,
    markersize=8,
)
plt.title("Mean Global Country Population Over Time (1970–2022)")
plt.xlabel("Year")
plt.ylabel("Mean Population (in Millions)")
plt.xticks(years)
plt.grid(True)
plt.tight_layout()
plt.show()