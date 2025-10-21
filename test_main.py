import shlex
import pytest
from script import my_script
from functions import average_rating
from read_write import read_csv
from test_cases import (
    TEST_AVERAGE_RATING_TRUE,
    TEST_AVERAGE_RATING_FALSE,
    TEST_MY_SCRIPT_TRUE,
    TEST_MY_SCRIPT_FALSE,
    TEST_READ_CSV_TRUE,
    TEST_READ_CSV_FALSE,
)


def test_shlex():
    command = "-f products1.csv products2.csv -r average_rating"
    as_list = ["-f", "products1.csv", "products2.csv", "-r", "average_rating"]
    assert shlex.split(command) == as_list


@pytest.mark.parametrize("test_list, header, expected_output", TEST_AVERAGE_RATING_TRUE)
def test_average_rating(capsys, test_list, header, expected_output):
    undecorated_average_rating = average_rating.__wrapped__
    assert undecorated_average_rating(test_list, header) == expected_output


@pytest.mark.parametrize(
    "test_list, header, expected_output", TEST_AVERAGE_RATING_FALSE
)
def test_average_rating(capsys, test_list, header, expected_output):
    undecorated_average_rating = average_rating.__wrapped__
    assert undecorated_average_rating(test_list, header) != expected_output


@pytest.mark.parametrize("command, expected_output", TEST_MY_SCRIPT_TRUE)
def test_my_script(capsys, command, expected_output):
    parser = my_script(shlex.split(command))
    result = parser.files, parser.report, parser.output
    assert result == expected_output


@pytest.mark.parametrize("command, expected_output", TEST_MY_SCRIPT_FALSE)
def test_my_script(capsys, command, expected_output):
    parser = my_script(shlex.split(command))
    result = parser.files, parser.report, parser.output
    assert result != expected_output


@pytest.mark.parametrize("file_name, expected_output", TEST_READ_CSV_TRUE)
def test_read_csv(capsys, file_name, expected_output):
    result = read_csv(file_name)
    assert result == expected_output


@pytest.mark.parametrize("file_name, expected_output", TEST_READ_CSV_FALSE)
def test_read_csv(capsys, file_name, expected_output):
    result = read_csv(file_name)
    assert result != expected_output
