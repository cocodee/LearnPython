#lee


def compare(item1,item2):
    if item1[1]<item2[1]:
        return -1
    elif item1[1]>item2[1]:
        return 1
    else:
        return 0

class Solution:
    #Single Number
    # @param A, a list of integer
    # @return an integer
    def __init__(self):
        self.stairRem = dict()

    def singleNumber(self, A):
        num = A[0]
        for a in A[1:]:
            num = num^a
        return num
    #twoSum
    # @return a tuple, (index1, index2)
    def twoSum(self,num,target):
        i = 0
        numenum = enumerate(num)
        numenum = sorted(numenum,cmp=compare)
        j = len(num) - 1
        while i<j :
            sum = numenum[i][1]+numenum[j][1]
            if sum == target:
                result=[numenum[i][0]+1,numenum[j][0]+1]
                result.sort()
                return (result[0],result[1])
            elif sum < target:
                i=i+1
            else:
                j=j-1
    #Climbing Stairs
    #Fibonacci
    '''
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2: 
            return 2
        if self.stairRem.has_key(n):
            return self.stairRem.get(n)
        else:
            result = self.climbStairs(n-1)+self.climbStairs(n-2)  
            self.stairRem[n]=result
            return result 
    '''
    def climbStairs(self, n):
        if n==1:
            return 1
        if n==2: 
            return 2
        s1 = 1
        s2 = 2
        s3 = 0
        for i in range(3,n+1):
            s3 =s1+s2
            s1 = s2
            s2 = s3
        return s3
    #word search
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        mark = []
        for row in board:
            l = len(row)
            mark.append([0 for x in range(0,l)])
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if self.DFS(board,i,j,word,mark):
                    return True
        return False
    def DFS(self,board,i,j,word,mark):
        if word==None or len(word)==0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[i]):
            return False
        if board[i][j]!=word[0]:
            return False
        if mark[i][j] == 0:
            mark[i][j] = 1
            if len(word)>1:
                newword = word[1:]
            else:
                newword = []
            result = self.DFS(board,i+1,j,newword,mark) or self.DFS(board,i-1,j,newword,mark) or self.DFS(board,i,j+1,newword,mark) or self.DFS(board,i,j-1,newword,mark)
            mark[i][j]=0
            return result
        return False

    def levenshtein(self,s1,s2):
        if len(s1) < len(s2):
            return self.levenshtein(s2,s1)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2)+1)
        for i,c1 in enumerate(s1):
            current_row = [i+1]
            for j,c2 in enumerate(s2):
                insertions = previous_row[j+1]+1 #insertions of s2
                deletions = current_row[j]+1# deletions of s2
                substitutions = previous_row[j] +(c1!=c2)
                current_row.append(min(insertions,deletions,substitutions))
            previous_row = current_row
        return previous_row[-1]
    
    def diff(self,s1,s2):
        if len(s1) < len(s2):
            temp = s1
            s1 = s2
            s2 = temp
        mark = [['0' for y in range(len(s1)+1)] for x in range(len(s1)+1)]
        news1 = []
        news2 = []
        self.levenshtein1(s1,s2,mark,)
        #for i in range(len(mark)):
        #    print mark[i]
        i=len(s1)-1
        j=len(s2)-1
        while i>=0 and j>=0:
            #print mark[i][j]
            if mark[i][j] == '+':
                news1.insert(0,s1[i])
                news2.insert(0,' ')
                i = i-1
            elif mark[i][j] == '-':
                news1.insert(0,' ')
                news2.insert(0,s2[j])
                j = j-1                
            else:
                news1.insert(0,s1[i])
                news2.insert(0,s2[j])  
                i = i-1
                j = j-1                      
        print ''.join(news1)
        print ''.join(news2)
    def levenshtein1(self,s1,s2,mark):
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2)+1)
        for i,c1 in enumerate(s1):
            current_row = [i+1]
            for j,c2 in enumerate(s2):
                insertions = previous_row[j+1]+1 #insertions of s2
                deletions = current_row[j]+1# deletions of s2
                if c1 == c2:
                    substitutions = previous_row[j]
                    keep = True
                else:
                    substitutions = previous_row[j] +1
                    keep = False
                current_row.append(min(insertions,deletions,substitutions))
                minop = min(insertions,deletions,substitutions)
                if minop == insertions:
                    mark[i][j] = '+'
                elif minop == deletions:
                    mark[i][j] = '-'
                elif keep == True:
                    mark[i][j] = 'O'
                else:
                    mark[i][j] = 'X'              
            previous_row = current_row
        return previous_row[-1]
s = Solution()
print s.singleNumber([1,6,4,5,1,4,3,6,5])
print s.twoSum([2,7,11,15],9)
print s.climbStairs(100)
print s.exist(['123','456','789s'],'125896')
print s.exist(['ab'],'ba')
print s.levenshtein('abcde','adcde')
print s.diff('This is the Index where the object obj need to be inserted.','This is the index where the object needed to be inserted.')