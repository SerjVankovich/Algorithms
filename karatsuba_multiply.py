def karatsuba_multiply(x, y):
    x_str_len = len(str(x))
    y_str_len = len(str(y))
    n = max(x_str_len, y_str_len)
    half_n = n // 2
    if n == 1:
        return x * y
    xl = x // (10 ** half_n)
    xr = x % (10 ** half_n)
    yl = y // (10 ** half_n)
    yr = y % (10 ** half_n)

    p1 = karatsuba_multiply(xl, yl)
    p2 = karatsuba_multiply(xr, yr)
    p3 = karatsuba_multiply((xl + xr), (yr + yl))

    return (p1 * (10 ** (2 * half_n))) + ((p3 - p2 - p1) * (10 ** half_n)) + p2


def karatsuba_multiply_binary(x, y):
    x_str_len = len(bin(x))
    y_str_len = len(bin(y))
    n = max(x_str_len, y_str_len) - 2
    half_n = n // 2
    if n == 1:
        return x * y
    mask = int('0b' + ('1' * half_n), base=2)
    xl = x >> half_n
    xr = x & mask
    yl = y >> half_n
    yr = y & mask

    p1 = karatsuba_multiply(xl, yl)
    p2 = karatsuba_multiply(xr, yr)
    p3 = karatsuba_multiply((xl + xr), (yr + yl))

    return (p1 << (2 * half_n)) + ((p3 - p2 - p1) << half_n) + p2


num1, num2 = map(int, input('Input 2 int numbers: ').split())
print(karatsuba_multiply(num1, num2))
print('Binary multiply:', karatsuba_multiply_binary(num1, num2))
