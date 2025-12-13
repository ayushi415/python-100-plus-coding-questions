# Subsets and Supersets

# Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. 
# Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results.

set1 = set(range(1, 6))
set2 = set(range(1, 4))
print(f"Is set2 a subset of set1? {set2.issubset(set1)}")
print(f"Is set1 a superset of set2? {set1.issuperset(set2)}")