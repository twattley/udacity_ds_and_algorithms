from queue import PriorityQueue

def shortest_path(_map, start, goal):
    
    previous_node = {}
    score = {}
    
    previous_node[start]=None
    score[start]=0
  
    path_queue = PriorityQueue()
    path_queue.put(start)
    
    while not path_queue.empty():
        current_node = path_queue.get()

        #break state
        if current_node == goal:
            return_path_as_list(previous_node, start, goal)

        #loop through chilren of current node and calculate distance from origin 
        for node in _map.roads[current_node]:

            #update current score for node
            g_score = score[current_node] + point_distance(_map.intersections[current_node],
                                                               _map.intersections[node])
            
            if node not in score or g_score < score[node]:
                
                score[node] = g_score

                h_score = point_distance(_map.intersections[current_node],
                                                          _map.intersections[goal])

                f_score = g_score + h_score #a star search criteria

                path_queue.put(node, f_score)
                previous_node[node] = current_node

    path = return_path_as_list(previous_node, start, goal)

    return path


def point_distance(point_a: List, point_b: List) -> int:

    """ heuristic helper, direct distance between points """

    x = abs(point_a[0] - point_b[0])
    y = abs(point_a[1] - point_b[1])

    return x + y 


def return_path_as_list(previous_node, start, goal):

    """ loop back and create a list of nodes visited for that path """
    
    node = goal
    path = [node]
    
    while node:
        node = previous_node[node]
        path.insert(0,node)
        
    return path[1:]