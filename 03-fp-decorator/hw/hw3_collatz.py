def collatz_steps(n):
    if n <= 0:
        raise ValueError("Positive, non-zero integers required!")

    def steps_inner(num, count):
        if num == 1:
            return count
        elif num % 2 == 0:
            return steps_inner(num // 2, count + 1)
        else:
            return steps_inner(3 * num + 1, count + 1)

    return steps_inner(n, 0)


assert collatz_steps(16) == 4
assert collatz_steps(12) == 9
assert collatz_steps(1000000) == 152
