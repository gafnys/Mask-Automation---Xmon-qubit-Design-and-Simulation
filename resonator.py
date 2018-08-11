from gdsCAD import *
from sys import *
from argparse import *
import argparse
import datetime

now = datetime.datetime.now()
parser = argparse.ArgumentParser(add_help=False,description='Generates the gds for the resonator.\nRefer to the pdf file for all the parametrizations')
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='shows the default value of each parameters')
parser.add_argument('-g4', action="store",  dest="g4", default=4, type = int, help="4")
parser.add_argument('-g2', action="store", dest="g2", default=20,  type=int, help="20")
parser.add_argument('-g3', action="store", dest="g3", default=16, type=int, help="16")
parser.add_argument('-x', action="store",  dest="x", default=60, type = int, help="60")
parser.add_argument('-s', action="store", dest="s", default=8, type=int, help="8")
parser.add_argument('-w', action="store",  dest="w", default=4, type = int, help="4")
parser.add_argument('-main', action="store_true", default=False)
parser.add_argument('-x_ref', action="store",  dest="x_ref", default=0, type = int, help = "4")
parser.add_argument('-y_ref', action="store",  dest="y_ref", default=0, type = int, help = "4")
args = parser.parse_args()
args = parser.parse_args()
cell=core.Cell('TOP3')
main = args.main
x_ref = args.x_ref
s = args.s
w = args.w
g4 = args.g4
g2 = args.g2
g3 = args.g3
g = g4 + s + w
x = args.x
y_ref = args.y_ref + g4
points1 = [(x_ref-g-2*w-g2, y_ref - x), (x_ref-g-2*w-g2, y_ref+g4+2*w+g3), (x_ref+g+2*w+g2, y_ref+g4+2*w+g3), (x_ref+g+2*w+g2, y_ref -x), (x_ref+g, y_ref -x), (x_ref+g, y_ref +g4), (x_ref-g, y_ref+g4), (x_ref-g, y_ref -x), (x_ref-g-2*w-g2, y_ref - x)]
points2 = [(x_ref-g-w-g2, y_ref - x+w), (x_ref-g-w-g2, y_ref+g4+w+g3), (x_ref+g+w+g2, y_ref+g4+w+g3), (x_ref+g+w+g2, y_ref -x), (x_ref+g+w, y_ref -x), (x_ref+g+w, y_ref +g4+w), (x_ref-g-w, y_ref+g4+w), (x_ref-g-w, y_ref -x+w), (x_ref-g-w-g2, y_ref - x+w)]
points= points1 + points2
pth = core.Boundary(points)
cell.add(pth)

if main:
    name = 'temp.gds'
    layout = core.GdsImport('temp.gds')
    cell.add(layout['TOP2'], origin=(0,0))
else:
    name = 'XYcontrol'+now.strftime('%H_%M_%S')+'.gds'
    layout = core.Layout('LIBRARY')

layout.add(cell)
layout.save(name)
