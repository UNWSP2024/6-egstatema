# Eliya Statema
# 2/27/25
# Monthly Tax Rate

print("This program calculates monthly sales tax based on state and county tax rates.")

def calculate_sales_tax():
    state_tax_rate = 0.05
    county_tax_rate = 0.025
    total_sales = int(input("Enter the total sales for the month: "))
    state_taxes_payable = total_sales * state_tax_rate
    county_taxes_payable = total_sales * county_tax_rate
    total_taxes_payable = state_taxes_payable + county_taxes_payable
    return f'''STATE TAX: ${state_taxes_payable:.2f} 
COUNTY TAX: ${county_taxes_payable:.2f}
TOTAL TAX: ${total_taxes_payable:.2f}'''

print(calculate_sales_tax())