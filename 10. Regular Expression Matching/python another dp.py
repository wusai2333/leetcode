class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        f= [[False]*(n+1) for _ in range(m+1)]
        """
         * f[i][j]: if s[0..i-1] matches p[0..j-1]
         * if p[j - 1] != '*'
         *      f[i][j] = f[i - 1][j - 1] && s[i - 1] == p[j - 1]
         * if p[j - 1] == '*', denote p[j - 2] with x
         *      f[i][j] is true iff any of the following is true
         *      1) "x*" repeats 0 time and matches empty: f[i][j - 2]
         *      2) "x*" repeats >= 1 times and matches "x*x": s[i - 1] == x && f[i - 1][j]
         * '.' matches any single character
        """
        f[0][0] = True
        for i in range(1, m+1):
            f[i][0] = False
            # p[0.., j - 3, j - 2, j - 1] matches empty iff p[j - 1] is '*' and p[0..j - 3] matches empty
        for j in range(1, n+1):
            f[0][j] = j > 1 and p[j - 1] == '*' and f[0][j - 2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j - 1] != '*':
                    f[i][j] = f[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    # p[0] cannot be '*' so no need to check "j > 1" here
                    f[i][j] = f[i][j-2] or (s[i-1] == p[j-2] or p[j-2] == '.') and f[i-1][j]
                    
        return f[m][n]
                    