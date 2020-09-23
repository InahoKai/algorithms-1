def reverseInts(num):
    look, at = divmod(num, 10)
    me, go = divmod(look, 10)
    return at*10**2 + go*10*1 + me*10**0


print(reverseInts(543))
