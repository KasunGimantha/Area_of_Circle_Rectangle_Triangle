choice = int(input("Enter\n1 for Rectangle\n2 for Circle\n3 for triangle\n"))


def rect_area(a=None, b=None):

    if a is None and b is None:
        print("Enter at least one demension!")
        exit()

    if a is None:
        a = b
    if b is None:
        b = a

    area = int(a)*int(b)

    if (a == b):
        print(f"Area of the Square is {area}")
    else:
        print(f"Area of the Rectangle is {area}")


def circle_area(r=None):

    if r is None:
        print("Enter radius!")
        exit()

    area = 3.14*(float(r)*float(r))
    print(f"Area of Circle is {area}")


def triangle_area(h=None, b=None):
    if h is None or b is None:
        print("Enter height and base!")
        exit()

    area = 0.5*int(h)*int(b)
    print(f"Area of Triangle is {area}")


if (choice == 1):
    height = input("Enter height: ")
    width = input("Enter width: ")
    rect_area(height if height else None, width if width else None)

elif (choice == 2):
    radius = input("Enter radius:")
    circle_area(radius if radius else None)

elif (choice == 3):
    t_height = input("Enter Height:")
    t_base = input("Enter base:")
    triangle_area(t_height if t_height else None, t_base if t_base else None)
else:
    print("Invalid Choice!!")
