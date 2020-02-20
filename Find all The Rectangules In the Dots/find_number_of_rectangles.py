import math
from itertools import combinations


board = [
			[0,0,0,0,0,0],
			[1,1,1,0,0,0],
			[1,1,1,0,0,0],

		]

coordenates = []
lines = 0
col = 0

#Get all the dots
for line in board:
	if (1 in line):
		for element in line:
			if(element == 1):
				coordenates.append([lines,col])
				col += 1
			else:
				pass
		col = 0
		lines += 1
	else:
		lines += 1

def rectangule(xy_points):
	a_x = xy_points[0][0]
	b_x = xy_points[1][0]
	c_x = xy_points[2][0]
	d_x = xy_points[3][0]

	e_y = xy_points[0][1]
	f_y = xy_points[1][1]
	g_y = xy_points[2][1]
	h_y = xy_points[3][1]

	if (a_x == b_x == c_x == d_x):
		if(e_y in(f_y,g_y,h_y) and (f_y in (e_y,g_y,h_y)) and (g_y in (e_y,f_y,h_y)) and (h_y in (e_y,f_y,g_y))):
			return 1
	elif (a_x == b_x and c_x == d_x):
		if(e_y in(f_y,g_y,h_y) and (f_y in (e_y,g_y,h_y)) and (g_y in (e_y,f_y,h_y)) and (h_y in (e_y,f_y,g_y))):
			return 1
	elif (a_x == d_x and c_x == b_x):
		if(e_y in(f_y,g_y,h_y) and (f_y in (e_y,g_y,h_y)) and (g_y in (e_y,f_y,h_y)) and (h_y in (e_y,f_y,g_y))):
			return 1
	elif (a_x == c_x and d_x == b_x):
		if(e_y in(f_y,g_y,h_y) and (f_y in (e_y,g_y,h_y)) and (g_y in (e_y,f_y,h_y)) and (h_y in (e_y,f_y,g_y))):
			return 1


def all_combination_4(xy):
	output = sum([list(map(list, combinations(xy, i))) for i in range(len(xy) + 1)], [])
	c = 0
	soma = 0
	for i in output:
		if (len(i) == 4):
			c = rectangule(i)
			if (c != None):
				soma += 1
	return soma



count = all_combination_4(coordenates)
print(count)
