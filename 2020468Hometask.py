import random as rand
import time as t
import numpy as np
import matplotlib.pyplot as plt

#Tree implemenation

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
    

#generating random  umbers 
    
root = Node(rand.randint(0,1000))
root = Node(rand.randint(0,5000))
root = Node(rand.randint(0,8000))
        
#inserting all the ranges of generated Rand nums
for i in range (0,1000):
    x = rand.randint(0,7000)
    while(ifNodeExists(root,x)):
        x = rand.randint(0,7000)
    root.insert(x)

for i in range (0,1000):
    x = rand.randint(0,5000)
    while(ifNodeExists(root,x)):
        x = rand.randint(0,5000)
    root.insert(x)
            
        
    
for i in range (0,1000):
    x = rand.randint(0,8000)
    while(ifNodeExists(root,x)):
        x = rand.randint(0,8000)
    root.insert(x)




#BFS implementation             
def convert_num(q):
    w =[]
    for i in q:
        w.append(i.data)
    return w

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

#DFS implementation

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


#finding indexes using BFS and DFS           
BFS(820)
BFS(4100)
BFS(6560)

DFS(820)
DFS(4100)
DFS(6560)


#calculating time for each index and BFS/DFS
start1 = t.time()
BFS(820)
end1 = t.time()

t1 = end1-start1

print("time for 820 BFS index:",t1)

start2 = t.time()
BFS(4100)
end2 = t.time()

t2 = end2-start2

print("time for 4100 BFS index:",t2)

start3 = t.time()
BFS(6560)
end3 = t.time()

t3 = end3-start3

print("time for 6560 BFS index:",t3)



start4 = t.time()
DFS(820)
end4 = t.time()

tt1 = end4-start4

print("time for 820 DFS index:",tt1)

start5 = t.time()
DFS(4100)
end5 = t.time()

tt2 = end5-start5

print("time for 4100 DFS index:",tt2)

start6  = t.time()
DFS(6560)
end6 = t.time()

tt3 = end6-start6

print("time for 6560 DFS index:",tt3)


#plotting graph


data = {'820':t1,'4100':t2,'6560':t3}
times1 =list(data.values())
index = list(data.keys())

fig = plt.figure(figsize = (10, 5))
plt.bar(index, times1, color ='maroon',
        width = 0.4)

plt.xlabel("Indexs")
plt.ylabel("Time taken")
plt.show()