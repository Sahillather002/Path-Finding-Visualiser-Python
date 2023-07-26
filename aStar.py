from pyamaze import maze
#defining maze size
m=maze(5,5)
m.CreateMaze()

# print(m.maze_map)
# mapping is done in four directions e w n s
# e.g : (1,1): e=1 w=0 n=0 s=0
# 1 means path to that direction is open but path to 0 is closed 


m.run()