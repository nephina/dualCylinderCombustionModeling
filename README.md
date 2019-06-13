# dualCylinderCombustionModeling
Simulation models of consecutive combustion in connected cylinders


You will need OpenFOAM in order to run this, and you will need to chmod +x the Allrun and Allclean files beforehand as well.

Geometry of the two cylinders and connecting tube is parametrized in the python script in constant/polyMesh/.
Solver/turbulence models all come from the OpenFOAM 6 tuturials/incompressible/simpleFoam/pitzDaily/ example. These are only
preliminary tests, compressible solvers and turbulence models need to be figured out.
