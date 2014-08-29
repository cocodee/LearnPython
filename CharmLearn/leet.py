__author__ = 'kdi'
class Solution:
    #Regular Expression Matching
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
    #Palindrome Partitioning
    def partition(self, s):
        result = []
        cur = []
        lens = len(s)
        mp = self.allpalindrome(s)
        self.parchild(s,0,mp,cur,result)
        return result
    def allpalindrome(self,s):
        lens = len(s)
        mp = [[False for x in range(0,lens)] for y in range(0,lens)]
        for i in range(0,lens):
            for j in range(0,i+1):
                if s[j]==s[i] and (i-j<2 or mp[j+1][i-1]):
                    mp[j][i]=True
                else:
                    mp[j][i]=False
        return mp
    def parchild(self,s,start,mp,cur,result):
        lens = len(s)
        if start==lens:
            result.append(list(cur))
        for i in range(start,lens):
            if mp[start][i]:
                cur.append(s[start:i+1])
                self.parchild(s,i+1,mp,cur,result)
                cur.pop()
    #Palindrome Partition II---TLE Time Limit Exceeded
    def minCut(self, s):
        lens=len(s)
        if lens == 0:
            return 0
        mp = self.allpalindrome(s)
        minc = [0 for x in range(len(s))]

        for i in range(0,lens):
            min = lens
            if mp[0][i]:
                minc[i] = 1
            else:
                for j in range(0,i):
                    if mp[j+1][i] and minc[j]+1<min:
                        min = minc[j]+1
                minc[i]=min
        return minc[lens-1]
    #Valid Palindrome
    def isPalindrome(self, s):
        lens = len(s)
        s=s.upper()
        i = 0
        j =lens-1
        while i<j:
            if not s[i].isalnum():
                i=i+1
            elif not s[j].isalnum():
                j=j-1
            else:
                if s[i]==s[j]:
                    i=i+1
                    j=j-1
                else:
                    return False
        return True
    #Palindrome number
    def isPalindromeN(self, x):
        if x<0:
            return False
        div =1
        while x//div >=10:
            div*=10
        while x>0:
            if x//div!=x%10:
                return False
            else:
                x=x%div//10
                div=div//100
        return True
s=Solution()
print s.isMatch('aa','a*')
print s.allpalindrome('aaba')
print s.partition('aaba')
print s.partition('aab')
print s.partition('aa')
print s.partition('a')
print s.minCut('aaba')
print s.minCut('aab')
print s.minCut('aa')
print s.minCut('a')
print s.minCut('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
print s.isPalindrome('A man, a plan, a canal: Panama')
print s.isPalindrome('race a car')
print s.isPalindrome('1a2')
print s.isPalindromeN(1231)