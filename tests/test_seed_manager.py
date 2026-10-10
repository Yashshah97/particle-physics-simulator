"""Smoke tests for seed_manager."""
import unittest

from particle_physics_simulator import seed_manager


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(seed_manager, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(seed_manager) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
