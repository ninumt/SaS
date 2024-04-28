import re
import logging
from datetime import datetime


class CheckDateTimeFormat:
    def __init__(self):
        self.file1_path = "../testData/input.txt"
        self.file2_path = "../testOutput/output.txt"

    def configure_logging(self):
        logging.basicConfig(filename='../testLogs/myLogfile.log',
                            level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def read_write_check_date_time(self, file1_path=None, file2_path=None):
        if file1_path:
            self.file1_path = file1_path
        if file2_path:
            self.file2_path = file2_path

        logging.info("Reading and writing date-time from input file...")
        with open(self.file1_path, 'r') as file1:
            content = file1.readlines()
            valid_dates = set()
            for line in content:
                line = line.strip('\n')
                line = line.strip(',')
                date_str = line.strip()
                if self.is_valid_utc_date(date_str):
                    valid_dates.add(date_str)

        sorted_dates = sorted(valid_dates)
        self.write_output_file(sorted_dates)

    def is_valid_utc_date1(self, date_str):
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%SZ")
            datetime.datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S%z")
            return True
        except ValueError as e:
            logging.error(f"Invalid date String {e} returning None ")
            return False

    def is_valid_utc_date2(self, dateString):
        '''
        checks if the date string is a valid UTC date format.
        :param dateString:
        :return: Date string if string is valid/ False if string is invalid.
        '''

        try:
            dt = datetime.fromisoformat(dateString)
            return dt
        except ValueError:
            return False

    def is_valid_utc_date(self, date_str):
        '''
        checks if the date string is a valid UTC date format.
        :param date_str:
        :return:  date(string) if date is valid else return False.
        '''
        self.date_str = date_str
        matchExpression = '^\d{4}-([0-1][0-2])-([0-2][0-9]|3[0-1])T([0-2][0-3]|[0-1][0-9]):[0-5][0-9]:[0-5][0-9](Z|\+([0-2][0-3]|[0-1][0-9]):[0-5][0-9]|\-([0-2][0-3]|[0-1][0-9]):[0-5][0-9])$'

        matchObj = re.search(matchExpression, self.date_str)
        if matchObj:
            return self.date_str
        else:
            return False

    def write_output_file(self, data):
        with open(self.file2_path, 'w') as file2:
            for date_str in data:
                file2.write(date_str + '\n')

if __name__ == "__main__":
    processor = CheckDateTimeFormat()
    processor.read_write_check_date_time()
