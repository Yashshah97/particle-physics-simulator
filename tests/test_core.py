import unittest
from particle_physics_simulator import core

class TestParticlePhysicsSimulator(unittest.TestCase):

    def test_run_simulation(self):
        num_particles = 5
        seed = 42
        result = core.run_simulation(num_particles, seed)
        self.assertEqual(len(result), 10)

    def test_run_simulation_no_seed(self):
        num_particles = 5
        result = core.run_simulation(num_particles)
        self.assertIsNotNone(core.ParticlePhysicsSimulator(1).simulate())

if __name__ == '__main__':
    unittest.main()
