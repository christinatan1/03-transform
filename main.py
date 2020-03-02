from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 100, 100, 100 ]
edges = []
transform = new_matrix()


# edges = make_translate(1,2,3)
# print_matrix(edges)
# print("\n")
#
# edges = make_scale(1,2,3)
# print_matrix(edges)
# print("\n")
#
# edges = make_rotX(1)
# print_matrix(edges)
# print("\n")
#
# edges = make_rotY(1)
# print_matrix(edges)
# print("\n")

parse_file('script', edges, transform, screen, color)
