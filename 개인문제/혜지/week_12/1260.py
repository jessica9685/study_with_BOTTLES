'''그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.'''

'''첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
입력으로 주어지는 간선은 양방향이다.'''

'''첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.'''



from collections import deque

def DFS(graph, root) :
    visited = []
    stack = [root]

    while stack :
        n = stack.pop()
        if n not in visited :
            visited.append(n)
        if n in graph :
            temp = list(set(graph[n]) - set(visited))
            temp.sort(reverse = True)
            stack += temp
    return " ".join(str(i) for i in visited)

def BFS(graph, root) :
    visited =[]
    queue = deque([root])

    while queue :
        n = queue.popleft()
        if n not in visited :
            visited.append(n)
        if n in graph :
            temp = list(set(graph[n])-set(visited))
            temp.sort()
            queue += temp
    return " ".join(str(i) for i in visited)


graph = {}
n = input().split(' ')
node, edge, start = [int(i) for i in n]
for i in range(edge) :
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph :
        graph[n1] = [n2]
    elif n2 not in graph[n1] :
        graph[n1].append(n2)

    if n2 not in graph :
        graph[n2] = [n1]
    elif n1 not in graph[n1] :
        graph[n2].append(n1)

print(DFS(graph, start))
print(BFS(graph, start))
