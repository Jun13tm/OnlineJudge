def isPalindrome(self, x: int) -> bool:
    # Two edge cases: x < 0 and x ends with 0
    if x< 0:
        return False
    if x % 10 == 0 and x != 0:
        return False
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x = int(x / 10)
    return x == reverted or x == int(reverted/10)