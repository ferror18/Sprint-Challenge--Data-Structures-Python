import time
from collections import Counter
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()



duplicates = [item for item, count in Counter(names_1).items() if count > 1]
duplicates.extend([item for item, count in Counter(names_2).items() if count > 1])


# duplicates = []  # Return the list of duplicates in this data structure
# unique = []
# print(names_1.extend(names_2))
# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Returns Duplicates across both list and internal dups


# for name_1 in names_1:
#     if name_1 in unique:
#         if name_1 not in duplicates:
#             duplicates.append(name_1)
#         else:
#             pass
#     else:
#         unique.append(name_1)
# for name_2 in names_2:
#     if name_2 in unique:
#         if name_2 not in duplicates:
#             duplicates.append(name_2)
#         else:
#             pass
#     else:
#         unique.append(name_2)

# Returns dups only btetween the lists

# for name_1 in names_1:
#     if name_1 in names_2:
#         if name_1 not in duplicates:
#             duplicates.append(name_1)
#         else:
#             pass
#     else:
#         unique.append(name_1)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# print(f'They\'re the same: {duplicates == duplicates2}')

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
