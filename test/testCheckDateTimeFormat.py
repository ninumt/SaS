import os
import filecmp
from main.checkDateTimeFormat import *

def test_file_comparison():
    # Provide a mixed data which contains invalid, duplicate dates with whitespace, ,', blank spaces in input file
    input_file_path = "../testData/input.txt"
    output_file_path = "../testOutput/output.txt"
    expected_file_path = "../testData/expected.txt"
    processor = CheckDateTimeFormat()
    processor.read_write_check_date_time(input_file_path, output_file_path)

    assert os.path.exists(output_file_path)
    assert os.path.exists(expected_file_path)

    assert filecmp.cmp(output_file_path, expected_file_path)

def test_duplicate_date_strings():
    # Provide input file containing duplicate date strings
    input_file_path = "../testData/duplicate_input.txt"
    output_file_path = "../testOutput/duplicate_output.txt"
    expected_file_path = "../testData/duplicate_expected.txt"
    processor = CheckDateTimeFormat()
    processor.read_write_check_date_time(input_file_path, output_file_path)

    assert os.path.exists(output_file_path)
    assert os.path.exists(expected_file_path)

    assert filecmp.cmp(output_file_path, expected_file_path)
def test_empty_input_file():
    # Provide an empty input file
    input_file_path = "../testData/empty_input.txt"
    output_file_path = "../testOutput/empty_output.txt"
    expected_file_path = "../testData/empty_expected.txt"
    processor = CheckDateTimeFormat()
    processor.read_write_check_date_time(input_file_path, output_file_path)

    assert os.path.exists(output_file_path)
    assert os.path.exists(expected_file_path)

    assert filecmp.cmp(output_file_path, expected_file_path)

def test_invalid_datetime_input_file():
    # Provide an invalid date time format in input file
    input_file_path = "../testData/invalid_input.txt"
    output_file_path = "../testOutput/invalid_output.txt"
    expected_file_path = "../testData/invalid_expected.txt"
    processor = CheckDateTimeFormat()

    processor.read_write_check_date_time(input_file_path, output_file_path)

    assert os.path.exists(output_file_path)
    assert os.path.exists(expected_file_path)

    assert filecmp.cmp(output_file_path, expected_file_path)

# def test_sorting():
#     # Provide input file containing unsorted date strings
#     input_file_path = "../testData/unsorted_input.txt"
#     output_file_path = "../testOutput/unsorted_output.txt"
#     expected_file_path = "../testData/sorted_expected.txt"
#     processor = CheckDateTimeFormat(input_file_path, output_file_path)
#     processor.read_write_check_date_time()
#
#     assert os.path.exists(output_file_path)
#     assert os.path.exists(expected_file_path)

#    assert filecmp.cmp(file2_path, file3_path)