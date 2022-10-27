from collections import deque

class Graphs:
    # Count Paths, Backtracking
    def dfs(grid, r, c, visit):
        ROWS, COLS = len(grid), len(grid[0])
        if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == 1):
            return 0
        if r == ROWS - 1 and c == COLS - 1:
            return 1

        visit.add((r, c))

        count = 0
        count += Graphs.dfs(grid, r + 1, c, visit)
        count += Graphs.dfs(grid, r - 1, c, visit)
        count += Graphs.dfs(grid, r, c + 1, visit)
        count += Graphs.dfs(grid, r, c - 1, visit)

        visit.remove((r, c))
        return count

    # Shortest path from top left to bottom right
    def bfs(grid):
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        queue.append((0, 0))
        visit.add((0, 0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or
                            r + dr == ROWS or c + dc == COLS or
                            (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))
            length += 1

if __name__ == '__main__':
    # Matrix
    grid = [[0, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]]

    # Adjacency matrix
    adjMatrix = [[0, 0, 0, 0],
                 [1, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 1, 0, 0]]

    print(Graphs.dfs(grid, 0, 0, set()))
    print(Graphs.bfs(grid))