"""Smoke tests for simulator."""
import unittest

from particle_physics_simulator import simulator


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(simulator, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(simulator) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
