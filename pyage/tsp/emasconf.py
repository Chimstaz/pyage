"""Config for emas."""
import logging

import datetime
# import os
# import Pyro4

from pyage.core import address
from pyage.core.agent.aggregate import AggregateAgent
from pyage.core.emas import EmasService
from pyage.core.locator import GridLocator
from pyage.core.migration import ParentMigration
# from pyage.core.migration import Pyro4Migration
# from pyage.core.stats.distributed import GlobalStepStatistics
from pyage.core.stats.gnuplot import StepStatistics
from pyage.core.stop_condition import StepLimitStopCondition
from pyage.elect.el_init import root_agents_factory
from pyage.elect.naming_service import NamingService
from pyage.tsp.crossover import TSPMultiplePointCrossover
from pyage.tsp.eval import TSPEvaluator
from pyage.tsp.mutation import TSPRandomMutation
from pyage.tsp.initializer import EmasInitializer

logger = logging.getLogger(__name__)

number_of_points_in_mutation = 20
agents_count = 50
stop_condition = lambda: StepLimitStopCondition(2000)

logger.debug("EMAS, %s agents", agents_count)
agents = root_agents_factory(agents_count, AggregateAgent)

agg_size = 80
aggregated_agents = EmasInitializer("in/cities.txt", size=agg_size, energy=40)

emas = EmasService

minimal_energy = lambda: 10
reproduction_minimum = lambda: 100
migration_minimum = lambda: 120
newborn_energy = lambda: 100
transferred_energy = lambda: 40

budget = 0
evaluation = lambda: TSPEvaluator()
crossover = lambda: TSPMultiplePointCrossover(size=agg_size, number_of_points=number_of_points_in_mutation)
mutation = lambda: TSPRandomMutation(probability=0.1)


def simple_cost_func(x):
    """."""
    return abs(x) * 10


address_provider = address.SequenceAddressProvider

migration = ParentMigration
# migration = Pyro4Migration
# ns_hostname = lambda: os.environ['NS_HOSTNAME']
# pyro_daemon = Pyro4.Daemon()
# daemon = lambda: pyro_daemon
locator = GridLocator

stats = lambda: StepStatistics('out/fitness_{}_{}_RandomMutation_{}_PointCrossover_{}-{}.txt'.format(__name__, datetime.datetime.now(), number_of_points_in_mutation, agents_count, agg_size))

naming_service = lambda: NamingService(starting_number=4)
