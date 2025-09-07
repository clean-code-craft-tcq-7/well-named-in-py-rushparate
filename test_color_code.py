from color_code_utils import get_color_from_pair_number, get_pair_number_from_color
from color_code_report import generate_reference_manual, generate_csv_report

def test_number_to_pair(pair_number, expected_major, expected_minor):
    major, minor = get_color_from_pair_number(pair_number)
    assert major == expected_major, f"{major} != {expected_major}"
    assert minor == expected_minor, f"{minor} != {expected_minor}"

def test_pair_to_number(major, minor, expected_number):
    number = get_pair_number_from_color(major, minor)
    assert number == expected_number, f"{number} != {expected_number}"

def test_reference_manual():
    manual = generate_reference_manual()
    assert " 1: White  Blue" in manual
    assert "25: Violet Slate" in manual

def test_csv_report():
    csv = generate_csv_report()
    assert "1,White,Blue" in csv
    assert "25,Violet,Slate" in csv

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    test_pair_to_number('Red', 'Orange', 7)
    test_reference_manual()
    test_csv_report()
    print("All tests passed.")
