"""Mutation."""
import logging
import random

from pyage.elect.el_mutation import AbstractMutation
from pyage.tsp.genotype import TSPGenotype

logger = logging.getLogger(__name__)


class TSPRandomMutation(AbstractMutation):
    """."""

    def __init__(self, probability):
        """."""
        super(TSPRandomMutation, self).__init__(TSPGenotype, probability)

    def mutate(self, genotype):
        """Change position of random city in the order."""
        logger.debug("Random mutation of {0}".format(str(genotype)))

        n = len(genotype.inverse_seq)
        point = random.randint(0, n - 1)
        genotype.inverse_seq[point] = random.randint(0, n - point - 1)
