file1_name = str(input())
file2_name = str(input())
f1 = open('%s'%file1_name, 'r')
circle_coord = f1.readline().split()
circle_x = float(circle_coord[0])
circle_y = float(circle_coord[1])
circle_radius = float(f1.readline(2))
f2 = open('%s'%file2_name, 'r')
lst_coord = []
for i in f2:
    point_coord = (float(i.split()[0]), float(i.split()[1]))
    lst_coord.append(point_coord)
for j in lst_coord:
    a = (j[0] - circle_x) ** 2 + (j[1] - circle_y) ** 2
    if a > circle_radius**2:
        print(2)
    elif a == circle_radius**2:
        print(1)
    else:
        print(0)
print()