#sum of list numbers,sort in ascending and descending order and remove the duplicate from the list


num_list = [23,33,43,56,67,78,65,34,65,99,67,33]
print(sum(num_list))

num_list.sort()
print(f"Ascending order ",num_list)

num_list.reverse()
print(f"Descending order ",num_list)

num_list=list(set(num_list))
print(f"without duplicates ",num_list)