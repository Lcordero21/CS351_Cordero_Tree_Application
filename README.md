# CS351_Cordero_Tree_Application

## Project Title and Description
    Homework Tracker - A Quick Way to track which assignments you need to complete in order based on time estimate

## What tree did you implement?
    A Binary Heap Tree

## What does your application do?
    It tracks assignments (name, description, time estimate) and puts them in order based on time estimate. It also allows the user to complete the top or bottom assignment, and decrease the time estimate of any assignment (if need be).

## Who would use this and why?
    It's good for students mainly, but anyone who needs to keep track of tasks can use it!

## Installation & Setup
    To use the program, run the Main.py file.

## Usage Guide
    Press one of the following numbers after booting up the program:
    1 - To look at all current assigments
    2 - To add a new assignment
    3 - To complete the assignment at the top of the list
    4 - To complete the assignment at the bottom of the list
    5 - To decrease the time estimate of an assignment
    6 - To look at the description of an assignment
    7 - To quit the application

## Tree Implementation Details
    I made a Binary Heap Tree (that is stored in an array). I technically added the code to find the parent and left/right node of a specific node, however I didn't quite put this into practice, I will be honest...It is something that I would like to utilize more in the future (perhaps to actually print the tree in a tree form, or add some sort of scrolling function for the code)

## Time complexity of key operations
    I added these as comments in the code (except for the Main.py, which is O(1) for the most part)

## Any interesting implementation choices
    Not that I can think of other than the fact that the user can only complete the shortest time estimated assignment or the longest time estimated assignment.

## Evolution of the Interface
    Not much changed from my initial design, I made the binary heap with the final design in mind and had written out what functions I wanted the final program to have (adding an assignment, viewing the description, completing only the longest or shortest assignment). The most iterative part of it was adding more and more elements to the final design to make it look prettier and more cohesive (and fixing any errors).

## Future Enhancements
    If I had more time, I would love to implement a much prettier version of this that isn't just in the terminal (and have it read in files perchance).