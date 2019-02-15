def Loyalty(amount_of_shopping, amount_of_purchase):
    if amount_of_shopping > 150_000:
        bonus = 100 * (amount_of_purchase // 1000)  # gold status
    if 15_001 <= amount_of_shopping <= 150_000:
        bonus = 70 * (amount_of_purchase // 1000)  # silver status
    if amount_of_shopping < 15_000:
        bonus = 50 * (amount_of_purchase // 1000)  # blu status

    return bonus