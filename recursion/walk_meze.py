"""
 * @Author: TuffyTian 
 * @Date: 2020-06-06 17:56:10 
 * @Last Modified by:   TuffyTian 
 * @Last Modified time: 2020-06-06 17:56:10 
"""
"""
这是一个走迷宫的问题. 运用递归的方式解决
"""

maze = [[0 for i in range(10)] for i in range(10)]
for j in range(10):
    maze[0][j] = 1
    maze[9][j] = 1

for i in range(10):
    maze[i][0] = 1
    maze[i][9] = 1

maze[5][0] = 1
maze[5][1] = 1
maze[5][2] = 1
maze[6][6] = 1


# start: where we start to walk the maze
# end: where we stop to walk the maze
# the value of the matrix:
# 1: represent the wall. 2: represent the point we have passed. 3: represent the point that can't get to end point
# 1代表墙。 2 代表我们走过的点。 3 代表不能通往终点的点
def walk_maze(maze, start: (int, int), end: (int, int)):
    # The condition fo ending this recursion is when we get the end point.
    # 结束的递归的条件。如果终点的值为2 我们就结束递归
    if maze[end[0]][end[1]] == 2:
        return True
    else:
        if maze[start[0]][start[1]] == 0:
            # 假设我们走这一个点， 我们看接下来我们是不是可以到终点
            maze[start[0]][start[1]] = 2
            # 定制好策略 先右， 下， 左， 上
            # right
            if walk_maze(maze, (start[0], start[1]+1), end):
                return True
            # down
            elif walk_maze(maze, (start[0]+1, start[1]), end):
                return True
            # left
            elif walk_maze(maze, (start[0], start[1]-1), end):
                return True
            # up
            elif walk_maze(maze, (start[0] - 1, start[1]), end):
                return True
            else:
                maze[start[0]][start[1]] = 3
                return False
        else:
            return False


if __name__ == "__main__":
    walk_maze(maze, (1, 1), (8, 8))
    for i in range(10):
        for j in range(10):
            print(maze[i][j], end="")
        print()
