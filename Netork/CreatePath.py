##I have a  map 3x3, from any point, you can only go to up/down/left/right point. 
##[***]
##[***]
##[***]
## i want to create a path contain 7 point from this map :D 

import random
def main():
    n = int(input())
    board = [[0 for i in range(n)] for i in range(n)]
    m = int(input())
    for _ in range(m):
        u,v = map(int, input().split(' '))
        board[u][v] = 1
        board[v][u] = 1
    
    print (board)
    s = []
    pFree = [x for x in range(n)]
    for i in range(n):
        option = [i]
        pFree.remove(i)
        rflush(pFree, option,s,board,n)
        pFree.append(i)
        option.remove(i)
    print (len(s))

    pass


def rflush(pFree, option,s,board,n):
    
    if (len(pFree) == 0):
        c = option.copy()
        print (option)
        s.append(c)
    else:
        
        last = option[len(option)-1]
        
        for j in range(n):
            if (board[last][j]==1 and j in pFree):
                pFree.remove(j)
                option.append(j)
                rflush(pFree,option,s,board,n)
                pFree.append(j)
                option.remove(j)

    pass

if __name__ == "__main__":
    main()

