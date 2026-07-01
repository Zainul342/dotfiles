## ADDED Requirements

### Requirement: CLI Subcommands
The CLI system SHALL expose two primary subcommands: `generate` and `install`.
*   `generate` SHALL require a `--days` parameter specifying how many past days of commits to generate.
*   `install` SHALL set up the daily autostart system service.

#### Scenario: Running the generate subcommand
- **WHEN** user executes `git-green generate --days 30`
- **THEN** the system SHALL start the contribution generator targeting the last 30 days.

#### Scenario: Running the install subcommand
- **WHEN** user executes `git-green install`
- **THEN** the system SHALL install systemd services locally.
