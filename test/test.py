import pytest
import filecmp
from main.dateValidator import  dateTimeValidator,dateClass

def test_check_date_validity_valid():
    date_string = "9999-10-30T20:59:00Z"
    assert dateTimeValidator().checkDateValidity(date_string) == date_string


def test_check_date_validity_invalid():
    date_string = "2024-04-27T15:30:00"
    assert dateTimeValidator().checkDateValidity(date_string) is None

def test_date_validator1():
    dateClass().findValidDate()
    actualResult="testOutput/output.txt"
    expectedResult="testData/expected.txt"
    assert filecmp.cmp(actualResult, expectedResult, shallow=True), "Files are not identical."


def test_date_validator():
    # Perform the validation and capture the result
    validation_result = dateClass().findValidDate()

    # Define the paths to the actual and expected result files
    actual_result_path = "testOutput/output.txt"
    expected_result_path = "testData/expected.txt"

    # Check if the actual result matches the expected result
    assert filecmp.cmp(actual_result_path, expected_result_path, shallow=True), \
        f"Files '{actual_result_path}' and '{expected_result_path}' are not identical."





