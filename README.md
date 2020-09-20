# -Least-Cost-Path-using-Priority-Queue

Task: Use Priority Queue and Uniform-Cost Search algorithm to find the least cost route from Arad to Bucharest.

Step 1: Define a Class “Priority Queue”
Step 2: Define the following functions for the Priority Queue class:
	__init()__: initializer for the queue
	__str()__:  to store the path and cost as a string in the queue
	isEmpty(): to check if the queue is empty or not
	insert(): to put an element(cost, path) into the queue
	get(): to retreive an element(cost, path) from the queue based on minimum cost or 	         highest priority.
Step 3: Store every location, its subsequent neighbour and cost from location to its neighbour in a dictionary “graph”.
Step 4: Define a function “search” to implement UCS
Step 5: Define a Priority Queue using PriorityQueue() class and put the first location “Arad” and its cost “0” into the queue using queue.insert().
Step 6: Iterate through the queue until it’s not empty, get the queue element using queue.get() in a tuple and store the last location of the tuple in a variable. This location will be used to access the same location in the dictionary. Also store the current total cost in a variable.
Step 7: Go to the dictionary and Iterate through the values of the current location in the dictionary. Append the current location with its neighbour and put the whole path into the queue and the current total cost into the queue. Do this process until all of the values of the current dictionary key have been iterated and put into the queue.
Step 8: If the queue element has the Target location “Bucharest” in it then print the current total cost and the whole start to end path.
