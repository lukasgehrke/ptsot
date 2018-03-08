# Perspective Taking/Spatial Orientation Test
Electronic version of the "Perspective Taking/Spatial Orientation Test" by Hegarty, Kozhevnikov and Waller. It avoids
the need for measuring the participants' response angles by hand and for computing the delta angle to the correct solution. The following document hosted by the Spatial Intelligence and Learning Center served as a reference for the implementation: http://spatiallearning.org/resource-info/Spatial_Ability_Tests/PTSOT.pdf (accessed 13 Feb 2017).
It also mentions the two main papers the test is based on:

 * Hegarty, M., & Waller, D. (2004). A dissociation between mental rotation and perspective-taking spatial abilities. Intelligence, 32, 175-191.

 * Kozhevnikov, M., & Hegarty, M. (2001). A dissociation between object-manipulation and perspective-taking spatial abilities. Memory & Cognition, 29, 745-756.
 
## Dependencies
 * Python3 (`sudo apt-get install python3` on Debian-based systems) - http://www.python.org/
 * Matplotlib (`sudo apt-get install python3-matplotlib` on Debian-based systems) - http://matplotlib.org/
 
## Usage Instructions
The test can be run by `python3 perspective_taking_test.py`. After entering the participants ID on the console (which determines the name of the result file),
the test GUI is loaded and shows the instructions and example task, followed by the logged trials. 

The name of the output file is `results-ID.txt`, where ID is the entered participant ID. On each line, it shows the
task number, correct response angle (deg), actually logged response angle (deg) and absolute angular error (deg) in a comma-separated fashion. The last
line gives the average angular error (deg) over all 12 trials as a participant's total score.

## Screenshot
![Screenshot](screenshot.png)
 
##
PTSOT Version taken from https://github.com/TimDomino/ptsot working with python3
itall the following dependencies:
0. check if pip3 (pip for python3) is installed: type "which pip3" or "pip3 -V" on a mac terminal or windows shell
 -> if it is installed, the installed path should display
 -> if not follow (https://pip.pypa.io/en/stable/installing/)
1. install pip3 (when on osx or windows), apt-get (Linux)
install the following packages with dependecies by typing the following command on a mac terminal or windows shell
"python3 -mpip install matplotlib"
"python3 -mpip install nose"
"python3 -mpip install pylsl"

2. run the task by typing "python3 perspective_taking_test_german.py" on a mac terminal or windows shell