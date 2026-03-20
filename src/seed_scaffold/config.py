"""User configuration handling."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def get_config_dir() -> Path:
    """Return the user configuration directory."""
    return Path(os.path.expanduser("~/.seed-scaffold"))


def get_config_path() -> Path:
    """Return the path to the user configuration file."""
    return get_config_dir() / "config.toml"


def get_user_config_path() -> Path:
    """Return the path to the user configuration file in ~/.config."""
    return Path(os.path.expanduser("~/.config/seed-scaffold/user.conf"))


def load_config() -> dict[str, Any]:
    """Load user configuration from disk."""
    config_path = get_config_path()
    user_config_path = get_user_config_path()
    
    # Load from primary config location
    config = {}
    if config_path.exists():
        try:
            with config_path.open("rb") as f:
                config = tomllib.load(f)
        except (tomllib.TOMLDecodeError, OSError) as exc:
            print(f"Warning: Failed to load config file {config_path}: {exc}")
    
    # Load from user config location if it exists
    if user_config_path.exists():
        try:
            with user_config_path.open("rb") as f:
                user_config = tomllib.load(f)
                # Merge user config with existing config
                # User config takes precedence
                config = merge_configs(config, user_config)
        except (tomllib.TOMLDecodeError, OSError) as exc:
            print(f"Warning: Failed to load user config file {user_config_path}: {exc}")
    
    return config


def merge_configs(old_config: dict[str, Any], new_config: dict[str, Any]) -> dict[str, Any]:
    """Merge two configuration dictionaries, with new_config taking precedence."""
    result = old_config.copy()
    
    for key, value in new_config.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # Recursively merge nested dictionaries
            result[key] = merge_configs(result[key], value)
        else:
            # Overwrite with new value
            result[key] = value
    
    return result


def get_default_value(key_path: list[str], config: dict[str, Any]) -> Any:
    """Get a default value from the configuration using a dot-separated key path."""
    value = config
    for key in key_path:
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value
