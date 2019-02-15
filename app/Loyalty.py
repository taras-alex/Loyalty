def Loyalty(amount_of_shopping, amount_of_purchase):
    if amount_of_shopping > 150_000:
        gold = 100                                   # gold status 10% of purchase
        bonus = gold * (amount_of_purchase // 1000)
    if 15_001 <= amount_of_shopping <= 150_000:
        silver = 70                                  # silver status 7% of purchase
        bonus = silver * (amount_of_purchase // 1000)
    if amount_of_shopping < 15_000:
        blu = 50                                     # blu status 5% of purchase
        bonus = blu * (amount_of_purchase // 1000)

    return bonus
