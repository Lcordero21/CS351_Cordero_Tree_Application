from BinaryHeap import BinaryHeap
from NewNode import Node

def runMain():
 allAssignments = BinaryHeap()

 while True:
    option = int(input("\n 1.See Current Assignments \n 2.Add An Assignment \n 3.Complete the top assignment"
                   "\n 4.Complete the last assignment \n 5.Decrease Time Estimate for Assignment \n 6.See info about an Assignment"
                   "\n 7.Quit Application\nYour Option:"))
    print("-"*15)
    if option == 1:
        # Show list of all assignments
        print("-CURRENT ASSIGNMENTS-\n")
        allAssignments.printList()

    elif option == 2:
        # Add a new assignment to the list
        print("-NEW ASSIGNMENT-\n")
        name:str = str(input("Assignment Name:"))
        description:str = str(input("Description About Assignment:"))
        timeEst:float = int(input("Time Estimate in Hours (Ex: 1.5 for 1 hour and 30 minutes):"))
        newAssignment = Node(name,timeEst,description)

        print("Adding",name, "To The List!\n")
        allAssignments.insertNode(newAssignment)
       
    elif option == 3:
        # Complete the top assignment
        print("-REMOVING TOP ASSIGNMENT-\n")
        if allAssignments.getLength() != 0:
            print("Completing Top Assignment....\nAssignment:",allAssignments.getMin().getName())
        allAssignments.removeMin()
    elif option == 4:
        # Complete the last assignment
        print("-REMOVING LAST ASSIGNMENT-\n")
        if allAssignments.getLength() != 0:
            print("Completing Last Assignment....\nAssignment:",allAssignments.getMax().getName())
        allAssignments.removeMax()
    elif option == 5:
        # Decrease an assignment's time estimate
        print("-DECREASE TIME ESTIMATE-\n")
        length = allAssignments.getLength()
        if length != 0:
            allAssignments.printList()
            index = int(input("Choose an assignment to decrease the time:"))
            if (index > 0) and (index <= length):
                newTime = float(input("What new time would you like to decrease the time estimate to? (In hrs):"))
                if newTime >= 0:
                    allAssignments.decreaseTimeEst(index-1,newTime)
                elif newTime < 0: 
                    print("Not a valid time!❌")
        elif allAssignments.getLength() == 0:
            print("There are no assignments!\n")
    elif option == 6:
        #View Assignment Info
        print("-ASSIGNMENT INFO-\n")
        length = allAssignments.getLength()
        if length != 0:
            allAssignments.printList()
            index = int(input("Choose an assignment to see:"))
            if (index > 0) and (index <= length):
                node = allAssignments.getNode(index-1)
                print("\nAssignment:",node.getName(),"\nDescription:", node.getDesc(),"\nTime estimate(hrs):",node.getTimeEst())
        elif allAssignments.getLength() == 0:
            print("There are no assignments!\n")

    elif option == 7:
        # Quit the program (which will erase all the data, so there will be a warning)
        print("-QUIT PROGRAM-\n")
        quitting = (input ("Doing this will erase all your data. Are you sure? (Y/N):")).lower()
        if quitting == "y":
            print("Ending Program...Thank You For Using The Homework Tracker!✨")
            quit()
        elif quitting == "n":
            print("Not ending program!")
        else:
            print("Not a valid answer, not quitting program❌")
    else:
       print("Please Choose a Valid Option ❌\n")

if __name__ == "__main__":
    print("Welcome to Homework Tracker!📝\n---------------------------------------------")
    runMain()
