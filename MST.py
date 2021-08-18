# --------------------------------------------------------------|
# Name: Brandon Schultz
# Date: 7-30-21
# Assignment: Graph Algorithms
# Question 4   -   MST implementation using Prims' Algorithm
# 4a. Input format: nodes/vertices of nodes
#     Output format: edge count total and depiction of given nodes MST if applicable
#
# Sources:
# - https://docs.python.org/3/library/sys.html
# - https://www.python-course.eu/graphs_python.php#:~:text=Python
# %20has%20no%20built-in%20data%20type%20or%20class,ideal%20for%
# 20representing%20graphs%20in%20Python%2C%20i.e.%20dictionaries.
# -  https://www.tutorialspoint.com/python_data_structure/
# python_graphs.htm
# - https://www.python-course.eu/examples/graph2.py 
# - https://www.programiz.com/dsa/graph-adjacency-matrix#:~:text=An%20adjacency%20matrix%20is%20a%20way%20of%20representing,an%20edge%20from%20Node%20i%20to%20Node%20j.
# - https://canvas.oregonstate.edu/courses/1821195/pages/exploration-minimum-spanning-tree-kruskals-algorithm?module_item_id=21221777
# - https://stackoverflow.com/questions/63164064/unable-to-understand-lt-method#:~:text=__lt__%20is%20a%20magic%20method%20that%20lets%20you,then%20it%20uses%20that%20method%20for%20the%20comparison.
# --------------------------------------------------------------|

# Prim’s MST algorithm applies a greedy approach via use of a priority queue data structure to determine what elements (nodes) are connected to other elements (nodes). Given a source Node of A with edges 1, 3, this method will add both edge values to a priority queue, before selecting the smaller of the two edges (1) to use as a means of navigation to the node asscoiated with said smaller edge. The process repeats until an MST is formed. Additional information is provided below.
from queue import PriorityQueue

# Defines vertices/Nodes and their charcteristics that will be used in building of MST. This includes nodes/vertices graph is composed of, edges linking them to adjacent node/vertices and a processed/not processed flag to detemrine if node has/hasnt already been processed by the priority que and is/isnt reflected in MST.  
class Node:
  def __init__(self, label):
    self.label = label                # source vertex
    self.nodeEdges = []               # vertices edges
    self.traversed = False           

  # Method for connecting nodes to one another
  def connectNode(self, adjNode, edgeWeight):
    global totalEdges
    self.nodeEdges.append(nodeEdge(self, adjNode, edgeWeight))
    adjNode.nodeEdges.append(nodeEdge(adjNode, self, edgeWeight))
    totalEdges += 2
    
  # Returns string representation of object(s) fron node class.
  # aka vertices
  def __repr__(self):
    return self.label

 # Defines edges of nodes that will be used in building of MST. 
class nodeEdge:
  def __init__(self, origin, destination, Weight):
    self.origin = origin                 # Comign From this node/v
    self.destination = destination       # Attach to this node/v
    self.Weight = Weight                 # Val of attachment/dis traveled between nodes

  # Used to compare wedge weight vals of nodes and select smaller/greedier val for addition to priority queue/mst.
  def __lt__(self, comparedToNode):
    if isinstance(comparedToNode, nodeEdge):
      return self.Weight < comparedToNode.Weight
    return False

  # Returns string representation of object(s) fron nodeEdge class.
  # connecting points to/from vertices.
  def __repr__(self):
    return f"{self.origin}--{self.destination}"

 #----------------------------------------------------------------------------| 
 # - Implementation of Prim's algorithm:
 # searchs for edge values of smallest weight val via PriorityQ
 # until all edges have been accounted for via edgecount and totalEdges
 # not matching. ie, more edges remain to be compared if vals =! one another.
 # Once equal, smallest cost edge is poppred from PriorityQ,
 # its destination node is checked for being/not being a node
 # previously traveled whose edges have/hevnt been processed by PrimsG
 # If edge is determined to be new,  edgecount's value is incremented, edges 
 # weight val is added weight total of all edges, then added to MST 
 #----------------------------------------------------------------------------|
class PrimsAlg:
  def __init__(self):
    self.PriorityQ = PriorityQueue()  # priority queue for min edge searching
    self.MST = []                     # min spanning tree
    self.weightTotal = 0              # mst's total cost

  #Function for Implementation of Prim's algorithm used in assignment.
  def PrimsG(self, s):
    global totalEdges                 # intialization for
    self.addEdges(s)                  # count total of first v's edges
    edgeCount = 0
    #
    while not self.PriorityQ.empty() and edgeCount != totalEdges:
      minEdge = self.PriorityQ.get()

      if minEdge.destination.traversed:
        continue

      else:
        edgeCount += 1
        self.weightTotal += minEdge.Weight
        self.MST.append(minEdge)
        self.addEdges(minEdge.destination)

    return edgeCount != totalEdges  # graph doesnt have MST

  def addEdges(self, check):
    check.traversed = True;
    for nodeEdge in check.nodeEdges:
      if not nodeEdge.destination.traversed:
        self.PriorityQ.put(nodeEdge)


if __name__ == '__main__':
  # Sum of edges in graph
  totalEdges = 0

  # Nodes making up graph
  Nodes = [Node('A'), Node('B'), Node('C'),
           Node('D'), Node('E'),  Node('F')]

  #Vertices connecting nodes to one another:
  Nodes[0].connectNode(Nodes[1], 5)
  Nodes[0].connectNode(Nodes[3], 7)
  Nodes[1].connectNode(Nodes[2], 4)
  Nodes[1].connectNode(Nodes[3], 12)
  Nodes[2].connectNode(Nodes[3], 9)
  Nodes[2].connectNode(Nodes[4], 10)
  Nodes[3].connectNode(Nodes[4], 3)
  Nodes[4].connectNode(Nodes[5], 13)
  

  PrimsAlg = PrimsAlg()
  
  if PrimsAlg.PrimsG(Nodes[0]):
    print(PrimsAlg.MST)
    print("Total Weight: ",PrimsAlg.weightTotal)

  else:
    print("MST N/A")