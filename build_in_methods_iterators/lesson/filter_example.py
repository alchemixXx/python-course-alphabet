data = [x for x in range(0, 100)]

print(data)

# print(filter(lambda x: x % 2 == 0, data))

new_data = list(filter(lambda x: x % 2 == 0, data))

members = [
    {'age': 43, 'name': 'Denis'},
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'Spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'Claus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'Homer'}
]
# Suppose we have to get all members that are older than 49 years.
# In current example we could do it in at least two ways
# Using list comprehension
print([x for x in members if x.get('age') > 49])

# Or using a filter
# using list method to filter result is not necessary if you will iterate trow them
# filter return filter object(iterator)
print(list(filter(lambda x: x.get('age', 0) > 49, members)))


