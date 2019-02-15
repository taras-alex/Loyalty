def Loyalty(amount_of_shopping, amount_of_purchase):
    if amount_of_shopping > 150_000:
        bonus = 100  # gold status 10% of purchase
    if 15_001 <= amount_of_shopping <= 150_000:
        bonus = 70  # silver status 7% of purchase
    if amount_of_shopping < 15_000:
        bonus = 50  # blu status 5% of purchase
    result = bonus * (amount_of_purchase // 1000)
    return result
