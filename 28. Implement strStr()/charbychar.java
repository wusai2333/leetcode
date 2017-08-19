class Solution {
    public int strStr(String haystack, String needle) {
        int m = haystack.length(), n = needle.length();
        for (int i = 0; i < m ;i++) {
            for (int j = 0; j < n; j++) {
                if (j == needle.length()) return i;
                if (i + j == haystack.length()) return -1;
                if (needle.charAt(j) != haystack.charAt(i+j)) break;
            }
        }
        return -1;
    }
}