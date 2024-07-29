import rubik

def BFS_step(frontier,parent):
    new_frontier = []
    for node in frontier:
        perms_neighbors = [(perm,rubik.perm_apply(perm, node)) for perm in rubik.quarter_twists]
        for perm,neighbor in perms_neighbors:   
            if neighbor not in parent:
                parent[neighbor] = (perm,node)
                new_frontier.append(neighbor)
    return new_frontier

def shortest_path(start, end):
    """
    Using 2-way BFS, finds the shortest path from start_position to
    end_position. Returns a list of moves. 

    You can use the rubik.quarter_twists move set.
    Each move can be applied using rubik.perm_apply
    """
    if start == end:
        return []
    
    parent = {start:None}
    back_parent = {end:None}
    frontier = [start]
    back_frontier = [end]
    for j in range(7):
        frontier = BFS_step(frontier,parent)
        back_frontier = BFS_step(back_frontier,back_parent)
        for i in parent:
            if i in back_parent:
                result = []
                x = i
                while x!=start:
                    result.append(parent[x][0])
                    x = parent[x][1]

                result2 = []    
                x = i
                while x!=end:
                    result2.append(rubik.perm_inverse(back_parent[x][0]))
                    x = back_parent[x][1]
                return list(reversed(result))+result2

    return None


start = rubik.I
middle = rubik.perm_apply(rubik.F, start)
end = rubik.perm_apply(rubik.L, middle)
ans = shortest_path(start, end)
