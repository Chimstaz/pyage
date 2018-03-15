"""."""
from pyage.core.emas import EmasAgent
from pyage.core.inject import Inject
from pyage.core.operator import Operator
from pyage.tsp.world import WorldOnList
from pyage.tsp.genotype import TSPGenotype


class EmasInitializer(object):
    """."""

    def __init__(self, filename, energy, size):
        """."""
        self.filename = filename
        self.world = initialize_world(self.filename)
        self.energy = energy
        self.size = size

    @Inject("naming_service")
    def __call__(self):
        """."""
        agents = {}
        for i in range(self.size):
            agent = EmasAgent(TSPGenotype(self.world), self.energy,
                              self.naming_service.get_next_agent())
            agents[agent.get_address()] = agent
        return agents


def initialize_world(filename):
    """."""
    cities = []
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            x, y = l.split()
            cities.append((int(x), int(y)))
    return WorldOnList(cities)


class TSPInitializer(Operator):
    def __init__(self, population_size=1000, filename=None):
        super(TSPInitializer, self).__init__(TSPGenotype)
        self.size = population_size
        if filename:
            self.world = initialize_world(filename)
            self.population = [TSPGenotype(self.world) for _ in range(self.size)]

    def __call__(self, *args, **kwargs):
        return self.population

    def process(self, population):
        for i in range(self.size):
            population.append(self.population[i])
