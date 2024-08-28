#Write a prog to calculate area of circle given its radius using the formula ... area = pie*rof 2
#logic building formula
import math

#step 1: figure out input and output
#input of r is int
#pi  - 3.142
#power = pow or **
#o/p is float - and print the area

#step2 : rough logic - area = 3.14 *  pow(r,2)

radius = float(input("Enter the radius of the circle\n"))
print(radius)
print(math.pi)
area = math.pi*math.pow(radius, 2)
area2 = 3.14 * radius**2
print("Area of the circle is",area)
print(f"Area of the circle is {area:.2f}")
print(f"Area of the circle is {area2:.2f}")

# * --> multiplication
# ** --> power

