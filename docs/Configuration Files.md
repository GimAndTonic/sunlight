# Configuration Files

The application uses JSON configuration files to define settings for simulation and runtime behavior.

## Directory Structure
Configuration files are organized into two directories:
- `/etc/default/` – Contains default settings.
- `/etc/local/` – Contains local overrides (e.g. private settingsn), not tracked in Git.

On startup, the application merges these two configurations, giving priority to `/etc/local/`. 
- The merged result is saved in: `/var/`merged_config.json`

### Developer Information
The `/etc/local/` directory is intended for private or sensitive settings, such as:
- Specific GPS coordinates
- API keys
- Local debug options
This folder's content is excluded within `.gitignore` be committed to version control.

## Structure

`sim_config.json`

```
{
  "location": {
    "latitude": 59.3293,
    "longitude": 18.0686,
    "elevation": 0
}
```