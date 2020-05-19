# first, we should create the graph, the key is a vertex, but the values is the vertexs which connect with the key
# 首先我们需要创建一个图, 字典的key就是一个节点，节点的值就是这个与这个节点相连的节点
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["E"]
}


def DFS(start):
    """
    For DFS we should use stack consturcture.
    对于深度优先算法，我们可以使用stack来实现
    """
    stack = []
    # create a stack and input the start vertex, 创建一个队列把起始节点添加进去
    stack.append(start)
    # create a set to store the vertexes which have been seen and putted in the stack
    # 创建一个集合来保存那些我们已经访问并添加到队列里的节点。
    seen = set()
    seen.add(start)
    # in evey round loop, we should pop the fist item, and put the vertexes which connect with it in the stack.
    # if we have seen the vertex, we will drop it.
    # 每一次的循环，我们需要pop出第一个进入的元素，然后把与他相连的其他节点都添加到 satck 中，如果有些节点我们已经访问过了，就直接舍弃不再重复添加
    while len(stack) != 0:
        vertex = stack.pop()
        for v in graph[vertex]:
            if v not in seen:
                stack.append(v)
                seen.add(v)
        print(vertex)


if __name__ == "__main__":
    DFS("A")