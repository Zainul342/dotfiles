## ADDED Requirements

### Requirement: Systemd User Service Integration
The auto-daemon installer SHALL create and enable a Systemd User Service and Timer to execute daily.
*   The timer configuration MUST be set to run daily at 10:30 PM.
*   The timer MUST have `Persistent=true` enabled to run immediately on boot if missed.

#### Scenario: Running daemon installation
- **WHEN** user executes daemon installation
- **THEN** a `github-green.timer` and `github-green.service` SHALL be created in `~/.config/systemd/user/` and activated.
