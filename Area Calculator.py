def areacalculator():
    _input_ = input("Enter the shape and i will give u area: ")
    area = 0
    pie = 3.14
    if _input_ == "Square":
        side = int(input("Enter value :) "))
        area = area + (side ** 2)
    elif _input_ == "Circle":
        radius = int(input("Enter value :) "))
        area = area + (pie * radius * radius)
    elif _input_ == "Rectangle":
        length = int(input("Enter length :) "))
        breadth = int(input("Enter breadth :) "))
        area = area + (length * breadth)
    elif _input_ == "Triangle":
        base = int(input("Give the base length: "))
        height = int(input("Give the height length: "))
        area = area + (0.5 * base * height)

    else:
        print("You suck")
    print("%.2f" % area)

areacalculator()
    