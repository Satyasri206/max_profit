def max_profit(n, memo={}):
    # Memoization: store answers to avoid recalculation
    if n in memo:
        return memo[n]

    # If not enough time to build anything → profit 0
    if n < 4:
        return (0, {"T": 0, "P": 0, "C": 0})

    best_profit = 0
    best_choice = {"T": 0, "P": 0, "C": 0}

    # Option 1: Build Theatre (takes 5 time units)
    if n >= 5:
        profit_after, choice_after = max_profit(n - 5, memo)
        profit = 1500 * (n - 5) + profit_after
        if profit > best_profit:
            best_profit = profit
            best_choice = choice_after.copy()
            best_choice["T"] += 1

    # Option 2: Build Pub (takes 4 time units)
    if n >= 4:
        profit_after, choice_after = max_profit(n - 4, memo)
        profit = 1000 * (n - 4) + profit_after
        if profit > best_profit:
            best_profit = profit
            best_choice = choice_after.copy()
            best_choice["P"] += 1

    # Option 3: Build Commercial Park (takes 10 time units)
    if n >= 10:
        profit_after, choice_after = max_profit(n - 10, memo)
        profit = 3000 * (n - 10) + profit_after
        if profit > best_profit:
            best_profit = profit
            best_choice = choice_after.copy()
            best_choice["C"] += 1

    memo[n] = (best_profit, best_choice)
    return memo[n]

#  Test with examples from the PDF
for t in [7, 8, 13]:
    profit, choice = max_profit(t, {})
    print(f"Time = {t}, Profit = ${profit}, Choice = {choice}")
