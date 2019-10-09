class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# # Class Solution
# class Graph:
#     def __init__(self):
#         self.verticies = {}
#
#     def add_vertex(self, vertex_id):
#         if vertex_id not in self.verticies:
#             self.verticies[vertex_id] = set()
#
#     def add_edges(self, v1, v2):
#         if v1 in self.verticies and v2 in self.verticies:
#             self.verticies[v1].add(v2)
#         else:
#             raise IndexError("That vertex does not exist")
    
def earliest_ancestor(ancestors, starting_node):
    # # Class Solution
    # # build our graph
    # graph = Graph()
    #
    # for pair in ancestors:
    #     graph.add_vertex(pair[0])
    #     graph.add_vertex(pair[1])
    #     # build edges in reverse
    #     graph.add_edges(pair[1], pair[0])
    #
    # queue = Queue()
    # queue.enqueue([starting_node])
    #
    # max_path_length = 1
    # earliest_ancestor = -1
    #
    # while queue.size() > 0:
    #     path = queue.dequeue()
    #     vertex = path[-1]
    #
    #     if(len(path) >= max_path_length and vertex < earliest_ancestor) or (len(path) > max_path_length):
    #         earliest_ancestor = vertex
    #         max_path_length = len(path)
    #
    #     for neighbor in graph.verticies[vertex]:
    #         path_copy = list(path)
    #         path_copy.append(neighbor)
    #         queue.enqueue(path_copy)
    #
    # return earliest_ancestor
    
# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known
# ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for
# "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should
# return -1.

# * The input will not be empty.
# * There are no cycles in the input.
# * There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
# * IDs will always be positive integers.
# * A parent may have any number of children.

# def find_word_ladder(beginWord, endWord):
#     queue = Queue()
#     visited = set()
#     queue.enqueue([beginWord])
#     while queue.size() > 0:
#         path = queue.dequeue()
#         vertex = path[-1]
#         if vertex not in visited:
#     # here is the point to do whatever is we are trying to accomplish
#             if vertex == endWord:
#                 return path
#             visited.add(vertex)
#             for new_vert in get_neighbors(vertex):
#                 new_path = list(path)
#                 new_path.append(new_vert)
#                 queue.enqueue(new_path)