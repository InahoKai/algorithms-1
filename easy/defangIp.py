# Memory Usage: 13.6 MB, less than 95.90% of Python3 online submissions for Defanging an IP Address.
# Runtime: 32 ms, faster than 51.97% of Python3 online submissions for Defanging an IP Address.

def defangIPaddr(address: str) -> str:
    return address.replace('.', '[.]')


print(defangIPaddr('1.1.1.1'))
