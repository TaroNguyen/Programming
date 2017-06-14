fruit = {"apple" : 5, "pear" : 3, "banana" : 4, "pineapple" : 1, "cherry" : 20}

# Access the `fruit` dictionary directly (without using get) and print the value of "banana"
print(fruit["apple"])

# Pick one of 5 the fruits and show that both retrieval styles obtain equal results
print(fruit["apple"] == fruit.get("apple"))