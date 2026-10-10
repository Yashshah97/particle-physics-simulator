"""
Configuration management for simulation parameters.

This module provides a simple dataclass-based configuration management system,
allowing users to easily configure the simulator with various parameters.
"""

import dataclasses
from typing import Optional

@dataclasses.dataclass(frozen=True)
class SimulationConfig:
    """
    Configuration for the particle physics simulator.

    Attributes:
        num_particles (int): The number of particles in the simulation.
        collision_threshold (float): The threshold energy required for a collision to occur.
        seed (Optional[int]): A random seed for reproducibility. If None, a random seed will be generated.
        time_step (float): The time step size for each iteration.
    """
    num_particles: int
    collision_threshold: float
    seed: Optional[int]
    time_step: float

@dataclasses.dataclass(frozen=True)
class CollisionConfig:
    """
    Configuration for the collision event data.

    Attributes:
        output_file (str): The file path to write the collision event data.
        format (str): The format of the output file. Currently only supports 'csv'.
    """
    output_file: str
    format: str

@dataclasses.dataclass(frozen=True)
class SimulatorConfig:
    """
    Configuration for the simulation engine.

    Attributes:
        simulation_config (SimulationConfig): The configuration for the simulation.
        collision_config (CollisionConfig): The configuration for the collision event data.
    """
    simulation_config: SimulationConfig
    collision_config: CollisionConfig

def get_default_config() -> SimulatorConfig:
    """
    Returns a default simulator configuration.

    This method returns a default configuration with reasonable values for the simulation and collision event data.
    """
    return SimulatorConfig(
        simulation_config=SimulationConfig(num_particles=1000, collision_threshold=1.0, seed=None, time_step=0.01),
        collision_config=CollisionConfig(output_file='collision_data.csv', format='csv')
    )
