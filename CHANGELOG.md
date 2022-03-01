# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

Versions before 0.1.0 are untracked

## [Unreleased]
### Added
* `py.typed` file

## [0.1.3] - 2022-02-19
### Changed
* move pypi publish from check to release workflow

### Fixed
* run release workflow only on "release" event and type "published"

## [0.1.2] - 2022-02-19
### Fixed
* forgot to bump version

## [0.1.1] - 2022-02-19
### Fixed
* fix release workflow break

## [0.1.0] - 2022-02-19
### Added
* `pd ls`
* `pd user`
* `CHANGELOG.md`
* github action release workflow (under testing)

### Changed
* version number retrieved from metadata in `__init__.py`
* avoid dependencies version cap
* replace [jake](https://pypi.org/project/jake/) by [pip-audit](https://pypi.org/project/pip-audit/)


[Unreleased]: https://github.com/koyeung/python-pdcli/compare/0.1.3...HEAD
[0.1.3]: https://github.com/koyeung/python-pdcli/releases/tag/0.1.3
[0.1.2]: https://github.com/koyeung/python-pdcli/releases/tag/0.1.2
[0.1.1]: https://github.com/koyeung/python-pdcli/releases/tag/0.1.1
[0.1.0]: https://github.com/koyeung/python-pdcli/releases/tag/0.1.0
