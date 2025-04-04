from collections import deque
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node, end="")
            visited.add(node)
        queue.extend(graph.get(node,[]))
graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':['G'],
    'F':[],
    'G':[]
}
visited=[]
queue=[]
bfs(graph,'A')