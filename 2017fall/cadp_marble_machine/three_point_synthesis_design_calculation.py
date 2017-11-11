from sympy.geometry import *
from sympy import N
# N(expr, <args>) 等於 sympify(expr).evalf(<args>)

P1 = Point(-127.11, 37.29)
P2 = Point(-89.42, 50.69)
P3 = Point(-113.61, 73.77)
P4 = Point(-74.73, 64.37)
P5 = Point(-89.19, 88.52)
P6 = Point(-56.84, 64.99)
S1 = Segment(P1, P2)
S2 = Segment(P3, P4)
S3 = Segment(P5, P6)
#print(N(S1.length)) # 求 numerical value
#print(N(S2.length))
#print(N(S3.length))

#print(S1.slope)
#print(S1.intersection(S2))
#print(angle_between(S1, S2))

# 求 L13, L35 通過兩線中點垂直線的交點, 即為固定點 1
L13 = Line(P1, P3)
L35 = Line(P3, P5)
S13 = Segment(P1, P3)
S35 = Segment(P3, P5)
midS13 = S13.midpoint
midS35 = S35.midpoint
perL13 = L13.perpendicular_line(midS13)  # perpendicular line to L1
perL35 = L35.perpendicular_line(midS35)  # perpendicular line to L2
#print(L2.arbitrary_point() )           # parametric equation of L2
#Point(4*t + 2, -3*t - 1)
#print(L2.equation()    )               # algebraic equation of L2
#3*x + 4*y - 2
#print(L2.distance(P4))               # distance from P4 to L2
print(N(perL13.intersection(perL35)[0], 3))

# 求 L24, L46 通過兩線中點垂直線的交點, 即為固定點 2
L24 = Line(P2, P4)
L46 = Line(P4, P6)
S24 = Segment(P2, P4)
S46 = Segment(P4, P6)
midS24 = S24.midpoint
midS46 = S46.midpoint
perL24 = L24.perpendicular_line(midS24)  # perpendicular line to L1
perL46 = L46.perpendicular_line(midS46)  # perpendicular line to L2
#print(L2.arbitrary_point() )           # parametric equation of L2
#Point(4*t + 2, -3*t - 1)
#print(L2.equation()    )               # algebraic equation of L2
#3*x + 4*y - 2
#print(L2.distance(P4))               # distance from P4 to L2
print(N(perL24.intersection(perL46)[0], 3))

