import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('inputs/sample_customer_data_for_exam.csv')

# Check basic info
print(data.info())
print(data.describe())

# Filter numerical columns
numerical_cols = data[['age', 'income', 'purchase_amount', 'promotion_usage', 'satisfaction_score']]

# Create a correlation matrix
corr_matrix = numerical_cols.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Variables')
plt.show()

# Histograms for 'age' and 'income'
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

# Box plot for 'purchase_amount' across 'product_category'
plt.figure(figsize=(10, 6))
sns.boxplot(x='product_category', y='purchase_amount', data=data)
plt.title('Purchase Amount Distribution by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Purchase Amount')
plt.xticks(rotation=45)
plt.show()

# Pie chart for gender distribution
plt.figure(figsize=(6, 6))
gender_counts = data['gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])
plt.title('Customer Gender Distribution')
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (update the path as needed)
data = pd.read_csv('inputs/sample_customer_data_for_exam.csv')

# i. Calculate average purchase amount for each 'education' level, sort and display the results
avg_purchase_by_education = data.groupby('education')['purchase_amount'].mean().sort_values(ascending=False)
print("Average Purchase Amount by Education Level:")
print(avg_purchase_by_education)

# ii. Calculate the average satisfaction score for each 'loyalty_status', sort and display the results
avg_satisfaction_by_loyalty = data.groupby('loyalty_status')['satisfaction_score'].mean().sort_values(ascending=False)
print("\nAverage Satisfaction Score by Loyalty Status:")
print(avg_satisfaction_by_loyalty)

# iii. Create a bar plot comparing 'purchase_frequency' across different 'region' values
plt.figure(figsize=(8, 6))
sns.countplot(x='region', hue='purchase_frequency', data=data)
plt.title('Purchase Frequency Across Regions')
plt.xlabel('Region')
plt.ylabel('Count of Purchase Frequency')
plt.legend(title='Purchase Frequency')
plt.show()

# iv. Compute the percentage of customers who used promotional offers (promotion_usage = 1)
promotion_usage_count = data['promotion_usage'].value_counts(normalize=True) * 100
promo_used_percentage = promotion_usage_count[1] if 1 in promotion_usage_count.index else 0
print(f"\nPercentage of customers who used promotional offers: {promo_used_percentage:.2f}%")

# v. Investigate if there is a correlation between 'income' and 'purchase_amount'
income_purchase_corr = data['income'].corr(data['purchase_amount'])
print(f"\nCorrelation between 'Income' and 'Purchase Amount': {income_purchase_corr:.2f}")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (adjust the file path as necessary)
data = pd.read_csv('inputs/sample_customer_data_for_exam.csv')

# i. Scatter plot of 'purchase frequency' vs 'purchase amount', color-coded by 'loyalty status'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='purchase_frequency', y='purchase_amount', hue='loyalty_status', data=data, palette='Set2')
plt.title('Purchase Frequency vs Purchase Amount by Loyalty Status')
plt.xlabel('Purchase Frequency')
plt.ylabel('Purchase Amount')
plt.legend(title='Loyalty Status')
plt.show()

# ii. Calculate average 'purchase amount' for customers who used promotions vs those who didn’t
avg_purchase_by_promotion = data.groupby('promotion_usage')['purchase_amount'].mean()
print("Average Purchase Amount:")
print(f"With Promotions: {avg_purchase_by_promotion[1]:.2f}")
print(f"Without Promotions: {avg_purchase_by_promotion[0]:.2f}")

# iii. Violin plot showing the distribution of 'satisfaction score' for different 'loyalty status' groups
plt.figure(figsize=(10, 6))
sns.violinplot(x='loyalty_status', y='satisfaction_score', data=data, palette='Set1')
plt.title('Satisfaction Score Distribution by Loyalty Status')
plt.xlabel('Loyalty Status')
plt.ylabel('Satisfaction Score')
plt.show()

# iv. Stacked bar chart showing the proportion of promotion usage across different 'product category' values
promotion_usage_by_category = pd.crosstab(data['product_category'], data['promotion_usage'], normalize='index')
promotion_usage_by_category.plot(kind='bar', stacked=True, color=['lightcoral', 'lightgreen'], figsize=(10, 6))
plt.title('Proportion of Promotion Usage Across Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Proportion of Customers')
plt.legend(['Did not use Promotion', 'Used Promotion'], title='Promotion Usage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# v. Calculate the correlation between 'satisfaction score' and 'purchase frequency'
# First, we'll convert 'purchase_frequency' into numerical values (assigning ranks)
frequency_mapping = {'rare': 1, 'occasional': 2, 'frequent': 3}
data['purchase_frequency_numeric'] = data['purchase_frequency'].map(frequency_mapping)

satisfaction_purchase_corr = data['satisfaction_score'].corr(data['purchase_frequency_numeric'])
print(f"\nCorrelation between 'Satisfaction Score' and 'Purchase Frequency': {satisfaction_purchase_corr:.2f}")

# Discuss any notable findings
if satisfaction_purchase_corr > 0.2:
    print("Notable finding: There is a positive correlation between satisfaction score and purchase frequency.")
elif satisfaction_purchase_corr < -0.2:
    print("Notable finding: There is a negative correlation between satisfaction score and purchase frequency.")
else:
    print("Notable finding: There is no strong correlation between satisfaction score and purchase frequency.")
