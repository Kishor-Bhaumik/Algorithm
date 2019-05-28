from operator import itemgetter

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)

def is_explored(explored_vertices,vertex):
    return vertex in list(explored_vertices)

def FIFO_push(queuing_structure,initial_vertex,par):
    tmp=list()
    tmp.extend((initial_vertex,par))
    queuing_structure.append(tmp)
    return queuing_structure

def FIFO_pop(queuing_structure):
    queuing_structure.pop()

##########

def BFS(maze_graph,initial_vertex):

    explored_vertices=list()
    queuing_structure=list()
    parent_dict=dict()

    FIFO_push(queuing_structure,initial_vertex,None)
    while len(queuing_structure)>0:
        current_vertex,parent=queuing_structure.pop(0)
        if current_vertex not in explored_vertices:
            add_to_explored_vertices(explored_vertices,current_vertex)
            parent_dict.update({current_vertex:parent})
            qq=list(maze_graph[current_vertex].keys())
            for i in range(0,len(qq)):
                if qq[i] not in explored_vertices:
                    FIFO_push(queuing_structure,qq[i],current_vertex)
        #current_vertex,parent=FIFO_pop(queuing_structure)

    return explored_vertices,parent_dict



maze_graph = {
    (0,0): {(0,1):1,(1,0):1},
    (0,1): {(0,2):1,(0,0):1},
    (1,0): {(1,1):1,(0,0):1},
    (1,1): {(1,2):1,(1,0):1},
    (0,2): {(0,1):1,(1,2):1},
    (1,2): {(0,2):1,(1,1):1}
}

explored_vertices,parent_dict = BFS(maze_graph, (0,0))
print("Explored vertices order: {}".format(explored_vertices))
for vertex,parent in sorted(parent_dict.items(),key=itemgetter(0,0)):
    print("Vertex {} is the parent of vertex {}".format(parent,vertex))
