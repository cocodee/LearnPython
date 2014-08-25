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
    def pathSum(self, root, sum):
        result = []
        work = []
        work.append([root,0,[]])
        while len(work)>0:
            a = work[0]
            work.pop(0)
            node = a[0]
            presum = a[1]
            if node ==None:
                return result
            elif node.left == None and node.right == None:
                if presum + node.val ==sum:
                    trace = list(a[2])
                    trace.append(node.val)
                    result.append(trace)
            else:
                if node.left != None:
                    trace = list(a[2])
                    trace.append(node.val)
                    work.append([node.left,node.val+presum,trace])
                if node.right != None:
                    trace = list(a[2])
                    trace.append(node.val)
                    work.append([node.right,node.val+presum,trace])
        return result        
    def atoi(self, str):
        if str == None:
            return 0
        phase = 0
        sum = 0
        sign = '+'
        for chr in str:
            if phase ==0:
                if chr ==' ':
                    continue
                elif chr =='+':
                    sign = '+'
                    phase = 1
                elif chr == '-':
                    sign = '-'
                    phase =1
                elif chr >='0' and chr <='9':
                    num = int(chr)
                    sum = sum*10+num
                    phase =1
                else:
                    return 0
            elif phase ==1:
                if chr >='0' and chr <='9': 
                    if sum>2147483647//10 or ((sum ==(2147483647//10)) and int(chr)>7):
                        if sign == '+':
                            return 2147483647
                        else:
                            return -2147483648                    
                    num = int(chr)
                    sum = sum*10+num
                else:
                    phase = 2                 
            else:
                continue
        if sign == '-':
            sum=-sum
        return sum

    def maxPathSum(self, root):
        if root == None:
            return 0
        maxSum = [root.val]
        self.recNodes(root,maxSum)
        return maxSum[0]
    def recNodes(self,node,maxSum):
        numl = 0
        numr = 0
        if node.left != None:
            numl = self.recNodes(node.left,maxSum)
        if node.right != None:
            numr = self.recNodes(node.right,maxSum)
        value = node.val
        sumWhole  = self.checkMax(value,numl+numr,maxSum)
        if numl>0:
            sumLeft = self.checkMax(value,numl,maxSum)
        else:
            sumLeft = value
        if numr>0:
            sumRight = self.checkMax(value,numr,maxSum)
        else:
            sumRight = value
        return max([sumLeft,sumRight])
    def checkMax(self,value,sum,maxSum):
        if sum>0:
            sum =sum+value
        else:
            sum =value
        if(sum>maxSum[0]):
            maxSum[0]=sum
        return sum
    def preorderTraversal(self, root):
        result = []
        self.subPreorder(root,result)
        return result
    def subPreorder(self,node,result):
        if node == None:
            return
        result.append(node.val)
        self.subPreorder(node.left,result)
        self.subPreorder(node.right,result)
    def postorderTraversal(self, root):
        result = []
        self.subPostorder(root,result)
        return result
    def subPostorder(self,node,result):
        if node == None:
            return
        self.subPostorder(node.left,result)
        self.subPostorder(node.right,result) 
        result.append(node.val)   
    def buildTree1(self,str):
        return self.subBuildTree(str,1)
    def subBuildTree(self,str,start):
        if start>len(str):
            return None
        else:
            if str[start-1] == '#':
                return None
            else:
                node = TreeNode(int(str[start-1]))
                node.left = self.subBuildTree(str,start*2)
                node.right = self.subBuildTree(str,start*2+1)
                return node
        return None
    def buildTree(self, inorder, postorder):
        return self.buildTreeSub(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1)
    def buildTreeSub(self, inorder, isi,ie,postorder,ps,pe):
        if isi>ie or ps>pe:
            return None
        rootval = postorder[pe]
        root = TreeNode(rootval)
        mid = isi
        for i in range(isi,ie+1):
            if inorder[i] == rootval:
                mid = i 
        leftnum = mid -isi
        root.left = self.buildTreeSub(inorder,isi,mid-1,postorder,ps,ps+leftnum-1)
        root.right = self.buildTreeSub(inorder,mid+1,ie,postorder,ps+leftnum,pe-1)
        return root
    def buildTree2(self, preorder,inorder):
        return self.buildTreeSub2(inorder,0,len(inorder)-1,preorder,0,len(preorder)-1)
    def buildTreeSub2(self, inorder, isi,ie,preorder,ps,pe):
        if isi>ie or ps>pe:
            return None
        rootval = preorder[ps]
        root = TreeNode(rootval)
        mid = isi
        for i in range(isi,ie+1):
            if inorder[i] == rootval:
                mid = i 
        leftnum = mid -isi
        root.left = self.buildTreeSub2(inorder,isi,mid-1,preorder,ps+1,ps+leftnum)
        root.right = self.buildTreeSub2(inorder,mid+1,ie,preorder,ps+leftnum+1,pe)
        return root  
    def threeSum(self,num):
        result = []
        num.sort()
        length = len(num)
        for i in range(0,length):
            if i!= 0 and num[i]==num[i-1]:
                continue
            start = i+1
            end = length -1
            while start<end:
                sum = num[i]+num[start]+num[end]
                if sum>0:
                    end=end-1
                elif sum<0:
                    start=start+1
                elif start != i+1 and num[start]==num[start-1]:
                    start=start+1
                elif end !=length-1 and num[end]==num[end+1]:
                    end = end -1
                else:
                    result.append([num[i],num[start],num[end]])
                    start = start+1
                    end = end-1
        return result 
    def threeSumClosest(self,num,target):
        result = None
        diff = None
        value = None
        num.sort()
        length = len(num)
        for i in range(0,length):
            if i!= 0 and num[i]==num[i-1]:
                continue
            start = i+1
            end = length -1
            while start<end:
                sum = num[i]+num[start]+num[end]
                if sum>target:
                    d = sum - target
                    if diff == None or d<diff:
                        value =sum
                        diff = d
                        result = [num[i],num[start],num[end]]
                    end=end-1
                elif sum<target:
                    d = target-sum
                    if diff == None or d<diff:
                        value =sum
                        diff = d
                        result = [num[i],num[start],num[end]]                   
                    start=start+1
                elif start != i+1 and num[start]==num[start-1]:
                    start=start+1
                elif end !=length-1 and num[end]==num[end+1]:
                    end = end -1
                else:
                    value =target
                    diff = 0
                    result = [num[i],num[start],num[end]]                    
                    start = start+1
                    end = end-1
        return value         
    def fourSum(self, num, target):
        result = []
        num.sort()
        length = len(num)  
        for i in range(0,length-3):
            if i>0 and num[i]==num[i-1]:
                continue
            for j in range(i+1,length-2):
                if j>i+1 and num[j]==num[j-1]:
                    continue
                target2 = target-num[i]-num[j]
                start,end = j+1,length-1
                while start<end:
                    sum = num[start]+num[end]
                    if sum>target2:
                        end = end -1
                    elif sum<target2:
                        start=start+1
                    else:
                        result.append([num[i],num[j],num[start],num[end]])
                        k = start+1
                        while k<end and num[k]==num[start]:
                            k=k+1
                        start =k

                        k = end-1
                        while k> start and num[k]==num[end]:
                            k=k-1     
                        end =k 
        return result
    def findLadders(self, start, end, dict):
        curQueue = []
        nextQueue = []
        levelMap ={}
        curlevelMap={}
        found = False
        if start not in dict:
            dict.append(start)
        if end in dict:
            dict.remove(end)
        tmp = {}
        for i in dict:
            tmp[i]=None
        dict = tmp
        curQueue.append(end)
        while len(curQueue)>0:
            for item in curQueue:
                for i in range(len(item)):
                    originc = item[i]
                    foundCurCycle = False
                    for ci in range(ord('a'),ord('z')+1):
                        c = chr(ci)
                        if c!=originc:
                            newStr = item[:i]+c+item[i+1:]
                            if newStr in dict:
                                if newStr in curlevelMap:
                                    curlevelMap[newStr].append(item)
                                elif (newStr not in levelMap) and (newStr not in curlevelMap):
                                    curlevelMap[newStr] = []
                                    curlevelMap[newStr].append(item) 
                                    nextQueue.append(newStr)
                                    if newStr == start:
                                        found = True
                                        foundCurCycle = True
                                        break
                    if foundCurCycle:
                        break
            levelMap.update(curlevelMap)
            curlevelMap = {}     
            curQueue=nextQueue
            nextQueue=[]          
            if found:
                break
        result = []
        if found:
            self.buildLadders(start,end,start,levelMap,[start],result)
        return result
    def buildLadders(self,start,end,current,levelMap,li,result):
        if current == end:
            result.append(list(li))
        else:
            parent = levelMap[current]
            for item in parent:
                li.append(item)
                self.buildLadders(start,end,item,levelMap,li,result)
                li.remove(item)
    def ladderLength(self, start, end, dict):
        curQueue = []
        nextQueue = []
        levelMap ={}
        curlevelMap={}
        found = False
        if start not in dict:
            dict.append(start)
        if end in dict:
            dict.remove(end)
        tmp = {}
        for i in dict:
            tmp[i]=None
        dict = tmp
        level = 1
        curQueue.append(end)
        while len(curQueue)>0:
            level = level+1
            for item in curQueue:
                for i in range(len(item)):
                    originc = item[i]
                    foundCurCycle = False
                    for ci in range(ord('a'),ord('z')+1):
                        c = chr(ci)
                        if c!=originc:
                            newStr = item[:i]+c+item[i+1:]
                            if newStr in dict:
                                if newStr in curlevelMap:
                                    curlevelMap[newStr].append(item)
                                elif (newStr not in levelMap) and (newStr not in curlevelMap):
                                    curlevelMap[newStr] = []
                                    curlevelMap[newStr].append(item) 
                                    nextQueue.append(newStr)
                                    if newStr == start:
                                        found = True
                                        foundCurCycle = True
                                        break
                    if foundCurCycle:
                        break
                if found:
                    break
            levelMap.update(curlevelMap)
            curlevelMap = {}     
            curQueue=nextQueue
            nextQueue=[]          
            if found:
                break
        if found:
            return level
        else:
            return 0   
    def nextPermutation(self, num):
        found = False
        for i in reversed(range(len(num)-1)):
            j=i+1
            while j<len(num) and num[i]<num[j]:
                j=j+1
            j = j-1
            if num[i]<num[j]:
                num[i],num[j]=num[j],num[i]
                tmp = list(num[i+1:])
                tmp.sort()
                for k in range(i+1,len(num)):
                    num[k]=tmp[k-i-1]
                found = True
                break;
        if not found:
            num.reverse()
            return num
        else: 
            return num
    def permute2(self, num):
        result = []
        self.subpermute2(num,0,result)
        return result
    def subpermute2(self,num,n,result):
        if n == len(num) -1:
            result.append(list(num))
            return;
        else:
            hash = {num[n]:None}
            self.subpermute2(num,n+1,result)
            for i in range(n+1,len(num)):
                if num[i] in hash:
                    continue
                hash[num[i]] = None
                num[n],num[i] = num[i], num[n]
                self.subpermute2(num,n+1,result)
                num[n],num[i] = num[i], num[n]
    def numDecodings(self, s):
        if len(s)==0:
            return 0
        ways ={}
        if s[0]!= '0':
            ways[0] = 1
        else:
            return 0
        if len(s) == 1:
            return 1
        if int(s[0:2])<=26 and s[0] !='0':
            if s[1]=='0':
                ways[1] = 1
            else:
                ways[1] = 2
        else:
            if s[1]=='0':
                ways[1] = 0
            else:
                ways[1] = 1
        for i in range(2,len(s)):
            if int(s[i-1:i+1])<=26 and s[i-1] !='0':
                if s[i]=='0':
                    ways[i] = ways[i-2]
                else:
                    ways[i] = ways[i-1]+ways[i-2]
            else:
                if s[i]=='0':
                    ways[i] = 0
                else:
                    ways[i] = ways[i-1]
        return ways[len(s)-1]            
    def isMatch(self, s, p):
        lens = len(s)
        lenp = len(p)
        i=0
        cnt =0
        while i<lenp and p[i]!='*':
            cnt=cnt+1
            i=i+1
        if cnt>lens:
            return False
        dp = [[False for x in range(lenp+1)] for y in range(lens+1) ]
        dp[0][0] = True
        for i in range(1,lenp+1):
            if dp[0][i-1] and p[i-1]=='*':
                dp[0][i]=True
            for j in range(1,lens+1):
                if p[i-1]=='*':
                    dp[j][i]=dp[j-1][i] or dp[j][i-1]
                elif p[i-1]=='?' or p[i-1]==s[j-1]:
                    dp[j][i]=dp[j-1][i-1]
                else:
                    dp[j][i]=False
        return dp[lens][lenp]
    def isMatch1(self, s, p):
        lens = len(s)
        lenp = len(p)
        star = -1
        match = 0
        trs = 0
        trp = 0
        while trs<lens:
            if trp<lenp and (s[trs]==p[trp] or p[trp]=='?'):
                trs =trs+1
                trp = trp+1
            elif trp<lenp and p[trp]=='*':
                match = trs
                star =trp
                trp =trp+1
            elif star !=-1:
                trp = star+1
                match = match+1
                trs = match
            else:
                return False
        while trp<lenp and p[trp]=='*':
            trp = trp+1
        if trp == lenp:
            return True
        else:
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
print s.pathSum(r,-5)
print s.pathSum(r,-2)
print s.preorderTraversal(r)
print s.postorderTraversal(r)
rc = TreeNode(11)
r = TreeNode(7)
l = TreeNode(2)
rc.left = l
rc.right =r
l = rc
rc = TreeNode(4)
rc.left = l
l = rc
rc = TreeNode(5)
rc.left = l
print s.pathSum(rc,22)
print s.maxPathSum(rc)
print s.preorderTraversal(rc)
print s.postorderTraversal(rc)
print None != None
print None == None
print s.atoi('-2157483646-ee56')
print s.atoi('2147483648')
print s.atoi('-1010023630o4')
print s.atoi('1234567890123456789012345678901234567890')

tree = s.buildTree1('1#3##5#')
print s.preorderTraversal(tree)

inorder = [4,2,5,1,3]
postorder = [4,5,2,3,1]
preorder = [1,2,4,5,3]
root = s.buildTree(inorder,postorder)
print s.preorderTraversal(root)
root  = s.buildTree2(preorder,inorder)
print s.preorderTraversal(root)
print s.threeSum([-1,0,1,2,-1,-4])
print s.fourSum([91277418,66271374,38763793,4092006,11415077,60468277,1122637,72398035,-62267800,22082642,60359529,-16540633,92671879,-64462734,-55855043,-40899846,88007957,-57387813,-49552230,-96789394,18318594,-3246760,-44346548,-21370279,42493875,25185969,83216261,-70078020,-53687927,-76072023,-65863359,-61708176,-29175835,85675811,-80575807,-92211746,44755622,-23368379,23619674,-749263,-40707953,-68966953,72694581,-52328726,-78618474,40958224,-2921736,-55902268,-74278762,63342010,29076029,58781716,56045007,-67966567,-79405127,-45778231,-47167435,1586413,-58822903,-51277270,87348634,-86955956,-47418266,74884315,-36952674,-29067969,-98812826,-44893101,-22516153,-34522513,34091871,-79583480,47562301,6154068,87601405,-48859327,-2183204,17736781,31189878,-23814871,-35880166,39204002,93248899,-42067196,-49473145,-75235452,-61923200,64824322,-88505198,20903451,-80926102,56089387,-58094433,37743524,-71480010,-14975982,19473982,47085913,-90793462,-33520678,70775566,-76347995,-16091435,94700640,17183454,85735982,90399615,-86251609,-68167910,-95327478,90586275,-99524469,16999817,27815883,-88279865,53092631,75125438,44270568,-23129316,-846252,-59608044,90938699,80923976,3534451,6218186,41256179,-9165388,-11897463,92423776,-38991231,-6082654,92275443,74040861,77457712,-80549965,-42515693,69918944,-95198414,15677446,-52451179,-50111167,-23732840,39520751,-90474508,-27860023,65164540,26582346,-20183515,99018741,-2826130,-28461563,-24759460,-83828963,-1739800,71207113,26434787,52931083,-33111208,38314304,-29429107,-5567826,-5149750,9582750,85289753,75490866,-93202942,-85974081,7365682,-42953023,21825824,68329208,-87994788,3460985,18744871,-49724457,-12982362,-47800372,39958829,-95981751,-71017359,-18397211,27941418,-34699076,74174334,96928957,44328607,49293516,-39034828,5945763,-47046163,10986423,63478877,30677010,-21202664,-86235407,3164123,8956697,-9003909,-18929014,-73824245], -236727523)
print s.threeSumClosest([-1,2,1,-4],1)
print s.findLadders('hit','cog',['hot','dot','dog','lot','log'])
print s.findLadders("nape", "mild", ["dose","ends","dine","jars","prow","soap","guns","hops","cray","hove","ella","hour","lens","jive","wiry","earl","mara","part","flue","putt","rory","bull","york","ruts","lily","vamp","bask","peer","boat","dens","lyre","jets","wide","rile","boos","down","path","onyx","mows","toke","soto","dork","nape","mans","loin","jots","male","sits","minn","sale","pets","hugo","woke","suds","rugs","vole","warp","mite","pews","lips","pals","nigh","sulk","vice","clod","iowa","gibe","shad","carl","huns","coot","sera","mils","rose","orly","ford","void","time","eloy","risk","veep","reps","dolt","hens","tray","melt","rung","rich","saga","lust","yews","rode","many","cods","rape","last","tile","nosy","take","nope","toni","bank","jock","jody","diss","nips","bake","lima","wore","kins","cult","hart","wuss","tale","sing","lake","bogy","wigs","kari","magi","bass","pent","tost","fops","bags","duns","will","tart","drug","gale","mold","disk","spay","hows","naps","puss","gina","kara","zorn","boll","cams","boas","rave","sets","lego","hays","judy","chap","live","bahs","ohio","nibs","cuts","pups","data","kate","rump","hews","mary","stow","fang","bolt","rues","mesh","mice","rise","rant","dune","jell","laws","jove","bode","sung","nils","vila","mode","hued","cell","fies","swat","wags","nate","wist","honk","goth","told","oise","wail","tels","sore","hunk","mate","luke","tore","bond","bast","vows","ripe","fond","benz","firs","zeds","wary","baas","wins","pair","tags","cost","woes","buns","lend","bops","code","eddy","siva","oops","toed","bale","hutu","jolt","rife","darn","tape","bold","cope","cake","wisp","vats","wave","hems","bill","cord","pert","type","kroc","ucla","albs","yoko","silt","pock","drub","puny","fads","mull","pray","mole","talc","east","slay","jamb","mill","dung","jack","lynx","nome","leos","lade","sana","tike","cali","toge","pled","mile","mass","leon","sloe","lube","kans","cory","burs","race","toss","mild","tops","maze","city","sadr","bays","poet","volt","laze","gold","zuni","shea","gags","fist","ping","pope","cora","yaks","cosy","foci","plan","colo","hume","yowl","craw","pied","toga","lobs","love","lode","duds","bled","juts","gabs","fink","rock","pant","wipe","pele","suez","nina","ring","okra","warm","lyle","gape","bead","lead","jane","oink","ware","zibo","inns","mope","hang","made","fobs","gamy","fort","peak","gill","dino","dina","tier"])
print s.ladderLength('hit','cog',['hot','dot','dog','lot','log'])
print s.ladderLength("nape", "mild", ["dose","ends","dine","jars","prow","soap","guns","hops","cray","hove","ella","hour","lens","jive","wiry","earl","mara","part","flue","putt","rory","bull","york","ruts","lily","vamp","bask","peer","boat","dens","lyre","jets","wide","rile","boos","down","path","onyx","mows","toke","soto","dork","nape","mans","loin","jots","male","sits","minn","sale","pets","hugo","woke","suds","rugs","vole","warp","mite","pews","lips","pals","nigh","sulk","vice","clod","iowa","gibe","shad","carl","huns","coot","sera","mils","rose","orly","ford","void","time","eloy","risk","veep","reps","dolt","hens","tray","melt","rung","rich","saga","lust","yews","rode","many","cods","rape","last","tile","nosy","take","nope","toni","bank","jock","jody","diss","nips","bake","lima","wore","kins","cult","hart","wuss","tale","sing","lake","bogy","wigs","kari","magi","bass","pent","tost","fops","bags","duns","will","tart","drug","gale","mold","disk","spay","hows","naps","puss","gina","kara","zorn","boll","cams","boas","rave","sets","lego","hays","judy","chap","live","bahs","ohio","nibs","cuts","pups","data","kate","rump","hews","mary","stow","fang","bolt","rues","mesh","mice","rise","rant","dune","jell","laws","jove","bode","sung","nils","vila","mode","hued","cell","fies","swat","wags","nate","wist","honk","goth","told","oise","wail","tels","sore","hunk","mate","luke","tore","bond","bast","vows","ripe","fond","benz","firs","zeds","wary","baas","wins","pair","tags","cost","woes","buns","lend","bops","code","eddy","siva","oops","toed","bale","hutu","jolt","rife","darn","tape","bold","cope","cake","wisp","vats","wave","hems","bill","cord","pert","type","kroc","ucla","albs","yoko","silt","pock","drub","puny","fads","mull","pray","mole","talc","east","slay","jamb","mill","dung","jack","lynx","nome","leos","lade","sana","tike","cali","toge","pled","mile","mass","leon","sloe","lube","kans","cory","burs","race","toss","mild","tops","maze","city","sadr","bays","poet","volt","laze","gold","zuni","shea","gags","fist","ping","pope","cora","yaks","cosy","foci","plan","colo","hume","yowl","craw","pied","toga","lobs","love","lode","duds","bled","juts","gabs","fink","rock","pant","wipe","pele","suez","nina","ring","okra","warm","lyle","gape","bead","lead","jane","oink","ware","zibo","inns","mope","hang","made","fobs","gamy","fort","peak","gill","dino","dina","tier"])
print s.nextPermutation([1,2,3])
print s.nextPermutation([3,2,1])
print s.nextPermutation([1,1,5])
print s.nextPermutation([1,3,2])
print s.nextPermutation([1])

print s.permute2([1,1,2])

print s.numDecodings('12')
print s.numDecodings('126')
print s.numDecodings('106')
print s.numDecodings('1006')

print s.isMatch('acbacba','ac*a')
print s.isMatch1('acbacbac','ac*a')