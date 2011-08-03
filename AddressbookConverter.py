#!/usr/bin/env python
from InOut import InOut
from Person import Person
from PersonCollection import PersonCollection
from Mapping import Mapping
from Merge import Merge
from Log import Log
import Correction
import getopt, sys

# BEGIN: METHODS
def printUsage():
	print("Usage:")
	print("\tpython AdressbookConverter.py --" + LO_HELP + "|-" + O_HELP)
	print("\tpython AdressbookConverter.py --" + LO_MAP + "|-" + O_MAP + " <mapping-file> --" + LO_IFILE + "|-" + O_IFILE + " <file> --" + LO_OFILE + "|-" + O_OFILE + " <file>")
	print("\tpython AdressbookConverter.py --" + LO_MERGE + "|-" + O_MERGE + " --" + LO_IFILE + "|-" + O_IFILE + " <file1>,<file2> --" + LO_OFILE + "|-" + O_OFILE + " <file>")
	print("\tpython AdressbookConverter.py --" + LO_CORRECT + "|-" + O_CORRECT + " --" + LO_IFILE + "|-" + O_IFILE + " <file> --" + LO_OFILE + "|-" + O_OFILE + " <file>")

def doHelp():
	print("\nOverview:")
	print("\"AdressbookConverter\" can convert a contact list to different formats, merge two lists together and can correct inaccurate records.")
	
	print("\nOutput file format:  text/csv (Comma-separated values) or text/x-vcard (vCard)")
	
	print("\nInput file format:  text/csv (Comma-separated values)")
	print("The first line contains the column names. The values are separated by a comma or tabulator. A value is embraced by a double quote (\").")
	print("Example:")
	print("\t\"name\",\"name_first\",\"email\"")
	print("\t\"bar\",\"foo\",\"foo@baz.org\"")
	print("\t...")
	
	print("\nMapping file format:  text/csv (Comma-separated values)")
	print("This file defines the mapping from the old column names to the new column names. Additionally a default value can be defined.\nThe values are separated by a comma or tabulator. A value is embraced by a double quote (\").")
	print("Example:")
	print("\t\"name\",\"surname\",\"no_name\"")
	print("\t\"name_first\",\"firstname\",\"\"")
	print("\t\"email\",\"E-Mail\",\"unknown\"")
	print("\t...")
	
	print("\nMerge: ")
	print("Each input file needs at least the two columns \"" + Person.NAME + "\" and \"" + Person.NAME_FIRST + "\"!\nYou can ensure this by running a mapping at first.")
	
	print("\nCorrection:")
	print("There are no correct methods implemented yet!")
	
	print()
	printUsage()
	
	print("\nPython: Version 3.x or later, http://www.python.org")
	print("Programmer: executor")
	print("Date: December 2010")

def doMap(iFile, mFile, oFile):
	pc = InOut.read(iFile)
	if(pc == None):
		return False
	mapKies = Mapping(mFile)
	pcMapped = mapKies.doMapping(pc)
	InOut.write(oFile, pcMapped)

def doMerge(iFile1, iFile2, oFile):
	pc1 = InOut.read(iFile1)
	if(pc1 == None):
		return False
	pc2 = InOut.read(iFile2)
	if(pc2 == None):
		return False
	pcMerged = Merge.merge(pc1, pc2)
	InOut.write(oFile, pcMerged)
	
def doCorrection():
	Log.warn(__class__, "Not yet implemented!")

# END: METHODS

# BEGIN: VARIABLES
__class__ = "AdressbookConverter"
# command line arguments
LO_MAP = "map"
O_MAP = "m"
LO_MERGE = "merge"
O_MERGE = "j"
LO_CORRECT = "correct"
O_CORRECT = "c"
LO_OFILE = "output-file"
O_OFILE = "o"
LO_IFILE = "input-files"
O_IFILE = "i"
LO_HELP = "help"
O_HELP = "h"

IFILES = None
OFILE = None
MFILE = None
MODE = None

# END: VARIABLES

# BEGIN: PROGRAM
print("< Adressbook Converter >")
try:
	opts, args = getopt.getopt(sys.argv[1:], O_MAP + ":" + O_MERGE + O_CORRECT + O_OFILE + ":" + O_IFILE + ":" + O_HELP, [LO_MAP + "=", LO_MERGE, LO_CORRECT, LO_OFILE + "=", LO_IFILE + "=", LO_HELP])
except getopt.GetoptError:
	Log.error(__class__, "Error in command line arguments")
	printUsage()
	sys.exit(2)
for o, a in opts:
	if o in ("--" + LO_MAP, "-" + O_MAP):
		Log.debug(__class__, "Mode: " + LO_MAP + " - File: " + a)
		MODE = LO_MAP
		MFILE = a
	elif o in ("--" + LO_MERGE, "-" + O_MERGE):
		Log.debug(__class__, "Mode: " + LO_MERGE)
		MODE = LO_MERGE
	elif o in ("--" + LO_CORRECT, "-" + O_CORRECT):
		Log.debug(__class__, "Mode: " + LO_CORRECT)
		MODE = LO_CORRECT
	elif o in ("--" + LO_OFILE, "-" + O_OFILE):
		Log.debug(__class__, "Mode: " + LO_OFILE + " - File: " + a)
		OFILE = a
	elif o in ("--" + LO_IFILE, "-" + O_IFILE):
		Log.debug(__class__, "Mode: " + LO_IFILE + " - File: " + a)
		IFILES = a.split(',')
		Log.debug(__class__, "IFILES: " + str(IFILES))
	elif o in ("--" + LO_HELP, "-" + O_HELP):
		Log.debug(__class__, "Mode: " + LO_HELP)
		MODE = LO_HELP
	else:
		Log.error(__class__, "Option not supported!")
		
if(MODE == None):
	printUsage()
	Log.debug(__class__, "No mode defined!")
	sys.exit(1)

print("Starting mode \"" + MODE + "\" ...")
if(MODE == LO_MAP):
	doMap(IFILES[0], MFILE, OFILE)
elif(MODE == LO_MERGE):
	doMerge(IFILES[0], IFILES[1], OFILE)
elif(MODE == LO_CORRECT):
	doCorrection()
elif(MODE == LO_HELP):
	doHelp()
	sys.exit(0)
else:
	Log.error(__class__, "Mode not supported!")
print("Finished!")
	
# END: PROGRAM

# 1: Read .csv
#pcKies = PersonCollection()
#pcKies.read('kies.csv')
#pcTb = PersonCollection()
#pcTb.read('thunderbird.csv')

# 2: Do mapping
#mapKies = Mapping('mappingKies.csv')
#pcKiesMapped = mapKies.doMapping(pcKies)
#mapTb = Mapping('mappingThunderbird.csv')
#pcTbMapped = mapTb.doMapping(pcTb)

# 3: Do merge
#pc = Merge.merge(pcKiesMapped, pcTbMapped)

# 4: Do correction

# 5: Save to file
#pc.write('new.csv')

