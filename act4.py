import math
class C:
    def __init__(s,r):s.r=r
    def a(s):return math.pi*s.r**2
    def p(s):return 2*math.pi*s.r
r=float(input("Radius: "))
c=C(r)
print("Area: ",round(c.a(),2))
print("Perimeter:",round(c.p(),2))

