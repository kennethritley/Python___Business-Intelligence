#--------------------------------------------------------------------
# KEN, 07.04.2022, based on 
# https://towardsdatascience.com/business-intelligence-visualizations-with-python-1d2d30ce8bd9
# 
# This is just a little script to test out
#    (1) creating graphs that might be useful for a BI application
#    (2) working with a JSON file and creating an Excel file, also useful
#    (3) reading and plotting an Excel file
#--------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

#--------------------------------------------------------------------
# EXAMPLE 1: Using a Pandas "DataFrame"
#--------------------------------------------------------------------

# Here we see how to create a "DataFrame" which is the main object in Pandas

drinks = ["Cappuccino", "Latte", "Chai", "Americano", "Mocha", "Espresso"]
sales =  [91, 76, 56, 66, 52, 27]
tea_df = pd.DataFrame(sales, index=drinks, columns=['Total Sales'])

# Now we print out the dataframe

print(tea_df)

#--------------------------------------------------------------------
# EXAMPLE 2: Business Intelligence plot with matplotlib and Python lists
#--------------------------------------------------------------------

# Days of the week:
days = [1, 2, 3, 4, 5, 6,7]
# Money spend one week 1
money_spent = [1000, 1200, 1500, 1080, 1400, 1650, 1350]
# Money spend one week 2
money_spent_2 = [900, 1500, 1200, 1050, 950, 1250, 1000]
# Create figure:
fig = plt.figure(figsize=(10,5))
# Plot first week expenses:
plt.plot(days, money_spent)
# Plot second week expenses:
plt.plot(days, money_spent_2)
# Display the result:
plt.title('Company Expenditure Comparison')
plt.legend(['First week', 'Second week'])

# Warn the user
print("\n\n\033[1;31;40m A new window will appear. You must close that window for the code to proceed.")
plt.show()

#--------------------------------------------------------------------
# EXAMPLE 3: Side-by-side plots
#--------------------------------------------------------------------

# Temperature and flight sales 
months = range(12)
temperature = [37, 38, 40, 53, 62, 71, 78, 74, 69, 56, 47, 48]
flights = [1100, 1300, 1200, 1400, 800, 700, 450, 500, 450, 900, 950, 1100]
# Create figure:
fig = plt.figure(figsize=(12,6))
# Display the result - Plot 1:
plt.subplot(1,2,1)
# Plot temperatures:
plt.plot(months,temperature,color='steelblue',linestyle='--')
# Configure labels and title:
plt.xlabel('Months')
plt.ylabel('Temperature')
plt.title('Temperature Representation')
# Display the result - Plot 2:
plt.subplot(1,2,2)
# Plot flights:
plt.plot(months,flights,color='red',marker='o')
plt.xlabel('Month')
# Configure labels and title:
plt.ylabel('Flights Summary')
plt.title('Flights per month')
plt.show()

#--------------------------------------------------------------------
# EXAMPLE 4: Business Intelligence plot with matplotlib and Python lists
# Be careful, there are mistakes in the code on the source webpage
#--------------------------------------------------------------------

# Values for X axis bar separation:
x_values1 = [0.8,2.8,4.8,6.8,8.8,10.8]
x_values2 = [1.6,3.6,5.6,7.6,9.6,11.6]
# Sales by month and labels:
drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
months_sales = ['Jan','Mar','May','Jul','Sep','Nov']
sales_cappuccino = [95, 72, 53, 62, 51, 25]
sales_latte = [62, 81, 34, 62, 35, 42]

# Figure creation:
fig = plt.figure(figsize=(12,8))
# Subplot configuration:
ax = plt.subplot()
ax.set_xticks(range(1,12,2))
ax.set_xticklabels(months_sales)
# Bar plot creation:
plt.bar(x_values1, sales_cappuccino, color='gray')
plt.bar(x_values2, sales_latte, color='purple')
# Display plot:
plt.title("Coffee Sales Comparison")
plt.xlabel("Types of coffees")
plt.ylabel("Pounds sold")
plt.legend(labels=drinks, loc='upper right')
plt.show()

#--------------------------------------------------------------------
# EXAMPLE 5: The power of pandas to read and write files
#--------------------------------------------------------------------

import pandas as pd

# Read a JSON file - or your favorite file by changing the code

employeedata = pd.read_json("./data/EmployeeData.json")
print("\n\n\033[1;32;40m Here's the content of the json file.\n")
print(employeedata.head(5))

# Write an Excel file with the data.  SPECIAL NOTE: be sure to "pip3 install openpyxl" 

employeedata.to_excel("./data/EmployeeData.xlsx", sheet_name="EmployeeData", index=False)

#--------------------------------------------------------------------
# EXAMPLE 6: See if you can open and read the Excel file TestData.xlsx
# and plot the results
#--------------------------------------------------------------------

# your own code goes here!sales_data = []
