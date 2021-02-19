# 그래프 표현

def dfs(graph):
    counts=[]
    for i in range(len(graph)):
        visited, need_visit = list(), list()
        start_node = list(graph.keys())[i]
        need_visit.append(str(start_node))
        count = 1
        while need_visit:
            # pop 인덱스 없으면 스택
            node = need_visit.pop()
            if node not in visited:
                visited.append(node)
                if node in graph:
                    need_visit.append(graph[node])
                else:
                    counts.append(count)
                count += 1
            else:
                counts.append(count)
    return max(counts)

results = []
for _ in range(int(input())):
    graph = dict()
    for __ in range(int(input())):
        m, s = input().split(' ')
        graph[m] = s
        results.append(str(dfs(graph)))
print('\n'.join(results))
# graph["A"] = ["B", "C"]
# graph["B"] = ["A", "D"]
