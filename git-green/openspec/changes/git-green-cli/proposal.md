## Why

Currently, automated Git contribution generators use highly repetitive commits (e.g. dummy lines in a text file with redundant commit messages) which easily flag them as artificial. 
This proposal establishes **`git-green`**, a real, open-source CLI utility designed to maintain organic, semantic Git contribution graphs. The commits made during its development and execution will represent real, structured contributions, making the developer's profile history look natural, professional, and purposeful.

## What Changes

*   **Create `git-green` CLI:** Build a Python-based command-line interface to orchestrate and run contribution tasks.
*   **Organic Shading Engine:** Add an algorithm to distribute commit frequencies and hours realistically across a calendar (busy mid-week, lighter start/end of week, weekend breaks/variance).
*   **Semantic Commit Generator:** Build an engine that writes structured developer journal logs or programming tips (e.g., "Today I Learned" markdown notes) using standard semantic commit messages (`docs:`, `feat:`, `refactor:`, `style:`).
*   **Auto-Daemon Installer:** Provide commands to automatically configure and register Systemd user services/timers or Cron jobs.

## Capabilities

### New Capabilities

- `git-green-core`: Core CLI script structure, arguments, configuration files, and command execution framework.
- `organic-scheduler`: Frequency curves and timing models simulating human developer activity.
- `semantic-generator`: Markdown TIL content database and semantic commit message generator.
- `auto-daemon`: Systemd service/timer template generator and system registration installer.

### Modified Capabilities

*(None)*

## Impact

*   **Repository:** Creates a new, standalone Python project structures under `/home/zainm/git-green`.
*   **System Services:** Installs systemd user timers/services locally for the active user session.
*   **Git History:** Will write to a `wiki/` directory in the repository where it is deployed, keeping git logs clean and readable.
