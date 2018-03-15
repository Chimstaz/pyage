"""Genotype."""
import random
from itertools import tee


class TSPGenotype(object):
    """This genotype is compatible with methode described here: http://user.ceng.metu.edu.tr/~ucoluk/research/publications/tspnew.pdf ."""

    def __init__(self, world, inverse_seq=None, order=None):
        """Init genotype.

        Arguments:
            world -- contain number_of_cities and function to get distance between two cities (cities are numbered from 0 to number_of_cities - 1)
            inverse_seq -- (optional) permutation described as number of elements greater then i-th element on left from there
            order -- (optional) i
        """
        self.world = world
        self.inverse_seq = inverse_seq
        self.order = order
        self.fitness = None
        self.calculate_fitness()

    def __str__(self):
        """To str."""
        return "TSPGenotype{order=" + str(self.order) + ", fitness=" + str(self.fitness) + "}"

    def calculate_fitness(self):
        """Calculate fitness from order, If order not defined try to obtain it from inverse_seq."""
        if self.fitness is None:
            if self.order is None:
                self.calculate_order()

            fitness = 0
            for index1, index2 in pairwise(self.order):
                fitness -= self.world.get_distance(index1, index2)
            self.fitness = fitness

    def calculate_order(self):
        """Calculate order from inverse_seq if available. If not then generate inverse_seq."""
        if self.inverse_seq is None:
            self.generate_random_inverse_seq()
        n = self.world.number_of_cities
        self.order = [0] * n
        pos = list(range(n))

        for c, o in enumerate(self.inverse_seq):
            self.order[pos[o]] = c
            del pos[o]

    def calculate_inverse_seq(self):
        """Calculate inverse_seq from order. If not available then generate random."""
        if self.order is None:
            self.generate_random_inverse_seq()
            return
        n = self.world.number_of_cities

        self.inverse_seq = []
        for i in range(n):
            j = 0
            greater_on_left = 0
            while self.order[j] != i:
                if self.order[j] > i:
                    greater_on_left += 1
                j += 1
            self.inverse_seq.append(greater_on_left)

    def generate_random_inverse_seq(self):
        """Generate random genotype."""
        n = self.world.number_of_cities
        self.inverse_seq = []
        for i in range(n):
            self.inverse_seq.append(random.randint(0, n - i - 1))


def pairwise(iterable):
    """. s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
