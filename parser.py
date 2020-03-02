from display import *
from matrix import *
from draw import *
import math

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):

    f = open(fname, "r")
    args = []
    for line in f:
        line = line.strip()
        args.append(line)
    f.close()
    idx = 0
    while idx < len(args):
        command = args[idx]

        if command == "line":
            idx += 1
            pts = args[idx].split()
            pts = [int(i) for i in pts]
            # print('points: ' + str(args[idx]))
            # print('points: ' + str(pts))
            add_edge(points, pts[0], pts[1], pts[2], pts[3], pts[4], pts[5])

        if command == "ident":
            ident(transform)

        if command == "scale":
            idx += 1
            pts = args[idx].split()
            # print('SCALE ERROR' + str(pts))
            pts = [int(i) for i in pts]
            scale = make_scale(pts[0], pts[1], pts[2])
            # print('SCALE MATRIX' + str(transform))
            matrix_mult(scale, transform)

        if command == "move":
            idx += 1
            pts = args[idx].split()
            pts = [int(i) for i in pts]
            transl = make_translate(int(pts[0]), int(pts[1]), int(pts[2]))
            matrix_mult(transl, transform)

        if command == "rotate":
            idx += 1
            pts = args[idx].split()
            theta = int(pts[1])
            if pts[0] == "x":
                rotate = make_rotX(theta)
            elif pts[0] == "y":
                rotate = make_rotY(theta)
            else:
                rotate = make_rotZ(theta)
            matrix_mult(rotate, transform)

        if command == "apply":
            matrix_mult(transform, points)

        if command == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        if command == "save":
            clear_screen(screen)
            draw_lines(points, screen, color)
            idx += 1
            save_ppm(screen, 'img.ppm')
            save_extension(screen, args[idx])

        if command == "quit":
            break

        idx+=1
