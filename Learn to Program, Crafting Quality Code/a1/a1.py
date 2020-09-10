def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(75)
    2
    """

    per_limit = 50
    i = 1
    if n == 0:
        return 0
    if i * per_limit < n:
        i = i + 1

    return i

def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    """

    sum_gain = 0.0
    sum_loss = -0.0
    i = 0

    for i in price_changes:
        if i >= 0.0:
            sum_gain = sum_gain + i
        else:
            sum_loss = sum_loss + i
    summary_tup = (sum_gain, sum_loss)
    return summary_tup



def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondtion: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums, 2)
    >>> nums
    [5, 6, 3, 4, 1, 2]
    """

    for i in range(k):
        temp = L[i]
        L[i] = L[len(L) - k + i]
        L[len(L) - k + i] = temp



if __name__ == '__main__':
    import doctest
    doctest.testmod()
