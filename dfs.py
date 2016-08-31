## v = no of vertice
## e = no of edge
## start, end...
## after that, we put [e] line, 1 line <=> [u,v]
v,e,start,end = map(int, input().split(' '))
a = [[False for i in range(v)] for j in range(v)]
## read adjenct matrix for graph
for _ in range(e):
    i,j = map(int, input().split(' '))
    a[i][j] = True
    a[j][i] = True

## dfs
free = [True for _ in range(v)] ## use for check if verticle has been come
trace = [-1 for _ in range(v)] ## use for get way from start to end
mask = [] ## stack for dfs
mask.append(start)
free[start] = False

while (len(mask) > 0):
    last = mask.pop()
    for i in range(v):
        if (a[last][i] and free[i] == True):
            free[i] = False
            mask.append(last)
            mask.append(i)
            trace[i] = last
            break
    

## print result
if (free[end]!=True):
    print ("found end")
    way = []
    last = end
    way.append(last)
    while (trace[last]!=-1):
        way.append(trace[last])
        last = trace[last]
    way.reverse()
    print (' '.join(map(str,way)))
else:
    print ("no found end")
