from gdsCAD import *
from sys import *
from numpy import *
# Create a Cell and add the box
cell=core.Cell('TOP')
l = 18
w = 6
g = 4
g2 = 20
w = 3
s = 8
x = 50
y = 20
z = 40

y_ref = 0
x_ref = 0
g3 = (g2-g)/2

# Create three boxes on layer 2 of different sizes centered at
# the origin and add them to the cell.
points1=[(x_ref + g/2, y_ref), (x_ref + g/2 + l, y_ref), (x_ref + g/2 +l,y_ref -w), (x_ref + g/2 + w, y_ref - w), (x_ref + g/2+w,y_ref -x), (x_ref +  g2/2 + w, y_ref -x-y), (x_ref + g2/2 + w,y_ref -x-y-z), (x_ref + g2/2,y_ref -x-y-z), (x_ref + g2/2,y_ref -x-y), (x_ref + g/2,y_ref -x), (x_ref + g/2, y_ref)]
points2 = [(x_ref - g/2, y_ref), (x_ref - g/2 - w, y_ref), (x_ref - g/2 - w, y_ref -x), (x_ref - g2/2 - w, y_ref - x - y), (x_ref - g2/2 - w, y_ref - x - y - z), (x_ref - g2/2, y_ref -x - y - z), (x_ref - g2/2, y_ref - x - y), (x_ref - g/2, y_ref -x), (x_ref - g/2, y_ref)]

bdy = core.Boundary(points1)
bdy2 = core.Boundary(points2)


cell.add(bdy)
#cell.add(bdy2)


#cell.add(arrow2)
#cell.add(arrow3)
#cell.add(arrow4)

# Create a layout and add the cell
layout = core.Layout('LIBRARY')
layout.add(cell)

# Save the layout and then display it on screen
layout.save('Zcontrol.gds')
