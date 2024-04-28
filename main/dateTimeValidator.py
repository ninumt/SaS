import re
import logging
from datetime import datetime

class DateTimeValidator:
    '''
    A class to validate date strings and handle input/output files.
    '''

    def __init__(self):
        logging.basicConfig(filename='../testLogs/myLogfile.log',
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def check_date_validity(self, date_string):
        '''
        Checks if the date string is a valid UTC date format.
        :param date_string: The date string to validate.
        :return: Date string if string is valid, None if string is invalid.
        '''
        match_expression = r'^\d{4}-([0-1][0-2])-([0-2][0-9]|3[0-1])T([0-2][0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9](Z|\+([0-2][0-3]|[0-1][0-9]):[0-5][0-9]|\-([0-2][0-3]|[0-1][0-9]):[0-5][0-9])$'

        if re.match(match_expression, date_string):
            logging.info(f"Valid date format {date_string}, returning Date")
            return date_string
        else:
            logging.info(f"Invalid date String {date_string}, returning None ")
            return None

class DateProcessor(DateTimeValidator):
    '''
    A class to handle input and output data files.
    '''

    def __init__(self):
        super().__init__()
        self.input_file = "../testData/input.txt"
        self.output_file = "../testOutput/output.txt"

    def read_file_lines(self):
        '''
        Reads lines from the input file.
        :return: List of unique lines in the file.
        '''
        lines = set()
        with open(self.input_file, 'r') as file:
            for line in file:
                line = line.strip('\n, ')
                lines.add(line)
        return list(lines)

    def write_to_file(self, valid_date_list):
        '''
        Writes valid dates to the output file in sorted order.
        :param valid_date_list: List of valid dates.
        :return: True if successful, False otherwise.
        '''
        valid_date_list.sort()  # Sort the list of valid dates
        with open(self.output_file, 'w') as file:
            for date in valid_date_list:
                file.write(date + '\n')
        return True

    def find_valid_dates(self):
        '''
        Finds valid dates from input file and writes them to an output file.
        :return: True if successful, False otherwise.
        '''
        lines = self.read_file_lines()
        valid_dates = []
        for line in lines:
            status = self.check_date_validity(line)
            if status:
                print(f"About to write valid date {status} to file.")
                valid_dates.append(status)
            else:
                logging.info(f"Not writing date {line} as it is not a valid UTC date")
                continue

        logging.info("Writing to output file.")
        self.write_to_file(valid_dates)
        print("Program completed.")
        return True

if __name__ == "__main__":
    status = DateProcessor().find_valid_dates()
