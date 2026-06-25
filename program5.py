n = int(input("Enter number of items: "))
items = []

for i in range(n):
    name = input("Enter item name: ")
    price = int(input("Enter price: "))
    items.append((name, price))

items.sort(key=lambda x: x[1])

print("Items in increasing order of price:")
for name, price in items:
    print(name, "-", price)