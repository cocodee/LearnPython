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
    #Edit distance
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            return self.minDistance(word2,word1)
        if len(word2) == 0:
            return len(word1)
        previous_row = range(len(word2)+1)
        for i,c1 in enumerate(word1):
            current_row = [i+1]
            for j,c2 in enumerate(word2):
                insertions = previous_row[j+1]+1 #insertions of word2
                deletions = current_row[j]+1# deletions of 
                substitutions = previous_row[j] +(c1!=c2)
                current_row.append(min(insertions,deletions,substitutions))
            previous_row = current_row
        return previous_row[-1]    
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
    #Permutation
    def permute(self, num):
        result = []
        self.subpermute(num,0,result)
        return result
    def subpermute(self,num,n,result):
        if n == len(num) -1:
            result.append(list(num))
            return;
        else:
            for i in range(n,len(num)):
                num[n],num[i] = num[i], num[n]
                self.subpermute(num,n+1,result)
                num[n],num[i] = num[i], num[n]
    #Subsets
    def subsets(self,S):
        S.sort()
        result = self.subsetsUtil(S)
        result.append([])
        return result
    def subsetsUtil(self,S):
        if len(S)<=1:
            return list([S])
        else:
            result=[]
            sset = self.subsetsUtil(list(S[1:]))
            for item in sset:
                result.append(list(item))
            for item in sset:
                item.insert(0,S[0])
                result.append(list(item))
            result.append([S[0]])
            return result
    #addTwoNumbers
    def addTwoNumbers(self,l1,l2):
        n1 = self.getnum(l1)
        n2 = self.getnum(l2)
        n = n1+n2
        return self.getlist(n)
    def getnum(self,l):
        head = l
        n = 0
        mul = 1
        while head!=None:
            n = n+head.val*mul
            mul = mul*10
            head = head.next
        return n
    def getlist(self,n):
        num = n%10
        n = n//10
        node = ListNode(num)
        h = node
        t = node
        while n!=0:
            num = n%10
            n = n//10
            node = ListNode(num)
            t.next = node
            t = t.next
        return h
    #Word Break&Word break II
    def wordBreak(self, s, dict):
        if s is None or dict is None:
            return False
        if s in dict:
            return True
        starts=[0]
        for i in range(1,len(s)+1):
            for j in range(0,len(starts)):
                if s[starts[j]:i] in dict:
                    starts.insert(0,i)
                    break
        return starts[0]==len(s)              
    def wordBreak2(self,s,dict):
        startcache = {}
        if s is None or dict is None:
            return False
        if s in dict:
            startcache ={len(s):[0]}
            return [s]
        starts=[0]
        for i in range(1,len(s)+1):
            add = 0
            for j in range(0,len(starts)):
                if s[starts[j+add]:i] in dict:
                    if (startcache.get(i)!=None):
                        startcache.get(i).append(starts[j+add])
                    else:
                        startcache[i]=[starts[j+add]]
                        starts.insert(0,i)
                        add=add+1
        if starts[0] == len(s):
            return self.buildWord(s,startcache,starts)
        else:
            return []
    def wordBreak3(self,s,dict):
        startcache = {}
        if s is None or dict is None:
            return False
        if s in dict:
            startcache ={len(s):[0]}
            return [s]
        starts=[0]
        for i in range(1,len(s)+1):
            for j in range(0,len(starts)):
                if s[starts[j]:i] in dict:
                    if (startcache.get(i)!=None):
                        startcache.get(i).append(starts[j])
                    else:
                        startcache[i]=[starts[j]]
                        starts.append(i)
                        print starts
        if starts[len(starts)-1] == len(s):
            return self.buildWord(s,startcache,starts)
        else:
            return []            
    def buildWord(self,s,startcache,starts):
        result = []
        work = []
        work.append([len(s),''])
        while len(work)>0:
            a = work[0]
            work.pop(0)
            stops = startcache[a[0]]
            for stop in stops:
                if stop == 0:
                    sb = s[stop:a[0]]+a[1]
                    result.append(sb)
                else:
                    sb = ' '+s[stop:a[0]]+a[1]
                    work.append([stop,sb])
        return result
    def subsetsWithDup(self, S):
        S.sort()
        res = [[]]
        pre,count =None,1
        for e in S:
            if e!=pre:
                pre,count = e,len(res)
            for i in range(len(res)-count,len(res)):
                ss = res[i][:]
                ss.append(e)
                res.append(ss)
        return res
    def subsetsWithDup1(self, S):
        S.sort()
        res = [[]]
        pre, count = None, 0
        for e in S:
            if e != pre:
                pre,count = e,len(res)
            res = res + [l+[e] for l in res[len(res)-count:]]
        return res 
    def pow(self,x,n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n<0:
            x = 1/x
            n=-n
        if n == 1:
            return x
        m = n//2
        r = n%2
        sub = self.pow(x,m)
        if r == 0:
            return sub*sub
        else:
            return sub*sub*x
    def hasPathSum(self, root, sum):
        work = []
        work.append([root,0])
        while len(work)>0:
            a = work[0]
            work.pop(0)
            node = a[0]
            presum = a[1]
            if node ==None:
                return False
            elif node.left == None and node.right == None:
                if presum + node.val ==sum:
                    return True
            else:
                if node.left != None:
                    work.append([node.left,node.val+presum])
                if node.right != None:
                    work.append([node.right,node.val+presum])
        return False
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
s = Solution()
print s.singleNumber([1,6,4,5,1,4,3,6,5])
print s.twoSum([2,7,11,15],9)
print s.climbStairs(100)
print s.exist(['123','456','789s'],'125896')
print s.exist(['ab'],'ba')
print s.levenshtein('abcde','adcde')
print s.diff('This is the Index where the object obj need to be inserted.','This is the index where the object needed to be inserted.')
print s.minDistance('abcde','adcde')
print s.minDistance('','a')

print s.permute([1,2,3,4])
print s.permute([1])
print s.permute([5,8,1,6])

print list([3][1:])
print s.subsets([1,2,3,4])
print s.subsets([0])
print s.wordBreak3('catsanddog',['cat','cats','and','sand','dog'])

print s.wordBreak2('a',['a'])
print s.subsetsWithDup([1,2,2,2])
print s.subsetsWithDup1([1,2,2,2])
print s.pow(3,5)

rc = TreeNode(-3)
r = TreeNode(-2)
print r.val
r.right = rc
print s.hasPathSum(r,-2)
print None != None
print None == None
