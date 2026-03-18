# Program to calculate area of circle and triangle

radius = float(input("Enter radius: "))
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

# Circle area
circle_area = 3.14 * radius ** 2

# Triangle area
triangle_area = (base * height) / 2

print("Area of Circle:", circle_area)
print("Area of Triangle:", triangle_area)


#output:
# Enter radius: 6
# Enter base of triangle: 12
# Enter height of triangle: 7
# Area of Circle: 113.04
# Area of Triangle: 42.0