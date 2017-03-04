# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    
        
                 
        
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
    
        self.b=[] 
        self.x=-1
        self.m=0
        #z=[]
        self.haha(nestedList)
        print(self.b)
        self.m=len(self.b)
        
    
    def haha(self,list):
        for i in range(len(list)):
            if(list[i].isInteger()):
                self.b.append(list[i].getInteger())
            else:
                 z=list[i].getList()
                 self.haha(z)               

    def next(self):
        """
        :rtype: int
        """
        self.x+=1
        return self.b[self.x]

    def hasNext(self):
        """
        :rtype: bool
        """
        self.m=len(self.b)
        if (self.x<self.m-1):
            return True 
        else :
            return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#这个程序直接运行会有错误
#Traceback (most recent call last):
# File "C:\Users\PKJ\Desktop\flaten.py", line 78, in <module>
#   i,v=NestedIterator(s),[]
# File "C:\Users\PKJ\Desktop\flaten.py", line 41, in __init__
#   self.haha(nestedList)
# File "C:\Users\PKJ\Desktop\flaten.py", line 48, in haha
#   if(list[i].isInteger()):
#AttributeError: 'list' object has no attribute 'isInteger'
#因为下面提供的S不是class NestedInteger(object)，详情请看上面class NestedInteger注释
#这个在OJ上能通过
s=[[1,1],2,[1,1],5,6,7,[6,34,56]]
i,v=NestedIterator(s),[]
while i.hasNext():  v.append(i.next())   
print(v)

    
