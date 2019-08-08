What Are Graphs?

Graph:

G:(V, E)

Set of vertices:

v E V

A graph is a data stucture that is good at modeling relationships between data points


What is AI?

Science of making machines (computers) that do things requiring intelligence

What is intelligence?

Tha ablity to adapt one's behaviour to fit new conditions

Intelligence includes:

Learning 

Reasoning

Problem Soliving
Perception
Language Understanding
AI is a frild of creating intelligence through artificial means


//Ways to Develop //Game AI

- Hardcorded rules, condtions, and actions

- Decision Trees (DT)
- Finite-State Machines (FSM) or FSM-based approches

- Behavior Trees (BT)

- Goal-Oriented Action Planning(GOAP)

-Machine learning techinques and so on

Zero-sum game

if one gains, another loses
Poker and gambling are popular examples

- Games like chess, tic tac toe tennis are also zero-sum games
In these if one looses another one gains


/////Search algorithms///
- Search algorithms are used to find the best path

- Best depends o  your requirements


What are trees?
In treess we refer to vertices as nodes and tree has a root node


How graphs are used in games.
Representing game state
-  or navigatio
- For keeping track of progress
- For level designers



///A map of a game World///

Cities to vist
Which can be reached?
- Cities are vertices
- Roads are edges
- Edge weights are distances


//The grid can be a graph//
-The cells are the vertices
- The roads are edges
-  Can be used for navigation and pathfinding

////What is the shortest path?

- Shortest path
- DiJkstra's algorith
-Pathfinding in graphs

-Grids and mazes

-Pathfinding in grids


///
- The BFS optimizes on vertex count, not path weight
lentgh of edge= weight of the edg e

Dijkstras algorithm solves the problem of finding the shortest path on weighted 

- It is from a class of algorithms called single-source shortest path algorithms

- It starts at a single source vertexx and finds the shortest path from all other  vertices to the source vertex.

-A common property of singe source shortest path algoritms is, that the algorithm revists vertices in order to find the path with the shortest weight.

-A vertex is not finished until all the paths leading to it has been examined. 

-Dijkstas algorithm can find path with the lowest path weight as opposed to breadth first search which doesnot take path and edge weights into account 


Asume that all edge weights are non distance negative (>=0)
Keep a shortest distance estimate on each vertex, initially infinity

For each vertex, vist all neighbours and update shortest distnace estimate

In each iteration, look at the vertex with the shortest distance estimate

Dijkstras algorihm works by keeping an estimate of the shortest distance to source for each vertex

In each iteration of the algorithm, we select the vertex that has the lowest distance estimate to the source.

A vertex is finished when we find the shortest path from the source
Then a vertex is removed from the set of vertices to inspect, as it now has the shortest path

So, once a vertex is finished and has a shortest path to the source, this vertex can be part of other shortest paths for neihbouring vertices

If we do not wish to find the shortest path form all the vertices to the source, but it's only interested in finding the shortest path to a goal vertex, we can terminate our search once the goal vertex is finished and has been removed from the set of vertices to inspect




/////Action///

The adjacent vertices get the distances updated, which is the weight of of the (parent which is turned to black)vertex plus the edge weight

Chose the next unfinished vertex with lowest distance

def find_path(graph, start, end, path=[]): path = path + [start]
        if start == end:
            print("Ending")
return path
        for node in graph[start]:
            print("Checking Node ", node)
            if node not in path:
                print("Path so far ", path)
                newp = find_path(graph, node, end, path)
                if newp:
                    return newp



