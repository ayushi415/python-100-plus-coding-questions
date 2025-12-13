#write a program to find out whether a given point is talking about "sweety"or not

post = input("Enter the post :")

if("Sweety".lower() in post.lower()):
    print("This post is talking about Sweety")
else:
    print("This post is not talking about Sweety")


# if we don't use .lower() here , and if we use the name exact the way it was defines than it works only , (just a simple change like captital letter or small letter in name dosen't work), so after using .lower() we easily sort this problem