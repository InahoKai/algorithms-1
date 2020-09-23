# Description: Given a two parameters of type integer 'N', 'D', return a string of the decimal representation where N is the numerator and D is the denominator. If the decimal has a repeating sequence of digits, indicate the sequence by enclosing it in brackets. Use xxx.0 to denote an integer.
import decimal


def frick_fractions(N, D):
    res = [str(N // D) + "."]
    subres = [N % D]
    N %= D
    while N != 0:
        N *= 10
        result_digit, N = divmod(N, D)
        res.append(str(result_digit))

        if N not in subres:
            subres.append(N)
        else:
            res.insert(subres.index(N) + 1, "(")
            res.append(")")
            break
    return "".join(res)


print(frick_fractions(500, 501))
print(frick_fractions(1, 3))
