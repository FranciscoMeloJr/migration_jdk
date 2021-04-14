import csv

"""
This module reads the alternatives.csv, which is the file with table for alternatives
The alternatives are based on:
https://medium.com/@speakjava/jdk-11-pitfalls-for-the-unwary-e08d864065c1
https://medium.com/criciumadev/its-time-migrating-to-java-11-5eb3868354f9
"""

def read_alternative_create_dict(alt_file='alternatives.csv', debug = False):
    dict_alternatives= {}
    with open(alt_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print "COLUMNS: " + ", ".join(row)
                line_count += 1
            else:
                #print "Module " + row[0] + " alternative: " + row[1]
                dict_alternatives[row[0]] = row[1]
                line_count += 1
        if debug:
            print dict_alternatives

        return dict_alternatives

def read_alternative_file(alt_file='alternatives.csv'):
    with open(alt_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print "COLUMNS: " + ", ".join(row)
                line_count += 1
            else:
                print "Module " + row[0] + " alternative: " + row[1]
                dict_alternatives[row[0]] = row[1]
                line_count += 1

        print "Number of modules: " + str(line_count) + " lines."

#print read_alternative_create_dict()