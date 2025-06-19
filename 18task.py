import pandas as pd
import numpy as np

# data = {
#     'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
#     'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
#     'Age': [25, 32, 29, 41, 37, 45, 26, 38],
#     'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
#     'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
# }

# df = pd.DataFrame(data)


# avg_salary = df.groupby('Department')['Salary'].mean()
# print(avg_salary)

# highest_paid = df.loc[df.groupby('Department')['Salary'].idxmax(), ['Department', 'Employee', 'Salary']]
# print(highest_paid)

# f= df[(df['Experience'] > 5) & (df['Salary'] > 65000)]
# print(f[['Employee', 'Experience', 'Salary']])

# sorted = df[df['Department'] == 'IT'].sort_values(by='Salary', ascending=False)
# print(sorted[['Employee', 'Department', 'Salary']])

# np.random.seed(42)
# stock_prices = np.random.randint(100, 500, (30, 5))
# print(stock_prices)

# avg_prices = np.mean(stock_prices, axis=0)
# print("avg price:", avg_prices)

# max_price=np.max(stock_prices, axis=0)
# print("max price:", max_price)

# normalized_prices = (stock_prices - stock_prices.min()) / (stock_prices.max() - stock_prices.min())
# print("normalized price:", normalized_prices)

np.random.seed(42)
mission=np.random.randint(10,100,(6,3))
print(mission)

total=np.sum(mission,axis=0)
print(total)
