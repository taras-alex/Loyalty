def Loyalty(amount_of_shopping, amount_of_purchase):
    """
    >>> Loyalty(0,0)
    0

    >>> Loyalty(200_000,0)
    0

    >>> Loyalty(200_000,2300)
    200

    >>> Loyalty(140_000,0)
    0

    >>> Loyalty(140_000,56_500)
    3920

    >>> Loyalty(5000,0)
    0

    >>> Loyalty(12_000,7800)
    350

    """
    if amount_of_shopping > 150_000:
        bonus = 100  # gold status 10% of purchase

    if 15_001 <= amount_of_shopping <= 150_000:
        bonus = 70  # silver status 7% of purchase

    if amount_of_shopping < 15_000:
        bonus = 50  # blu status 5% of purchase

    result = bonus * (amount_of_purchase // 1000)
    return result
