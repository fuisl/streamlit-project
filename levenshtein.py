"""
This module contains the implementation of the Levenshtein distance algorithm.
"""


def load_vocab(file_path):
    """
    Load a vocabulary from a file.

    Args:
        file_path: The path to the file containing the vocabulary.
    
    Returns:
        A sorted list of words in the vocabulary.
    """
    with open(file_path, "r") as file:
        data = file.readlines()

    # build the set of words
    vocab = set()
    for word in data:
        vocab.add(word.strip().lower())

    return sorted(vocab)


def levenshtein(s1, s2):
    """
    Calculate the Levenshtein distance between two strings.

    Args:
        s1: The first string.
        s2: The second string.

    Returns:
        The Levenshtein distance between the two strings.
    """
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def levenshtein_closest_word(word, vocab):
    """
    Find the closest word in the vocabulary to the given word.

    Args:
        word: The word to compare.
        vocab: The vocabulary of words to compare against.

    Returns:
        The closest word in the vocabulary to the given word.
    """
    closest_word = None
    closest_distance = float("inf")
    for vocab_word in vocab:
        distance = levenshtein(word, vocab_word)
        if distance < closest_distance:
            closest_word = vocab_word
            closest_distance = distance

    return closest_word


def levenshtein_all_vocab(word, vocab):
    """
    Find the levenshtein distance between the given word and all vocab words.

    Args:
        word: The word to compare.
        vocab: The vocabulary of words to compare against.

    Returns:
        A dictionary containing all vocab as keys and levenshtein distance as values.
        Sorted by distance.
    """

    distances = {}
    for vocab_word in vocab:
        distance = levenshtein(word, vocab_word)
        distances[vocab_word] = distance

    sorted_distances = dict(sorted(distances.items(), key=lambda item: item[1]))
    return sorted_distances


if __name__ == "__main__":
    vocab = load_vocab("data/vocab.txt")
    word = "bok"
    all_distances = levenshtein_all_vocab(word, vocab)
    closest_word = next(iter(all_distances))
    print(closest_word)
