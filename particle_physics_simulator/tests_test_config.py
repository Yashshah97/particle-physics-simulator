"""
Unit tests for configuration management.

This module contains unit tests for the `particle_physics_simulator` package's configuration management functionality.
"""

import sys
from unittest import TestCase
from tempfile import TemporaryDirectory
from typing import Dict, List

class TestConfig(TestCase):
    def test_default_config(self) -> None:
        """
        Verify that the default configuration is correctly generated.

        This test checks that the default configuration has the expected values for all parameters.
        """
        from particle_physics_simulator.config import DEFAULT_CONFIG
        self.assertEqual(DEFAULT_CONFIG["num_particles"], 100)
        self.assertEqual(DEFAULT_CONFIG["seed"], 42)

    def test_config_from_dict(self) -> None:
        """
        Verify that a configuration can be created from a dictionary.

        This test checks that creating a configuration from a dictionary results in the expected configuration.
        """
        config = {"num_particles": 50, "seed": 13}
        from particle_physics_simulator.config import Config
        self.assertEqual(Config(**config).to_dict(), config)

    def test_config_from_file(self) -> None:
        """
        Verify that a configuration can be created from a file.

        This test checks that creating a configuration from a file results in the expected configuration.
        """
        with TemporaryDirectory() as temp_dir:
            config_path = f"{temp_dir}/config.json"
            import json
            with open(config_path, "w") as f:
                json.dump({"num_particles": 75, "seed": 27}, f)
            from particle_physics_simulator.config import Config
            self.assertEqual(Config.from_file(config_path).to_dict(), {"num_particles": 75, "seed": 27})

    def test_config_to_file(self) -> None:
        """
        Verify that a configuration can be written to a file.

        This test checks that writing a configuration to a file results in the expected file contents.
        """
        with TemporaryDirectory() as temp_dir:
            config_path = f"{temp_dir}/config.json"
            from particle_physics_simulator.config import Config
            config = Config(num_particles=25, seed=11)
            config.to_file(config_path)
            import json
            with open(config_path, "r") as f:
                self.assertEqual(json.load(f), {"num_particles": 25, "seed": 11})

if __name__ == "__main__":
    sys.exit(unittest.main())
