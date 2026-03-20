from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from seed_scaffold.config import get_config_dir, get_config_path, load_config


class ConfigTests(unittest.TestCase):
    def test_config_dir_exists(self) -> None:
        config_dir = get_config_dir()
        # Config dir may not exist yet, so we just check it's a valid path
        self.assertIsInstance(config_dir, Path)

    def test_config_path(self) -> None:
        config_path = get_config_path()
        self.assertEqual(config_path, get_config_dir() / "config.toml")

    def test_load_config_empty(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.toml"
            config_path.write_text("")
            config = load_config()
            self.assertEqual(config, {})

    def test_load_config_valid(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            # Temporarily override the config path
            original_path = get_config_path()
            try:
                config_path = Path(temp_dir) / "config.toml"
                config_path.write_text(
                    """
[defaults]
author = "Test Author"
year = 2025
template = "meson-c-lib"
"""
                )
                # Monkey-patch the config path for this test
                import seed_scaffold.config as config_module
                config_module.get_config_path = lambda: config_path
                
                config = load_config()
                self.assertEqual(config["defaults"]["author"], "Test Author")
                self.assertEqual(config["defaults"]["year"], 2025)
                self.assertEqual(config["defaults"]["template"], "meson-c-lib")
            finally:
                # Restore original function
                import seed_scaffold.config as config_module
                config_module.get_config_path = lambda: original_path

    def test_load_config_invalid(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            config_path = Path(temp_dir) / "config.toml"
            config_path.write_text("invalid toml content [[[")
            config = load_config()
            self.assertEqual(config, {})


if __name__ == "__main__":
    unittest.main()
