v,e,start=map(int,input().split())

list_ = [[] for i in range(v+1)]
check = [0 for d in range(v+1)]
for i in range(1,e+1):
    v1,v2=map(int,input().split())
    list_[v1].append(v2)
    list_[v2].append(v1)
for t in range(1,v+1):
    list_[t].sort()

def dfs(list_,check,now):
    if check[now]==0:
        check[now]=1
    else:
        return
    print(now,'',end='')
    for z in list_[now]:
        dfs(list_,check,z)

dfs(list_,check, start)
print("")
queue = []
visited_qu=[0 for zz in range(v+1)]


def bfs(list_,check,now):
    queue.append(now)
    while queue:
        now = queue.pop(0)
        visited_qu[now]=1
        print(now,'',end='')
        for my in list_[now]:

            if visited_qu[my]==0:
                queue.append(my)
                visited_qu[my]=1


bfs(list_,check,start)
