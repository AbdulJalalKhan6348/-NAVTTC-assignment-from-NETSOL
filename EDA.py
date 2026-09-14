# TODO: Import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
# Also set sns theme to 'whitegrid' and default figure size to (10,5)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 5)

# TODO: Load the Auto-MPG dataset from the UCI repository URL below.
# Column names: ['mpg','cylinders','displacement','horsepower','weight',
#                'acceleration','model_year','origin','car_name']
# Missing values are marked with '?'
# URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
col_names = ['mpg','cylinders','displacement','horsepower','weight',
             'acceleration','model_year','origin','car_name']

#df = # TODO: read_csv with correct separator (\s+) and na_values
df = pd.read_csv(
    url,
    sep=r"\s+",
    names=col_names,
    na_values="?"
)


print("Shape:", df.shape)
df.head()
# TODO: Print df.info() to inspect dtypes and non-null counts
df.info()

# TODO: Print df.describe() to view summary statistics
df.describe()

# TODO: Check and print missing values per column
# Then drop all rows that contain NaN values (they are < 2% of data)

print(df.isna().sum())

df = df.dropna()

print("\nShape after dropping missing values:", df.shape)
# TODO: Check for and remove duplicate rows

print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)
# TODO:
# 1. Convert 'cylinders' and 'model_year' to category dtype
# 2. Map 'origin' from {1,2,3} to {'usa','europe','japan'}
# 3. Strip & lowercase 'car_name'

# 1. Convert cylinders and model_year to category dtype
df['cylinders'] = df['cylinders'].astype('category')
df['model_year'] = df['model_year'].astype('category')

# 2. Map origin codes to region names
df['origin'] = df['origin'].map({
    1: 'usa',
    2: 'europe',
    3: 'japan'
}).astype('category')

# 3. Strip whitespace and lowercase car names
df['car_name'] = df['car_name'].str.strip().str.lower()
# TODO: Create two lists:
# cat_cols — categorical column names (cylinders, origin, model_year)
# num_cols — numerical column names (mpg, displacement, horsepower, weight, acceleration)

cat_cols = []   # fill in
num_cols = []   # fill in
cat_cols = ['cylinders', 'origin', 'model_year']

num_cols = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']

# TODO: Create 'mpg_level' column using pd.cut()
# Bins: [0,17) → 'low', [17,29) → 'medium', [29, max] → 'high'

df['mpg_level'] = pd.cut(
    df['mpg'],
    bins=[0, 17, 29, df['mpg'].max()],
    labels=['low', 'medium', 'high'],
    right=False
)
# TODO: Create 'car_company' by extracting the first word from 'car_name'
df['car_company'] = df['car_name'].str.split().str[0]

# TODO: Plot a countplot for each of: origin, cylinders, mpg_level, model_year
# Arrange them in a 2×2 grid of subplots

fig, axes = plt.subplots(2, 2, figsize=(10, 5))

sns.countplot(data=df, x='origin', ax=axes[0, 0])
axes[0, 0].set_title('Origin')

sns.countplot(data=df, x='cylinders', ax=axes[0, 1])
axes[0, 1].set_title('Cylinders')

sns.countplot(data=df, x='mpg_level', ax=axes[1, 0])
axes[1, 0].set_title('MPG Level')

sns.countplot(data=df, x='model_year', ax=axes[1, 1])
axes[1, 1].set_title('Model Year')

plt.tight_layout()
plt.show()
# TODO: Print the proportion (%) of the dominant class for
# origin, cylinders, and mpg_level
for col in ['origin', 'cylinders', 'mpg_level']:
    dominant_proportion = df[col].value_counts(normalize=True).max() * 100
    print(f"{col}: {dominant_proportion:.2f}%")

# TODO: Create a crosstab of cylinders vs origin and visualise as a bar chart

# Create crosstab
ct = pd.crosstab(df['cylinders'], df['origin'])

# Visualise as a bar chart
ct.plot(kind='bar', figsize=(10, 5))

plt.title('Cylinders by Origin')
plt.xlabel('Cylinders')
plt.ylabel('Count')
plt.legend(title='Origin')
plt.tight_layout()
plt.show()
# TODO: Plot a countplot of mpg_level grouped by origin (use hue='mpg_level')

plt.figure(figsize=(10, 5))

sns.countplot(
    data=df,
    x='origin',
    hue='mpg_level'
)

plt.title('MPG Level by Origin')
plt.xlabel('Origin')
plt.ylabel('Count')
plt.legend(title='MPG Level')
plt.tight_layout()
plt.show()
# TODO: For each numerical column plot:
#   (a) Histogram + KDE  (b) Boxplot
# Arrange in a grid (n_cols rows × 2 columns)

n_cols = len(num_cols)

fig, axes = plt.subplots(n_cols, 2, figsize=(10, 4 * n_cols))

for i, col in enumerate(num_cols):
    # (a) Histogram + KDE
    sns.histplot(df[col], kde=True, ax=axes[i, 0])
    axes[i, 0].set_title(f'{col} - Histogram + KDE')
    
    # (b) Boxplot
    sns.boxplot(x=df[col], ax=axes[i, 1])
    axes[i, 1].set_title(f'{col} - Boxplot')

plt.tight_layout()
plt.show()
# TODO: Write a function tukey_outliers(series) that returns the outlier values
# using the IQR (Tukey) rule: Q1 - 1.5*IQR  and  Q3 + 1.5*IQR
# Then print the outlier count for each numerical column

def tukey_outliers(series):
    # TODO: implement
    pass
def tukey_outliers(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    
    return series[(series < lower_bound) | (series > upper_bound)]

for col in num_cols:
    outliers = tukey_outliers(df[col])
    print(f"{col}: {len(outliers)} outliers")

# TODO: Plot a correlation heatmap for all numerical columns (use annot=True)
plt.figure(figsize=(10, 5))

corr = df[num_cols].corr()

sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')

plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# TODO: Create a pairplot of numerical columns, coloured by mpg_level

sns.pairplot(
    df,
    vars=num_cols,
    hue='mpg_level',
    diag_kind='hist'
)

plt.show()
# TODO: Plot boxenplots of all numerical features grouped by 'origin'
# (1 row × 5 column subplot grid)

fig, axes = plt.subplots(1, 5, figsize=(20, 5))

for ax, col in zip(axes, num_cols):
    sns.boxenplot(data=df, x='origin', y=col, ax=ax)
    ax.set_title(f'{col} by Origin')
    ax.set_xlabel('Origin')
    ax.set_ylabel(col)

plt.tight_layout()
plt.show()
# TODO: Plot violinplots of all numerical features grouped by 'mpg_level'

fig, axes = plt.subplots(1, len(num_cols), figsize=(20, 5))

for ax, col in zip(axes, num_cols):
    sns.violinplot(data=df, x='mpg_level', y=col, ax=ax)
    ax.set_title(f'{col} by MPG Level')
    ax.set_xlabel('MPG Level')
    ax.set_ylabel(col)

plt.tight_layout()
plt.show()
# TODO: Plot a line chart showing mean mpg per model_year

mean_mpg = df.groupby('model_year', observed=True)['mpg'].mean()

plt.figure(figsize=(10, 5))
plt.plot(mean_mpg.index, mean_mpg.values, marker='o')

plt.title('Mean MPG per Model Year')
plt.xlabel('Model Year')
plt.ylabel('Mean MPG')
plt.grid(True)
plt.tight_layout()
plt.show()
