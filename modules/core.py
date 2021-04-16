#Import modules:
import mmap
import os
import sys

import modules.alternatives as alternatives

"""
This is the core module:
"""

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

#List alternatives:    CREATING LIST_ALTERNATIVES
def list_alternatives(list_deprecated=["runFinalizersOnExit"], debug = False, outfile='report_migration.txt'):
    #unify list
    flat_list_mod = [item for sublist in list_deprecated for item in sublist]
    #remove duplicates
    flat_list_mod = list(dict.fromkeys(flat_list_mod))
    if debug:
        print flat_list_mod

    #read dict alternatives
    dict_alternatives = alternatives.read_alternative_create_dict('modules/alternatives.csv')

    outfile.write("\n\n==== ALTERNATIVES ====")
    #iterate and record on the report.txt
    for each_mod in flat_list_mod:
        if dict_alternatives.get(each_mod):
            outfile.write("\nFor module " + each_mod +" : "+ str(dict_alternatives[each_mod]))
        else:
            outfile.write("\nNo recommendation for: "+ str(each_mod))

#fetch depreated modules
def get_deprecated_modules():
	return ["java.xml.ws","java.xml.bind", "java.xml.ws.annotation", "java.corba", "java.transaction", "java.activation", "java.se.ee", "jdk.xml.ws", "jdk.xml.bind", "jdk.snmp", "javax.security.auth.Policy", "java.lang.Runtime.runFinalizersOnExit(True)","java.lang.SecurityManager.checkAwtEventQueueAccess",
"java.lang.SecurityManager.checkMemberAccess", "java.lang.SecurityManager.checkSystemClipboardAccess", "java.lang.SecurityManager.checkTopLevelWindow", "java.lang.System.runFinalizersOnExit",
"java.lang.Thread.destroy()", "java.lang.Thread.stop", "Xbootclasspath/p"]

#create report [[fileA, [modulea, moduleb]], [[fileb, [modulea, moduleb]]
def create_report( report_name = 'report_migration.txt', debug = False):
    outfile = open(report_name, "w") 
    outfile.write("==== REPORT JDK 11 Migration ==== \n")
    outfile.write("==== File | Module & API ====\n")
    if debug == True:
        print "Report " + report_name +" will be created on " + os.getcwd()
    return outfile

def add_modules_report(outfile, list_results_deprecated_mods, debug = True):
    name_file = list_results_deprecated_mods[0]
    dep_modules = list_results_deprecated_mods[1]
    s1='\n'
    s1=name_file+':\t'
    if len(dep_modules) > 0:
        s1+='\t'.join(dep_modules)
    else:
        s1+= "no deprecated module"
    if debug:
        print s1
    outfile.write('\n')
    outfile.write(s1)

#find module from mmap
def find_module_from_mmap(mmap_data, module_name):
    if mmap_data:
    	if mmap_data.find(module_name) != -1:
    		return True
    return False

#add security
def add_security(outfile):
    outfile.write("\n\n==== SECURITY CERTIFICATES ====")
    outfile.write("\nGTE CyberTrust Global Root certificate has been removed from the keystore in JDK 11.\n")
    outfile.write("\nThe following root certificates have been removed from the truststore in JDK 11:\n")
    outfile.write("Several Symantec Root CAs, ")
    outfile.write("Baltimore Cybertrust Code Signing CA, ")
    outfile.write("SECOM Root Certificate, ")
    outfile.write("AOL and Swisscom root certificates.")

#add security
def add_warn(outfile):
    outfile.write("\n\n==== WARNINGS ====")
    outfile.write("\nList of JAva EE and Corba modules AND APIs were removed\n")
    outfile.write('%s' % ', '.join(map(str, get_deprecated_modules())))
    outfile.write("\nSee more references on https://docs.oracle.com/en/java/javase/11/migrate/migration-guide.pdf")

#list keystore given JAVA_HOME is set ~ Keystore file == keystore.jks | Truststore file == cacerts.jks
def list_certificates(java_path):
    import os
    stream = os.popen('keytool -keystore "$JAVA_HOME/jre/lib/security/cacerts" -storepass changeit -list')
    output = stream.read()
    print output

#read file to mmap
def read_module_to_mmap(fname, debug = False):
    if debug:
        print fname
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