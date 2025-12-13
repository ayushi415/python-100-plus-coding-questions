### Read a whole file

with open('example.txt','r') as file:
    content=file.read()
    print(content)

### Read a file line by line

with open('example.txt','r') as file:
    for line in file:
        print(line.strip()) # strip() removes the newline character

### Writing a file(Overwriting)

with open('example.txt','w') as file:
    file.write('Hello World! \n')
    file.write('this is a new line .')

### Write a file(Without Overwriting)
with open('example.txt','a') as file:
    file.write("Append operation taking place! \n")

### Writing a list of lines to a file
lines=['First line \n','Second line \n','Third line \n' ]
with open('example.txt','a') as file:
    file.writelines(lines)

### Writing to a binary file
data = b'\x00\x01\x02\x03\x04'
with open('example.bin','wb') as file:
    file.write(data)

### Reading a binary file
with open('example.bin','rb') as file:
    content = file.read()
    print(content)

### Read the content from a source text file and write to a destination text file
# Copying a text file
with open('example.txt','r') as file:
    content = file.read()
with open('destination.txt','w') as destination_file:
    destination_file.write(content)

### Writing and then reading a file
with open('example.txt','w+') as file:
    file.write("Hello World! \n")
    file.write("This is a new line \n")

    ## Move the file cursor to the beginning
    file.seek(0)

    ## Read the content of the file
    content=file.read()
    print(content)





