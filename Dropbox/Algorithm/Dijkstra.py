print('\n\n')

from operator import itemgetter

def weigh(elem):
    return elem[1]


def heap_pop(heap):
    if heap != []:
        heap.sort(key=weigh)
        vertex,weight,parent = heap.pop(0)
        return (vertex, weight, parent)
    else:
        raise

def heap_add_or_replace(heap, triplet):
    if triplet not in heap:
        heap.append(triplet)
        heap.sort(key=weigh)
        lenth=len(heap)
        for i in range(0,lenth-1):
            if ( (triplet[0]==heap[i][0]) and (triplet[1]<heap[i][1])):
                inde=heap.index((heap[i][0],heap[i][1],heap[i][2]))
                heap.pop(inde)
            if((triplet[0]==heap[i][0]) and (triplet[1]>heap[i][1])):
                index=heap.index((triplet[0],triplet[1],triplet[2]))
                heap.pop(index)


def is_explored(explored_vertices,vertex):
    return vertex in explored_vertices

def add_to_explored_vertices(explored_vertices,vertex):
    explored_vertices.append(vertex)

def Dijkstra(maze_graph,initial_vertex):
    # Variable storing the exploredled vertices vertexes not to go there again
    explored_vertices = list()

    # Stack of vertexes
    heap = list()

    #Parent dictionary
    parent_dict = dict()
    # Distances dictionary
    distances = dict()

    initial_vertex = (initial_vertex, 0, initial_vertex)

    heap_add_or_replace(heap,initial_vertex)
    while len(heap) > 0:
        vertex, dist, parent=heap_pop(heap)
        if vertex not in explored_vertices:
            parent_dict.update({vertex:parent})
            add_to_explored_vertices(explored_vertices,vertex)
            distances.update({vertex:dist})
            neighbour=list(maze_graph[vertex].keys())
            lenth=len(neighbour)
            for i in range(0,lenth):
                if neighbour[i] not in explored_vertices:
                    wi=maze_graph[(vertex)][neighbour[i]]
                    heap.append((neighbour[i],dist+wi,vertex))

    return explored_vertices,parent_dict,distances



maze_graph = {
    (0,0): {(1,0):3,(0,1):5},
    (1,0): {(0,1):1,(1,1):2},
    (0,1): {(1,1):1,(0,2):2},
    (1,1): {(1,2):2},
    (0,2): {(1,2):4},
    (1,2): {(0,1):3},
    (2,2): {(1,2):2,(3,2):1},
    (2,1): {(1,1):3,(2,2):7},
    (3,2): {(2,1):2}
}

explored_vertices,parent_dict,distances=Dijkstra(maze_graph,(0,0))
print("explored vertices order: {}".format(explored_vertices))

print(parent_dict)

for vertex,parent in sorted(parent_dict.items(),key=itemgetter(0,0)):
    print("Vertex {} is reached from vertex {}, and its distance from initial vertex is {}".format(vertex,parent,distances[vertex]))

print('\n\n')
