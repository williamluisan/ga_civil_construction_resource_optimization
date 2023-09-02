def letter_to_array_index(column_letter):
    """
    to convert the corresponding letter to its order in the alphabet
    and deduct its index with 1 to set the index following array index
    """
    column_letter = column_letter.upper()  # Convert to uppercase for consistency
    base = ord('A') - 1  # 'A' is 1, 'B' is 2, and so on...
    index = 0

    for char in column_letter:
        index = index * 26 + (ord(char) - base)

    return index - 1

def format_string_float_two_decimal_points(value: float) -> str:
    return format(value, ".2f")