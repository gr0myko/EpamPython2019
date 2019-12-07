def pythagorean_triplet_product(triplet_sum: int):
    result = [a * b * c for a in range(1, int(triplet_sum / 3) + 1) for b in range(a + 1, int(triplet_sum / 2) + 1) for
              c in range(b + 1, ((triplet_sum + 1) - a - b)) if a + b + c == triplet_sum and a ** 2 + b ** 2 == c ** 2]
    return result[0]


print(pythagorean_triplet_product(1000))
