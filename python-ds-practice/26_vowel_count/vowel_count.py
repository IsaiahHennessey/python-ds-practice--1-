def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive, in the order of their first appearance.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!')
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = 'aeiou'
    count = {}
    order = []

    # Convert phrase to lowercase to ensure case insensitivity
    phrase = phrase.lower()

    # Count occurrences of each vowel and track order of first appearance
    for char in phrase:
        if char in vowels:
            if char not in count:
                count[char] = 0
                order.append(char)
            count[char] += 1

    # Create the result dictionary in the order of first appearance
    result = {v: count[v] for v in order}

    return result
