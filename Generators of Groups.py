def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def is_primitive(g, p):
    p_minus_1 = p - 1
    divisors = get_divisors(p_minus_1)

    # Check if g^d != 1 mod p for all divisors d of p-1 except p-1 itself
    for d in divisors:
        if d == p - 1:
            continue
        if pow(g, d, p) == 1:
            return False
    return True


def find_primitive_element(p):
    for g in range(2, p):
        if is_primitive(g, p):
            return g


# Given value of p
p = 28151

# Find the smallest primitive element
g = find_primitive_element(p)
print(f"The smallest primitive element of F_{p} is: {g}")
