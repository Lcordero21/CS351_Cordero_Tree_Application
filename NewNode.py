from typing import Protocol, List

class Node (Protocol):
    def __init__(self, assignment, time, description, due)-> None:
        self.assignment = assignment
        self.timeEst = time
        self.description = description
        self.dueDate = due

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
