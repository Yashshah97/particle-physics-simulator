"""
Module for reproducible seed management in particle physics simulations.

This module provides a class for generating and managing seeds used in the simulation.
The goal is to ensure that simulations can be reproduced with the same results by using
the same seed value. This is particularly important when analyzing or comparing simulation
results.
"""

import random

class SeedManager:
    """
    Class for managing seeds used in particle physics simulations.

    Attributes:
        seed (int): The current seed value.
    """

    def __init__(self, seed=None):
        """
        Initialize the SeedManager with a given seed value.

        If no seed is provided, a random one will be generated.

        Args:
            seed (int): The initial seed value. Defaults to None.
        """
        if seed is not None:
            self.seed = seed
        else:
            self.seed = random.randint(0, 2**32 - 1)

    def get_seed(self):
        """
        Get the current seed value.

        Returns:
            int: The current seed value.
        """
        return self.seed

    def set_seed(self, new_seed):
        """
        Set a new seed value for the simulation.

        Args:
            new_seed (int): The new seed value to use.
        """
        self.seed = new_seed

    def reset_seed(self):
        """
        Reset the seed to its initial value.
        """
        self.seed = random.randint(0, 2**32 - 1)

def set_global_seed(seed):
    """
    Set the global seed for all SeedManager instances.

    This is a convenience function to ensure that all simulations use the same seed
    value. Note that this should only be used when setting up the simulation environment,
    not within the simulation itself.

    Args:
        seed (int): The new global seed value.
    """
    random.seed(seed)

# Example usage:
seed_manager = SeedManager()
print("Initial seed:", seed_manager.get_seed())
seed_manager.set_seed(12345)
print("Seed after setting:", seed_manager.get_seed())
