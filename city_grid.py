import random
from matplotlib import pyplot as plt
from collections import deque


class CityGrid:
    def __init__(self, n: int, m: int, block_percentage) -> None:
        self.n = n
        self.m = m
        self.grid = [[0] * m for _ in range(n)]

        # Placement of blocked
        num_blocks = int(n * m * block_percentage)
        blocked_positions = random.sample(range(n * m), num_blocks)
        for position in blocked_positions:
            row = position // m
            col = position % m
            self.grid[row][col] = 1

    # Placement of the tower and visualization
    def place_tower(self, row: int, col: int, radius: int) -> None:
        for r in range(max(0, row - radius), min(self.n, row + radius + 1)):
            for c in range(max(0, col - radius), min(self.m, col + radius + 1)):
                self.grid[r][c] = 'X'

    # sorting towers with the largest coverage of blocks
    def count_neighbors(self) -> list:
        matrix = self.grid
        rows = len(matrix)
        cols = len(matrix[0])
        radius = 1
        neighbors = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    count = 0
                    for x in range(max(0, i - radius), min(rows, i + radius + 1)):
                        for y in range(max(0, j - radius), min(cols, j + radius + 1)):
                            if matrix[x][y] != 1 and matrix[x][y] != 'r' and matrix[x][y] != 'T' and (x != i or y != j):
                                count += 1
                    neighbors.append((i, j, count))
        neighbors.sort(key=lambda x: x[2], reverse=True)

        return neighbors

    # Algorithm for adding a new tower to the grid
    def render_matrix(self) -> list:
        matrix = self.grid

        rows = len(matrix)
        cols = len(matrix[0])
        radius = 1

        list_neighbors = self.count_neighbors()
        first_neighbors = list_neighbors[0]

        x = first_neighbors[0]
        y = first_neighbors[1]
        matrix[x][y] = 'T'
        for i in range(x - radius, x + radius + 1):
            for j in range(y - radius, y + radius + 1):
                if 0 <= i < rows and 0 <= j < cols and matrix[i][j] == 0:
                    matrix[i][j] = 'r'
        return matrix

    # Algorithm for finding the smallest path between towers
    def find_path(self, start: tuple, end: tuple) -> deque:
        matrix = self.grid
        visited = []
        queue = deque()
        queue.append((start, []))

        while queue:
            point, path = queue.popleft()

            if point == end:
                return path

            if point in visited:
                continue

            visited.append(point)

            x, y = point
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

            for neighbor in neighbors:
                nx, ny = neighbor

                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] != 0 and neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return queue

    # Plotting
    def visualize_city(self, tower_positions=None, path=None) -> None:
        fig, ax = plt.subplots()

        # Visualize obstructed blocks
        for i in range(self.n):
            for j in range(self.m):
                if self.grid[i][j] == 1:
                    ax.add_patch(plt.Rectangle((j, self.n - i - 1), 1, 1, color="green"))
                if self.grid[i][j] == 0:
                    ax.add_patch(plt.Rectangle((j, self.n - i - 1), 1, 1, color="black"))
                if self.grid[i][j] == 'T':
                    ax.add_patch(plt.Rectangle((j, self.n - i - 1), 1, 1, color="yellow"))
                if self.grid[i][j] == 'r':
                    ax.add_patch(plt.Rectangle((j, self.n - i - 1), 1, 1, color="gray"))

        # Visualize towers
        if tower_positions:
            for tower in tower_positions:
                row, col = tower
                ax.add_patch(plt.Rectangle((col, self.n - row - 1), 1, 1, color="blue"))

        # Visualize path
        if path:
            for i in range(len(path) - 1):
                tower1 = path[i]
                tower2 = path[i + 1]
                row1, col1 = tower1
                row2, col2 = tower2
                plt.plot(
                    [col1 + 0.5, col2 + 0.5],
                    [self.n - row1 - 0.5, self.n - row2 - 0.5],
                    color="red",
                )

        ax.set_aspect("equal")
        ax.set_xlim(0, self.n)
        ax.set_ylim(0, self.m)
        plt.gca()

        ax.set_title("City grid")
        ax.set_xlabel("rows")
        ax.set_ylabel("columns")

        plt.show()

    # Drawing the grid
    def visualize_grid(self) -> None:
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))

    # Counting unprotected blocks
    def count_zeros(self) -> int:
        matrix = self.grid
        count = 0

        for row in matrix:
            for element in row:
                if element == 0:
                    count += 1

        return count
