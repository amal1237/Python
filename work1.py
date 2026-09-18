# Area of a triangle


base = float(input("enter base of the triangle:"))
height = float(input("enter height of the triangle:"))

area = 0.5 * base * height
print("area of the triangle:")


# Perimeter of a circle


radius = float(input("enter radius of the circle:"))

perimeter = 2 * 3.14 * radius
print("perimeter of the circle:")


# Square of a number


num = int(input("enter a number:"))

square = num**2
print("square of a number:")


# convert dollar into inr


usd = float(input("enter amount in usd: exchange_rate = 83.5"))

inr = usd * exchange_rate
print("usd = inr:")


# convert miles to kilometer


miles = float(input("enter distance in miles: miles = 1.6014"))

km = miles * 1.6014
print("miles = km:")


# check if a number is positive or negative


num = float(input("emter a number:"))

if num > 0:
    print("number is positive:")
else num <= 0:
    print("number is negative:")


# check if a number is multiple of 5


num = int(input("enter the number:"))

if num % 5 == 0:
    print("number is multiple of 5:")
else
print("number is not multiple of 5:")
