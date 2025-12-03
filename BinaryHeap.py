from typing import Protocol, List
from NewNode import Node

class BinaryHeap (Protocol):
    def __init__(self) -> None:
        """
        Docstring for __init__
        
        :param self: Description
        """
        self.heap: List[Node] = []

        
    def insertNode(self,node:Node)->None:
        min = self.getMin()
        max = self.getMax()

        if node.getTimeEst() < min.getTimeEst():
            self.heap.insert(0,node)
        if node.getTimeEst() > max.getTimeEst():
            self.heap.append(node)
        else:
            for nodes in self.heap:
                if node.getTimeEst() < nodes.getTimeEst():
                    self.heap.insert(nodes-1,node)
                    return
    
    def getMax(self) -> Node:
        return self.heap[len(self.heap)-1]
    
    def getMin(self) -> Node:
        return self.heap[0]
    
    def removeMin(self)-> None:
        self.heap.pop(0)
    
    def removeMax(self)-> None: 
        self.heap.pop()
    
    def decreaseTimeEst(self,index,newTime):
        if newTime < self.heap[index].getTimeEst():
            placeholder = self.heap.pop(index)
            placeholder.changeTimeEst(newTime)
            self.insertNode(placeholder)
            return
        print("Could not decrease time estimate, sorry!")
    
    def getParent(self, index) -> Node:
        if ((index/-1)/2) >0:
            return self.heap[(index/-1)/2]
        return None
    
    def getLeftChild(self, index):
        if ((index*2)+1) < (len(self.heap)-1):
            return self.heap[(index*2)+1]
        return None
    
    def getRightChild(self, index):
        if ((index*2)+2) < (len(self.heap)-1):
            return self.heap[(index*2)+2]
        return None
    
    def printNames(self):
        if len(self.heap) > 0:
            for i in range (len(self.heap)):
                node = self.heap[i]
                print(i+1,".", node.getName())
        else: 
            print("There are no tasks!")
