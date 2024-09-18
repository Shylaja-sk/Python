#task08
#Triangle classifier
# write a program that classifies a triangle based  on its side length.
# Given three inputs values representing the length of the sides ,
# determine if the triangle is equilateral,isosceles,or if scalene:

length_side1=int(input("Enter the length of side1 of triangle: "))
length_side2=int(input("Enter the length of side1 of triangle: "))
length_side3=int(input("Enter the length of side1 of triangle: "))
if length_side1==length_side2==length_side3:
    print(f"Equilateral Triangle as ALL three sides {length_side1} , {length_side2} ,{length_side3} are equal")
elif length_side1==length_side2 or length_side1==length_side3:
    print(f"Isosceles Triangle as two sides {length_side1} ,{length_side2} , {length_side3} are  equal")
else:
    print(f"Scalene Triangle as all three sides {length_side1},{length_side2} ,{length_side3} are not equal")