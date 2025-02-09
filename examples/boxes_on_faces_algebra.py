from build123d import *

b = Box(3, 3, 3)
b2 = Rot(0, 0, 45) * extrude(Rectangle(1, 2), 0.1)
for plane in [Plane(f) for f in b.faces()]:
    b += plane * b2

if "show_object" in locals():
    show_object(b, name="box on faces")
