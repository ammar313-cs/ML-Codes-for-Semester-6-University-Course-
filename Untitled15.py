#!/usr/bin/env python
# coding: utf-8

# In[12]:


import random as rand


list = []

for i in range(1300):
    list.append(rand.randint(0,7000))

    
list


# In[64]:


import random as rand
class Node:
    
    def __init__(self,key):
        
        self.right = None 
        self.left = None 
        self.val = key
        
    def insert(root,val):
        
        if root is None:
            
            return Node(key)
        else:
            if root.val == val:
                return root
            elif root.val < val:
                root.right = insert(root.right,val)
            else:
                root.left = insert(root.left,val)
        return root
    
    def ifNodeExists(node,key):
        if node == None:
            return False
        if (node.val == key):
            return True
        
        res1 = ifNodeExists(node.left,key)
        if res1:
            return True
        
        res2 = ifNodeExists(node.right,key)
        
        return res2
    


    
root = Node(rand.randint(0,7000))
        

for i in range (0,1000):
    x = rand.randint(0,7000)
    while(ifNodeExists(root,x)):
        x = rand.randint(0,7000)
    root.insert(x)
            
            
        
    


# In[52]:


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        
        print( self.data)
        
        if self.right:
            self.right.PrintTree()

def ifNodeExists(node, key):

    if (node == None):
        return False
    if (node.data == key):
        return True
    res1 = ifNodeExists(node.left, key)
    if res1:
        return True
    res2 = ifNodeExists(node.right, key)
 
    return res2

root = Node(random.randint(0, 7000))

for i in range(0, 1000):

    x = random.randint(0,7000)
    while (ifNodeExists(root, x)):
        x = random.randint(0,7000)
    
    root.insert(x)

''''root.PrintTree()'''
 
def bfs(root: Node):
    if root is None:
        return
    queue = [root]
    
    while len(queue) > 0:
        cur_node = queue.pop(0)
        
        for i in queue:
            print(i.data, end=" ")
        print()
        
        if cur_node.left is not None:
            queue.append(cur_node.left)

        if cur_node.right is not None:
            queue.append(cur_node.right)

bfs(root)


# In[ ]:





# In[65]:


import random as rand
class Node:
    
    def __init__(self,key):
        
        self.right = None 
        self.left = None 
        self.val = key
        
    def insert(root,val):
        
        if root is None:
            
            return Node(key)
        else:
            if root.val == val:
                return root
            elif root.val < val:
                root.right = insert(root.right,val)
            else:
                root.left = insert(root.left,val)
        return root
    
    def ifNodeExists(node,key):
        if node == None:
            return False
        if (node.val == key):
            return True
        
        res1 = ifNodeExists(node.left,key)
        if res1:
            return True
        
        res2 = ifNodeExists(node.right,key)
        
        return res2
    


    
root = Node(rand.randint(0,7000))
        

for i in range (0,1000):
    x = rand.randint(0,7000)
    while(ifNodeExists(root,x)):
        x = rand.randint(0,7000)
    root.insert(x)


# In[80]:


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        
        print( self.data)
        
        if self.right:
            self.right.PrintTree()

def ifNodeExists(node, key):

    if (node == None):
        return False
    if (node.data == key):
        return True
    res1 = ifNodeExists(node.left, key)
    if res1:
        return True
    res2 = ifNodeExists(node.right, key)
 
    return res2

root = Node(random.randint(0, 7000))

for i in range(0, 1000):

    x = random.randint(0,7000)
    while (ifNodeExists(root, x)):
        x = random.randint(0,7000)
    
    root.insert(x)

''''root.PrintTree()'''
def convert_num(q):
    w =[]
    for i in q:
        w.append(i.data)
    return w
 
def bfs(root: Node):
    if root is None:
        return
    queue = [root]
    
    while len(queue) > 0:
        cur_node = queue.pop(0)
        
        for i in queue:
            print(i.data, end=" ")
        print()
        
        if cur_node.left is not None:
            queue.append(cur_node.left)

        if cur_node.right is not None:
            queue.append(cur_node.right)

bfs(root)



# In[81]:


def BFS(goal):
    q=[]
    explord =[]
    q.append(root)
    while len(q)!=0:

        #print(q)
        print(convert_num(q))
        node = q.pop(0)

        if node not in explord:
            explord.append(node)

        if node.data == goal:
            print(f'GOAL: {goal}')
            return (convert_num(explord))


        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
            
BFS(820)


# In[85]:


def DFS(goal):
    q=[]
    explord =[]
    q.append(root)
    while len(q)!=0:

        #print(q)
        print(convert_num(q))
        node = q.pop()

        if node not in explord:
            explord.append(node)

        if node.data == goal:
            print(f'GOAL: {goal}')
            return (convert_num(explord))
        
        if node.right is not None:
            q.append(node.right)
        if node.left is not None:
            q.append(node.left)
DFS(8)


# In[ ]:




