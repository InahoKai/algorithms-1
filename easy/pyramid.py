def wordPyramid(word, height):
    for i in range(height):
        print(f'{word} '*i)


wordPyramid('hello', 5)