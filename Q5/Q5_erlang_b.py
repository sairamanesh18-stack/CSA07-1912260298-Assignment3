"""Erlang B: the probability that a call finds every trunk line busy."""

def erlang_b(traffic, lines):
    # TODO 1: Start with b = 1.0 (zero lines). For n = 1 .. lines apply b = traffic * b
    # / (n + traffic * b). Return b
    b = 1.0
    for n in range(1, lines + 1):
        b = traffic * b / (n + traffic * b)
    return b

A = 120 * 3 / 60        # 120 calls per hour, 3 minutes each, in Erlangs
print(f"offered load {A:.1f} Erlangs")
for n in (6, 8, 10, 12):
    print(f"{n:2d} lines: blocking {erlang_b(A, n):6.2%}")
need = next(n for n in range(1, 100) if erlang_b(A, n) <= 0.01)
print(f"lines needed for blocking of 1% or less: {need}")
