# Changelog

Format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [1.2.1] - 2026-11-03

- Require serato-tools 5.3.0 or newer

## [1.2.0] - 2026-11-03

- Remove the startup check that the installed serato-tools is the latest release. It made a network call on every run, needed `requests` without declaring it, and stopped the command from running whenever serato-tools published a new release
- Require serato-tools 5.2.0 or newer
- The package's Homepage link points at this repo, instead of serato-tools on PyPI

## [1.1.2] - 2026-02-26

- Require serato-tools 3.7.0 or newer

## [1.1.1] - 2025-12-06

- Require serato-tools 3.6.2 or newer

## [1.1.0] - 2025-05-17

- Exit at startup, telling you to upgrade, when the installed serato-tools isn't its latest release

## [1.0.3] - 2025-05-15

- Initial release: the `serato_usb_export` command, which runs serato-tools' USB export
