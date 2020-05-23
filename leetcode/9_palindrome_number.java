class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0)
            return false;

        int rev = 0, remainder;
        int len = Integer.toString(x).length();
        for (int i = 0; i < len / 2; i++) {
            remainder = x % 10;
            rev = rev * 10 + remainder;
            x /= 10;
        }
        // If x is odd
        if (len == 1) {
            return true;
        } else if (len % 2 == 1) {
            x /= 10;
            return x == rev;
        } else {
            return x == rev;
        }
    }
}