import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Time complexity of the first implementation = O(n^2)


# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# duplicates =[]

# First Attempt: runtime: 1.7698168754577637 seconds
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

#  second attempt: runtime: 1.613966703414917 seconds
# duplicates = filter(lambda name: name in names_1, names_2)
# duplicates = list(duplicates)

duplicates = []

#  Third attempt and stretch: runtime: 0.005743265151977539 seconds
memo = {}
for name in names_1:
    memo[name] = 1

for name_2 in names_2:
    if name_2 in memo:
        duplicates.append(name_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

