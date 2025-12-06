from typing import Protocol, List

"""
I didn't add comments under each function since it's purpose is to either change different 
components of the Node or to return a certain element. Thus, they all have a time complexity of 
O(1).
"""

class Node (Protocol):
    def __init__(self, assignment, time, description)-> None:
        self.assignment = assignment
        self.timeEst = time
        self.description = description
        self.dueDate = None

    def changeName(self,newName)-> None:
        self.assignment = newName

    def changeTimeEst (self,newTime) -> None:
        self.timeEst = newTime

    def changeDesc(self, newDesc) -> None:
        self.description = newDesc

    def changeDueDate(self, newDue) -> None:
        self.dueDate = newDue

    def getName (self) -> str:
        return self.assignment
    
    def getTimeEst (self) -> float:
        return self.timeEst
    
    def getDesc (self) -> str:
        return self.description
    
    def getDueDate (self) -> str:
        return self.dueDate
