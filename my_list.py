my_list = []

# Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("After appending:", my_list)

my_list.insert(1, 15)

print("After inserting 15 at index 1:", my_list)

my_list.extend([50, 60, 70])

print("After extending with [50, 60, 70]:", my_list)

my_list.pop()

print("After removing last element:", my_list)

my_list.sort()

print("Sorted list:", my_list)

index_of_30 = my_list.index(30)
print(f"The index of 30 is {index_of_30}")