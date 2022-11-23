import math

print("Ведите координаты двух точек и найдем расстояние между ними на плоскости")

coordinates = []

A = input('Ведите координаты точки А через заптую: x,y: ').split(',')
coordinates.extend(map(int,A))
B = input('Ведите координаты точки B через заптую: x,y: ').split(',')
coordinates.extend(map(int,B))
dist = math.hypot(coordinates[2]-coordinates[0], coordinates[3]-coordinates[1])

print(f'Расстояние между этими точками = {round(dist, 2)}')