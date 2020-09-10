def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    num_letters = 0
    for char in dna:
            if char in 'atcgATCG':
                    num_letters = num_letters + 1
    return num_letters


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    num_dna1 = 0
    num_dna2 = 0
    for char in dna1:
            if char in 'atcgATCG':
                    num_dna1 = num_dna1 + 1

    for char in dna2:
            if char in 'atcgATCG':
                    num_dna2 = num_dna2 + 1

    return num_dna1 > num_dna2


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    num_dna = 0
    for char in dna:
            if char in nucleotide:
                    num_dna = num_dna + 1
    return num_dna


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    return dna2 in dna1


def is_valid_sequence (dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than 'A',
    'T', 'C', 'G').

    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ABCTG')
    False
    >>> is_valid_sequence('BUGTERMITES')
    False
    """

    invalid_sequence = 0
    for char in dna:
        if char in 'abcdefghijklmnopqrstuvwxyzBDEFHIJKLMNOPQRSUVWXYZ':
            invalid_sequence = invalid_sequence + 1
    return invalid_sequence <= 0 


def insert_sequence (dna1, dna2, num):
    """ (str, str, int) -> str
    Return the DNA sequence obtained by inserting the second
    DNA sequence into the first DNA sequence at the given index.

    >>> insert_sequence ('CCGG', 'AT', 2)
    CCATGG
    >>> insert_sequence ('ATCGAA', 'CCGG', 1)
    ACCGGTCGAA
    """

    return dna1[:num] + dna2 + dna1[num:] 


def get_complement (nucleotide):
    """(str) -> str
    Return the nucleotide's complement.

    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    >>> get_complement('T')
    A
    >>> get_complement('C')
    G
    """

    for char in nucleotide:
        if char in 'A':
            return 'T'
        elif char in 'C':
            return 'G'
        elif char in 'T':
            return 'A'
        elif char in 'G':
            return 'C'

def get_complementary_sequence (dna):
    """(str) -> str
    Return the DNA sequence that is complementary
    to the given DNA sequence.

    >>> get_complementary_sequence ('AT')
    TA
    """

    sequence = ''
    for char in dna:
        if char in 'A':
            sequence = sequence + 'T'
        elif char in 'C':
            sequence = sequence + 'G'
        elif char in 'T':
            sequence = sequence + 'A'
        elif char in 'G':
            sequence = sequence + 'C'
    return sequence
    
