import numpy as np
from collections import deque

maze = np.array([[0, 1, 0],
                 [0, 1, 0],
                 [0, 0, 0]])

start = (0, 0)  # Starting position
goal = (0, 2)   # Goal position

row_count, col_count = maze.shape

print(f'size, {maze.size}')
path = [start]
queue = deque([(start, path)])
visited = set()
goal_reached = False

if start == goal:
    print("Start is the goal!")
    goal_reached = True


while goal_reached != True:
    
    state, path = queue.popleft()
    if state in visited:
        continue
    visited.add(state)

    x, y = state
    if state == goal:
        print("Goal reached!")
        print("Path to goal:", path)
        goal_reached = True
        break
    else:
        if x + 1 < row_count and maze[x + 1, y] == 0 and (x + 1, y) not in visited:
            queue.append(((x + 1, y), path + [(x + 1, y)]))
            print("Path so far:", path) 
        if x - 1 >= 0 and maze[x - 1, y] == 0 and (x - 1, y) not in visited:
            queue.append(((x - 1, y), path + [(x - 1, y)]))
            print("Path so far:", path)
        if y + 1 < col_count and maze[x, y + 1] == 0 and (x, y + 1) not in visited:
            queue.append(((x, y + 1), path + [(x, y + 1)]))
            print("Path so far:", path)
        if y - 1 >= 0 and maze[x, y - 1] == 0 and (x, y - 1) not in visited:
            queue.append(((x, y - 1), path + [(x, y - 1)]))
            print("Path so far:", path)

    if not queue:
        print("No path to the goal exists.")
        break
    



