import unittest
import sys
sys.path.append('../')

import modules.core as core

class TestMigrationMethods(unittest.TestCase):

    def test_get_java_files(self):	
    	import os
    	self.assertEqual(core.get_java_files(os.getcwd()), ['/home/fdemeloj/Downloads/cases/migration_jdk/test_files/jdk8b.java', '/home/fdemeloj/Downloads/cases/migration_jdk/test_files/jdk8a.java', '/home/fdemeloj/Downloads/cases/migration_jdk/test_files/jdk8.java', '/home/fdemeloj/Downloads/cases/migration_jdk/test_files/jdk8c.java'])

    def test_def_get_deprecated_modules(self):
		list_result = ["java.xml.ws","java.xml.bind", "java.xml.ws.annotation", "java.corba", "java.transaction", "java.activation", "java.se.ee", "jdk.xml.ws", "jdk.xml.bind", "jdk.snmp", "javax.security.auth.Policy", "java.lang.Runtime.runFinalizersOnExit(True)","java.lang.SecurityManager.checkAwtEventQueueAccess",
"java.lang.SecurityManager.checkMemberAccess", "java.lang.SecurityManager.checkSystemClipboardAccess", "java.lang.SecurityManager.checkTopLevelWindow", "java.lang.System.runFinalizersOnExit",
"java.lang.Thread.destroy()", "java.lang.Thread.stop", "Xbootclasspath/p"]
		self.assertEqual(core.get_deprecated_modules(), list_result)

    def test_create_report(self):
        import tempfile
        import os
        outfile_path = tempfile.mkstemp()[1]
        try:
            core.create_report(outfile_path)
            contents = open(outfile_path).read()
        finally:
            # NOTE: To retain the tempfile if the test fails, remove
            # the try-finally clauses
            os.remove(outfile_path)
        self.assertEqual(contents, "==== REPORT JDK 11 Migration ====")

    def test_read_module_to_mmap(self):
        self.assertEqual(core.read_module_to_mmap('test_files/jdk8.java', False).read(5), "corba")

    #def test_find_module_from_mmap():
    #    try:
    #        with open('../test_files/jdk8a.java') as f:
    #            file_mmap = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    #            self.assertEqual(core.find_module_from_mmap(file_mmap))

if __name__ == '__main__':
    unittest.main()