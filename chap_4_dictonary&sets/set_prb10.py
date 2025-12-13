#  Set Symmetric Difference Update
# Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set.

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)

# Set Membership Testing
# Create a set and test if certain elements are present in the set. Print the results.

s = set(range(1, 6))
print(3 in s)
print(6 in s)
