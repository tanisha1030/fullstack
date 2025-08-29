def process_input(data):
    """
    Process the input array and return required information.
    """
    even_numbers = []
    odd_numbers = []
    alphabets = []
    special_chars = []
    numbers_sum = 0
    alpha_concat = ""

    for item in data:
        if isinstance(item, int):
            numbers_sum += item
            if item % 2 == 0:
                even_numbers.append(item)
            else:
                odd_numbers.append(item)
        elif isinstance(item, str):
            if item.isalpha():
                alphabets.append(item.upper())
                alpha_concat += item
            else:
                special_chars.append(item)

    # Reverse the concatenated alphabets
    alpha_concat_rev = alpha_concat[::-1]

    # Alternating caps
    alpha_concat_alt = ''.join(
        char.upper() if i % 2 == 0 else char.lower()
        for i, char in enumerate(alpha_concat_rev)
    )

    return {
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "alphabets": alphabets,
        "special_chars": special_chars,
        "sum_of_numbers": numbers_sum,
        "concat_alternating_caps": alpha_concat_alt
    }
