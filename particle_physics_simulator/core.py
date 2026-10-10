"""
Particle Physics Simulation Engine - Core Module

This module contains the main domain logic and public entry points for the simulation engine.

Classes:
    ParticlePhysicsSimulator: A step-based simulator with configurable parameters.
"""

import random
from typing import Dict, List

class ParticlePhysicsSimulator:
    """
    A step-based simulator with configurable parameters.

    Attributes:
        num_particles (int): The number of particles in the simulation.
        seed (int): The random seed for reproducibility.
        time_step (float): The time step size for each simulation step.
        collision_threshold (float): The threshold for particle collisions.
    """

    def __init__(self, num_particles: int, seed: int = None, time_step: float = 1.0,
                 collision_threshold: float = 0.5):
        """
        Initialize the simulator with configurable parameters.

        Args:
            num_particles (int): The number of particles in the simulation.
            seed (int, optional): The random seed for reproducibility. Defaults to None.
            time_step (float, optional): The time step size for each simulation step. Defaults to 1.0.
            collision_threshold (float, optional): The threshold for particle collisions. Defaults to 0.5.
        """
        self.num_particles = num_particles
        if seed is not None:
            random.seed(seed)
        self.time_step = time_step
        self.collision_threshold = collision_threshold

    def simulate(self) -> List[Dict]:
        """
        Run the simulation and return a list of particle positions after each step.

        Returns:
            List[Dict]: A list of dictionaries containing particle positions at each step.
        """
        particles = [{'x': random.uniform(-1, 1), 'y': random.uniform(-1, 1)} for _ in range(self.num_particles)]
        steps = []

        for _ in range(10):  # Simulate for 10 steps
            new_particles = []
            for particle in particles:
                if random.random() < self.collision_threshold:
                    new_particle = {'x': particle['x'] + random.uniform(-1, 1),
                                    'y': particle['y'] + random.uniform(-1, 1)}
                else:
                    new_particle = particle
                new_particles.append(new_particle)
            steps.append(new_particles)
            particles = new_particles

        return steps

def run_simulation(num_particles: int, seed: int = None) -> List[Dict]:
    """
    Run the simulation with configurable parameters.

    Args:
        num_particles (int): The number of particles in the simulation.
        seed (int, optional): The random seed for reproducibility. Defaults to None.

    Returns:
        List[Dict]: A list of dictionaries containing particle positions at each step.
    """
    simulator = ParticlePhysicsSimulator(num_particles, seed=seed)
    return simulator.simulate()
