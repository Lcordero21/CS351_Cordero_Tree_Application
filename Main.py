from BinaryHeap import BinaryHeap
from NewNode import Node

def runMain():
 allAssignments = BinaryHeap()

 while True:
    option = int(input("\n 1.See Current Assignments \n 2.Add An Assignment \n 3.Complete the top assignment"
                   "\n 4.Complete the last assignment \n 5.Remove an Assignment \n 6.Quit Application\nYour Option:"))
    print("-"*15)
    if option == 1:
        # Show list of all assignments
        print("-CURRENT ASSIGNMENTS-\n")
        allAssignments.printList()

    elif option == 2:
        # Add a new assignment to the list
        name:str = str(input("Assignment Name:"))
        description:str = str(input("Description About Assignment:"))
        timeEst:float = int(input("Time Estimate in Hours (Ex: 1.5 for 1 hour and 30 minutes):"))
        newAssignment = Node(name,timeEst,description)

        print("Adding",name, "To The List!\n")
        allAssignments.insertNode(newAssignment)
       
    elif option == 3:
        # Complete the top assignment
        print("Completing Top Assignment....\nAssignment:",allAssignments.getMin().getName())
        allAssignments.removeMin()
    elif option == 4:
        # Complete the last assignment
        print("Completing Top Assignment....\nAssignment:",allAssignments.getMax().getName())
        allAssignments.removeMax()
    elif option == 5:
        # Remove an assignment from the list
        pass

    elif option == 6:
        # Quit the program (which will erase all the data, so there will be a warning)
        quitting = (input ("Doing this will erase all your data. Are you sure? (Y/N):")).lower()
        if quitting == "y":
            print("Ending Program...Thank You For Using The Homework Tracker!")
            quit()
        elif quitting == "n":
            print("Not ending program!")
        else:
            print("Not a valid answer, not quitting program")
    else:
       print("Please Choose a Valid Option ❌\n")


if __name__ == "__main__":
    print("Welcome to Homework Tracker!📝\n---------------------------------------------")
    runMain()
