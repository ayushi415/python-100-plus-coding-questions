# task 1 " string "

s = " this is string example "

# 1) reverse the string
rev_str = s[::-1]

# 2) word wise reverse
word_rev = " ".join(s.split()[::-1])

# 3) 2 character interchange
swap_chars = "".join([s[i+1] + s[i] for i in range(0,len(s)-1,2)]) + (s[-1] if len(s)%2 else "")

# 4) Split by space and join with '*' 
star_join = "*".join(s.split())

# 5) Replace 'is' -> 'was'
replace_is = " ".join(['was' if w == 'is' else w for w in s.split()])

print("1:",rev_str)
print("2:",word_rev)
print("3:",swap_chars)
print("4:",star_join)
print("5:",replace_is)