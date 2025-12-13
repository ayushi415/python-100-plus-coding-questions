### Variable length Aarguments
### Positional and keywords arguments

#positional arguments
def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1,23,32,44,"ayushi")

#keyword arguments
def print_details(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}: {values}")
print_details(Name="Ayushi",Age="20",Country="India")

#using both arguments
def print_details(*args,**kwargs):
    for val in args:
        print(f" Positional argument :{val}")

    for key,values in kwargs.items():
        print(f"{key}: {values}")
        
print_details(1,23,32,44,"ayushi",Name="Ayushi",Age="20",Country="India")
    

