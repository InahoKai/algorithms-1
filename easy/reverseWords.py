def reverseWords(s: str) -> str:
    # Cool but slower for some reason
    return ' '.join(word[::-1] for word in s.split(' '))
    # Not cool but faster
    new = []
    words_list = s.split(' ')
    for word in words_list:
        new.append(word[::-1])
    return ' '.join(new)


print(reverseWords("Let's take LeetCode contest"))
