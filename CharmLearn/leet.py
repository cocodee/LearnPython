__author__ = 'kdi'
class Solution:
    def isMatch(self,s,p):
        lens = len(s)
        lenp = len(p)
        dp = [[False for i in range(lenp+1)] for j in range(lens+1)]
        dp[0][0]=True
        for  i in range(1,lenp+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i] = dp[0][i-2]
        for i in range(1,lens+1):
            for j in range (1,lenp+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    #a a*||a ab*||abb ab*
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[lens][lenp]
s=Solution()
print s.isMatch('aa','a*')
