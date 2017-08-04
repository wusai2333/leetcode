public class Solution {
    public int shortestDistance(String[] words, String word1, String word2) {
        if (words == null) return -1;
        int p1 = -1, p2 = -1, min = Integer.MAX_VALUE;//words.length();
        
        for (int i = 0; i < words.length; i++) {

            if (words[i].equals(word1)) {
                p1 = i;
            }else if(words[i].equals(word2)) {
                p2 = i;
            }
            if (p2 != -1 && p1 != -1) {
                min = Math.min(min, Math.abs(p1 - p2));
            }
        }
        return min;
    }
}