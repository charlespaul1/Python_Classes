# looping constructs in python
# # for loop
# for i in range(1, 10):
#     print(i)


desserts = ["ice cream", "cookies", "pie", "brownies", "cake", "donuts"]
for idx, dessert in enumerate(desserts):#enumerate returns the index and the value
    print(idx,dessert)

    
# while loop
# count = 0
# while count < (len(desserts)):
#     print("i like ...",desserts[count])
#     count += 

# control flow.. break

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list')
    

# control flow.. continue

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert) 
