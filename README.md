This runs on python version 2.7.0

*NOTE: update core.py of gdsCAD with the file uploaded in the repository 
By default, the file can be found in the following path : "/home/aditya/.local/lib/python2.7/site-packages/gdsCAD/core.py"

The following libraries need to be installed before running this program:
->gdsCAD*
->matplotlib
->numpy
->descartes
->shapely
->datetime

For all the programs except for main.py, please run the command "python NAME.py -h" to display the list of parameters that can be modified 
along with their default values.
The parameterizations made are shown in the parametrizations.pdf file in the folder.

The main file is given in the repository : it makes the gds file for the whole xmon. 
Make sure all the files in the repository are in your folder before you run it!

When asked for the parametrizations, the main program is basically calling all the other programs, so type in the arguments
as if you were actually running the each one of these programs.
Example run:

>>>>> python main.py
Enter parameters for the capacitor : (Enter blank for default values)
-s 10 -w 4 -l 150
Enter parameters for the XY Control : (Enter blank for default values)
-c 20
Enter type of SQUID : (kelly/default)
kelly
Enter parameters for the SQUID and Z control : (Enter blank for default values)
-x 100 -y 150
Enter parameters for the Quantum Bus : (Enter blank for default values)
-l2 200
Enter parameters for the Resonator : (Enter blank for default values)

NOTE: Once the values of s and w are given, you don't need to provide them again.
