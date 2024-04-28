import pytest
import filecmp
from main.dateTimeValidator import DateTimeValidator, DateProcessor

@pytest.mark.parametrize("date_string, expected", [
    ("9999-10-30T20:59:00Z", "9999-10-30T20:59:00Z"),  # Valid date
    ("2024-04-27T15:30:00", None)                      # Invalid date
])
def test_check_date_validity(date_string, expected):
    assert DateTimeValidator().check_date_validity(date_string) == expected

def test_find_valid_dates():
    # Initialize DateProcessor
    date_processor = DateProcessor()

    # Call the method under test
    date_processor.find_valid_dates()

    # Define the paths to the actual and expected result files
    actual_result_path = "testOutput/output.txt"
    expected_result_path = "testData/expected.txt"

    # Check if the actual result matches the expected result
    assert filecmp.cmp(actual_result_path, expected_result_path, shallow=True), \
        f"Files '{actual_result_path}' and '{expected_result_path}' are not identical."
