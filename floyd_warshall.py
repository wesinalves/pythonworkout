# Python3 Program for Floyd Warshall Algorithm
# Number of vertices in the graph
from math import inf

def floyd_warshall(graph):
    n = len(graph)
    dist0 = graph
    for k in range(n):
        distN = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                distN[i][j] = min(dist0[i][j],
                                 dist0[i][k] + dist0[k][j]
                                 )
        dist0 = distN
    printSolution(distN)


# A utility function to print the solution
def printSolution(dist):
    n = len(dist)
    print("Resultado Final - Matriz D(n)")
    for i in range(n):
         for j in range(n):
            if(dist[i][j] == inf):
                print("INF", end="\t")
            else:
                print(dist[i][j], end="\t")
            if j == n-1:
                print()


if __name__ == "__main__":
    graph = [
        [0, 3, 8, inf, -4],
        [inf, 0, inf, 1, 7],
        [inf, 4, 0, inf, inf],
        [2, inf, -5, 0, inf],
        [inf, inf, inf, 6, 0]
    ]
        
    # Function call
    floyd_warshall(graph)