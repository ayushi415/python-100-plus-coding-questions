# write a python function to remove a given word from a list and step it at the same time

def remove_word(lst, word):
    while word in lst:
        lst.remove(word)
        print(lst)

        
words = ["apple", "banana", "apple", "cherry", "apple"]
remove_word(words, "apple")
