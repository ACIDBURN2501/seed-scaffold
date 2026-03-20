# User Configuration

This document describes the user configuration file format and available options.

## Configuration File

The tool supports configuration files in multiple locations:

1. Primary location: `~/.seed-scaffold/config.toml`
2. User-specific location: `~/.config/seed-scaffold/user.conf`

The user-specific location (`~/.config/seed-scaffold/user.conf`) takes precedence over the primary location, allowing you to have project-specific configurations while maintaining a global default configuration.

## Example Configuration

```toml
[defaults]
# Default author name for copyright headers
author = "Jane Developer"

# Default copyright year
# If not specified, the current year is used
year = 2024

# Default template to use
# If not specified, the default template (meson-c-lib) is used
template = "meson-c-lib"

# Default build type for generated projects
# Used in next steps output
build_type = "debug"

# Default options for meson build
[defaults.meson]
# Whether to build tests by default
build_tests = true

# Default options for project generation
[defaults.project]
# Default license type (e.g., "MIT", "Apache-2.0")
license = "MIT"

# Default programming language
language = "c"
```

## Example Configuration

```toml
[defaults]
# Default author name for copyright headers
author = "Jane Developer"

# Default copyright year
# If not specified, the current year is used
year = 2024

# Default template to use
# If not specified, the default template (meson-c-lib) is used
template = "meson-c-lib"

# Default build type for generated projects
# Used in next steps output
build_type = "debug"

# Default options for meson build
[defaults.meson]
# Whether to build tests by default
build_tests = true

# Default options for project generation
[defaults.project]
# Default license type (e.g., "MIT", "Apache-2.0")
license = "MIT"

# Default programming language
language = "c"
```

## Configuration Priority

Command-line arguments always take precedence over configuration file values.

## Supported Keys

### `[defaults]` Section

- `author` (string): Default copyright holder name
- `year` (integer): Default copyright year
- `template` (string): Default template ID
- `build_type` (string): Default build type (debug/release)

### `[defaults.meson]` Section

- `build_tests` (boolean): Whether to enable tests by default

### `[defaults.project]` Section

- `license` (string): Default license type
- `language` (string): Default programming language

## Usage

Create the configuration file at `~/.seed-scaffold/config.toml`:

```bash
mkdir -p ~/.seed-scaffold
cat > ~/.seed-scaffold/config.toml << 'EOF'
[defaults]
author = "Your Name"
year = 2024
EOF
```

Then use the tool as normal - the configuration will be automatically applied.
