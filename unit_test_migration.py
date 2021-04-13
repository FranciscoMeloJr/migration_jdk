import unittest
import migration_jdk11

class TestMigrationMethods(unittest.TestCase):

    def test_get_java_files(self):	
    	import os
    	self.assertEqual(migration_jdk11.get_java_files(os.getcwd()), ['/home/fdemeloj/Downloads/cases/EJBtests/migration/test_files/jdk8b.java', '/home/fdemeloj/Downloads/cases/EJBtests/migration/test_files/jdk8a.java', '/home/fdemeloj/Downloads/cases/EJBtests/migration/test_files/jdk8.java', '/home/fdemeloj/Downloads/cases/EJBtests/migration/test_files/jdk8c.java'])

    def test_def_get_deprecated_modules(self):
		list_result = ["java.xml.ws","java.xml.bind", "java.xml.ws.annotation", "java.corba", "java.transaction", "java.activation", "java.se.ee", "jdk.xml.ws", "jdk.xml.bind"]
		self.assertEqual(migration_jdk11.get_deprecated_modules(), list_result)

    def test_create_report(self):
        import tempfile
        import os
        outfile_path = tempfile.mkstemp()[1]
        try:
            migration_jdk11.create_report(outfile_path)
            contents = open(outfile_path).read()
        finally:
            # NOTE: To retain the tempfile if the test fails, remove
            # the try-finally clauses
            os.remove(outfile_path)
        self.assertEqual(contents, "==== Report JDK 11 Migration ====")

if __name__ == '__main__':
    unittest.main()


