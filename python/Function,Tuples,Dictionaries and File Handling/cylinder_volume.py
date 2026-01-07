def cylinder_volume(radius,height):

    print("radius : ",radius)
    print("height : ",height)
    volume = 3.14* (radius**2) *height
    return volume

r = 10
h = 7
g =cylinder_volume(r,h)
print(g)