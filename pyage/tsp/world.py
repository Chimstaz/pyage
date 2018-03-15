"""World."""
import math


class WorldOnList:
    """Contains description of cities map."""

    def __init__(self, cities):
        """First argument is list of pairs. Each pair represents coordinates of city."""
        self.number_of_cities = len(cities)
        self.distance_matrix = [[0.0] * self.number_of_cities for _ in range(self.number_of_cities)]
        for i, (x1, y1) in enumerate(cities):
            for j, (x2, y2) in enumerate(cities):
                self.distance_matrix[i][j] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                self.distance_matrix[j][i] = self.distance_matrix[i][j]

    def get_distance(self, c1, c2):
        """Return distance between cities."""
        return self.distance_matrix[c1][c2]
