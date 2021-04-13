import mmap
import os

#fetch all java files in diretory
def get_java_files(filepath=os.getcwd(), filetype='.java', debug = False):
    paths = []
    for root, dirs, files in os.walk(filepath):
        for file in files:
            if file.lower().endswith(filetype.lower()):
                paths.append(os.path.join(root, file))
    if debug == True:
        print paths
    return(paths)

#fetch depreated modules
def get_deprecated_modules():
	return ["java.xml.ws","java.xml.bind", "java.xml.ws.annotation", "java.corba", "java.transaction", "java.activation", "java.se.ee", "jdk.xml.ws", "jdk.xml.bind", "jdk.snmp", "javax.security.auth.Policy", "java.lang.Runtime.runFinalizersOnExit(True)","java.lang.SecurityManager.checkAwtEventQueueAccess()",
"java.lang.SecurityManager.checkMemberAccess", "java.lang.SecurityManager.checkSystemClipboardAccess", "java.lang.SecurityManager.checkTopLevelWindow", "java.lang.System.runFinalizersOnExit",
"java.lang.Thread.destroy()", "java.lang.Thread.stop"]

#create report [[fileA, [modulea, moduleb]], [[fileb, [modulea, moduleb]]
def create_report( report_name = 'report_migration.txt', debug = False):
    outfile = open(report_name, "w") 
    outfile.write("==== Report JDK 11 Migration ====")
    if debug == True:
        print "Report " + report_name +" will be created on " + os.getcwd()
    return outfile

def add_modules_report(outfile, list_results_deprecated_mods, debug = False):
    name_file = list_results_deprecated_mods[0]
    dep_modules = list_results_deprecated_mods[1]
    s1='\n'
    s1=name_file+':\t'
    if len(dep_modules) > 0:
        s1+='\t'.join(dep_modules)
    else:
        s1+= "no deprecated module"
    print s1
    outfile.write('\n')
    outfile.write(s1)

#find module from mmap
def find_module_from_mmap(mmap_data, module_name):
    if mmap_data:
    	if mmap_data.find(module_name) != -1:
    		return True

#read file to mmap
def read_module_to_mmap(fname, debug = False):
    try:
    	with open(fname) as f:
    	    file_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    	return file_mmap
    except IOError:
        print("File not accessible")
    except ValueError:
        print("Oops!  File is empty")

#List all deprecated modules in a file:
def deprecated_modules_in_file(deprecated_mods, fname, debug = False):
    list_deprecated = []
    #list of deprecated mmodules
    mmap_data = read_module_to_mmap(fname)

    #compare with files
    for mod in deprecated_mods:
        if find_module_from_mmap(mmap_data, mod) == True:
            list_deprecated.append(mod)

    if debug == True:
        print list_deprecated

    return list_deprecated

#Main function
def main(filepath=os.getcwd()):
    print("Migration JDK 8 to JDK 11 Tool")
    #get all files in diretory
    list_files = get_java_files(filepath)

    #Load deprecated modules
    deprecated_mods = get_deprecated_modules()

    #write report
    outfile = create_report()

    #get dir name
    for each_file in list_files:
        #iterating over each file name
        list_deprecated = []
        list_deprecated = deprecated_modules_in_file(deprecated_mods, each_file)
        #add file vs modules
        add_modules_report(outfile, [each_file, list_deprecated])
    outfile.close()
    
if __name__ == "__main__":
    main()
