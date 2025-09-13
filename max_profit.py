def max_profit(n):
    builds = [('T', 5, 1500), ('P', 4, 1000), ('C', 10, 3000)]

    best_profit = [0] * (n + 1)
    best_seq = [set() for _ in range(n + 1)]
    for i in range(n + 1):
        best_seq[i].add(tuple())

    for time in range(1, n + 1):
        for name, b, rate in builds:
            if time >= b:
                extra = rate * max(0, time - b)
                profit = extra + best_profit[time - b]
                if profit > best_profit[time]:
                    best_profit[time] = profit
                    best_seq[time].clear()
                if profit == best_profit[time]:
                    for seq in best_seq[time - b]:
                        new_seq = (name,) + seq
                        best_seq[time].add(new_seq)

    final_counts = set()
    for seq in best_seq[n]:
        times = []
        time_used = 0
        for ch in seq:
            if ch == 'T':
                time_used += 5
            elif ch == 'P':
                time_used += 4
            else:
                time_used += 10
            times.append(time_used)
        while times and times[-1] == n:
            times.pop()
            seq = seq[:-1]
        time_used = 0
        earnings = 0
        for ch in seq:
            if ch == 'T':
                time_used += 5
                earnings += max(0, n - time_used) * 1500
            elif ch == 'P':
                time_used += 4
                earnings += max(0, n - time_used) * 1000
            else:
                time_used += 10
                earnings += max(0, n - time_used) * 3000
        if earnings == best_profit[n]:
            t = seq.count('T')
            p = seq.count('P')
            c = seq.count('C')
            final_counts.add((t, p, c))

    return best_profit[n], final_counts


if __name__ == "__main__":
    try:
        n = int(input("Enter total units of time: ").strip())
        if n < 0:
            print("Time must be non-negative")
            raise SystemExit
    except:
        print("Invalid input")
        raise SystemExit

    profit, choices = max_profit(n)
    print(f"\nmaxEarnings: {profit}")
    if not choices:
        print("No valid builds possible.")
    else:
        print(f"{len(choices)} possibilities:")
        for t, p, c in sorted(list(choices), key=lambda x: (-x[0], x[1], x[2])):
            print(f"T: {t}, P: {p}, C: {c}")
