# if else elif(else if) statements
total_bill = 245
discount1 = 10
discount2 = 20
if total_bill > 100 and total_bill < 200:
    print("bill is greater than 100")
    total_bill = total_bill - discount1
elif total_bill > 200:
    print("bill is greater than 200")
    total_bill = total_bill - discount2
else:
    print("bill is less than 100")
    
print("total bill is now: ", str(total_bill))
