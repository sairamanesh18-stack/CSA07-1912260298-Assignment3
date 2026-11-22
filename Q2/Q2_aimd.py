"""AIMD fairness: two TCP-like flows share a link of 40 packets per round trip."""
CAPACITY = 40

def run(x1, x2, rounds):
    history = [(x1, x2)]
    for _ in range(rounds):
        # TODO 1: If x1 + x2 is more than CAPACITY (congestion), halve both windows
        # (multiplicative decrease); otherwise add 1 to both (additive increase)
        if x1 + x2 > CAPACITY:
            x1 /= 2
            x2 /= 2
        else:
            x1 += 1
            x2 += 1
        history.append((x1, x2))
    return history

h = run(4, 30, 80)
for r in (0, 1, 5, 10, 20, 40, 60, 80):
    x1, x2 = h[r]
    print(f"round {r:2d}: flow 1 {x1:5.1f}  flow 2 {x2:5.1f}  gap {abs(x1 - x2):5.1f}")
