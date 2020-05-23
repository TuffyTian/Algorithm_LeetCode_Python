"""
 * @Author: TuffyTian 
 * @Date: 2020-05-23 16:57:22 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-05-23 16:57:22 
 """
import heapq
import math

# dijkstra's algorithm is to get the shortest path from source to destination vertex.
# dijkstra's algorithm 是求图的最短路径的算法。
graph = {
    "A": {
        "B": 5,
        "C": 2
    },
    "B": {
        "A": 5,
        "C": 2,
        "D": 1
    },
    "C": {
        "A": 2,
        "B": 2,
        "D": 8,
        "E": 2
    },
    "D": {
        "B": 1,
        "C": 8,
        "E": 4,
        "F": 9
    },
    "E": {
        "C": 2,
        "D": 4
    },
    "F": {
        "D": 9
    }
}


def dijkstar(s):
    """
    In dijkstar, we need four structures to store the process.
    pq: this is a priority queue, it is the core of the process which stores (height, vertex, parent) of every vertex.
    distance: this is a map which store the result (destination, length)
    parent: to store the path, the pre-step of every vertex.
    seen: to store the result of every destination vertex. when vertex is popped, then it will be stored.
    """
    pq = []
    distance = {}
    parent = {}
    seen = set()

    # first we push the source vertex.
    heapq.heappush(pq, (0, s, None))
    while len(pq) != 0:
        # then we pop the shortest one
        vertex = heapq.heappop(pq)

        # update parent, distance and seen.
        if vertex[1] not in seen:
            seen.add(vertex[1])
            parent[vertex[1]] = vertex[2]
            distance[vertex[1]] = vertex[0]

        # and push all of its neighboors in the pq.(height, vertex, parent), ignore those vertexes that have been seen.
        for item in graph[vertex[1]].keys():
            if item not in seen:
                heapq.heappush(
                    pq, (graph[vertex[1]][item] + vertex[0], item, vertex[1]))
    return parent, distance


if __name__ == "__main__":
    parent, distance = dijkstar("A")
    print(parent)
    print(distance)