### PAHEK Core

Shared foundation for PAHEK Security's Frappe apps. Holds only what every PAHEK app (website today, possibly others later) needs:

- `PAHEK Site Settings` — organisation identity: name, NSCDC licence, contact details, social links
- Roles: `PAHEK Admin`, `PAHEK Editor`, `AI Drafter` (shipped as fixtures, synced on every `bench migrate`)

Nothing website-specific lives here — that belongs in `pahek_web`.

Platform-level documentation (architecture, deploy, runbook) lives in the `pahek-platform` repository.

### Installation

Installed via the Docker image build (`apps.json` in `pahek-platform`), then:

```bash
bench --site <site> install-app pahek_core
```

### License

Proprietary. Copyright PAHEK Security.
