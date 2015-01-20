#stler - generate stl file from shape and scale
#Seun Ogedengbe
#Digital Fabrication
#Lab 2
import sys
import math
if __name__ == "__main__":
    try:
        sh = sys.argv[1].lower()
        sc = sys.argv[2]
    except:
        print "Usage: stler.py [shape] [scale]"
        sys.exit(1)
    if int(sc) <= 0:
        print "scale must be greater than zero"
        sc = 1
    sc = str(sc)
    p=((1 + math.sqrt(5))/2)
    asc = str(p*int(sc))
    bsc = str(int(sc)/p)
    csc = str(2*int(sc))
    '''Originally going to recode whole stls,
but I figured this would be a waste of time.
The STL for cube for instance was 87 lines long.
    start = "solid OpenSCAD_Model\n"
    end = "endsolid OpenSCAD_Model"
    fcn = "  facet normal "
    olp = "    outer loop\n"
    elp = "    endloop\n"
    ver = "      vertex "'''
    if sh == "icosahedron":
        f = open('icosa.stl', 'w')
        f.write("solid OpenSCAD_Model\n  facet normal -0.57735 0.57735 0.57735\n    outer loop\n      vertex -"+asc+" "+sc+" 0\n      vertex -"+sc+" 0 "+asc+"\n      vertex 0 "+asc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.356822 0.934172 0\n    outer loop\n      vertex -"+asc+" "+sc+" 0\n      vertex 0 "+asc+" "+sc+"\n      vertex 0 "+asc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.356822 0.934172 0\n    outer loop\n      vertex 0 "+asc+" -"+sc+"\n      vertex 0 "+asc+" "+sc+"\n      vertex "+asc+" "+sc+" 0\n    endloop\n  endfacet\n  facet normal 0.57735 0.57735 0.57735\n    outer loop\n      vertex 0 "+asc+" "+sc+"\n      vertex "+sc+" 0 "+asc+"\n      vertex "+asc+" "+sc+" 0\n    endloop\n  endfacet\n  facet normal 0 0.356822 0.934172\n    outer loop\n      vertex -"+sc+" 0 "+asc+"\n      vertex "+sc+" 0 "+asc+"\n      vertex 0 "+asc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.934172 0 0.356822\n    outer loop\n      vertex -"+asc+" -"+sc+" 0\n      vertex -"+sc+" 0 "+asc+"\n      vertex -"+asc+" "+sc+" 0\n    endloop\n  endfacet\n  facet normal -0.934172 0 -0.356822\n    outer loop\n      vertex -"+asc+" -"+sc+" 0\n      vertex -"+asc+" "+sc+" 0\n      vertex -"+sc+" 0 -"+asc+"\n    endloop\n  endfacet\n  facet normal -0.57735 0.57735 -0.57735\n    outer loop\n      vertex -"+asc+" "+sc+" 0\n      vertex 0 "+asc+" -"+sc+"\n      vertex -"+sc+" 0 -"+asc+"\n    endloop\n  endfacet\n  facet normal 0 -0.356822 0.934172\n    outer loop\n      vertex -"+sc+" 0 "+asc+"\n      vertex 0 -"+asc+" "+sc+"\n      vertex "+sc+" 0 "+asc+"\n    endloop\n  endfacet\n  facet normal -0.57735 -0.57735 0.57735\n    outer loop\n      vertex -"+asc+" -"+sc+" 0\n      vertex 0 -"+asc+" "+sc+"\n      vertex -"+sc+" 0 "+asc+"\n    endloop\n  endfacet\n  facet normal 0 0.356822 -0.934172\n    outer loop\n      vertex -"+sc+" 0 -"+asc+"\n      vertex 0 "+asc+" -"+sc+"\n      vertex "+sc+" 0 -"+asc+"\n    endloop\n  endfacet\n  facet normal 0.57735 0.57735 -0.57735\n    outer loop\n      vertex 0 "+asc+" -"+sc+"\n      vertex "+asc+" "+sc+" 0\n      vertex "+sc+" 0 -"+asc+"\n    endloop\n  endfacet\n  facet normal 0.934172 0 0.356822\n    outer loop\n      vertex "+sc+" 0 "+asc+"\n      vertex "+asc+" -"+sc+" 0\n      vertex "+asc+" "+sc+" 0\n    endloop\n  endfacet\n  facet normal 0.934172 0 -0.356822\n    outer loop\n      vertex "+sc+" 0 -"+asc+"\n      vertex "+asc+" "+sc+" 0\n      vertex "+asc+" -"+sc+" 0\n    endloop\n  endfacet\n  facet normal 0.57735 -0.57735 0.57735\n    outer loop\n      vertex 0 -"+asc+" "+sc+"\n      vertex "+asc+" -"+sc+" 0\n      vertex "+sc+" 0 "+asc+"\n    endloop\n  endfacet\n  facet normal -0.356822 -0.934172 0\n    outer loop\n      vertex -"+asc+" -"+sc+" 0\n      vertex 0 -"+asc+" -"+sc+"\n      vertex 0 -"+asc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.57735 -0.57735 -0.57735\n    outer loop\n      vertex -"+asc+" -"+sc+" 0\n      vertex -"+sc+" 0 -"+asc+"\n      vertex 0 -"+asc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0 -0.356822 -0.934172\n    outer loop\n      vertex -"+sc+" 0 -"+asc+"\n      vertex "+sc+" 0 -"+asc+"\n      vertex 0 -"+asc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.356822 -0.934172 0\n    outer loop\n      vertex 0 -"+asc+" -"+sc+"\n      vertex "+asc+" -"+sc+" 0\n      vertex 0 -"+asc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0.57735 -0.57735 -0.57735\n    outer loop\n      vertex 0 -"+asc+" -"+sc+"\n      vertex "+sc+" 0 -"+asc+"\n      vertex "+asc+" -"+sc+" 0\n    endloop\n  endfacet\nendsolid OpenSCAD_Model\n")
    elif sh == "dodecahedron":
        f = open('dodeca.stl', 'w')
        f.write("solid OpenSCAD_Model\n  facet normal 1.73121e-008 -0.850651 0.525731\n    outer loop\n      vertex 0 -"+bsc+" "+asc+"\n      vertex "+bsc+" -"+asc+" 0\n      vertex "+sc+" -"+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0.525731 -1.73121e-008 0.850651\n    outer loop\n      vertex 0 -"+bsc+" "+asc+"\n      vertex "+sc+" -"+sc+" "+sc+"\n      vertex "+asc+" 0 "+bsc+"\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 1.73121e-008\n    outer loop\n      vertex "+bsc+" -"+asc+" 0\n      vertex "+asc+" 0 "+bsc+"\n      vertex "+sc+" -"+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.525731 0 0.850651\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex 0 -"+bsc+" "+asc+"\n      vertex 0 "+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal 0.525731 0 0.850651\n    outer loop\n      vertex 0 -"+bsc+" "+asc+"\n      vertex "+asc+" 0 "+bsc+"\n      vertex 0 "+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal 0 -0.850651 0.525731\n    outer loop\n      vertex -"+bsc+" -"+asc+" 0\n      vertex "+bsc+" -"+asc+" 0\n      vertex 0 -"+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 -0.850651 0.525731\n    outer loop\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex -"+bsc+" -"+asc+" 0\n      vertex 0 -"+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal -0.525731 -1.73121e-008 0.850651\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex 0 -"+bsc+" "+asc+"\n    endloop\n  endfacet\n  facet normal 0 -0.850651 -0.525731\n    outer loop\n      vertex -"+bsc+" -"+asc+" 0\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex "+bsc+" -"+asc+" 0\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 0\n    outer loop\n      vertex "+bsc+" -"+asc+" 0\n      vertex "+asc+" 0 -"+bsc+"\n      vertex "+asc+" 0 "+bsc+"\n    endloop\n  endfacet\n  facet normal 0.850651 -0.525731 -1.73121e-008\n    outer loop\n      vertex "+bsc+" -"+asc+" 0\n      vertex "+sc+" -"+sc+" -"+sc+"\n      vertex "+asc+" 0 -"+bsc+"\n    endloop\n  endfacet\n  facet normal 1.73121e-008 -0.850651 -0.525731\n    outer loop\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n      vertex "+bsc+" -"+asc+" 0\n    endloop\n  endfacet\n  facet normal 0.525731 1.73121e-008 0.850651\n    outer loop\n      vertex 0 "+bsc+" "+asc+"\n      vertex "+asc+" 0 "+bsc+"\n      vertex "+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 1.73121e-008\n    outer loop\n      vertex "+bsc+" "+asc+" 0\n      vertex "+sc+" "+sc+" "+sc+"\n      vertex "+asc+" 0 "+bsc+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 0\n    outer loop\n      vertex "+bsc+" "+asc+" 0\n      vertex "+asc+" 0 "+bsc+"\n      vertex "+asc+" 0 -"+bsc+"\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 0\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+asc+" 0 "+bsc+"\n      vertex -"+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 1.73121e-008\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex -"+sc+" "+sc+" "+sc+"\n      vertex -"+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal -0.525731 1.73121e-008 0.850651\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex 0 "+bsc+" "+asc+"\n      vertex -"+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 1.73121e-008\n    outer loop\n      vertex -"+asc+" 0 "+bsc+"\n      vertex -"+bsc+" -"+asc+" 0\n      vertex -"+sc+" -"+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 0\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+bsc+" -"+asc+" 0\n      vertex -"+asc+" 0 "+bsc+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 0.850651 0.525731\n    outer loop\n      vertex -"+sc+" "+sc+" "+sc+"\n      vertex 0 "+bsc+" "+asc+"\n      vertex -"+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal 0 0.850651 0.525731\n    outer loop\n      vertex -"+bsc+" "+asc+" 0\n      vertex 0 "+bsc+" "+asc+"\n      vertex "+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal 1.73121e-008 0.850651 0.525731\n    outer loop\n      vertex 0 "+bsc+" "+asc+"\n      vertex "+sc+" "+sc+" "+sc+"\n      vertex "+bsc+" "+asc+" 0\n    endloop\n  endfacet\n  facet normal -1.73121e-008 -0.850651 -0.525731\n    outer loop\n      vertex -"+sc+" -"+sc+" -"+sc+"\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex -"+bsc+" -"+asc+" 0\n    endloop\n  endfacet\n  facet normal -0.850651 -0.525731 -1.73121e-008\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+sc+" -"+sc+" -"+sc+"\n      vertex -"+bsc+" -"+asc+" 0\n    endloop\n  endfacet\n  facet normal 0.525731 -1.73121e-008 -0.850651\n    outer loop\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex "+asc+" 0 -"+bsc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.525731 0 -0.850651\n    outer loop\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex 0 "+bsc+" -"+asc+"\n      vertex "+asc+" 0 -"+bsc+"\n    endloop\n  endfacet\n  facet normal -0.525731 0 -0.850651\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex 0 "+bsc+" -"+asc+"\n      vertex 0 -"+bsc+" -"+asc+"\n    endloop\n  endfacet\n  facet normal -0.525731 -1.73121e-008 -0.850651\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex 0 -"+bsc+" -"+asc+"\n      vertex -"+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.850651 0.525731 -1.73121e-008\n    outer loop\n      vertex "+bsc+" "+asc+" 0\n      vertex "+asc+" 0 -"+bsc+"\n      vertex "+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.525731 1.73121e-008 -0.850651\n    outer loop\n      vertex 0 "+bsc+" -"+asc+"\n      vertex "+sc+" "+sc+" -"+sc+"\n      vertex "+asc+" 0 -"+bsc+"\n    endloop\n  endfacet\n  facet normal 0 0.850651 -0.525731\n    outer loop\n      vertex -"+bsc+" "+asc+" 0\n      vertex "+bsc+" "+asc+" 0\n      vertex 0 "+bsc+" -"+asc+"\n    endloop\n  endfacet\n  facet normal 1.73121e-008 0.850651 -0.525731\n    outer loop\n      vertex 0 "+bsc+" -"+asc+"\n      vertex "+bsc+" "+asc+" 0\n      vertex "+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal -0.525731 1.73121e-008 -0.850651\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+sc+" "+sc+" -"+sc+"\n      vertex 0 "+bsc+" -"+asc+"\n    endloop\n  endfacet\n  facet normal -0.850651 0.525731 -1.73121e-008\n    outer loop\n      vertex -"+asc+" 0 -"+bsc+"\n      vertex -"+bsc+" "+asc+" 0\n      vertex -"+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal -1.73121e-008 0.850651 -0.525731\n    outer loop\n      vertex -"+sc+" "+sc+" -"+sc+"\n      vertex -"+bsc+" "+asc+" 0\n      vertex 0 "+bsc+" -"+asc+"\n    endloop\n  endfacet\nendsolid OpenSCAD_Model\n")
    elif sh == "octahedron":
        f = open('octa.stl', 'w')
        f.write("solid OpenSCAD_Model\n  facet normal 0.57735 0.57735 -0.57735\n    outer loop\n      vertex 0 0 -"+csc+"\n      vertex 0 "+csc+" 0\n      vertex "+csc+" 0 0\n    endloop\n  endfacet\n  facet normal 0.57735 0.57735 0.57735\n    outer loop\n      vertex 0 0 "+csc+"\n      vertex "+csc+" 0 0\n      vertex 0 "+csc+" 0\n    endloop\n  endfacet\n  facet normal -0.57735 0.57735 0.57735\n    outer loop\n      vertex -"+csc+" 0 0\n      vertex 0 0 "+csc+"\n      vertex 0 "+csc+" 0\n    endloop\n  endfacet\n  facet normal -0.57735 0.57735 -0.57735\n    outer loop\n      vertex -"+csc+" 0 0\n      vertex 0 "+csc+" 0\n      vertex 0 0 -"+csc+"\n    endloop\n  endfacet\n  facet normal -0.57735 -0.57735 -0.57735\n    outer loop\n      vertex -"+csc+" 0 0\n      vertex 0 0 -"+csc+"\n      vertex 0 -"+csc+" 0\n    endloop\n  endfacet\n  facet normal 0.57735 -0.57735 -0.57735\n    outer loop\n      vertex 0 -"+csc+" 0\n      vertex 0 0 -"+csc+"\n      vertex "+csc+" 0 0\n    endloop\n  endfacet\n  facet normal 0.57735 -0.57735 0.57735\n    outer loop\n      vertex 0 -"+csc+" 0\n      vertex "+csc+" 0 0\n      vertex 0 0 "+csc+"\n    endloop\n  endfacet\n  facet normal -0.57735 -0.57735 0.57735\n    outer loop\n      vertex -"+csc+" 0 0\n      vertex 0 -"+csc+" 0\n      vertex 0 0 "+csc+"\n    endloop\n  endfacet\nendsolid OpenSCAD_Model\n")
    elif sh == "cube":
        f = open('cube.stl', 'w')
        f.write("solid OpenSCAD_Model\n  facet normal -1 0 0\n    outer loop\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex -"+sc+" "+sc+" "+sc+"\n      vertex -"+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal -1 0 0\n    outer loop\n      vertex -"+sc+" -"+sc+" -"+sc+"\n      vertex -"+sc+" "+sc+" "+sc+"\n      vertex -"+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0 1 0\n    outer loop\n      vertex -"+sc+" "+sc+" "+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n      vertex -"+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0 1 0\n    outer loop\n      vertex -"+sc+" "+sc+" -"+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n      vertex "+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0 0 1\n    outer loop\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex "+sc+" -"+sc+" "+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0 0 1\n    outer loop\n      vertex -"+sc+" "+sc+" "+sc+"\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0 -1 0\n    outer loop\n      vertex -"+sc+" -"+sc+" -"+sc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n      vertex "+sc+" -"+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0 -1 0\n    outer loop\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex -"+sc+" -"+sc+" -"+sc+"\n      vertex "+sc+" -"+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0 0 -1\n    outer loop\n      vertex -"+sc+" "+sc+" -"+sc+"\n      vertex "+sc+" "+sc+" -"+sc+"\n      vertex -"+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0 0 -1\n    outer loop\n      vertex -"+sc+" -"+sc+" -"+sc+"\n      vertex "+sc+" "+sc+" -"+sc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 1 0 0\n    outer loop\n      vertex "+sc+" -"+sc+" -"+sc+"\n      vertex "+sc+" "+sc+" -"+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 1 0 0\n    outer loop\n      vertex "+sc+" -"+sc+" "+sc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\nendsolid OpenSCAD_Model\n")
    else:
        if sh != "tetrahedron":
            print "shape must be a platonic solid: Tetrahedron, Cube, Octahedron, Dodecahedron, or Icosahedron"
        f = open('tetra.stl', 'w')
        f.write("solid OpenSCAD_Model\n  facet normal -0.57735 -0.57735 -0.57735\n    outer loop\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex -"+sc+" "+sc+" -"+sc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal -0.57735 0.57735 0.57735\n    outer loop\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n      vertex -"+sc+" "+sc+" -"+sc+"\n    endloop\n  endfacet\n  facet normal 0.57735 -0.57735 0.57735\n    outer loop\n      vertex -"+sc+" -"+sc+" "+sc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n    endloop\n  endfacet\n  facet normal 0.57735 0.57735 -0.57735\n    outer loop\n      vertex -"+sc+" "+sc+" -"+sc+"\n      vertex "+sc+" "+sc+" "+sc+"\n      vertex "+sc+" -"+sc+" -"+sc+"\n    endloop\n  endfacet\nendsolid OpenSCAD_Model\n")
    f.close()