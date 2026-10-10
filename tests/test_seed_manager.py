import unittest
from particle_physics_simulator import seed_manager

class TestSeedManager(unittest.TestCase):
    def test_seed_manager_init(self):
        manager = seed_manager.SeedManager()
        self.assertGreaterEqual(manager.seed, 0)
        self.assertLessEqual(manager.seed, 2**32 - 1)

    def test_seed_manager_get_seed(self):
        manager = seed_manager.SeedManager(12345)
        self.assertEqual(manager.get_seed(), 12345)

    def test_seed_manager_set_seed(self):
        manager = seed_manager.SeedManager()
        manager.set_seed(67890)
        self.assertEqual(manager.get_seed(), 67890)

    def test_seed_manager_reset_seed(self):
        manager = seed_manager.SeedManager(12345)
        manager.reset_seed()
        self.assertNotEqual(manager.get_seed(), 12345)

    def test_set_global_seed(self):
        original_seed = random.randint(0, 2**32 - 1)
        seed_manager.set_global_seed(67890)
        new_random = random.randint(0, 2**32 - 1)
        random.seed(original_seed)
        self.assertNotEqual(new_random, random.randint(0, 2**32 - 1))

if __name__ == '__main__':
    unittest.main()
