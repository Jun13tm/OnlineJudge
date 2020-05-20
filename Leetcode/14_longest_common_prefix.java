class Solution {
    /* Horizontal */
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0)
            return "";

        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            // indexOf() returns -1 if non-existent, other than 0 if not prefix
            while (strs[i].indexOf(prefix) != 0) {
                prefix = prefix.substring(0, prefix.length() - 1);
                // If no more prefix left, no common prefix
                if (prefix.isEmpty())
                    return "";
            }
        }
        return prefix;
    }

    /*
     * Vertical: for each char in str[0], compare all strings in the array public
     * String longestCommonPrefix(String[] strs) { if (strs.length == 0) return "";
     * 
     * for (int i = 0; i < strs[0].length(); i++) { char c = strs[0].charAt(i); for
     * (int j = 1; j < strs.length; j++) { if (i == strs[j].length() ||
     * strs[j].charAt(i) != c) { // substring() - [begin, end) return
     * strs[0].substring(0, i); } } } return strs[0]; }
     */
}