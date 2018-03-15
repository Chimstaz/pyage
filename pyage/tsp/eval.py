"""Evaluator."""
import logging

from pyage.core.operator import Operator
from pyage.tsp.genotype import TSPGenotype

logger = logging.getLogger(__name__)


class TSPEvaluator(Operator):
    """."""

    def __init__(self):
        """."""
        super(TSPEvaluator, self).__init__(TSPGenotype)

    def process(self, population):
        """Run function in TSPGenotype object."""
        for genotype in population:
            genotype.calculate_fitness()
