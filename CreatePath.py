##I have a  map 3x3, from any point, you can only go to up/down/left/right point. 
##[***]
##[***]
##[***]
## i want to create a path contain 7 point from this map :D 

import random
def main():
    board = [[0 for i in range(0,9)] for i in range(0,9)]
    for i in range(0,3):
        for j in range(0,3):
            if i-1 >=0:
               board[(i-1) + j*3][ i+j*3] = 1
            if i+1<=2:
                board[i+1 + j*3][i+j*3] =1
            if j-1>=0:
                board[i + j*3][i + (j-1)*3] = 1
            if j+1<=2:
                board[i+j*3][i+(j+1)*3] = 1
    print (board)
    s = []
    pFree = [0,1,2,3,4,5,6,7,8]
    for i in range(0,9):
        option = [i]
        pFree.remove(i)
        rflush(pFree, option,s,board)
        pFree.append(i)
        option.remove(i)
    print (len(s))

    pass


def rflush(pFree, option,s,board):
    
    if (len(option) == 7):
        c = option.copy()
        print (option)
        s.append(c)
    else:
        
        last = option[len(option)-1]
        
        for j in range(0,9):
            if (board[last][j]==1 and j in pFree):
                pFree.remove(j)
                option.append(j)
                rflush(pFree,option,s,board)
                pFree.append(j)
                option.remove(j)

    pass

if __name__ == "__main__":
    main()

