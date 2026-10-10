"""Smoke tests for tests_test_config."""
import unittest

from particle_physics_simulator import tests_test_config


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(tests_test_config, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(tests_test_config) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
