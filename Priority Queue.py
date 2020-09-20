# References
# https://www.geeksforgeeks.org/priority-queue-in-python/

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def insert(self, pathCost): 
        self.queue.append(pathCost) 
  
    # for retrieving an element based on Priority/Minimum Cost from the queue
    def get(self): 
        try: 
            minCost = 0
            for x in range(len(self.queue)): 
                if self.queue[x] < self.queue[minCost]: 
                    minCost = x 
            item = self.queue[minCost] 
            del self.queue[minCost] 
            return item 
        except IndexError: 
            print() 
            exit() 

def search(graph, start, end):
    
    queue = PriorityQueue()
    queue.insert((0, [start]))
    
    while not queue.isEmpty():
        node = queue.get()
        current = node[1][len(node[1]) - 1]
        if end in node[1]:
            print("UCS Route: " + str(node[1]) + ", TotalCost = " + str(node[0]))
            break
        
        cost = node[0]
        for nextNode in graph[current]:
            temp = node[1][:]
            temp.append(nextNode)
            queue.insert((cost + graph[current][nextNode], temp))
        

def main():
    graph = {'Arad':
            {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
            'Zerind':
            {'Oradea': 71},
            'Timisoara':
            {'Lugoj': 111},
            'Sibiu':
            {'Fagaras': 99, 'RimnicuVilcea': 80},
            'Oradea':
            {'Sibiu': 151},
            'Lugoj':
            {'Mehadia': 70},
            'RimnicuVilcea':
            {'Pitesti': 97, 'Craiova': 146},
            'Mehadia':
            {'Dobreta': 75},
            'Craiova':
            {'Pitesti': 138},
            'Pitesti':
            {'Bucharest': 101},
            'Fagaras':
            {'Bucharest': 211},
            'Dobreta':
            {'Craiova': 120},
            'Bucharest':
            {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90}}
    
    search(graph, 'Arad', 'Bucharest')

main()