import unittest
from particle_physics_simulator import config

class TestConfig(unittest.TestCase):
    def test_get_default_config(self):
        default_config = config.get_default_config()
        self.assertIsInstance(default_config, config.SimulatorConfig)
        self.assertEqual(default_config.simulation_config.num_particles, 1000)
        self.assertEqual(default_config.collision_config.output_file, 'collision_data.csv')

    def test_simulation_config_attributes(self):
        simulation_config = config.SimulationConfig(num_particles=1000, collision_threshold=1.0, seed=None, time_step=0.01)
        self.assertEqual(simulation_config.num_particles, 1000)
        self.assertEqual(simulation_config.collision_threshold, 1.0)
        self.assertIsNone(simulation_config.seed)
        self.assertEqual(simulation_config.time_step, 0.01)

    def test_collision_config_attributes(self):
        collision_config = config.CollisionConfig(output_file='collision_data.csv', format='csv')
        self.assertEqual(collision_config.output_file, 'collision_data.csv')
        self.assertEqual(collision_config.format, 'csv')

if __name__ == '__main__':
    unittest.main()
