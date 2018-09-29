# Analysis of Algorithms
# Practice Assignment 3
# Author: Julia Maliauka
# Quiz 8 - Kruskal's Algorithm 

# Kruskal's Algorithm is used to find a MCST from a graph. 

# define the graph we will be using to create a MCST  
# each edge is given a cost of 1 at the moment
graph = { "p1" : ["p2", "p3"],  
          "p2" : ["p1", "p3", "p4"],
          "p3" : ["p1", "p2", "p5"],
          "p4" : ["p2", "p5"],
          "p5" : ["p3", "p4"]
        } 

numberOfEdges = 6

edges = ["p1-p2", "p1-p3", "p2-p3", "p2-p4", "p3-p5", "p4-p5"] 

# We will populate this tree with edges from the graph
tree = []

def checkForNoCycles(tree):
    print(tree)
    return True

for i in range(numberOfEdges):
    if checkForNoCycles(tree):
        print("...")
        tree.append(edges[i])


        
