# python functions
def addition(a, b):
    return a + b

output = addition(12, 89)
print(output)
# tax rate function 
# takes in a bill amount and a tax rate
def total_tax(bill, tax_rate):
    return (bill * tax_rate) / 100

print("Total tax is: ",round(total_tax(164.33, 22), 2))
