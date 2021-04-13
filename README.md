Migration JDK 11 Helper

This is a simple tool to help migrate from JDK 8 to JDK 11 developed on Python 2.7.
To make this simple I broke the script in two: migration_jdk11.py and migration_cli.py

This is based on https://docs.oracle.com/en/java/javase/11/migrate/migration-guide.pdf

As defensive programming the script will give more false positives than false negatives.
The results are written to report_migration.txt

migration_jdk11.py: Core functionality
migration_cli.py: CLI interface

Example usage:
~~~
$ python migration_jdk11.py
Migration JDK 8 to JDK 11 Tool
/migration_jdk/test_files/jdk8b.java:	java.corba
/migration_jdk/test_files/jdk8a.java:	java.xml.bind
/migration_jdk/test_files/jdk8.java:	java.xml.ws	java.xml.bind
Oops!  File is empty
/migration_jdk/test_files/jdk8c.java:	no deprecated module
~~~

CLI interface:
~~~
$python migration_cli.py -p /EJBtests/migration_jdk
Migration JDK 8 to JDK 11 Tool
/migration_jdk/test_files/jdk8b.java:	java.corba
/migration_jdk/test_files/jdk8a.java:	java.xml.bind
/migration_jdk/test_files/jdk8.java:	java.xml.ws	java.xml.bind
Oops!  File is empty
/migration_jdk/test_files/jdk8c.java:	no deprecated module
~~~

~~~
$python migration_cli.py -h 
usage: python migration_cli.py -path

Migration JDK 11 Helper

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         shows debug logs
  -p PATH, --path PATH  The path of the source directory to do the migration
                        to JDK 11. In case none is given, current path is used
  -g, --guide           Opens the Oracle JDK Migration Guide found on
                        https://docs.oracle.com/en/java/javase/11/migrate
                        /migration-guide.pdf
  -jmc JMC              In JDK 11, JMC is available as a standalone package
                        and not bundled in the JDK
  -javaws JAVAWS        In JDK 11, Javaws was deprecated. See other options
  -w, --warn            The report will add warnings
  -s, --security        The report will add security details
~~~

Disclaimer
---

This tool contains/displays the migration guide from Oracle provided by them on https://docs.oracle.com/en/java/javase/11/migrate/migration-guide.pdf

