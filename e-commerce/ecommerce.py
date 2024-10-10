import pandas as pd

# Load dataset
data = pd.read_csv('/mnt/data/sample_customer_data_for_exam.csv')

# Display the first few rows of the dataset
print(data.head())

# Summary statistics for numerical columns
print(data.describe())
import seaborn as sns
import matplotlib.pyplot as plt

# Filter numerical columns
numerical_cols = data.select_dtypes(include=['float64', 'int64'])

# Create a correlation matrix
corr_matrix = numerical_cols.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Variables')
plt.show()
# Create histograms for 'age' and 'income' columns
plt.figure(figsize=(12, 5))

# Age histogram
plt.subplot(1, 2, 1)
plt.hist(data['age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Income histogram
plt.subplot(1, 2, 2)
plt.hist(data['income'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
# Generate box plot for 'purchase_amount' across 'product_category'
plt.figure(figsize=(10, 6))
sns.boxplot(x='product_category', y='purchase_amount', data=data)
plt.title('Purchase Amount Distribution by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Purchase Amount')
plt.xticks(rotation=45)
plt.show()
# Create a pie chart to visualize gender distribution
plt.figure(figsize=(6, 6))
gender_counts = data['gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.title('Customer Gender Distribution')
plt.show()
