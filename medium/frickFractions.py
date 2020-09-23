# Description: Given a two parameters of type integer 'N', 'D', return a string of the decimal representation where N is the numerator and D is the denominator. If the decimal has a repeating sequence of digits, indicate the sequence by enclosing it in brackets. Use xxx.0 to denote an integer.
import decimal


def frick_fractions(N, D):
    new = [f'{N // D}.']
    decimals = [N % D]
    N % D
    while N != 0:
        N *= 10
        result_digit, N = divmod(N, D)
        new.append(str(result_digit))
        if N not in decimals:
            decimals.append(N)
        else:
            new.insert(decimals.index(N) + 1, '(')
            new.append(')')
            break
    return ''.join(new)


print(frick_fractions(500, 501))
print(frick_fractions(1, 7))
