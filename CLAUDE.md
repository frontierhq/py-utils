# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

py-utils is a Python utility library for Frontier, providing reusable functions for common infrastructure and development tasks. The library is distributed via Git and consumed using uv package manager.

## Development Commands

### Setup
```bash
make install  # Install dependencies and pre-commit hooks (default target)
```

### Linting and Formatting
```bash
make test     # Run ruff linter and formatter checks
uv run ruff check py_utils           # Lint code
uv run ruff format --check py_utils  # Check formatting
uv run ruff format py_utils          # Format code
```

### Building
```bash
make build    # Build distribution package
make clean    # Remove dist/ directory
```

### Running Individual Utilities
Most utilities have a `_test()` function stub and can be run directly:
```bash
uv run python -m py_utils.module_name
```

## Architecture

### Code Organization

The project follows a flat utility module structure where each utility is a standalone Python file in `py_utils/`. All public functions are exported through `py_utils/__init__.py`.

**Key utility categories:**

1. **Terraform Wrappers** - High-level abstractions around python-terraform:
   - `init_terraform()`: Initialize and select workspace
   - `apply_terraform()`: Plan and apply changes
   - `destroy_terraform()`: Destroy resources
   - `test_terraform()`: Validate and plan
   - `format_terraform()`: Format code
   - `import_terraform_resource()`: Import existing resources
   - `get_terraform_azurerm_backend_config()`: Generate Azure backend config

2. **Process Execution**:
   - `exec()`: Run subprocess with stdout capture and error handling

3. **Project Metadata**:
   - `get_project_metadata()`: Extract project information
   - `get_version_from_file()`: Read version from files
   - `get_env_value()`: Environment variable retrieval
   - `get_azure_short_region()`: Convert Azure region to short code

4. **Template Rendering**:
   - `render_jinja_templates()`: Jinja2 template processing

5. **Utilities**:
   - `str_to_bool()`: String to boolean conversion

### Terraform Function Pattern

Terraform utilities follow a consistent pattern:
- `init_terraform()` returns a `Terraform` object instance
- Other terraform functions accept this `Terraform` instance as first parameter
- Functions use `capture_output=False` to stream output to console
- Exit codes are checked and propagated via `exit()`

### Pre-commit Hooks

The project uses pre-commit hooks that:
- Check for merge conflicts, case conflicts, and large files
- Detect private keys
- Enforce trailing whitespace and EOF rules
- Lock uv dependencies
- Run `make test` before commit

## Distribution

This library is consumed via Git URL using uv:
```bash
uv add git+https://github.com/frontierhq/py-utils.git
uv add git+https://github.com/frontierhq/py-utils.git@main --refresh
uv add git+https://github.com/frontierhq/py-utils.git@0.2.0 --refresh
```

It can also be consumed locally using uv:
```bash
uv add --editable ../py-utils
```
