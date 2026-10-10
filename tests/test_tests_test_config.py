import unittest
from particle_physics_simulator import tests_test_config

class TestTestConfig(unittest.TestCase):
    def test_default_config(self) -> None:
        self.assertEqual(tests_test_config.DEFAULT_CONFIG["num_particles"], 100)
        self.assertEqual(tests_test_config.DEFAULT_CONFIG["seed"], 42)

    def test_config_from_dict(self) -> None:
        config = {"num_particles": 50, "seed": 13}
        self.assertEqual(tests_test_config.Config(**config).to_dict(), config)

    def test_config_from_file(self) -> None:
        with unittest.mock.patch('tempfile.TemporaryDirectory'):
            with unittest.mock.patch('json.dump') as mock_dump:
                tests_test_config.test_config_from_file()
                mock_dump.assert_called_once_with({"num_particles": 75, "seed": 27}, any())

    def test_config_to_file(self) -> None:
        with unittest.mock.patch('tempfile.TemporaryDirectory'):
            tests_test_config.test_config_to_file()

if __name__ == "__main__":
    unittest.main()
