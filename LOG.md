# My 120-Day Learning Log

**Day 1 - May 4, 2026**  
Started my journey today to get the Dedicated Coder stamp for Lido CSM!  
I will commit every day for 120 days.


**Day 2 - May 5, 2026**  
Made my repo public today so I can also work toward the 50 and 100 public commits stamps.  
Continuing the streak!


**Day 3 - May 6, 2026**  
Day 3 of consistent commits. Repo is public and progressing toward 50 and 100 commits stamps too.


**Day 4 - May 7, 2026**  
Added basic project structure and started planning the architecture for a small CLI tool.  
Reviewed some open source repos for best practices on logging and modular design.


**Day 5 - May 8, 2026**  
Implemented the core CLI argument parser using argparse.  
Added basic command structure (`--help`, `init`, `status`) and tested it locally.


**Day 6 - May 9, 2026**  
Added proper error handling for invalid arguments and improved CLI help output.  
Started implementing the `init` command with basic project scaffolding logic.


**Day 7 - May 10, 2026**  
Completed the `init` command — it now creates the project directory structure and a basic config file.  
Added unit tests for argument parsing and init logic. Refactored some helper functions for better readability.


**Day 9 - May 12, 2026**  
Implemented the `run` command with basic execution flow and subprocess handling.  
Added support for Python's built-in logging module and cleaned up the main entry point.


**Day 8 - May 11, 2026**  
Implemented the `status` command to display current project configuration and health checks.  
Added JSON config loading and basic validation. Cleaned up the command registry for easier extension.


**Day 11 - May 14, 2026**  
Added a new `build` command that assembles the project based on the config file.  
Implemented basic dependency resolution and created a sample output directory structure. Wrote additional tests for the new command.


**Day 10 - May 13, 2026**  
Added configuration validation and environment variable support to the CLI.  
Refactored the command handlers into separate modules for better maintainability. Fixed a few edge cases in error handling.


**Day 12 - May 15, 2026**  
Added comprehensive README with installation instructions, usage examples, and command reference.  
Improved test coverage for the build command and fixed a small bug in config validation.


**Day 13 - May 16, 2026**  
Added a new `clean` command to remove build artifacts and temporary files.  
Implemented plugin system support using entry points and updated all command help texts for consistency.


**Day 14 - May 17, 2026**  
Added support for custom plugins via entry points and improved overall error reporting with detailed tracebacks.  
Refactored the plugin loader for better extensibility and wrote tests for the new plugin system.


**Day 15 - May 18, 2026**  
Implemented a template system using Jinja2 for generating new project scaffolds.  
Added a new `template` command with built-in templates (basic, web, data-science) and improved project initialization flow.


**Day 16 - May 19, 2026**  
Added packaging configuration (pyproject.toml + setuptools) so the tool can be installed via pip.  
Updated README with installation instructions using `pip install -e .` and added a basic setup.py fallback.


**Day 17 - May 20, 2026**  
Added CI/CD pipeline with GitHub Actions for automated testing and linting.  
Configured pytest with coverage reporting and added basic workflow for pull requests.


**Day 18 - May 21, 2026**  
Expanded test suite with more edge cases for the template system and plugin loader.  
Added pre-commit hooks for automatic linting (black + ruff) and updated the CI workflow to run them.


**Day 19 - May 22, 2026**  
Added support for configuration profiles (dev, prod, test) and improved command-line flag handling.  
Refactored the config module to support environment-specific settings and updated documentation accordingly.


**Day 21 - May 24, 2026**  
Added shell completion support for bash and zsh.  
Improved error messages and added more usage examples to the README.

**Day 20 - May 23, 2026**  
Added a new `doctor` command that performs environment checks and dependency validation.  
Improved help text formatting across all commands and added usage examples to the main CLI.


**Day 23 - May 26, 2026**  
Added structured logging with different log levels and improved error handling across commands.  
Started setting up release automation with semantic versioning and changelog generation.


**Day 22 - May 25, 2026**  
Added support for custom command extensions through plugins and created an example plugin.  
Improved the overall architecture by separating concerns between core CLI and plugin management.


**Day 24 - May 27, 2026**  
Added automatic changelog generation using conventional commits and GitHub release workflow.  
Refactored the logging system to support different output formats (console, JSON) and improved overall code organization.


**Day 26 - May 29, 2026**  
Added opt-in anonymous usage analytics and improved command auto-discovery.  
Fixed several edge-case bugs found during testing and updated project dependencies to latest versions.


**Day 27 - May 30, 2026**  
Added comprehensive documentation for all commands using Sphinx-style docstrings.  
Improved the help system to show detailed examples and started working on a website for the project.


**Day 25 - May 28, 2026**  
Implemented a `version` command that displays the current CLI version and checks for updates.  
Set up semantic versioning properly and prepared the project for its first public release.


**Day 28 - May 31, 2026**  
Added support for multiple configuration file formats (JSON + YAML) and a new `config` command for easy management.  
Improved CLI UX with better formatting and progress indicators for longer operations.


**Day 29 - June 1, 2026**  
Added HTTP client integration using httpx for remote operations and implemented a new `sync` command.  
Improved secret management and added basic encryption for sensitive environment variables.


**Day 30 - June 2, 2026**  
Added a new `monitor` command for real-time log tailing and process monitoring.  
Implemented background task support using asyncio and significantly improved performance for long-running operations.


**Day 31 - June 3, 2026**  
Added integration tests for the full command pipeline and improved test fixtures.  
Refactored core modules to use dependency injection for better testability and maintainability.


**Day 33 - June 5, 2026**  
Added Docker integration support and a new `docker` command for building and running containers.  
Improved overall CLI performance with caching and began writing the contributing guide.


**Day 32 - June 4, 2026**  
Added a new `validate` command to check project configuration, dependencies, and best practices.  
Improved error messages with actionable suggestions and began writing the plugin development guide.



**Day 34 - June 6, 2026**  
Added support for custom output formatters (JSON, YAML, table, rich) across all commands.  
Began prototyping a TUI (Text User Interface) mode using Textual for interactive workflows.

**Day 35 - June 7, 2026**  
Added a `migrate` command to help users upgrade between CLI versions and improved backward compatibility handling.  
Enhanced the test suite with property-based testing using Hypothesis for more robust validation.


**Day 36 - June 8, 2026**  
Added internationalization (i18n) support and began translating all user-facing messages.  
Improved rich formatting and added more visual polish to the TUI prototype.


**Day 37 - June 9, 2026**  
Added plugin marketplace integration (basic discovery and install commands).  
Improved dependency management and added automatic security vulnerability scanning in the validate command.


**Day 38 - June 10, 2026**  
Added support for workspace mode (multi-project management) and a new `workspace` command.  
Refactored the core architecture to better support multiple projects and improved configuration inheritance.


**Day 39 - June 11, 2026**  
Added a new `template` marketplace with ability to search, install, and update community templates directly from the CLI.  
Improved plugin system stability and added better error handling for plugin loading.


**Day 40 - June 12, 2026**  
Implemented full support for custom hooks (pre/post command hooks) and added a new `hook` command to manage them.  
Improved logging system with structured JSON output option and better log rotation.


**Day 41 - June 14, 2026**  
Added support for `.env` files and automatic environment variable expansion in all configuration files.  
Implemented a new `env` command to list, get, and set environment variables used by the tool.


**Day 42 - June 17, 2026**  
Added shell completion support for bash, zsh, and fish.  
Improved CLI startup time significantly and added progress spinners for long-running operations.


**Day 43 - June 18, 2026**  
Added a new `alias` command to create and manage custom command shortcuts.  
Improved the help system with better examples and started adding inline documentation for all commands.


**Day 43 - June 18, 2026**  
Added a new `alias` command to create and manage custom command shortcuts.  
Improved the help system with better examples and started adding inline documentation for all commands.


**Day 44 - June 22, 2026**  
Added support for custom themes and improved the rich output formatting across all commands.  
Started implementing a basic web dashboard (using FastAPI + simple frontend) for monitoring and managing projects.


**Day 45 - June 23, 2026**  
Added a basic web dashboard using FastAPI with project overview, command execution, and real-time logs.  
Improved the CLI’s remote execution capabilities and added better error reporting for the dashboard.


**Day 46 - June 24, 2026**  
Added token-based user authentication to the web dashboard and improved the overall UI/UX.  
Implemented command history viewing and better real-time log streaming in the dashboard.


**Day 47 - June 25, 2026**  
Added a settings page to the web dashboard for managing global and project-specific configurations.  
Improved error handling and added better validation throughout the CLI and dashboard backend.


**Day 48 - June 26, 2026**  
Added background task support and a task queue system for long-running operations in the web dashboard.  
Improved the overall architecture by better separating CLI core logic from the web components.

**Day 49 - June 27, 2026**  
Added user profile management and improved the authentication flow in the web dashboard.  
Began preparing the project for the first public release (v0.1.0) by updating documentation and cleaning up the codebase.


**Day 51 - June 29, 2026**  
Added an in-app notifications system to the web dashboard and improved task monitoring.  
Began planning and documenting the roadmap for version 0.2.0.


**Day 50 - June 28, 2026**  
Created a detailed CHANGELOG and finalized preparations for the first public release (v0.1.0).  
Improved the README significantly with better installation instructions, usage examples, and project overview.
