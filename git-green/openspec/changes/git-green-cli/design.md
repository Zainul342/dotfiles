## Context

Automated contribution generators traditionally look fake due to a lack of commit messaging variance, a single static log file, and uniform commit frequencies. `git-green` provides a technical solution by mimicking realistic human workflows.

## Goals / Non-Goals

**Goals:**
*   Create a dependency-free Python CLI tool utilizing only the Python standard library.
*   Implement a weekly shading distribution model to simulate natural work/weekend patterns.
*   Provide a curated dictionary of real programming tips (Git, Python, Linux) to generate human-readable commits.
*   Add native Systemd integration for automatic daily execution.

**Non-Goals:**
*   No Web UI or Desktop GUI (remain purely a terminal-focused CLI tool).
*   No external database dependencies (like SQLite/PostgreSQL) — use simple files.

## Decisions

### 1. Python Standard Library over Third-Party Libraries
*   **Choice:** Use `argparse`, `subprocess`, `datetime`, and `random` rather than third-party packages like `click` or `rich`.
*   **Rationale:** Keeps the tool extremely lightweight (takes less than 1 second to execute) and ensures a zero-dependency installation path on any system with Python 3.

### 2. Multi-File Topic Directory (`wiki/`)
*   **Choice:** Commit changes across multiple markdown files in a `wiki/` directory (e.g., `git.md`, `python.md`, `linux.md`) instead of a single log file.
*   **Rationale:** This creates a realistic git log. When inspecting the repository, the file changes look like a expanding reference wiki rather than a bot editing a single file.

### 3. Weekly Distribution Curve Model
*   **Choice:** The Scheduler uses a weekday multiplier (100% density on workdays, 5% on weekends).
*   **Rationale:** Simulates standard developer rest cycles (no activity on weekends) which is the most critical signature of human activity.

## Risks / Trade-offs

*   **[Risk] excessive commits trigger spam warnings** → *Mitigation:* Cap maximum weekday commits at 40 and default weekends to 0–2.
*   **[Risk] Clock skew conflicts on GitHub** → *Mitigation:* Auto-adjust generated timestamps to ensure they occur in the past relative to the execution run.
