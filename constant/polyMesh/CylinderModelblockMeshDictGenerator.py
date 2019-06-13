
# Geometry definitions
cyl1_dia = 0.075
cyl1_height = 0.1*cyl1_dia
cyl2_dia = 1*cyl1_dia
cyl2_height = 0.1*cyl1_dia
tube_dia = 0.1*cyl1_dia
tube_len = 0.5*cyl1_dia

# Mesh definitions
angular_resolution = 1 #degrees
cylinder1_axial_resolution = 200 #cells
cylinder1_radial_resolution = 1000 #cells
cylinder2_axial_resolution = 200 #cells
cylinder2_radial_resolution = 1000 #cells
tube_axial_resolution = 1000 #cells
tube_radial_resolution = 100 #cells

'''
            Back View                   Side View                 Front View
15        14         11        10    10    Top     4   4          5         8          9
+----------+         +----------+    +------+------+   +----------+         +----------+
|          |         |          |     \     |<a/2 /    |          |         |          |
|          |         |          |      \    |----/     |          |         |          |
| Cylinder |         | Cylinder |       \   |   /      | Cylinder |         | Cylinder |
|     2    |13     12|     1    |   Back \  |  /Front  |     1    |6       7|     2    |
|          +---------+          |         \-|-/        |          +---------+          |
|          |  Tube   |          |          \|/         |          |  Tube   |          |
+----------+---------+----------+           +          +----------+---------+----------+
3          2         1          0           0          0          1         2          3
                                          Bottom
                   ^                            ^                         ^
             <--x  |                      z --> |                   x-->  |
                   y                            y                         y

            Top View
9          8         5          4
+----------+         +----------+
|          |         |          |
|          |---------|          |
+ - - - - -+- - - - -+- - - - - +
| 3       2|---------|1        0|
|          |         |          |
+----------+         +----------+
15        14         11        10
                    ^
               <--x |
                    z
'''


from math import *

# Find vertices
angle = radians(angular_resolution)
Vertices = [
			[              0,                            0,                                0          ],
			[         cyl1_height,                       0,                                0          ], 
			[     cyl1_height+tube_len,                  0,                                0          ],
			[cyl1_height+tube_len+cyl2_height,           0,                                0          ],
			[              0,                  cyl1_dia*cos(angle/2)/2,        cyl1_dia*sin(angle/2)/2],
			[         cyl1_height,             cyl1_dia*cos(angle/2)/2,        cyl1_dia*sin(angle/2)/2],
			[         cyl1_height,             tube_dia*cos(angle/2)/2,        tube_dia*sin(angle/2)/2],
			[     cyl1_height+tube_len,        tube_dia*cos(angle/2)/2,        tube_dia*sin(angle/2)/2],
			[     cyl1_height+tube_len,        cyl1_dia*cos(angle/2)/2,        cyl1_dia*sin(angle/2)/2],
			[cyl1_height+tube_len+cyl2_height, cyl1_dia*cos(angle/2)/2,        cyl1_dia*sin(angle/2)/2],
			[              0,                  cyl1_dia*cos(angle/2)/2,       -cyl1_dia*sin(angle/2)/2],
			[         cyl1_height,             cyl1_dia*cos(angle/2)/2,       -cyl1_dia*sin(angle/2)/2],
			[         cyl1_height,             tube_dia*cos(angle/2)/2,       -tube_dia*sin(angle/2)/2],
			[     cyl1_height+tube_len,        tube_dia*cos(angle/2)/2,       -tube_dia*sin(angle/2)/2],
			[     cyl1_height+tube_len,        cyl1_dia*cos(angle/2)/2,       -cyl1_dia*sin(angle/2)/2],
			[cyl1_height+tube_len+cyl2_height, cyl1_dia*cos(angle/2)/2,       -cyl1_dia*sin(angle/2)/2]
		   ]


with open('blockMeshDict', 'w') as blockMeshDict:

    blockMeshDict.write('/*--------------------------------*- C++ -*----------------------------------*\\\n' +
    					'  =========                 |\n' +
    					'  \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox\n' +
    					'   \\\\    /   O peration     | Website:  https://openfoam.org\n' +
    					'    \\\\  /    A nd           | Version:  6\n' +
    					'     \\\\/     M anipulation  |\n' +
    					'\\*---------------------------------------------------------------------------*/\n' +
    					'FoamFile\n' +
    					'{\n' +
    					'    version     2.0;\n' +
    					'    format      ascii;\n' +
    					'    class       dictionary;\n' +
    					'    object      blockMeshDict;\n'+
    					'}\n' +
    					'// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n' +
    					'\n' +
    					'convertToMeters 1;\n' +
    					'\n'+
    					'vertices\n' +
    					'(\n')

    for vertex in range(len(Vertices)):
    	blockMeshDict.write('    ('+str(Vertices[vertex][0])+' '+str(Vertices[vertex][1])+' '+str(Vertices[vertex][2])+')\n')
    blockMeshDict.write(');\n' +
    					'\n' +
    					'edges\n' +
    					'(\n' +
    					'    arc 4 10 (0 '+str(cyl1_dia/2)+' 0)\n'+
    					'    arc 5 11 ('+str(cyl1_height)+' '+str(cyl1_dia/2)+' 0)\n'+
    					'    arc 6 12 ('+str(cyl1_height)+' '+str(tube_dia/2)+' 0)\n'+
    					'    arc 7 13 ('+str(cyl1_height+tube_len)+' '+str(tube_dia/2)+' 0)\n'+
    					'    arc 8 14 ('+str(cyl1_height+tube_len)+' '+str(cyl2_dia/2)+' 0)\n'+
    					'    arc 9 15 ('+str(cyl1_height+tube_len+cyl2_height)+' '+str(cyl2_dia/2)+' 0)\n'+
    					');\n')
    blockMeshDict.write('\n' +
    					'blocks\n' +
    					'(\n' +
    					'    hex (0 1 11 10 0 1 5 4) ('+str(cylinder1_axial_resolution)+' '+str(cylinder1_radial_resolution)+' 1) simpleGrading (1 1 1)\n'+
    					'    hex (1 2 13 12 1 2 7 6) ('+str(tube_axial_resolution)+' '+str(tube_radial_resolution)+' 1) simpleGrading (1 1 1)\n'+
    					'    hex (2 3 15 14 2 3 9 8) ('+str(cylinder2_axial_resolution)+' '+str(cylinder2_radial_resolution)+' 1) simpleGrading (1 1 1)\n'+
    					');\n')
    blockMeshDict.write('\nboundary\n'+
    					'(\n'+
    					'    front\n'+
    					'    {\n'+
    					'        type wedge;\n'+
    					'        faces\n'+
    					'        (\n'+
    					'            (0 1 5 4)\n'+
    					'            (1 2 7 6)\n'+
    					'            (2 3 9 8)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    back\n'+
    					'    {\n'+
    					'        type wedge;\n'+
    					'        faces\n'+
    					'        (\n'+
    					'            (1 0 10 11)\n'+
    					'            (2 1 12 13)\n'+
    					'            (3 2 14 15)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    cyl1_piston\n'+
    					'    {\n'+
    					'        type patch;\n'+
    					'        faces\n'+
    					'        (\n'+
    					'            (0 4 10 0)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    cyl1_wall\n'+
    					'    {\n'+
    					'        type wall;\n'+
    					'        faces\n'+
    					'        (\n'+
    					'            (4 5 11 10)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    cyl1_head\n'+
    					'    {\n'+
    					'        type wall;\n'+
    					'        faces\n'+
    					'        (\n'+
    					'            (1 11 5 1)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    tube_wall\n'+
    					'    {\n'+
    					'        type wall;\n'+
    					'        faces\n'+
    					'        (\n'+
    					'            (6 7 13 12)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    cyl2_head\n'+
    					'    {\n'+
    					'        type wall;\n'+
    					'        faces\n'+
    					'        (\n'+
    					'            (2 8 14 2)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    cyl2_wall\n'+
    					'    {\n'+
    					'        type wall;\n'+
    					'        faces\n'+
    					'        (\n'+
    					'            (8 9 15 14)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    cyl2_piston\n'+
    					'    {\n'+
    					'        type patch;\n'+	
    					'        faces\n'+
    					'        (\n'+
    					'            (3 15 9 3)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    cyl1_tube_entrance\n'+
    					'    {\n'+
    					'        type patch;\n'+	
    					'        faces\n'+
    					'        (\n'+
    					'            (1 6 12 1)\n'+
    					'        );\n'+
    					'    }\n'+
    					'    cyl2_tube_entrance\n'+
    					'    {\n'+
    					'        type patch;\n'+	
    					'        faces\n'+
    					'        (\n'+
    					'            (2 13 7 2)\n'+
    					'        );\n'+
    					'    }\n'+
    					');\n')
    blockMeshDict.write('\n\nmergePatchPairs\n(\n(cyl1_head cyl1_tube_entrance)\n(cyl2_head cyl2_tube_entrance));')
blockMeshDict.close()
