class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m+1][n+1];
        int numZeroes = 0, numOnes = 0;
        for (String s : strs) {
            numZeroes = 0; numOnes = 0;
            for (char c: s.toCharArray()) {
                if (c == '0') {
                    numZeroes++;
                } else if (c == '1') {
                    numOnes++;
                }
            }

            for (int i = m; i >= numZeroes; i--) {
                for (int j = n; j >= numOnes; j--) {
                    dp[i][j] = Math.max(dp[i][j], dp[i - numZeroes][j - numOnes] + 1);
                    //System.out.println("dp["+i+"]["+j+"] = " + dp[i][j]);
                }
            }
            System.out.println();
        }
       return dp[m][n];
    }
}