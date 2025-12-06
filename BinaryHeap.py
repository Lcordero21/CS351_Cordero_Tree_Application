from typing import Protocol, List
from NewNode import Node

#Note: I added comments in this document since it has quite a bit...


class BinaryHeap (Protocol):
    def __init__(self) -> None:
        """
        Purpose:
            To initialize the heap
        Time Complexity:
            O(1)
        """
        self.heap: List[Node] = []

        
    def insertNode(self,node:Node)->None:
        """
        Purpose:
            To insert a new node into the heap
        Time Complexity:
            O(n) - There's one for-loop
        """
        if len(self.heap) == 0:
            self.heap.append(node)
            print("Added! ✅")
            return
        min = self.getMin()
        max = self.getMax()

        if node.getTimeEst() < min.getTimeEst():
            self.heap.insert(0,node)
            print("Added! ✅")
            return
        if node.getTimeEst() > max.getTimeEst():
            self.heap.append(node)
            print("Added! ✅")
            return
        else:
            for nodes in self.heap:
                if node.getTimeEst() < nodes.getTimeEst():
                    self.heap.insert(nodes-1,node)
                    print("Added! ✅")
                    return
    
    def getMax(self) -> Node:
        """
        Purpose: 
            Get the maximum value in the heap
        Time Complexity:
            O(1)
        """
        if len(self.heap)>0:
            return self.heap[len(self.heap)-1]
        else:
            return None
    
    def getMin(self) -> Node:
        """
        Purpose:
            Get the minimum value in the heap
        Time Complexity:
            O(1)
        """
        if len(self.heap)>0:
            return self.heap[0]
        else:
            return None
    
    def removeMin(self)-> None:
        """
        Purpose: 
            Remove the minimum value in the heap
        Time Complexity:
            O(1)
        """
        if len(self.heap)>0:
            self.heap.pop(0)
            return
        else:
            print("There is no assignment to remove!\n")
    
    def removeMax(self)-> None: 
        """
        Purpose: 
            Remove the maximum value in the heap
        Time Complexity:
            O(1)
        """
        if len(self.heap)>0:
            self.heap.pop()
            return
        else:
            print("There is no assignment to remove!\n")
    
    def decreaseTimeEst(self,index:int,newTime:float)->None:
        """
        Purpose:
            Decrease the time estimate for a node (this will reorganize the heap)
        Time Complexity:
            O(1)
        """
        if newTime < self.heap[index].getTimeEst():
            placeholder = self.heap.pop(index)
            placeholder.changeTimeEst(newTime)
            self.insertNode(placeholder)
            print("Updated! ✅")
            return
        print("Could not decrease time estimate, sorry!\n")
    
    def getParent(self, index:int):
        """
        Purpose:
            Get the parent of the current node
        Time Complexity:
            O(1)
        """
        if ((index/-1)/2) >0:
            return self.heap[(index/-1)/2]
        return None
    
    def getLeftChild(self, index:int):
        """
        Purpose:
            Get the left child of the current node
        Time Complexity:
            O(1)
        """
        if ((index*2)+1) < (len(self.heap)-1):
            return self.heap[(index*2)+1]
        return None
    
    def getRightChild(self, index:int):
        """
        Purpose:
            Get the right child of the current node
        Time Complexity:
            O(1)
        """
        if ((index*2)+2) < (len(self.heap)-1):
            return self.heap[(index*2)+2]
        return None
    
    def printList(self)->None:
        """
        Purpose:
            Print the list of assignments in order
        Time Complexity:
            O(1)
        """
        if len(self.heap) > 0:
            for i in range (len(self.heap)):
                node = self.heap[i]
                print(i+1,".", node.getName(),"~",node.getTimeEst(),"hrs")
        else: 
            print("There are no tasks!")

    def getLength(self)-> int:
        """
        Purpose: 
            Get the length of the binary heap
        Time Complexity:
            O(1)
        """
        return len(self.heap)
    
    def getNode(self, index)-> Node:
        """
        Purpose: 
            Get the node from the heap
        Time Complexity:
            O(1)
        """
        return (self.heap[index])