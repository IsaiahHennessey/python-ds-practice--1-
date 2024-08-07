def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    translation_table = str.maketrans(
        to_swap.lower() + to_swap.upper(),
        to_swap.upper() + to_swap.lower()
    )

    return phrase.translate(translation_table)