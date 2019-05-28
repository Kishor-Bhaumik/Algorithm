
from operator import itemgetter

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)

def is_explored(explored_vertices,vertex):
    return vertex in list(explored_vertices)

def LIFO_push(queuing_structure,initial_vertex,par):
    tmp=list()
    tmp.extend((initial_vertex,par))
    queuing_structure.append(tmp)
    return queuing_structure

def LIFO_pop(queuing_structure):
    queuing_structure.pop(-1)

def DFS(maze_graph, initial_vertex) :

    # explored vertices list
    explored_vertices = list()

    #LIFO stack
    queuing_structure = list()

    #Parent Dictionary
    parent_dict = dict()


    LIFO_push(queuing_structure,initial_vertex,None)    # push the initial vertex to the queuing_structure

    while len(queuing_structure) > 0:        #   while queuing_structure is not empty:
        current_vertex,parent=queuing_structure.pop()      # current_vertex,parent = queuing_structure.pop()
        if current_vertex not in explored_vertices:        # if the current vertex is not explored
            add_to_explored_vertices(explored_vertices,current_vertex)# add current_vertex to explored vertices
            parent_dict.update({current_vertex:parent})# use parent_dict to map the parent of the current vertex
            qq=list((maze_graph[current_vertex].keys()))
            for i in range(0,len(qq)):# for each neighbor of the current vertex in the maze graph:
                if qq[i] not in explored_vertices:# if neighbor is not explored:
                    LIFO_push(queuing_structure,qq[i],current_vertex)# push the tuple (neighbor,current_vertex) to the queuing_structure

    return explored_vertices,parent_dict

maze_graph = {
    (0,0): {(0,1):1,(1,0):1},
    (0,1): {(0,2):1,(0,0):1},
    (1,0): {(1,1):1,(0,0):1},
    (1,1): {(1,2):1,(1,0):1},
    (0,2): {(0,1):1,(1,2):1},
    (1,2): {(0,2):1,(1,1):1}
}
explored_vertices,parent_dict = DFS(maze_graph, (0,0))
print("Explored vertices order: {}".format(explored_vertices))
for vertex,parent in sorted(parent_dict.items(),key=itemgetter(0,0)):
    print("Vertex {} is the parent of vertex {}".format(parent,vertex))
