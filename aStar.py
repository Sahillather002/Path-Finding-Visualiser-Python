from pyamaze import maze,agent,textLabel
from queue import PriorityQueue
#defining maze size
m=maze(15,15)
m.CreateMaze()

# print(m.maze_map)
# mapping is done in four directions e w n s
# e.g : (1,1): e=1 w=0 n=0 s=0
# 1 means path to that direction is open but path to 0 is closed 

# print(m.grid)
# it prints grids e.g for (5,5) maze we have (1,1),(1,2)to...(5,5)

#defining the manhatan distance
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2)+abs(y1-y2)

def aStar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))

    open=PriorityQueue()
    open.put((h(start,(1,1)),h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childcell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childcell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childcell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childcell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childcell,(1,1))

                if temp_f_score < f_score[childcell]:
                    g_score[childcell]= temp_g_score
                    f_score[childcell]= temp_f_score
                    open.put((temp_f_score,h(childcell,(1,1)),childcell))
                    aPath[childcell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

path=aStar(m)
a=agent(m,footprints=True)
m.tracePath({a:path})
l=textLabel(m,'A Star Algo Path Length',len(path))
m.run()