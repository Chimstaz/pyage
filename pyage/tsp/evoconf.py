"""."""
import logging

import datetime

from pyage.core import address
from pyage.core.agent.agent import generate_agents, Agent
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.solutions.evolution.selection import TournamentSelection
from pyage.elect.naming_service import NamingService
from pyage.tsp.crossover import TSPMultiplePointCrossover
from pyage.tsp.eval import TSPEvaluator
from pyage.tsp.mutation import TSPRandomMutation
from pyage.tsp.initializer import TSPInitializer

logger = logging.getLogger(__name__)

number_of_points_in_mutation = 20
agents_count = 50
stop_condition = lambda: StepLimitStopCondition(2000)

logger.debug("Evolutionary, %s agents", agents_count)
agents = generate_agents("agent", agents_count, Agent)

size = 80
population_size = 80
operators = lambda: [TSPEvaluator(),
                     TournamentSelection(size=20, tournament_size=20),
                     TSPMultiplePointCrossover(size=size, number_of_points=number_of_points_in_mutation), TSPRandomMutation(0.1)]
initializer = lambda: TSPInitializer(population_size=population_size, filename="in/cities.txt")

address_provider = address.SequenceAddressProvider

migration = ParentMigration
locator = GridLocator

stats = lambda: StepStatistics('out/fitness_{}_{}_RandomMutation_{}_PointCrossover_{}-{}.txt'.format(__name__, datetime.datetime.now(), number_of_points_in_mutation, agents_count, size))

naming_service = lambda: NamingService(starting_number=4)
