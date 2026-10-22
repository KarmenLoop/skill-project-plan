# Project Plan

English | [简体中文](README.zh-CN.md)

See what can start now and which dependency chain determines the finish. Describe tasks, durations, dependencies, and acceptance checks; the helper returns an ordered plan and critical path.

[Download v0.2.1](https://github.com/KarmenLoop/skill-project-plan/releases/tag/v0.2.1) · [Tutorial](docs/tutorial.en.md) · [Input reference](docs/INPUT.md) · [Report an issue](https://github.com/KarmenLoop/skill-project-plan/issues)

## What it does

The three dependent tasks finish at offsets 1, 4, and 6. The critical path is a → b → c, with estimated_duration 6.

Durations use a unit you choose consistently. This is not a resource calendar, staffing optimizer, or promised delivery date.

![Project Plan sample JSON output from version 0.2.1](docs/images/example-output-v0.2.1.svg)

*Actual local output from v0.2.1, rendered as an image. [Complete result](examples/expected.json) · [Image provenance](docs/images/provenance.json).*

## Start here

Download `karmen-project-plan-v0.2.1.zip` and its `.sha256` file from the release, verify the hash, then extract the ZIP. In the extracted directory, use Python 3.9 or later:

```sh
python3 scripts/run.py --version
python3 scripts/run.py --input examples/input.json
```

Expected version: `karmen-project-plan 0.2.1`. The three dependent tasks finish at offsets 1, 4, and 6. The critical path is a → b → c, with estimated_duration 6.

To install the complete skill into a host that reads `~/.agents/skills`:

```sh
python3 install.py --host agents
```

The installer refuses an existing destination. Host discovery and invocation vary; see the [full setup and practice guide](docs/tutorial.en.md). You can run the helper directly without an AI host.

## Use it with your own work

Give each task a unique ID, positive duration, depends_on IDs, and a checkable acceptance statement. Keep units consistent; owner is optional.

Add parallel work and compare its finish with the critical path. Try a missing dependency and a cycle to understand why invalid plans are rejected before scheduling.

Read the [field contract](docs/INPUT.md) before preparing a new input. The helper runs locally with the Python standard library; it needs no model account, API key, or network connection. An AI host has its own data and permission settings.

## Questions

**Does the critical path include weekends or people’s availability?** No. It uses durations and dependencies only. Map the result to real calendars and staffing separately.

**Where does the result go?** JSON is printed to stdout unless you request a new file with `--output`. Existing output files are preserved. The helper reads only the submitted records and any local paths documented in its input contract.

## Documentation and support

- [Download, install, configure, practice, upgrade, and remove](docs/tutorial.en.md)
- [Input/output contract](docs/INPUT.md) and [compatibility](docs/COMPATIBILITY.md)
- [Changelog](CHANGELOG.md), [contributing](CONTRIBUTING.md), [support](SUPPORT.md), and [security reports](SECURITY.md)

## License

[MIT](LICENSE). Keep the license and [notice](NOTICE.md) with redistributed copies. Maintained by [KarmenLoop](https://karmenloop.com).
