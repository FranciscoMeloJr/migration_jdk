#Import modules:
import mmap
import os
import sys

#Custom modules
import modules.alternatives as alternatives
import modules.core as core

"""
This is the main module of the migration tool.
The main functions are in modules/core.py and modules/alternatives.py
"""

#Main function
def main(filepath=os.getcwd(), warns = True, security=True):
    #Initial print
    print("Migration JDK 8 to JDK 11 Tool")
    #get all files in diretory
    list_files = core.get_java_files(filepath)

    #Load deprecated modules
    deprecated_mods = core.get_deprecated_modules()

    #total list of deprecated
    total_deprecated = []
    #write report
    outfile = core.create_report()

    #get dir name
    for each_file in list_files:
        #iterating over each file name
        list_deprecated = []
        list_deprecated = core.deprecated_modules_in_file(deprecated_mods, each_file)
        #add file vs modules
        core.add_modules_report(outfile, [each_file, list_deprecated])
        #add list_deprecated:
        total_deprecated.append(list_deprecated)

    #print warn:
    if warns == True:
        core.add_warn(outfile)

    #print security 
    if security == True:
        core.add_security(outfile)

    #list alternatives
    core.list_alternatives(total_deprecated, outfile=outfile)

    outfile.close()
    
if __name__ == "__main__":
    main()
