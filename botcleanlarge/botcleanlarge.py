__author__ = 'egor'

def next_move(posx, posy, dimx, dimy, board):
    if board[posx][posy]=='d':
        print("CLEAN")
        return 0
    #scanning circles around the bot
    empty = True
    radius = 1
    goals=[]
    g_indices=[]
    while empty:
        #going through the given circle
        current = [-radius, 0]
        for i in range(4*radius):
            if (posx+current[0]>=0) & (posx+current[0]<dimx) & (posy +current[1]>=0) & (posy + current[1]<dimy):
                if board[posx+current[0]][posy+current[1]]=='d':
                    goals.append([current[0],current[1]])
                    g_indices.append(i)
                    empty = False
            if i<radius:
                current[0]+=1
                current[1]+=1
            elif i<radius*2:
                current[0]+=1
                current[1]-=1
            elif i<radius*3:
                current[0]-=1
                current[1]-=1
            else:
                current[0]-=1
                current[1]+=1
        radius+=1
    distances=[(g_indices[i]-g_indices[i-1]) for i in range(len(g_indices))]
    distances[0]+=(radius-1)*4
    goal=goals[distances.index(max(distances))]
    if goal[0]>0:
        print("DOWN")
        return 0
    elif goal[0]<0:
        print("UP")
        return 0
    elif goal[1]>0:
        print("RIGHT")
        return 0
    else:
        print("LEFT")
        return 0


with open("sampleinput.txt") as f:
    pos = [int(i) for i in f.readline().strip().split()]
    dim = [int(i) for i in f.readline().strip().split()]
    board = [[j for j in f.readline().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
    #next_move(3, 3, dim[0], dim[1], board)
