#pass or fail using if else

marks1=int(input("Enter marks 1 :"))
marks2=int(input("Enter marks 2:"))
marks3=int(input("Enter marks 3 :"))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40):
    print("you are pass")
else:
    print("you failed, try next year")
    
