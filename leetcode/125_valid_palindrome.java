class Solution {
    public boolean isPalindrome(String s) {
        if (s == null) return false;
        
        s = s.toLowerCase();
        
        int i = 0, j = s.length() - 1;
        
        while (i < j) {
            while (i < s.length() && !Character.isLetterOrDigit(s.charAt(i))) 
                i++;
            while (j >= 0 && !Character.isLetterOrDigit(s.charAt(j)))
                j--;
            
            if (i < j && s.charAt(i++) != s.charAt(j--)) 
                return false;
        } 
        return true;
    }
}