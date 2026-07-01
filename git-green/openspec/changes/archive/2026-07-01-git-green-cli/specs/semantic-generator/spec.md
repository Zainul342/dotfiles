## ADDED Requirements

### Requirement: Semantic Commits and Content DB
The commit generator SHALL append developer log entries, tips, or cheat sheets from a built-in content database to corresponding files inside a `wiki/` directory.
*   Each commit message MUST begin with a semantic commit prefix (`docs:`, `feat:`, `refactor:`, `style:`).
*   The appended lines MUST be valid markdown content.

#### Scenario: Appending Git Tip
- **WHEN** a git tip is chosen from the database
- **THEN** it SHALL be appended to `wiki/git.md` and committed with a `docs(git):` message.
