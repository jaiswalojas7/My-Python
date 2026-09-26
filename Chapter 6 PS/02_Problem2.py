marks1 = int(input("Enter Your Physics Marks: "))
marks2 = int(input("Enter Your Chemistry Marks: "))
marks3 = int(input("Enter Your Maths Marks: "))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>33):
    print("Congratulations\nYou are Passed", total_percentage)

else:
    print("Sorry\nYou are failed, try again next year!", total_percentage)