#count o in following tuple

a = (7,7,5,0,0,8,0,9)
n = a.count(0)
print(n)

#Tuple Functions

# Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple.

def min_in_tuple(tpl):
    return min(tpl)

def max_in_tuple(tpl):
    return max(tpl)

def sum_of_tuple(tpl):
    return sum(tpl)

sample_tpl = (1, 2, 3, 4, 5)
print(f"Minimum: {min_in_tuple(sample_tpl)}")
print(f"Maximum: {max_in_tuple(sample_tpl)}")
print(f"Sum: {sum_of_tuple(sample_tpl)}")
