import csv
from robot.api import logger

class CSVLibrary(object):

    def read_csv_file(self, filename):
        '''Read CSV file and return its content as a Python list.
        Use Robot Framework's Collections library to futher manipulate lists.
        '''

        f = open(filename, 'r')
        csvfile = csv.reader(f)
        f.close
        return [row for row in csvfile]

    def empty_csv_file(self, filename):
        '''This keyword will empty (truncate) the CSV file.
        '''

        f = open(filename, "w")
        f.truncate()
        f.close()

    def append_to_csv_file(self, filename, data):
        '''This keyword will append data to a new or existing CSV file.
        Data should be iterable (e.g. list or tuple)
        '''

        f = open(filename, 'a')
        csvfile = csv.writer(f)
        for item in data:
            csvfile.writerow([item])
        f.close()
