from color_code_utils import get_color_from_pair_number, get_pair_number_from_color
from color_code_constants import MAJOR_COLORS, MINOR_COLORS

def generate_reference_manual():
    lines = []
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major, minor = get_color_from_pair_number(pair_number)
        lines.append(f"{pair_number:2}: {major:6} {minor:6}")
    return "\n".join(lines)

def generate_csv_report():
    rows = ["PairNumber,MajorColor,MinorColor"]
    for pair_number in range(1, len(MAJOR_COLORS) * len(MINOR_COLORS) + 1):
        major, minor = get_color_from_pair_number(pair_number)
        rows.append(f"{pair_number},{major},{minor}")
    return "\n".join(rows)
