from vehicle import Vehicle
from car import Car

v_1 = Vehicle()
print(str(v_1))

v_2 = Vehicle('NO 12345', 1, 1999)
print(str(v_2))

v_1 = Vehicle(None, 0, 1990)
print(str(v_1))

c_1 = Car()
print(str(c_1))


c_2 = Car('NO 54321', 5, 2017, 100000, 'black', 2)
print(str(c_2))