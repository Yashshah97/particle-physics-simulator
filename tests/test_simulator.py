import unittest
from particle_physics_simulator import simulator

class TestSimulator(unittest.TestCase):
    def test_init(self):
        simulator.Simulator(10, 5)
        self.assertEqual(simulator.Simulator(10, 5).num_particles, 10)

    def test_step(self):
        simulator = simulator.Simulator(1, 1)
        with unittest.mock.patch.object(simulator.rng, 'randint') as mock_randint:
            simulator.step()
            mock_randint.assert_called_once()

    def test_run(self):
        simulator = simulator.Simulator(10, 5)
        with unittest.mock.patch.object(simulator, 'step') as mock_step:
            simulator.run()
            self.assertEqual(mock_step.call_count, 5)

if __name__ == '__main__':
    unittest.main()
