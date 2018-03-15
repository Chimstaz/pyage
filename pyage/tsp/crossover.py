"""Crossover."""
import logging
import random

from pyage.elect.el_crossover import AbstractCrossover
from pyage.tsp.genotype import TSPGenotype, pairwise

logger = logging.getLogger(__name__)


class TSPSinglePointCrossover(AbstractCrossover):
    """Simple SinglePointCrossover for TSPGenotype."""

    def __init__(self, size):
        """."""
        super(TSPSinglePointCrossover, self).__init__(TSPGenotype, size)

    def cross(self, p1, p2):
        """."""
        crossingPoint = random.randint(1, len(p1.inverse_seq))

        logger.debug("Crossing {0} and {1} at point {2}".format(str(p1), str(p2), crossingPoint))

        return TSPGenotype(p1.world, p1.inverse_seq[:crossingPoint] + p2.inverse_seq[crossingPoint:])


class TSPMultiplePointCrossover(AbstractCrossover):
    """Corssover in multiple points."""

    def __init__(self, size, number_of_points):
        """."""
        super(TSPMultiplePointCrossover, self).__init__(TSPGenotype, size)
        self.number_of_points = number_of_points

    def cross(self, p1, p2):
        """."""
        new_inverse_seq = []

        crossingPoints = [0] + random.sample(range(len(p1.inverse_seq)), self.number_of_points) + [len(p1.inverse_seq)]
        crossingPoints.sort()

        logger.debug("Crossing {0} and {1} at point {2}".format(str(p1), str(p2), crossingPoints))

        for i, (x, y) in enumerate(pairwise(crossingPoints)):
            if i % 2 == 0:
                new_inverse_seq.extend(p1.inverse_seq[x:y])
            else:
                new_inverse_seq.extend(p2.inverse_seq[x:y])

        return TSPGenotype(p1.world, new_inverse_seq)
